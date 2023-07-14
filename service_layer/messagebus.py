from sqlalchemy.orm import Session

from typing import Union
from domain import events, commands
from . import event_handlers
from . import command_handlers

Message = Union[commands.Command, events.Event]

def handle(message: Message, session:Session):
    if isinstance(message, commands.Command):
        handle_command(message, session)
    elif isinstance(message, events.Event):
        handle_event(message, session)
    # for handler in HANDLERS[type(event)]:
    #     handle(event)

def handle_command(command: commands.Command, session:Session):
    handlers = COMMAND_HANDLERS[type(command)]
    for handler in handlers:
        handler(command, session)
    session.commit()
    
def handle_event(event: events.Event):
    pass


COMMAND_HANDLERS = {
    commands.CreateBook: [command_handlers.create_book]
}

HANDLERS = {
    events.BookLimitReached: [event_handlers.send_book_limit_reached_notification],
}