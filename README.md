Outstanding Tasks
    Modularize Routes

Architecture

ORM / Repository
    Currently, I map tables imperatively, without assigning specific routing rules. I map imperatively, because in doing this, I can easily map a book_table SQLAlchemy Table and its respective columns to a class that I have created, a class without reference to the tables and rows to be persisted in the database. The mapping of my class to DB table is isolated from the domain objects themselves. Using imperative mapping seems more intuitive than declaritive, because in imperative, the columns are explicitly mapped to the rows. If I use declarative, I will have objects for both the DBModel and the Model itself, which is unintuitive. 

    Why have a start mappers function?
    Bidirectionality in Domain Objects



Plan to Go Forward
    Finalize basic book api, with just authors and users.
    Determine domain requirements for expanded bookstore - implement and test the domain models.
        Study design patterns with OOP first? 
    Go further with the event driven architecture.  