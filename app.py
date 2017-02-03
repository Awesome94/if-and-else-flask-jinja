from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return 'welcome to results'

@app.route('/result')
def result():
   dict = {'Awesome':100,'haters':0,'fans':70}
   return render_template('result.html', result=dict)

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=False)
