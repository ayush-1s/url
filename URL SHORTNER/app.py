from flask import Flask, redirect, render_template, request
import string
import random
app = Flask(__name__)
def generate_short_code():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(6))
    return short_code
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        long_url = request.form['url']
        short_code = generate_short_code()
        # Save the mapping of short code to long URL in a database or file
        # For simplicity, we'll just print it here
        print(f'Short URL: http://your-domain.com/{short_code}')
    return render_template('index.html')

@app.route('/<short_code>')
def redirect_to_url(short_code):
    # Retrieve the long URL associated with the short code from the database or file
    # For simplicity, we'll just print it here
    print(f'Redirecting to long URL for code: {short_code}')
    return redirect('http://original-url.com')
if __name__ == '__main__':
    app.run()
