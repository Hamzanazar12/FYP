


from flask import Flask,jsonify, render_template, request, flash, redirect,session

from DataPipeline.dataMiner import DataMiner
import mysql.connector 
import os
import json













app = Flask(__name__)


obj = DataMiner('data')

lst = obj.extractArticle()
img = obj.imageList()
app.secret_key=os.urandom(24)

conn=mysql.connector.connect(host="localhost", user="root", password="", database="user")
cursor=conn.cursor()


    

@app.route('/signup')
def signup():
     if 'user_id' in session:
      return render_template('dashboard.html')
     else:
      return render_template('signup.html')
   


@app.route('/' )
def home():
    
    if 'user_id' in session:
      
      return render_template('dashboard.html')
    else:
        return redirect('/signup')

@app.route('/login' )
def login():
     if 'user_id' in session:
      return render_template('dashboard.html')
     else:
      return render_template('login.html')



@app.route('/validation' , methods=['Post'])
def val():
   
    email=request.form.get('email')
    password=request.form.get('password')
    cursor.execute( "SELECT * FROM details WHERE email LIKE '{}' AND password LIKE '{}'".format(email,password))
    users=cursor.fetchall()
    if len(users)>0:
       
        session['user_id']=users[0][0] 
        session['username']=users[0][1]
        return redirect('/')
    else :
          
         return redirect('/login')


@app.route('/add', methods=['POST'])
def add():
    fname=request.form.get('first')
    lname=request.form.get('last')   
    email=request.form.get('Email')
    password=request.form.get('password')
    cursor.execute("INSERT INTO  details (id,firstname,lastname,email,password) VALUES (NULL,'{}','{}','{}','{}')".format(fname,lname,email,password))
    conn.commit()
    cursor.execute( "SELECT * FROM details WHERE email LIKE '{}' ".format(email))
    myuser=cursor.fetchall()
    session['user_id']=myuser[0][0] 
    session['username']=myuser[0][1]
        
    return redirect('/')

@app.route('/logout')
def logout():
    session.pop('user_id')
    return redirect('/login')




@app.route('/chat', methods=['GET','POST'])
def chatPage():
    return render_template('chat.html')


       
@app.route('/news')
def index():
    if 'user_id' in session:
    
    
    
        return render_template('news.html',artic=lst,im=img)
    else:
        return redirect('/signup')
@app.route('/virtual')
def virtual():
    if 'user_id' in session:
    
    
    
        return render_template('virtual.html',artic=lst,im=img)
    else:
        return redirect('/signup')



@app.route('/abd')
def abdominal():
    if 'user_id' in session:
    
    
    
        return render_template('Abdominal Pain.html',artic=lst,im=img)
    else:
        return redirect('/signup')






@app.get('/abd')
def index1():
    
    return render_template('Abdominal Pain.html')



@app.route('/abdominal', methods = ['POST'])
def AbdominalPain():
    
    if request.method == 'POST':
        data = request.form
        outFile = open('abdominal.json','w')
        json.dump(data,outFile)
        outFile.close()
        
        return '''
    
        <p> form data submitted for  </p>
        <br>
        <a class="btn btn-info" href="/diarrhea">Lets process furthur</a>
    
    '''
@app.get('/diarrhea')
def dPage():
    return render_template('Acute diarrhea.html')
@app.get('/fissures')
def fPage():
    return render_template('Anal fissures.html')
@app.get('/tract')
def tPage():
    return render_template('Biliary Tract Disorders, Gallbladder Disorders, and Gallstone Pancreatitis.html')
@app.get('/C_Diarrhea')
def cPage():
    return render_template('Chronic diarrhea.html')
@app.get('/constipation')
def conPage():
    return render_template('Constipation and Defecation Problems.html')
@app.get('/stones')
def sPage():
    return render_template('Gallstones.html')
@app.get('/gas')
def gPage():
    return render_template('gas.html')
@app.get('/gerd')
def gerdPage():
    return render_template('gerd.html')
@app.get('/indigestion')
def iPage():
    return render_template('Indigestion.html')
@app.get('/irritable')
def irrPage():
    return render_template('Irritable Bowel Syndrome.html')
@app.get('/lactose')
def lacPage():
    return render_template('Lactose Intolerance.html')
@app.get('/liver')
def liverPage():
    return render_template('Liver Disease.html')
@app.get('/loss')
def lossPage():
    return render_template('loss of apetite.html')
@app.get('/ulcer')
def ulcerPage():
    return render_template('ulcer.html')
@app.get('/vomit')
def vomitPage():
    return render_template('vomiting.html')


#form post request process functions
@app.route('/diarrhea1', methods = ['POST'])
def Diarrhea():
    
    if request.method == 'POST':
        data = request.form
        outFile = open('diarrhea.json','w')
        json.dump(data,outFile)
        outFile.close()
        
        return '''
    
        <p> form data submitted for  </p>
        <br>
        <a class="btn btn-info" href="/fissures">Lets process furthur</a>
    
    '''
@app.route('/fiss', methods = ['POST'])
def Fissure():
    
    if request.method == 'POST':
        data = request.form
        outFile = open('fissure.json','w')
        json.dump(data,outFile)
        outFile.close()
        
        return '''
    
        <p> form data submitted for  </p>
        <br>
        <a class="btn btn-info" href="/tract">Lets process furthur</a>
    
    '''
