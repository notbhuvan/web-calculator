from flask import Flask, render_template, request

app = Flask(__name__)


def calculate_values(form_data):
    try:
        num1 = float(form_data.get("num1"))
        num2 = float(form_data.get("num2"))
    except (ValueError, TypeError):
        return {
            "error": "Invalid number!",
            "num1": form_data.get("num1"),
            "num2": form_data.get("num2"),
            "operator": form_data.get("operator"),
        }

    operator = form_data.get("operator")

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == "%":
        if num2 == 0:
            return {"error": "MATH ERROR!!", "num1": num1, "num2": num2, "operator": operator}
        result = num1 % num2
    elif operator == '/':
        if num2 == 0:
            return {"error": "MATH ERROR!!", "num1": num1, "num2": num2, "operator": operator}
        result = num1 / num2
    else:
        return {"error": "Invalid operator!", "num1": num1, "num2": num2, "operator": operator}

    return {"result": result, "num1": num1, "num2": num2, "operator": operator}


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        data = calculate_values(request.form)
        return render_template("index.html", **data)
    return render_template("index.html")


@app.route("/calculate", methods=["GET", "POST"])
def calculate():
    if request.method == "POST":
        data = calculate_values(request.form)
        return render_template("index.html", **data)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
