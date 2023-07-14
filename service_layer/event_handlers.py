from domain import events



def send_book_limit_reached_notification(event: events.BookLimitReached):
    print("Sending email! You reached your limit!")

