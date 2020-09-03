import os
import glob
import shutil
import csv
import sys
from flask import Flask, render_template, url_for, flash, redirect, request
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_bootstrap import Bootstrap
from wtforms import StringField, IntegerField, SubmitField, SelectField
from wtforms.validators import DataRequired
from collections import Counter
import string
import re
import pandas as pd
from flask import Flask, request, render_template
import pymysql
import random
#database connection
database_instance_endpoint=""
port=3306
dbname=""
user=""
password=""

conn = pymysql.connect(database_instance_endpoint,
                      user = user,
                      port = port,
                      passwd = password,
                      database = dbname)
cursor = conn.cursor()


# application = Flask(__name__)

# @application.route('/')
# def home1():
#     return render_template('home1.html')

# #Quiz practise question working fine
# @application.route("/QuizPractise01", methods=["POST", "GET"])
# def QuizPractise01():
#     range1 = str(request.form.get('range1', ''))

#     query1 = "SELECT  mag, count(mag) AS number from mytable WHERE net =  '" + str(range1) + "'"

#     cursor.execute(query1)
#     r1 = cursor.fetchall()
#     rows = ([['head1', 'head2']])
#     for ele in r1:
#         rows.append ([ele[0], ele[1]])
#     print(rows)

#     return render_template('index1.html', rows=rows)

# @application.route("/setpage", methods=["POST", "GET"])
# def setpage():

#     #x = str(request.form.get('x'))

#     return render_template('set.html')

# #@application.route("/withinrange", methods=["POST", "GET"])
# #def withinrange():
#  #   range1 = str(request.form['range1'])
#   ##
#     #sql1 = "UPDATE mydb.VOLCANOS SET Volcano_Name = '" + str(range2) + "' WHERE Number = '" + str(range1) + "'"
#     #sql2 = "SELECT * FROM mydb.VOLCANOS WHERE Number = '" + str(range1) + "'"
#     #cursor.execute(sql1)
#     #cursor.execute(sql2)
#     #rows1 = cursor.fetchall()


#     #return render_template("withinrange.html", rows=rows1, rowcount=len(rows1))






# # run the app.
# if __name__ == "__main__":
#     # Setting debug to True enables debug output. This line should be
#     # removed before deploying a production app.
#     application.debug = True
#     application.run()



application = Flask(__name__)
bootstrap = Bootstrap(application)

# Configurations
application.config['SECRET_KEY'] = 'blah blah blah blah'


class NameForm(FlaskForm):
    name = StringField('Name', default="Bruce Springsteen")
    submit = SubmitField('Submit')

# ROUTES!


@application.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        return render_template('home.html', form=form, name=name)
    return render_template('login.html', form=form, name=None)


@application.route('/help')
def help():
    text_list = []
    # Python Version
    text_list.append({
        'label': 'Python Version',
        'value': str(sys.version)})
    # os.path.abspath(os.path.dirname(__file__))
    text_list.append({
        'label': 'os.path.abspath(os.path.dirname(__file__))',
        'value': str(os.path.abspath(os.path.dirname(__file__)))
    })
    # OS Current Working Directory
    text_list.append({
        'label': 'OS CWD',
        'value': str(os.getcwd())})
    # OS CWD Contents
    label = 'OS CWD Contents'
    value = ''
    text_list.append({
        'label': label,
        'value': value})
    return render_template('help.html', text_list=text_list, title='help')

#hi
# Hi from Box


# @application.route("/box",  methods=['POST'])
# def box():
#     range1 = float(request.form['range1'])
#     range2 = float(request.form['range2'])
#     range3 = float(request.form['range3'])
#     range4 = float(request.form['range4'])
    

#     #sql1 = "SELECT Number,Country,Latitude,Longitude FROM mydb.VOLCANOS WHERE Latitude between '" + str(range1) + "' AND '" + str(range2) + "' AND Longitude Between '" + str(range3) + "' AND '" + str(range4) + "'"
#     sql1 = "SELECT Number,Country,Latitude,Longitude FROM test1.volcano WHERE Latitude between '" + str(range1) + "' AND '" + str(range2) + "' AND Longitude Between '" + str(range3) + "' AND '" + str(range4) + "'"
#     cursor.execute(sql1)
#     rows1 = cursor.fetchall()

#     return render_template("box.html", rows=rows1, rowcount=len(rows1))


# @application.route("/home2",  methods=['POST'])
# def home2():
#     # value1 = str(request.form['one'])
#     return render_template("home2.html")

# Sanket edits for Hackathon 

@application.route('/home2', methods=['GET', 'POST'])
def home2():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home'))

    # show the form, it wasn't submitted
    return render_template('home2.html')

@application.route('/login', methods=['GET', 'POST'])
def login():
    username = str(request.form['username'])
    pwd = str(request.form['pwd'])
    print(username)
    print(pwd)

        #sql1 = "SELECT Number,Country,Latitude,Longitude FROM mydb.VOLCANOS WHERE Latitude between '" + str(range1) + "' AND '" + str(range2) + "' AND Longitude Between '" + str(range3) + "' AND '" + str(range4) + "'"
    sql1 = "SELECT * FROM test2.new WHERE id = '" + str(username) + "' AND pass = '" + str(pwd) + "'"
    cursor.execute(sql1)
    result = cursor.fetchone()
    print(result)
    if result!= None:
        return render_template('home.html')
    else:
        b="Ooops ! Looks you have entered wrong Email/password"
        return render_template('failed.html', output= b)

@application.route('/signup', methods=['GET', 'POST'])
def signup():
    return render_template('signup.html')

