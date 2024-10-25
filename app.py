from flask import Flask,render_template,request
import joblib
import numpy as np

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

if __name__ == "__main__":
    app.run(port=1234)
model = joblib.load('/workspaces/Sep-24-intake-13/templates/bankruptcy_model.pkl')

@app.route("/predict",methods=["GET","POST"])
def index():
    return(render_template("index.html"))

if request.method == 'POST':

        net_profit = float(request.form['net_profit'])
        working_capital = float(request.form['working_capital'])
        sales = float(request.form['sales'])
        equity = float(request.form['equity'])
        gross_profit = float(request.form['gross_profit'])
        net_profit = float(request.form['net_profit'])

        data = np.array([[net_profit, working_capital, sales, equity, gross_profit, net_profit]])
        prediction = model.predict(data)


from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        # Assuming `prediction` is obtained from some model based on input data.
        # You would likely have something like: prediction = model.predict(input_data)

        prediction = 0  # Example prediction value (replace with actual model prediction)

        if prediction == 0:
            return render_template('index.html', prediction_text='The company is NOT likely to go bankrupt.')
        else:
            return render_template('index.html', prediction_text='The company is likely to go bankrupt.')

    return render_template('index.html')