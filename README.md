# Sif_Excel_Entry

This is a web application built with Python and Flask. It allows users to submit data through forms and write the data to an Excel file.

Requirements

Python 3.6 or later

The following packages are required to run this application:

    datetime
    glob
    os
    secrets
    shutil
    pandas
    flask
    flask-login
    Pillow
    flask
    flask_bcrypt
    flask_login
    flask_sqlalchemy
    flask_wtf
    Pillow
    pip
    WTForms
    openpyxl
    email-validator
    psycopg2


    

Running the application

To run the application, you can use the following command:
python3 run.py


Features

    User registration and login
    Form submission that writes data to an Excel file
    Saving form data to a database


Form Submission

The form submission feature allows users to submit data through a form and write the data to an Excel file. The Excel file is saved to a directory named after the Purchase Order number and the current date.
Database

This application uses a database to store form data. The database is created using SQLite.
