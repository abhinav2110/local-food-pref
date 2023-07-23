
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import json
from flask import Flask
from flask import render_template
import pandas as pd
from flask import request
import requests
import json
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = '\xec\x11\xf1\xab\xa9\xf2\x01-F\xd6\xb2wR(\xe4'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'panace'


mysql = MySQL(app)
global c1
c1=''
@app.route('/')
@app.route('/login', methods =['GET', 'POST'])
def login():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
		username = request.form['username']
		password = request.form['password']
		c1=username
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE username = % s AND password = % s', (username, password, ))
		account = cursor.fetchone()
		if account:
			session['loggedin'] = True
			session['id'] = account['id']
			session['username'] = account['username']
			msg = 'Logged in successfully !'
			return render_template('index.html', msg = msg)
		else:
			msg = 'Incorrect username / password !'
	return render_template('login.html', msg = msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/register', methods =['GET', 'POST'])
def register():
	msg = ''
	if request.method == 'POST' and 'username' in request.form and 'password' in request.form :
		username = request.form['username']
		password = request.form['password']
		Energy='0'
		Total_lipid='0'
		Fatty_acids ='0'
		Carbohydrate ='0'
		Fiber ='0'
		Sugars ='0'
		Protein ='0'
		Cholestrol ='0'
		Sodium ='0'
		Magnesium='0'
		Potassium='0'
		Iron ='0'
		Zinc='0'
		Phosphorus ='0'
		Vitamin_A ='0'
		Vitamin_C ='0'
		Thiamin='0'
		Riboflavin='0' 
		Niacin ='0'
		Vitamin_B6 ='0'
		Folate =''
		Folic_acid ='0'
		Vitamin_B12 ='0'
		Vitamin_D ='0'
		Vitamin_E ='0'
		Vitamin_K='0'
		Water ='0'
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
		account = cursor.fetchone()
		if account:
			msg = 'Account already exists !'
		else:
			cursor.execute('INSERT INTO accounts VALUES (NULL, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s, % s)', (username, password, Energy, Total_lipid, Fatty_acids, Carbohydrate, Fiber, Sugars, Protein, Cholestrol, Sodium, Magnesium, Potassium, Iron, Zinc, Phosphorus, Vitamin_A, Vitamin_C, Thiamin, Riboflavin, Niacin, Vitamin_B6, Folate, Folic_acid, Vitamin_B12, Vitamin_D, Vitamin_E, Vitamin_K, Water))
			mysql.connection.commit()
			msg = 'You have successfully registered !'
	elif request.method == 'POST':
		msg = 'Please fill out the form !'
	return render_template('register.html', msg = msg)


@app.route("/index")
def index():
	if 'loggedin' in session:
		return render_template("index.html")
	return redirect(url_for('login'))


@app.route("/display")
def display():
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE id = % s', (session['id'], ))
		account = cursor.fetchone()	
		return render_template("display.html", account = account)
	return redirect(url_for('login'))

@app.route("/update", methods =['GET', 'POST'])
def update():
	msg = ''
	if 'loggedin' in session:
		if request.method == 'POST' and 'username' in request.form and 'password' in request.form :
			username = request.form['username']
			password = request.form['password']
			cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
			cursor.execute('SELECT * FROM accounts WHERE username = % s', (username, ))
			account = cursor.fetchone()
			if account:
				msg = 'Account already exists !'
			else:
				cursor.execute('UPDATE accounts SET username =% s, password =% s WHERE id =% s', (username, password, (session['id'], ), ))
				mysql.connection.commit()
				msg = 'You have successfully updated !'
		elif request.method == 'POST':
			msg = 'Please fill out the form !'
		return render_template("update.html", msg = msg)
	return redirect(url_for('login'))

d=pd.read_csv("restaurant-1-orders.csv")
k=list(d['Item Name'])
l=[]
for i in k:
    if i not in l:
        l.append(i)
#print(l)
len(l)
d1=pd.read_csv("IndianFoodDatasetCSV.csv")
#d1
l1=[]
foo=[]
m=list(d1['TranslatedRecipeName'])
m1=list(d1['TranslatedIngredients'])
ing={}
for i in l:
    for j in m:
        if i in j:
            p=m.index(j)
            ing[j]=m1[p]
            foo.append(j)
s=foo
@app.route('/user') 
def user():
    users=s
    return render_template('user.html', users=users)
l2=[]
#d={}
l4=['Energy', 
'Total_lipid', 
'Fatty_acids', 
'Carbohydrate', 
'Fiber', 
'Sugars',
'Protein', 
'Cholesterol', 'Sodium', 'Magnesium', 'Potassium', 'Iron', 'Zinc', 'Phosphorus', 'Vitamin_A', 'Vitamin_C', 'Thiamin', 'Riboflavin', 'Niacin', 'Vitamin_B6', 'Folate', 'Folic_acid', 'Vitamin_B12', 'Vitamin_D', 'Vitamin_E', 'Vitamin_K', 'Water']
l3=[ 'Energy',
'Total lipid (fat)',
'Fatty acids, total saturated',
'Carbohydrate, by difference',
'Fiber, total dietary',	
'Sugars, total',
'Protein',
'Cholesterol',
'Sodium, Na',
'Magnesium, Mg ',	
'Potassium, K',	
'Iron, Fe',	
'Zinc, Zn',	
'Phosphorus, P',	
'Vitamin A, RAE',	
'Vitamin C, total ascorbic acid',	
'Thiamin',
'Riboflavin',	
'Niacin	',
'Vitamin B-6',	
'Folate, food',	
'Folic acid',
'Vitamin B-12 ',	
'Vitamin D (D2 + D3)',
'Vitamin E (alpha-tocopherol)',	
'Vitamin K (phylloquinone)',
'Water']

# for i in l3:
# 	d[i]=['a',0,0]
inggg=[]
@app.route('/process',methods=['POST'])
def process():
	name=request.args.get('value')
	inggg.append(name)
	print(ing[name].split(","))
	b=list(ing[name].split(","))
	print(b)
	d={}
	l2.clear()
	for i in l3:
		d[i]=['a',0,0]
	for b1 in b:
		b1=b1.replace(" ",'%20')
		response_API = requests.get('https://api.edamam.com/api/nutrition-data?app_id=9fcaeeea&app_key=842290d81d5c6752f51a346f60bfe550&nutrition-type=cooking&ingr='+b1)
		data = response_API.text
		parse_json = json.loads(data)
		active_case = parse_json
		l=[]
		l1=[]
		l.append(list(active_case["totalNutrients"].values()))
		l1.append(active_case["totalNutrients"].keys())
		#print(l1)
		#print(d)
		for i in l[0]:
			if i['label'] in l3:
				d[i['label']][0]=i['label']
				d[i['label']][1]+=int(i['quantity'])
				d[i['label']][2]=i['unit']
		
	l5=list(d.values())
	k=0
	for i in l5:
		i[0]=l4[k]
		k=k+1
	#print(l5)
	l2.append(l5)
	#print(l2)
	return 'sucess'

@app.route('/process1',methods=['GET'])
def process1():
	f=[]
	for i in l2[0]:
		f.append(str(i[1]))
	d3=' '
	for i in inggg:
		d3=d3+i
	inggg.clear()
	Energy=f[0]
	Total_lipid=f[1]
	Fatty_acids =f[2]
	Carbohydrate =f[3]
	Fiber =f[4]
	Sugars =f[5]
	Protein =f[6]
	Cholesterol =f[7]
	Sodium =f[8]
	Magnesium=f[9]
	Potassium=f[10]
	Iron =f[11]
	Zinc=f[12]
	Phosphorus =f[13]
	Vitamin_A =f[14]
	Vitamin_C =f[15]
	Thiamin=f[16]
	Riboflavin=f[17] 
	Niacin =f[18]
	Vitamin_B6 =f[19]
	Folic_acid =f[21]
	Vitamin_B12 =f[22]
	Vitamin_D =f[23]
	Vitamin_E =f[24]
	Vitamin_K=f[25]
	Water =f[26]
	print(f)
	#cursor.execute('UPDATE accounts SET username =% s, password =% s,WHERE id =% s', (username, password, (session['id'], ), ))
	if 'loggedin' in session:
		cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cursor.execute('SELECT * FROM accounts WHERE id = % s', (session['id'], ))
		data1=cursor.fetchall()
		data2=list(data1)
		data=data2[0]
		print("data",data)
		Energy= str(int(data['Energy'])+int(f[0]))
		Total_lipid=str(int(data['Total_lipid'])+int(f[1]))
		Fatty_acids =str(int(data['Fatty_acids'])+int(f[2]))
		Carbohydrate =str(int(f[3])+int(data['Carbohydrate']))
		Fiber =str(int(f[4])+int(data['Fiber']))
		Sugars =str(int(f[5])+int(data['Sugars']))
		Protein =str(int(f[6])+int(data['Protein']))
		Cholesterol =str(int(f[7])+int(data['Cholesterol']))
		Sodium =str(int(f[8])+int(data['Sodium']))
		Magnesium=str(int(f[9])+int(data['Magnesium']))
		Potassium=str(int(f[10])+int(data['Potassium']))
		Iron =str(int(f[11])+int(data['Iron']))
		Zinc=str(int(f[12])+int(data['Zinc']))
		Phosphorus =str(int(f[13])+int(data['Phosphorus']))
		Vitamin_A =str(int(f[14])+int(data['Vitamin_A']))
		Vitamin_C =str(int(f[15])+int(data['Vitamin_C']))
		Thiamin=str(int(f[16])+int(data['Thiamin']))
		Riboflavin=str(int(f[17] )+int(data['Riboflavin']))
		Niacin =str(int(f[18])+int(data['Niacin']))
		Vitamin_B6 =str(int(f[19])+int(data['Vitamin_B6']))
		Folate =d3+data['Folate']
		Folic_acid =str(int(f[21])+int(data['Folic_acid']))
		Vitamin_B12 =str(int(f[22])+int(data['Vitamin_B12']))
		Vitamin_D =str(int(f[23])+int(data['Vitamin_D']))
		Vitamin_E =str(int(f[24])+int(data['Vitamin_E']))
		Vitamin_K=str(int(f[25])+int(data['Vitamin_K']))
		Water =str(int(f[26])+int(data['Water']))
		s5=l2[0]
		# l2.clear()
		cursor.execute('UPDATE accounts SET Energy=% s, Total_lipid=% s, Fatty_acids =% s,Carbohydrate =% s,Fiber =% s,Sugars =% s,Protein =% s,Cholesterol =% s,Sodium =% s,Magnesium=% s,Potassium=% s,Iron =% s,Zinc=% s,Phosphorus =% s,Vitamin_A =% s,Vitamin_C =% s,Thiamin=% s,Riboflavin=% s,Niacin =% s,Vitamin_B6 =% s,Folate =% s,Folic_acid =% s,Vitamin_B12 =% s,Vitamin_D =% s,Vitamin_E =% s,Vitamin_K=% s,Water =% s WHERE id =% s', (Energy,Total_lipid,Fatty_acids,Carbohydrate,Fiber,Sugars,Protein,Cholesterol,Sodium,Magnesium,Potassium,Iron ,Zinc,Phosphorus ,Vitamin_A ,Vitamin_C ,Thiamin,Riboflavin ,Niacin ,Vitamin_B6 ,Folate ,Folic_acid ,Vitamin_B12 ,Vitamin_D,Vitamin_E,Vitamin_K,Water,session['id'], ))
		#cursor.execute("UPDATE accounts SET Energy = %s WHERE id =%s", (Energy,session['id'],))
		mysql.connection.commit()
	return render_template("reg.html",users=s5)


if __name__ == "__main__":
	app.run(debug=True)
