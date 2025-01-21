from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/")
def home_view():
    return '''
        <h1>Welcome to Geeks for Geeks</h1>
        <form action="/submit" method="post">
            <input type="text" name="text_input" placeholder="Enter text here">
            <input type="submit" value="Submit">
        </form>
    '''

@app.route("/submit", methods=["POST"])
def submit_view():
    text = request.form.get("text_input")
    return f"<h1>You submitted: {text}</h1>"