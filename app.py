from flask import Flask, render_template, request
import random
import os

app = Flask(__name__)

def generate_password(name, length=12, include_symbols=True):
    letter_alternatives = {
        'a': '@', 'b': '8', 'c': '(', 'd': '|)', 'e': '3', 'f': '|=', 'g': '9',
        'h': '#', 'i': '!', 'j': '_|', 'k': '|<', 'l': '1', 'm': '|\\/|',
        'n': '|\\|', 'o': '0', 'p': '|*', 'q': 'O_', 'r': '|2', 's': '$',
        't': '7', 'u': '|_|', 'v': '\\/', 'w': '\\/\\/', 'x': '><', 'y': '`/',
        'z': '2'
    }

    password = ''

    # Step 1: Replace characters in order
    for letter in name.lower():
        if letter.isalpha() and include_symbols and letter in letter_alternatives:
            password += letter_alternatives[letter]
        else:
            password += letter

    # Step 2: Append symbols (optional)
    if include_symbols:
        symbols = "!@#$%^&*()"
        password += ''.join(random.choice(symbols) for _ in range(2))

    # Step 3: Append 3 digits
    password += ''.join(str(random.randint(0, 9)) for _ in range(3))

    # Step 4: Trim to desired length
    return password[:length]


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/generate', methods=['POST'])
def generate():
    input_name = request.form['name-input']
    length = int(request.form.get('length', 12))
    include_symbols = 'symbols' in request.form
    generated_password = generate_password(input_name, length, include_symbols)
    return render_template('index.html', generated_password=generated_password, input_name=input_name)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
