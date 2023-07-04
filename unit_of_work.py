from abc import ABC, abstractmethod
import adapters.respository as respository

class AbstractUnitOfWork(ABC):
    authors: respository.AbstractRepository

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def commit(self):
        pass
    def rollback(self):
        raise NotImplementedError
    
class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=None):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()
        self.authors = respository.SQLAlchemyRepository(self.session)
        return super().__enter__()
    def __exit__(self, *args):
        super().__exit__(*args)
