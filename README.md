# YOUR PROJECT TITLE
#### Video Demo:  <URL https://youtu.be/T-u5lcQ1m3U>
#### Description:
**--Mys recosrdatorios es un proyecto hecho en Flask con mySql

The project contains a static folder that contains the stiles.css file which is used to change the appearance of the html files, in the stiles.css file there are some custom classes to give the application a personal style.

--In the template folder you will find the html files of the project.
The index.html file contains the list of important reminders
The add.html file contains a form where the title, description and date of the reminder are requested, just like the edit.html file.
There are two html files login and register which have the forms to start the section.
the layout.html file contains the main template to make html code in which you have the boilerplate code with the navigation bar which is needed in all other html files.**

--app.py contains the necessary methods to make reminders work
En el archivo app.py se importan todas las librerias necersarias para que el proyecto se ejecute correctamente las librerias son pymysql, Flask, render_template, request, redirect, session, jsonify. The methods that make up app.py are:

conection():
#Get the connection to the database in mysql  host='localhost', user='root', password='', db='reminders'

login():
#login allows the login template to be rendered, allows the user to enter a username and password to be able to enter the system if they are registered

index():
#index renders the main template, in which it loads the reminders of the user, loads each reminder in the form of a card showing its title description, only the reminders of the user who successfully started the section will be loaded,
The method gets the reminders associated with the user with a sql console that returns the reminders by user id.

logout():
#This method removes the active section of the user returning it to the log in.

register():
#allows the user to create a new account, it is validated that the user's name does notexist in the application and that the password and confirmation are the same.

#add():
allows the user to create a new reminder with a title, description, date and save it in the database through a sql query, it also validates that all data is entered

update():
allows the user to update my reminder by id with a title, description, date and save it in the database through a sql query, it also validates that all data is entered

delete():
#allows you to delete a reminder by its id

reminders.sql
contains the mysql code needed to create the existing my reminders tables and records for the application to run correctly