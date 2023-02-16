import json
import mysql.connector
from mysql.connector import Error
from random import randint


# def convertToBinaryData(filename):
#     # Convert digital data to binary format
#     with open(filename, 'rb') as file:
#         binaryData = file.read()
#     return binaryData


# def convertBinaryToFile(binarydata, filename):
#     "Convert Binary data to digital"
#     with open(filename, "wb") as file:
#         file.write(binarydata)

def main():
    """Insert data of the books"""

    # read the file
    with open('seed.json', 'r') as file_read:
        data = file_read.read()

    books = json.loads(data)
    # print(books)



    for book in books:
        bookname = book['bookname']
        price = int(book['price'])
        author = book['author']
        genre = book['genre']
        poster = book['poster']
        book_pdf = book['book_pdf']

        book_id = 0
        res = None

        while res != []:
            book_id = randint(0, 2147483646)
            selectQuery = "Select book_id from books where book_id = %s"
            value = (book_id,)
            res = runQuery(selectQuery,value)

        # convertPoster = convertToBinaryData(poster)
        # convertPDf = convertToBinaryData(book_pdf)

        insertQuery = """Insert into books (book_id, bookname, price, author, genre, poster, book_pdf) values (%s, %s, %s, %s, %s, %s, %s)"""
        value = (book_id, bookname, price, author, genre, poster, book_pdf)

        res = runQuery(insertQuery, value,1)


        # Insert query
        print("Book inserted in tabled", bookname)



# VARCHAR(Max)

def runQuery(query, value, flag=0):
	try:
		db = mysql.connector.connect(
			host='localhost',
			database='bookmania',
			user='theatre_user',
			password='password')

		if db.is_connected():
			cursor = db.cursor(buffered = True)
			
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



if __name__ == '__main__':
    main()