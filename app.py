from flask import Flask, request, jsonify

app = Flask(__name__)

# ---------- FACTORING FUNCTION ----------
def trial_division(n):
    factors = []
    if n <= 1:
        return [n]

    # Handle 2 separately
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Handle odd numbers up to sqrt(n)
    p = 3
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 2

    if n > 1:
        factors.append(n)
    return factors

# ---------- ROUTES ----------
@app.route("/")
def hello():
    return "You called the Flask server!\n"

# Example: curl -d "text=Hello!" -X POST http://localhost:5000/echo
@app.route("/echo", methods=['POST'])
def echo():
    return "You said: " + request.form['text']

# Example: curl "http://localhost:5000/factors?inINT=12"
@app.route("/factors", methods=['GET'])
def get_factors():
    try:
        in_int = int(request.args.get("inINT", ""))
    except ValueError:
        return jsonify({"error": "Invalid integer"}), 400

    factors = trial_division(in_int)
    return jsonify({"number": in_int, "factors": factors})

# ---------- MAIN ----------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
