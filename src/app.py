from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        password_length = int(request.form['length'])
        uppercase = 'uppercase' in request.form
        password = generate_password(password_length, uppercase)
        return render_template('index.html', password=password)
    return render_template('index.html')

def generate_password(length, uppercase):
    if uppercase:
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

if __name__ == '__main__':
    app.run(debug=True)
