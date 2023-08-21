#!/usr/bin/python3
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission data Food Provider
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        
        # Handle form submission data for the food
        quantity = request.form.get('quantity')

        # Handle volunteer data 
        namev = request.form.get('name of volunteer')
        emailv = request.form.get('email of the volunteer')
        phonev = request.form.get('phone no of the volunteer')
        
        
        # You can process the form data here
        
        # For demonstration, just printing the data in the console that the client will be providing
        print(f"Name: {name}\nEmail: {email}\nPhone: {phone}\nAddress: {address}\nQuantity: {quantity}")

        # For demonstration, just printing the data in the console that the volunteer will be providing
        print(f"Name: {namev}\nEmail: {emailv}\nPhone: {phonev}")
        
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
