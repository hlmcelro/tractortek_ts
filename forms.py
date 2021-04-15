from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField



class AddForm(FlaskForm):

    sales_team_lead = StringField('Sales Team Lead:')
    emp_id = StringField('Employee ID:')
    item_code = StringField("Item Code:")
    year = StringField("Year:")    
    week = StringField("Week:")
    quantity = IntegerField('Quantity Sold in Week:')
    submit = SubmitField('Add Sale')

#class AddOwnerForm(FlaskForm):

#    name = StringField('Name of Owner:')
#    puppy_id = IntegerField("Id of Puppy: ")
#    address = StringField('Address:')
#    city = StringField('City:')
#    state = StringField('State:')
#    phone = StringField('Phone Number:')
#    submit = SubmitField('Add Owner')

class DelForm(FlaskForm):

    id = IntegerField('Id Number of Sale to Remove:')
    submit = SubmitField('Remove Sale')
