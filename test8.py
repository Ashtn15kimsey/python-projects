import sqlite3

filelist = ('information.docx', 'Hello.text', 'myImage.png',\
            'myMovie.mpg', 'word.text', 'data.pdf', 'myPhoto.jpg')

conn = sqlite3.connect('test8.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
       ID INTEGER PRIMARY KEY AUTOINCREMENT, \
       file_name TEXT\
       )")
    conn.commit()
conn.close()
    


conn = sqlite3.connect('test8.db')
with conn:
        cur.execute
        for x in filelist:
            if x.endswith('.txt'):
                cur.execute("INSERT INTO tbl_files(file_name) VALUES()", (X))
                print(x)


                conn.commit()
            conn.close()
   

            