@app.route('/tract1', methods = ['POST'])
def Tract():
    
    if request.method == 'POST':
        data = request.form
        outFile = open('tract.json','w')
        json.dump(data,outFile)
        outFile.close()
        
        return '''
    
        <p> form data submitted for  </p>
        <br>
        <a class="btn btn-info" href="/C_Diarrhea">Lets process furthur</a>
    
    '''
@app.route('/cd1', methods = ['POST'])
def CD():
    
    if request.method == 'POST':
        data = request.form
        outFile = open('cd.json','w')
        json.dump(data,outFile)
        outFile.close()
        
        return '''
    
        <p> form data submitted for  </p>
        <br>
        <a class="btn btn-info" href="/constipation">Lets process furthur</a>
    
    '''
@app.route('/consti', methods = ['POST'])
def Constipation():
    
    if request.method == 'POST':
        data = request.form
        outFile = open('constipation.json','w')
        json.dump(data,outFile)
        outFile.close()
        
        return '''
    
        <p> form data submitted for  </p>
        <br>
        <a class="btn btn-info" href="/stones">Lets process furthur</a>
    
    '''
@app.route('/stones1', methods = ['POST'])
def Stone():
    
    if request.method == 'POST':
        data = request.form
        outFile = open('stone.json','w')
        json.dump(data,outFile)
        outFile.close()
        
        return '''
    
        <p> form data submitted for  </p>
        <br>
        <a class="btn btn-info" href="/gas">Lets process furthur</a>
    
    '''
@app.route('/gas1', methods = ['POST'])
def Gas():
    
    if request.method == 'POST':
        data = request.form
        outFile = open('gas.json','w')
        json.dump(data,outFile)
        outFile.close()
        
        return '''
    
        <p> form data submitted for  </p>
        <br>
        <a class="btn btn-info" href="/gerd">Lets process furthur</a>
    
    '''
@app.route('/gerd1', methods = ['POST'])
def GERD():
    
    if request.method == 'POST':
        data = request.form
        outFile = open('gerd.json','w')
        json.dump(data,outFile)
        outFile.close()
        
        return '''
    
        <p> form data submitted for  </p>
        <br>
        <a class="btn btn-info" href="/indigestion">Lets process furthur</a>
    
    '''
@app.route('/digestion', methods = ['POST'])
def Digestion():
    
    if request.method == 'POST':
        data = request.form
        outFile = open('digestion.json','w')
        json.dump(data,outFile)
        outFile.close()
        
        return '''
    
        <p> form data submitted for  </p>
        <br>
        <a class="btn btn-info" href="/irritable">Lets process furthur</a>
    
    '''
@app.route('/irr1', methods = ['POST'])
def IRR():
    
    if request.method == 'POST':
        data = request.form
        outFile = open('irritation.json','w')
        json.dump(data,outFile)
        outFile.close()
        
        return '''
    
        <p> form data submitted for  </p>
        <br>
        <a class="btn btn-info" href="/lactose">Lets process furthur</a>
    
    '''
@app.route('/lactose1', methods = ['POST'])
def Lactose():
    
    if request.method == 'POST':
        data = request.form
        outFile = open('lactose.json','w')
        json.dump(data,outFile)
        outFile.close()
        
        return '''
    
        <p> form data submitted for  </p>
        <br>
        <a class="btn btn-info" href="/liver">Lets process furthur</a>
    
    '''
@app.route('/liver1', methods = ['POST'])
def Liver():
    
    if request.method == 'POST':
        data = request.form
        outFile = open('liver.json','w')
        json.dump(data,outFile)
        outFile.close()
        
        return '''
    
        <p> form data submitted for  </p>
        <br>
        <a class="btn btn-info" href="/loss">Lets process furthur</a>
    
    '''
@app.route('/loss1', methods = ['POST'])
def Loss():
    
    if request.method == 'POST':
        data = request.form
        outFile = open('loss.json','w')
        json.dump(data,outFile)
        outFile.close()
        
        return '''
    
        <p> form data submitted for  </p>
        <br>
        <a class="btn btn-info" href="/ulcer">Lets process furthur</a>
    
    '''
@app.route('/ulcer1', methods = ['POST'])
def ulcer():
    
    if request.method == 'POST':
        data = request.form
        outFile = open('ulcer.json','w')
        json.dump(data,outFile)
        outFile.close()
        
        return '''
    
        <p> form data submitted for  </p>
        <br>
        <a class="btn btn-info" href="/vomit">Lets process furthur</a>
    
    '''
@app.route('/vomit1', methods = ['POST'])
def Vomit():
    
    if request.method == 'POST':
        data = request.form
        outFile = open('vomit.json','w')
        json.dump(data,outFile)
        outFile.close()
        
        return '''
    
        <p> form data submitted for  </p>
        <br>
        <a class="btn btn-info" href="/diarrhea">Lets process furthur</a>
    
    '''




















if __name__ == '__main__':
    
    app.run(debug = True)
    
    
    
    




if __name__ == '__main__':
    app.run(debug=True)
 