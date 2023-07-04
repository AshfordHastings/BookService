from abc import ABC, abstractmethod
from domain.model import Book, Author
from typing import List, TypeVar

Entity = TypeVar("Entity", Book, Author)

class AbstractRepository(ABC):
    @abstractmethod
    def add(self, entity: Entity):
        raise NotImplementedError
    @abstractmethod
    def get(self, id, EntityType:Entity) -> Entity:
        raise NotImplementedError
    
class SQLAlchemyRepository(AbstractRepository):
    def __init__(self, session):
        self.session = session
    
    def add(self, entity:Entity):
        self.session.add(entity)

    def add_all(self, entities:List[Entity]):
        self.session.add_all(entities)
    
    def get(self, EntityType:Entity, id) -> Entity:
        return self.session.query(EntityType).filter_by(id=id).one()
    
    def list(self, EntityType:Entity) -> List[Entity]:
        return self.session.query(EntityType).all()
    
class FakeRepository(AbstractRepository):
    def __init__(self, entities):
        self._entities = set(entities)
    
    def add(self, entity:Entity):
        self._entities.add(entity)
    
    def add_all(self, entities):
        self._entities.update(entities)
    
    def get(self, id):
        return next(e for e in self._entities if e.id ==id )
    
    def list(self):
        return list(self._entities)