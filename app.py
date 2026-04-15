from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)
users = {}
message = ""
logs = []

HTML = """
<!DOCTYPE html>
<html>
<head>
<title>Admin Panel</title>

<style>
body {
    font-family: Arial;
    background: #eef2f7;
}

.container {
    width: 450px;
    margin: 60px auto;
    background: white;
    padding: 25px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
}

h2 {
    text-align: center;
}

input {
    padding: 8px;
    width: 65%;
    margin-right: 10px;
}

button {
    background: #007BFF;
    color: white;
    border: none;
    padding: 8px 12px;
    border-radius: 6px;
}

button:hover {
    opacity: 0.85;
    cursor: pointer;
}

.success {
    color: green;
    margin-bottom: 10px;
    font-weight: bold;
}

ul {
    list-style: none;
    padding: 0;
}

li {
    background: #f1f5f9;
    margin: 6px 0;
    padding: 8px;
    border-radius: 6px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.reset-btn {
    color: red;
    text-decoration: none;
    font-weight: bold;
}
</style>

</head>

<body>

<div class="container">

<h2>IT Admin Panel</h2>

{% if message %}
<p class="success">{{ message }}</p>
{% endif %}

<form method="post">
<input name="email" placeholder="Enter email" required/>
<button>Create User</button>
</form>

<h3>Users</h3>
<ul>
{% for user in users %}
<li>
<span>{{ user }} - Password: {{ users[user] }}</span>
<a class="reset-btn" href="/reset/{{ user }}">Reset</a>
</li>
{% endfor %}
</ul>

<h3>Activity Logs</h3>
<ul>
{% for log in logs %}
<li>{{ log }}</li>
{% endfor %}
</ul>

</div>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    global message

    if request.method == "POST":
        email = request.form["email"]
        users[email] = "default123"

        message = f"User {email} created successfully"
        logs.insert(0, f" User {email} created")

    return render_template_string(HTML, users=users, message=message, logs=logs)

@app.route("/reset/<email>")
def reset(email):
    global message
    if email in users:
        users[email] = "newpassword123"
        message = f"Password reset for {email}"
        logs.insert(0, f"Password reset for {email}")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)