from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
import csv
from form import CafeForm


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add',methods = ["GET","POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        # Collect form data
        data = [
            form.cafe_name.data,
            form.location.data,
            form.open.data,
            form.close.data,
            form.coffee.data,
            form.wifi.data,
            form.power.data
        ]
        with open("cafe-data.csv",mode ="a", newline='', encoding='utf-8') as file:
            writer = csv.writer(file,delimiter=',')
            writer.writerow(data)
        return redirect(url_for('cafes'))
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
