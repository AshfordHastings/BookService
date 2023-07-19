from adapters.kafka_eventpublisher import publish

from domain import events

#TODO: Consolidate these - have maybe one topic that I publish to for wishlist, and make everything share that topic. 

def publish_book_created_event(session, event: events.BookCreated):
    publish("book-created", event)

def publish_author_created_event(session, event: events.BookCreated):
    publish("author-created", event)

def send_book_limit_reached_notification(event: events.BookLimitReached):
    print("Sending email! You reached your limit!")

