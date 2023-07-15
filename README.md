ToDo:
    JSON Serializaton of inputs
    Update API resource modeling 
    Clean up __init__ files etc
    Error handling for event bus





Book Rental Service
Basic Requirements:
User Requirements
    A user can sign into the service and check out books.
    A user can download the book in any format.
    The user can receive a preview of the book on the website.
    The user can browse the selection of books and authors.
User Permissions
    A free user can only download 5 books per month.
    A free user can subscribe to premium and get unlimited access to books per month.
Billing
    A user subscribing to premium must enter the account information to subscribe to premium
    A user will be charged for the corresponding amount. 
Book Downlaoding
    A book is posted in a certain format.
    The user must download that book as that format.
    Premium users are able to convert the book to another format. 
Adding Books
    A certain role is able to upload books to the website.
    Books must be added with their corresponding metadata, including premium, free, format, etc.
    Admin Users can delete books, update book metadata
Recommendations
    Book Downloads for both a user and all users are tracked and used to generate recommendations on new books to read. 

Events:
    Poll the remote location to see if there are any new items to grab