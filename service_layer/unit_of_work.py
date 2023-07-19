
from abc import ABC, abstractmethod

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

#from allocation import config

#TODO: Implement this at some point.

class AbstractUnitOfWork(ABC):
    products: repository.AbstractRepository

    def __enter__(self) -> 'AbstractUnitOfWork':
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        self._commit()

    def collect_new_events(self):
        for product in self.products.seen:
            while product.events:
                yield product.events.pop(0)

    @abstractmethod
    def _commit(self):
        raise NotImplementedError

    @abstractmethod
    def rollback(self):
        raise NotImplementedError


DEFAULT_SESSION_FACTORY = sessionmaker(
    bind=create_engine(
        config.get_postgres_uri(),
        isolation_level="REPEATABLE READ",
    )
)


class SqlAlchemyUnitOfWork(AbstractUnitOfWork):
    def __init__(self, session_factory=DEFAULT_SESSION_FACTORY):
        self.session_factory = session_factory

    def __enter__(self):
        self.session = self.session_factory()  # type: Session
        self.products = repository.SqlAlchemyRepository(self.session)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__(*args)
        self.session.close()

    def _commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()