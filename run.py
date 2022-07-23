from flask import Flask,redirect,url_for,render_template,request
import sqlite3
app=Flask(__name__)

@app.route('/demo',methods=['GET','POST'])
def demo():
    if request.method=='POST':
        _username=name=request.form['u_name']
        _password=name=request.form['u_pass']
        conn = sqlite3.connect('project.db')
        # query=f"insert into News(u_name,u_pass) values('{_username}','{_password}')" #yazdiginiz melumat elave etmek hissesi#
        # querys='DELETE FROM News WHERE id=1'#silinmesi ucun#
        Querry='UPDATE News SET u_name = 1234 WHERE id=7' #melumat yenilenmesi
        conn.execute(Querry)
        
        data = conn.execute('''SELECT * FROM News''')#ekranda gosterilmesi
        for row in data:
            print(row)
       
        conn.commit()
        
   
    return render_template('demo.html')

if __name__ == '__main__':
    app.run(port=5000,debug=True)