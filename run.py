from flask import Flask,redirect,url_for,render_template,request
import sqlite3
app=Flask(__name__)

@app.route('/demo',methods=['GET','POST'])
def demo():
    if request.method=='POST':
        _username=name=request.form['u_name']
        _password=name=request.form['u_pass']
        conn = sqlite3.connect('project.db')
        query=f"insert into News(u_name,u_pass) values('{_username}','{_password}')"
        conn.execute(query)
        
        data = conn.execute('''SELECT * FROM News''')
        return render_template('demo.html',data=data)
        
   
    return render_template('demo.html')

@app.route("/update",methods=['POST','GET'])
def edit_user():
    if request.method=='POST':
        _username=name=request.form['name_']
        _password=name=request.form['pass_']
        id=name=request.form['ID']
        conn = sqlite3.connect('project.db')
        cur=conn.cursor()
        cur.execute("update News set u_name=?,u_pass=? where id=?",(_username,_password,id))
        conn.commit()
        return render_template('update.html')
    return render_template('update.html')

    
@app.route("/delete",methods=['POST','GET'])
def delete_user():
    if request.method=='POST':

        id=name=request.form['ID']
        conn = sqlite3.connect('project.db')
        cur=conn.cursor()
        cur.execute("DELETE FROM News WHERE id=?",(id))
        conn.commit()
    
        return render_template('delete.html')
    return render_template('delete.html')
if __name__ == '__main__':
    app.run(port=5000,debug=True)