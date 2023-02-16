# importing libraries needed

from urllib.parse import unquote_plus
import mysql.connector
import json

from mysql.connector import Error
from flask import Flask, Response, request, render_template, redirect
from random import randint
from flask import  session
from flask_session import Session
from datetime import date
from datetime import datetime

# initializng Flask object
app = Flask(__name__)

# session creation
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Function for rendering login template
@app.route("/")
def renderLoginPage():
    return render_template('login.html')

# Function for rendering login template
@app.route('/login.html', methods=['GET'])
def renderLoginTestPage():
	return render_template('login.html')

# Function for rendering Signup template
@app.route('/signup.html')
def renderSignUpPage():
	return render_template('signup.html')

# Function for rendering AboutUS template
@app.route('/aboutUs.html')
def renderAboutUsPage():
	return render_template('aboutUs.html')

# Function to request entered details while signing up
@app.route("/create", methods = ['POST','GET'])
def signUp():
	"""Sign Up"""

	# requesting user details
	FullName = request.form['FullName']
	email = request.form['email']
	username = request.form['username']
	password = request.form['password']

	# check if user is already registered in the database or not
	res = runQuery("Select email from users;")
	# print(res)
	for id in res:
		# print(id[0])
		if (email == id[0]):
			url = ""
				# return "<h1>Login Successfull</h1>"
			response = json.dumps({
			'response': render_template('login.html'),
				'url': url
			})
			return response
		
	user_id = 0
	res = None

	# generating unique user id for the user
	while res != []:
		user_id = randint(0, 2147483646)
		res = runQuery("Select user_id from users where user_id = " + str(user_id))

	# inserting user details for creating his acoount
	try:
		res = None	

		insertQuery = "INSERT INTO users (FullName, user_id, email, password) VALUES(%s, %s, %s, %s)"
		value = (FullName, user_id, email, password)
		res = runQuery(insertQuery, value, 1)

		# print(res)
		url = 'http://localhost:5000/login.html'

		# once details are entered, redirecting them to login page
		if res == True:
			# print("Success")
			response = json.dumps({
				'response': render_template('login.html'),
				'user_id': user_id,
				'url' : url
			})
			return Response(response)

		else:
			url = ""
				# return "<h1>Login Successfull</h1>"
			response = json.dumps({
			'response': render_template('login.html'),
				'url': url
			})
			return response

	# if error occurs, redirect them again to signup page
	except:
		url = ""
				# return "<h1>Login Successfull</h1>"
		
		response = json.dumps({
			'response': render_template('login.html'),
				'url': url
			})
		return response
	

# function for requesting user details while logging in
@app.route('/login', methods=['POST','GET'])
def	verifyAndRenderLogin():
	"""Logging In"""
	if request.method == 'POST':

		# getting entered user details
		email = request.form['email']
		password = request.form['password']

		# checking if credentials entered are correct or not
		res = runQuery("Select user_id, email, password, fullname from users where email = '" + str(email) + "'" )

		for data in res:

			if (password == data[2]):
				user_id = data[0]
				# print("Login Successfull")

				# creating session and storing user id in the session while he is logged in
				session["user_id"] = user_id

				# redirecting them to dashboar page
				url = 'http://localhost:5000/dashboard.html'
				# return "<h1>Login Successfull</h1>"
				response = json.dumps({
				'response': render_template('dashboard.html'),
				'user_id': user_id,
				'url': url
			})
				return Response(response)


			else:
				url = ""
				# return "<h1>Login Successfull</h1>"
				response = json.dumps({
			'response': render_template('login.html'),
				'url': url
			})
				return response

		else:
			url = ""
				# return "<h1>Login Successfull</h1>"
			response = json.dumps({
			'response': render_template('login.html'),
				'url': url
			})
			return response

	return render_template('login.html')

# function to log out
@app.route("/logout", methods=['POST','GET'])
def logout():
	"""Logout"""

	session["user_id"] = None
	
	url = 'http://localhost:5000/login.html'

	# print("Success")
	response = json.dumps({
		'response': render_template('login.html'),
		'url' : url
	})
	return Response(response)

