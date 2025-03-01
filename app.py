from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # Make sure index.html exists in the "templates" folder

if __name__ == '__main__':
    app.run(debug=True)
