from flask import Flask, render_template, request, redirect, flash
from werkzeug import secure_filename
import pandas as pd
import numpy as np

app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/import', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))

      upload_file.dataSet = pd.read_csv(f.filename)
      flash('Imported '+ f.filename+ ' successfully')
      return render_template('index.html', dataSet = upload_file.dataSet)

@app.route('/func', methods=['GET', 'POST'])
def func():
    X = upload_file.dataSet.iloc[:, :-1].values
    Y = upload_file.dataSet.iloc[:, 2].values
    print(X)
    print(Y)
    flash('Divided into Dependent and Independent variables.')
    return render_template('index.html', dataSet = upload_file.dataSet, X = X, Y=Y)

if __name__ == '__main__':
   app.run(debug = True)