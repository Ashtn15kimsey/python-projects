import sqlite3

# get personal data from user
firstName = input("ENTER your first name: ")
lastName = input("ENTER your last name: ")
age = int(input("Enter your age: "))



# execute insert statment from supplied person data
with sqlite3.connect('test_database.db') as connection:
     c = connection.cursor()
     line = "INSERT INTO people VALUES ('"+ firstName +"', '"lastName +"', " +str(age) +")"
     c.execute(line)
     
        
          