# display menu page for the avaialble books
@app.route('/dashboard.html')
def renderDashboardPage():
	"""Display dashboard"""

	# display user id who is logged in using sessions
	user_id = session["user_id"]
	# print(user_id)

	# get book_id of the books already bought by the user
	boughtBooksId = runQuery("Select book_id from boughtBooks where user_id = " + str(user_id))
	# print("Boughtbook = " + str(boughtBooksId[0]))

	list_bought_books = []

	for id in boughtBooksId:
		# print("id = " + str(id[0]))
		list_bought_books.append(id[0])

	# if user has few books bought, then don't display them in dashboard 
	if (len(boughtBooksId) == 0):
		res = runQuery("Select * from books")
	else:


		selectQuery = "Select * from books where book_id NOT IN (" + ",".join(map(str, list_bought_books)) + ")"

		res = runQuery(selectQuery)
	
	arrival = runQuery("Select * from featured_books")

	new_res = []
	for url in res:

		temp_tuple = (url[0], url[1],url[2],url[3],url[4],unquote_plus(url[5]),unquote_plus(url[6]))
		new_res.append(temp_tuple)
	
	new_arrival = []
	for item in arrival:
		new_temp_tuple = (item[0],item[1],item[2],item[3],item[4],unquote_plus(item[5]),unquote_plus(item[6]))
		new_arrival.append(new_temp_tuple)

	# to return the books which are bought by the user

	bought_books = runQuery("Select * from boughtbooks where user_id = " + str(user_id))

	new_bought_books = []
	for item in bought_books:
		new_tuple = (item[0],item[1],item[2],unquote_plus(item[3]),unquote_plus(item[4]))
		new_bought_books.append(new_tuple)
	
	coins_available = runQuery("Select coins from users where user_id = " + str(user_id))

	return render_template('dashboard.html', books=new_res, new_books = new_arrival, boughtbooks = new_bought_books, coins = coins_available)

# function to buy a book selected by uer
@app.route('/buyBook',methods=['POST','GET'])
def buySelectedBook():
	"""Buy Book"""

	# get user_id from session and book_id from request
	user_id = session["user_id"]
	book_id = request.form["Book_id"]

	# get all user details and book details
	book_details = runQuery("Select * from books where book_id = " + str(book_id))
	user_details = runQuery("Select * from users where user_id = " + str(user_id))

	# get books price , poster and pdf
	for p in book_details:
		book_price = p[2]
		poster = p[5]
		book_pdf = p[6]


	# get available coins detail by user
	for c in user_details:
		available_coins = c[4]

	# check if user has the sufficient balance or not
	if (int(book_price) < int(available_coins)):
		# print("U can buy the book")

		current_amt = int(available_coins) - int(book_price)

		updateQuery = "Update users set coins = %s where user_id = %s"
		value = (current_amt, user_id)
		res = runQuery(updateQuery, value,1)

		if res == True:
			print("Coins Updated")

	else:
		url = ""

		response = json.dumps({
			'response': render_template('dashboard.html'),
				'url': url
			})
		return response
		
	# insert bought books details into the database
	insertQuery = "Insert into boughtbooks(user_id, book_id, poster, book_pdf) values (%s, %s, %s, %s)"
	value = (user_id, book_id, poster, book_pdf)
	res = runQuery(insertQuery, value,1)


	if res == True:
		print("Success")	

	# return render_template("dashboard.html")
	url = 'http://localhost:5000/dashboard.html'
				# return "<h1>Login Successfull</h1>"
	response = json.dumps({
			'response': render_template('dashboard.html'),
				'url': url
			})
	return Response(response)


@app.route('/payment.html')
def renderPaymnetPage():
	return render_template('payment.html')

