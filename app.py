from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Page 1 - Name input
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        username = request.form["username"]
        return redirect(url_for("events", username=username))
    return render_template("index.html")

# Page 2 - Event selection
@app.route("/events/<username>", methods=["GET", "POST"])
def events(username):
    if request.method == "POST":
        event = request.form["event"]
        return redirect(url_for("services", username=username, event=event))
    return render_template("events.html", username=username)

# Page 3 - Sub events + services
@app.route("/services/<username>/<event>", methods=["GET", "POST"])
def services(username, event):
    if request.method == "POST":
        sub_event = request.form.get("sub_event")
        services = request.form.getlist("services")
        return redirect(url_for("contact", username=username))
    return render_template("services.html", username=username, event=event)

# Page 4 - Contact
@app.route("/contact/<username>", methods=["GET", "POST"])
def contact(username):
    if request.method == "POST":
        phone = request.form["phone"]
        email = request.form["email"]
        return redirect(url_for("success", username=username))
    return render_template("contact.html", username=username)

# Page 5 - Success
@app.route("/success/<username>")
def success(username):
    return render_template("success.html", username=username)

if __name__ == "__main__":
    app.run(debug=True)