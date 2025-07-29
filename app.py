from flask import Flask, render_template, request, Response

app = Flask(__name__)

# --- PASSWORD PROTECTION ---
PASSWORD = "alizu"

@app.before_request
def require_password():
    auth = request.authorization
    if not auth or auth.username != "sonia" or auth.password != PASSWORD:
        return Response(
            'Login Required',
            401,
            {'WWW-Authenticate': 'Basic realm="Login Required"'}
        )

# --- ROUTES ---
@app.route("/", methods=["GET", "POST"])
def home():
    answer = None
    if request.method == "POST":
        answer = request.form.get("answer")
    return render_template("index.html", answer=answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
