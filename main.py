from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/me")
def me_api():
    # user = get_current_user()
    return {
        "username": "simo",
        "theme": "blue",
        "image": "url_for('user_image', filename=user.image)",
    }

@app.post("/send")
def send_some_data():
    data = request.get_json()
    print(data)
    assert "name" in data
    
    return data["name"]