from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle form submission data
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        # You can process the form data here
        
        # For demonstration, just printing the data
        print(f"Name: {name}\nEmail: {email}\nMessage: {message}")
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