@app.route('/payment', methods=['POST'])
def buyMoreCoins():
	user_id = session["user_id"]
	coins = request.form['coins']

	# collect amount to be paid by user
	res = runQuery("Select coins from users where user_id = " + str(user_id))
	
	coins_at_present = res[0][0]

	coins = coins_at_present + int(coins)
	updateQuery = "Update users set coins = %s where user_id = %s"
	value = (coins, user_id)
	res = runQuery(updateQuery, value,1)

	if res == True:
		print("Coins added")

	url = 'http://localhost:5000/dashboard.html'
	
	response = json.dumps({
			'response': render_template('dashboard.html'),
			'url' : url
		})
	return Response(response)


 
# @app.route("/downloads/tos/")
# def tos():
#     workingdir = os.path.abspath(os.getcwd())
#     filepath = workingdir + '/static/Sample_Books/Books'
# 	# bookname
# 	# render_template(pdf_.html, book_path)
#     return send_from_directory(filepath, 'ikigai.pdf')



@app.route('/userDetails', methods=['POST','GET'])
def displayUserDetails():

	user_id = session["user_id"]
	res = runQuery("Select * from users where user_id = " + str(user_id))
	
	url = 'http://localhost:5000/profile.html'
	
	response = json.dumps({
			'response': render_template('profile.html', userDetails = res),
			'url' : url
		})
	return Response(response)


@app.route('/book', methods=['GET', 'POST'])
def displaybook():

	bookId = request.form['bookId']

	book_pdf = runQuery("Select book_pdf, book_id from boughtbooks where book_id = " + str(bookId))

	new_book_pdf = []
	for item in book_pdf:
		new_tuple = (unquote_plus(item[0]), item[1])
		new_book_pdf.append(new_tuple)

	url = 'http://localhost:5000/demo.html'
	
	response = json.dumps({
			'response': render_template('demo.html' ,pdf_path = new_book_pdf),
			'url' : url
		})
	return Response(response)


# Function to change Password
@app.route('/changePass', methods=['GET', 'POST'])
def changePassword():
	user_id = session["user_id"]

	newPassword = request.form['newPassword']

	updateQuery = "Update users set password = %s where user_id = %s"
	value = (newPassword, user_id)
	res = runQuery(updateQuery, value,1)

	
	# redirecting them to dashboar page
	url = 'http://localhost:5000/dashboard.html'
	
	response = json.dumps({
	'response': render_template('dashboard.html'),
	'url': url
})
	return Response(response)


@app.route('/completeBook', methods=['GET', 'POST'])
def completeBook():
	user_id = session["user_id"]
	
	book_id = request.form["bookId"]

	res = runQuery("Select BoughtDate from boughtbooks where user_id = " + str(user_id) + " and book_id = " + str(book_id))

	for item in res:
		boughtDate = item[0]

	today = date.today()

	difference = today - boughtDate

	if (difference.days < 30):

		res = runQuery("Select coins from users where user_id = " + str(user_id))

		for item in res:
			available_coins = item[0]

		completion_coins = 100

		coins = available_coins + completion_coins

		updateQuery = "Update users set coins = %s where user_id = %s"
		value = (coins, user_id)
		res = runQuery(updateQuery, value,1)

		deleteQuery = "Delete from boughtbooks where user_id = %s and book_id = %s"
		value = (user_id, book_id)
		res = runQuery(deleteQuery, value, 1)

		# redirecting them to dashboar page
	url = 'http://localhost:5000/dashboard.html'
	response = json.dumps({
	'response': render_template('dashboard.html'),
	'url': url
})
	return Response(response)


def runQuery(query, value = 0, flag=0):
	try:
		db = mysql.connector.connect(
			host='localhost',
			database='bookmania',
			user='theatre_user',
			password='password')

		if db.is_connected():
			cursor = db.cursor(buffered = True)
			
			if (value == 0):
				cursor.execute(query)
			else:

				cursor.execute(query, value)
			db.commit()
			if (flag == 0):
			# print(dir(cursor))
				return cursor.fetchall()
			else:
				return True

	except Error as e:
		print(e)
		#Some error occured
		return str(e.args)

	finally:
		db.close()

    #Couldn't connect to MySQL
	return None

if __name__ == "__main__":
    app.run(host='localhost', debug=True)