from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

# Password strength checking function
def password_strength(password):
    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r"[a-z]", password)
    uppercase_criteria = re.search(r"[A-Z]", password)
    digit_criteria = re.search(r"\d", password)
    special_char_criteria = re.search(r"[$!?#-]", password)

    strength = 0
    if length_criteria:
        strength += 1
    if lowercase_criteria:
        strength += 1
    if uppercase_criteria:
        strength += 1
    if digit_criteria:
        strength += 1
    if special_char_criteria:
        strength += 1

    if strength == 5:
        return "Strong password!"
    elif 3 <= strength < 5:
        return "Moderate password."
    else:
        return "Weak password."

# Route to render the homepage
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle AJAX request for checking password strength
@app.route('/check_password', methods=['POST'])
def check_password():
    data = request.get_json()
    password = data['password']
    result = password_strength(password)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
