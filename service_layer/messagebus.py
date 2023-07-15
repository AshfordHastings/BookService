from sqlalchemy.orm import Session

from typing import Union
from domain import events, commands
from . import event_handlers
from . import command_handlers

Message = Union[commands.Command, events.Event]
#TODO: Update Error handling here!!
def handle(session:Session, message: Message):
    results = []
    queue = [message]
    while [queue]:
        message = queue.pop(0)
        if isinstance(message, commands.Command):
            command_result = handle_command(session, message)
            results.append(command_result)
        elif isinstance(message, events.Event):
            handle_event(session, message)
        else:
            raise Exception(f"{message} is not of type Event or Command.")
        return results

# def handle_command(command: commands.Command, session:Session):
#     handlers = COMMAND_HANDLERS[type(command)]
#     results = []
#     for handler in handlers:
#         results.append(handler(command, session))
#     session.commit()
#     return results[0]
def handle_command(session:Session, command: commands.Command):
    try: 
        #TODO: Use kwargs to pass in results of one command to next command - chaining 
        handler = COMMAND_HANDLERS[type(command)]
        result = handler(session, command)
        print(f"RESULT: {result}")
        return result
    except Exception:
        print(f"Exception on command: {command}.")
        raise

def handle_event(event: events.Event):
    pass


COMMAND_HANDLERS = {
    commands.CreateBook: command_handlers.create_book,
    commands.CreateAuthor: command_handlers.create_author
}

HANDLERS = {
    events.BookLimitReached: [event_handlers.send_book_limit_reached_notification],
}