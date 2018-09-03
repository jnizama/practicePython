
# Practices using Phyton Part 1


## Getting Started

In this material you can find out how Python work and remeber python syntax in daily works.

+ Convert Decimal to Binary
+ Arrays & Tuplas
+ Using Dictionary
+ Define procedures
+ Root Squared & Time

## SQL Server connector

Steps to Install
For MAC: https://www.microsoft.com/en-us/sql-server/developer-get-started/python/mac/3
more environment or others languages: https://www.microsoft.com/en-us/sql-server/developer-get-started/

### Windows:
 + Install the ODBC Driver and SQL Command Line Utility for SQL Server
 + Test if is installed with
       sqlcmd -S localhost -U sa -P your_password
 + Install pip (package manager) or use npm
     - Install pip from https://bootstrap.pypa.io/get-pip.py and put it in a older and run python get-pip.py in it
     - Setup environment path with Programs\Python\Python37-32\Scripts
        pip install virtualenv
        check if is pip installed with 
        pip freez
     - virtualenv venv
     - venv\Scripts\activate
     - pip install pyodbc.
