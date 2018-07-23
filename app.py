from flask import Flask, render_template, request, redirect, flash
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/rfr.html')
def index():
    return render_template('rfr.html')


@app.route('/import', methods = ['GET', 'POST'])
def upload_file():
   if request.method == 'POST':
      f = request.files['file']
      f.save(secure_filename(f.filename))

      upload_file.dataSet = pd.read_csv(f.filename)
      flash('Imported '+ f.filename+ ' successfully')
      return render_template('rfr.html', dataSet = upload_file.dataSet)


@app.route('/divide', methods=['GET', 'POST'])
def func():
    func.X = upload_file.dataSet.iloc[:, 1:2].values
    func.Y = upload_file.dataSet.iloc[:, 2].values
    flash('Divided into Dependent and Independent variables.')
    return render_template('rfr.html', dataSet = upload_file.dataSet)


@app.route('/rfc', methods=['Get', 'POST'])
def rfc():
    yoe = request.form['YOE']
    rfc_n_estimators = request.form['n_estimators']
    regressor = RandomForestRegressor(n_estimators=int(rfc_n_estimators), random_state=0)
    regressor.fit(func.X, func.Y)
    y_pred = regressor.predict(yoe)
    return render_template('rfr.html', dataSet = upload_file.dataSet, prediction=y_pred)


if __name__ == '__main__':
   app.run(debug = True)