# BookMania
This project is an ebook portal which has the following features:
1. Login and Signup module
2. For new users, free coins will be provided initially
3. Different genres of books can be browsed in the menu
4. Books can be bought using the coins
5. More coins can be bought using dummy payment method.
6. User can read the books on the portal
7. If user finishes the book in 1 month time, they are awarded with free coins.
8. User can change their password.

### Tools used:
1. Python Flask
2. Mysql server
3. HTML, CSS
4. Javascript, Jquery

### How to Run?
1. Clone the repository into your respective directory
2. Initally run the sql commands present in the bookmania.sql file
3. Run the seed.py file and featured_books.py file present in the folder seed_scripts using command (which will enter the paths for the books and their images present to the database) - 

`python seed.py`

`python featued_books.py`

4. Run the app.py file using - 

`python app.py`

### Future Works
1. Implement the payment system using the actual API
2. Divide the book into chapters and display to user with the option to switch between chapters
3. User can preview inital few pages for the book, afterwards they can have the option to buy the whole book or unlock each chapters using coins.
4. Once user finishes the book, they click on finish book button, and a quiz can be asked for each book, so if they answer correctly, they will be awarded free coins.