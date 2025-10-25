from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/features/financial_planning.html')
def financial_planning():
    # This function tells Flask to render the specific template
    # Flask looks in the 'templates/features/' folder
    return render_template('features/financial_planning.html')

@app.route('/features/ai_coach.html')
def ai_coach():
    # This function tells Flask to render the specific template
    # Flask looks in the 'templates/features/' folder
    return render_template('features/ai_coach.html')

@app.route('/features/financial_planning.html', methods=['POST'])
def calculate_budget(salary):
    return {
        "Housing": round(salary * 0.30, 2),
        "Food": round(salary * 0.15, 2),
        "Savings": round(salary * 0.20, 2),
        "Entertainment": round(salary * 0.10, 2),
        "Miscellaneous": round(salary * 0.25, 2)
    }
@app.route('/features/financial_planning.html', methods=['GET'])
def financial_planning():
    return render_template('features/financial_planning.html')

if __name__ == '__main__':
    app.run(debug=True)
