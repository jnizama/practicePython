#Connect to SQL Server & Azure

##STEPS
#For MAC: https://www.microsoft.com/en-us/sql-server/developer-get-started/python/mac/3
#more environment or others languages: https://www.microsoft.com/en-us/sql-server/developer-get-started/
#Windows:
# 1)Install the ODBC Driver and SQL Command Line Utility for SQL Server
# 2)Test if is installed with
#       sqlcmd -S localhost -U sa -P your_password
# 3) Install pip (package manager) or use npm
#/    3.1)Install pip from https://bootstrap.pypa.io/get-pip.py and put it in a folder and run python get-pip.py in it
#     3.2)Setup environment path with Programs\Python\Python37-32\Scripts
#        pip install virtualenv
#        check if is pip installed with 
#        pip freez
#     3.3) virtualenv venv
#     3.4) venv\Scripts\activate
#     3.5) pip install pyodbc
#
#
# Follow the next example

import pyodbc

server = "ZXNLAP046\SQLDEV2017"
database = "kimerdb"
username = "sa"
password = "jnizama"
cnxn = pyodbc.connect('DRIVER={ODBC Driver 13 for SQL Server};SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
#cursor = cnxn.cursor()

cursor = cnxn.cursor()
print ('Reading data from table')
tsql = "SELECT TOP 15 PersonId, FirstName FROM Person;"
with cursor.execute(tsql):
    row = cursor.fetchone()
    while row:
        print(str(row[1]))
        row = cursor.fetchone()
    