@application.route('/signup1', methods=['GET', 'POST'])
def signup1 ():
    username = str(request.form['username'])
    pwd = str(request.form['pwd'])
    rpwd = str(request.form['rpwd'])
    print(username)
    print(pwd)
    print(rpwd)

        #sql1 = "SELECT Number,Country,Latitude,Longitude FROM mydb.VOLCANOS WHERE Latitude between '" + str(range1) + "' AND '" + str(range2) + "' AND Longitude Between '" + str(range3) + "' AND '" + str(range4) + "'"
    #  sql1 = "SELECT * FROM test1.l WHERE id = '" + str(username) + "' AND pass = '" + str(pwd) + "'"
    sql1 = "INSERT INTO test2.new (id,pass) VALUES (\""+username+"\",\""+pwd+"\")"
    # cursor.execute("INSERT INTO (id,pass) test1.l VALUES (?,?)", (username,pwd,))
    cursor.execute(sql1)
    sql2 = "SELECT * FROM test2.new"
    cursor.execute(sql2)
    result = cursor.fetchall()
    print(result)
    
    return render_template('login.html')
    

    # return render_template('home.html')

        


@application.route('/home1', methods=['GET', 'POST'])
def home1():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home2'))

    # show the form, it wasn't submitted
    return render_template('home1.html')

@application.route('/iphonesecopy6', methods=['GET', 'POST'])
def iphonesecopy6():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home1'))

    # show the form, it wasn't submitted
    return render_template('iphonesecopy6.html')

@application.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('iphonesecopy6'))

    # show the form, it wasn't submitted
    return render_template('home.html')

@application.route('/dinein1', methods=['GET', 'POST'])
def dinein1():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('iphonesecopy6'))

    # show the form, it wasn't submitted
    return render_template('dinein1.html')

@application.route('/dinein2', methods=['GET', 'POST'])
def dinein2():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('iphonesecopy6'))

    # show the form, it wasn't submitted
    return render_template('dinein2.html')

@application.route('/pickup', methods=['GET', 'POST'])
def pickup():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('iphonesecopy6'))

    # show the form, it wasn't submitted
    return render_template('pickup.html')

@application.route('/delivery', methods=['GET', 'POST'])
def delivery():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('iphonesecopy6'))

    # show the form, it wasn't submitted
    return render_template('delivery.html')

@application.route('/home1copy', methods=['GET', 'POST'])
def home1copy():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home1copy'))

    # show the form, it wasn't submitted
    return render_template('home1copy.html')

@application.route('/home2copy', methods=['GET', 'POST'])
def home2copy():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('home2copy'))

    # show the form, it wasn't submitted
    return render_template('home2copy.html')



#teacher
# @application.route("/t1",  methods=['POST'])
# def t1():
#     value1 = str(request.form['one'])



#     return render_template("t1.html", output = value1)

# @application.route("/s1",  methods=['POST'])
# def s1():
#     value2 = str(request.form['q1'])
#     value3 = str(request.form['q2'])
#     value4 = str(request.form['q3'])


#     return render_template("s1.html", output1 = value2, output2 = value3, output3 = value4)



# @application.route("/Ans",  methods=['POST'])
# def Ans():
#     # q = str(request.form['q'])
#     name = str(request.form['name'])
#     ans1 = str(request.form['ans1'])
#     ans2 = str(request.form['ans2'])
#     ans3 = str(request.form['ans3'])


#     num1 = random.randint(0,9)
#     num2 = random.randint(0,9)
#     num3 = random.randint(0,9)

#     avg = (num1+num2+num3)/3


#     return render_template("display.html", output1 = name,output2 = num1,output4 = num2,output5 = num3,output3 = avg)





# read the file code

# @application.route('/readFile1', methods=['POST'])
# def readFile1():
#     file1 = 'Spanish.csv'
#     file2 = 'Alamo.txt'  # Files to open and then compare
#     # file11 = open(file1, 'rt', encoding="latin1")
#     # data1 = file11.read()
#     # file11.close()
#     # one = data1.split()
#     # print(one)

#     with open(file1, 'r', encoding="latin1") as f1:
#         data1 = f1.read()
#         f1.close()
#         one = data1.split()
#         # print(one)

#     with open(file2, 'r', encoding="utf-8") as f2:
#         data2 = f2.read()
#         f2.close()
#         two = data2.split()
#         # print(two)

#     temp = [s.translate(str.maketrans('', '', string.punctuation))
#             for s in two]
#     # print(temp)
#     # now change everything in lower case for comparison
#     temp = [one.lower() for one in temp]
#     # print(temp)
#     # compare the lower case list with the stop list
#     listFinal = []
#     # counter = 0
#     # for i in one:
#     #     for j in two:
#     #         if (i==j):
#     #             counter= counter+1
#     #         if(counter):
#     #             listFinal.append(i)
#     #         counter = 0

#     for i in one:
#         for j in two:
#             if (i == j):
#                 listFinal.append(i)

#     # with open(file2, 'r', encoding="utf-8") as f:
#     #     text = f.read()
#     #     split_it = text.split()
#     #     Counter1 = Counter(split_it)
#     #     most_occur = Counter1.most_common(len(split_it))
#     #     print(most_occur)
#     listFinal1 = list(set(listFinal))
#     return render_template('out.html', text=listFinal1)




# @application.route('/q8', methods=['POST'])
# def q8():
#     return render_template('q8.html', text="")

# @application.route('/q9', methods=['POST'])
# def q9():
#     return render_template('q8.html', text="")




@application.errorhandler(404)
@application.route("/error404")
def page_not_found(error):
    return render_template('404.html', title='404')


@application.errorhandler(500)
@application.route("/error500")
def requests_error(error):
    return render_template('500.html', title='500')


if __name__ == "__main__":
    port = int(os.getenv('PORT', '3000'))
    application.run(host='0.0.0.0', port=port, debug=True)
