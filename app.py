from flask import Flask, render_template, request
from send_mail import send_mail
import datetime
app = Flask(__name__)





@app.route("/")
def template_test():
    return render_template('mail.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      receiver_mail = result['mail']
      subject = result['subject']
      message = result['message']
    
      send_mail(receiver_mail, subject , message)
      return render_template("send.html")




if __name__ == '__main__':
    app.run(debug=True)
