from flask import Flask, render_template, request, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

@app.route('/', methods=["GET", "POST"])
def index():
    try:
        if 'notes' not in session:
            session['notes'] = []

        if request.method == "POST":
            note_text = request.form.get("note")
            category = request.form.get("category")
            if note_text:
                note = {'text': note_text, 'category': category}
                session['notes'].append(note)
                session.modified = True  # Mark the session as modified to ensure it's saved

        return render_template("home.html", notes=session['notes'])
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    app.run(debug=True)
