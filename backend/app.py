from flask import Flask, render_template, request
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        score_str = request.form['score']
        score = float(score_str)

        # --- HMPI calculation logic (placeholder) ---
        hampi_result = score
        # --------------------------------------------

        return render_template('index.html', result=hampi_result)
    except ValueError:
        return render_template('index.html', error="Invalid input. Please enter a valid number.")
    except Exception as e:
        return render_template('index.html', error=f"An error occurred: {e}")

if __name__ == '__main__':
    app.run(debug=True)
