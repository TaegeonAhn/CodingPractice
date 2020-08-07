import pyodbc

conn = pyodbc.connect('DRIVER={Devart ODBC Driver for ASE};'
                      'Server=myserver;'
                      'Port=myport;'
                      'Database=mydatabase;'
                      'User ID=myuserid;'
                      'Password=mypassword;'
                      'String Types=Unicode')



