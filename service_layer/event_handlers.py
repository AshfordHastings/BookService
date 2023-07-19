from adapters.kafka_eventpublisher import publish

from domain import events

def publish_book_created_event(session, event: events.BookCreated):
    publish("book-created", event)

def send_book_limit_reached_notification(event: events.BookLimitReached):
    print("Sending email! You reached your limit!")

