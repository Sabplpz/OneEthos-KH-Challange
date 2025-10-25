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

if __name__ == '__main__':
    app.run(debug=True)
