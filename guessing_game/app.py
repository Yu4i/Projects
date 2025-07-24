from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for session data

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        level = request.form.get('level')
        chances_map = {"easy": 10, "medium": 5, "hard af": 1}
        range_map = {"easy": 10, "medium": 20, "hard af": 50}

        if level not in chances_map:
            return render_template('index.html', error="Invalid level selected.")

        session['chances'] = chances_map[level]
        session['target'] = random.randint(1, range_map[level])
        session['level'] = level
        return redirect(url_for('guess'))

    return render_template('index.html')

@app.route('/guess', methods=['GET', 'POST'])
def guess():
    if 'chances' not in session:
        return redirect(url_for('index'))

    message = ""
    if request.method == 'POST':
        guess = int(request.form.get('guess'))
        target = session['target']
        session['chances'] -= 1

        if guess == target:
            message = "🎉 Correct! You win!"
            session.clear()
        elif session['chances'] == 0:
            message = f"❌ Out of chances! The number was {target}."
            session.clear()
        else:
            message = "❌ Wrong guess. Try again!"

    return render_template('guess.html', chances=session.get('chances', 0), message=message)

if __name__ == '__main__':
    app.run(debug=True)