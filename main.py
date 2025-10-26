from flask import Flask, jsonify, request, render_template
#from financial_agent.agent import root_agent
#from flask_cors import CORS

app = Flask(__name__)

#Defines root route
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/financial_planning')
def financial_planning():
    return render_template('features/financial_planning.html')

@app.route('/ai_coach')
def ai_coach():
    return render_template('features/ai_coach.html')


# Financial Planning Feature
@app.route('/calculate', methods=['POST'])
def calculate_budget():
    data = request.get_json()
    salary = float(data.get('salary', 0))
    budget = {
        "Housing": round(salary*0.30, 2),
        "Food": round(salary*0.15, 2),
        "Savings": round(salary*0.20, 2),
        "Entertainment": round(salary*0.10, 2),
        "Miscellaneous": round(salary*0.25, 2)
    }
    return jsonify(budget)

# AI Coach Feature
"""@app.route('/ask', methods=['POST'])
def ai_coach_response():
    data = request.get.json()
    user_input = data.get('input', '')
    response = root_agent.run(user_input)
    return jsonify({"response": response})
"""


if __name__ == '__main__':
    app.run(debug=True)
