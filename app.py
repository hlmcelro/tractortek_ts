import pymysql
import csv
import os
from forms import  AddForm , DelForm    #, AddOwnerForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import username, password

app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################

        # SQL DATABASE AND MODELS

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:9hannah9ms@localhost/tractortekdb' # DB connection
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # DB connection

db = SQLAlchemy(app)
#db_name="tractortekdb.db"
Migrate(app,db)

class TractortekSales(db.Model):

    __tablename__ = 'tractortek_sales'
    id = db.Column(db.Integer,primary_key = True)
    sales_team_lead = db.Column(db.Text)
    emp_id = db.Column(db.Text)
    item_code = db.Column(db.Text)
    year = db.Column(db.Text)
    week = db.Column(db.Text)
    quantity = db.Column(db.Integer)

    def init(self, sales_team_lead, emp_id, item_code, year, week, quantity):    
        self.sales_team_lead = sales_team_lead
        self.emp_id = emp_id
        self.item_code = item_code
        self.year = year
        self.week - week
        self.quantity = quantity

    def __repr__(self):
        if self.id:
            return f"For this sale, the sales team lead is {self.sales_team_lead}."
        else:
            return f"The sale does not exist."
            
db.create_all()


        
############################################

        # VIEWS WITH FORMS

##########################################
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_sale():
    form = AddForm()

    if form.validate_on_submit():
        new_sale = TractortekSales(
            sales_team_lead=form.sales_team_lead.data,
            item_code=form.item_code.data,
            emp_id=form.emp_id.data,
            year=form.year.data,
            week=form.week.data,
            quantity=form.quantity.data)

        sql = (
            f"Insert into tractortek_sales (sales_team_lead, item_code, emp_id, year, week, quantity) "
            f"values ('{form.sales_team_lead.data}', "
            f"'{form.item_code.data}'," 
            f"'{form.emp_id.data}', "
            f"'{form.year.data}', "
            f"'{form.week.data}', "
            f"'{form.quantity.data}');"
        )
        #repr(eval(sql))
        db.engine.execute(sql)

        return redirect(url_for("index"))
    else:
        return render_template('add.html', form=form)




@app.route('/list')
def list_sale():
    # Grab a list of tractortek_sales from database.
    sales_list = TractortekSales.query.all()
    print(sales_list)
    return render_template('list.html', sales_list=sales_list)

@app.route('/delete', methods=['GET', 'POST'])
def del_sale():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        sale = TractortekSales.query.get(id)
        db.session.delete(sale)
        db.session.commit()

        return redirect(url_for('list_sale'))
    return render_template('delete.html',form=form)


@app.route("/list")
def tractor_csv():

    with open("sample_tractortek_sales.csv", "rt") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if not row:
                continue
            sales_team_lead = row.get("sales_team_lead", "")
            emp_id = row.get("emp_id", "")
            item_code = row.get("item_code", "")
            year = row.get("year", "")
            week = row.get("week", "")
            quantity = row.get("quantity", "")

            sql = (
                f"Insert into tractortek_sales (sales_team_lead, item_code, emp_id, year, week, quantity) "
                f"values ('{sales_team_lead}', '{item_code}', '{emp_id}', '{year}', '{week}', '{quantity}');"
            )
            db.engine.execute(sql)

    return redirect(url_for("index"))



if __name__ == '__main__':
    app.run(debug=True)
