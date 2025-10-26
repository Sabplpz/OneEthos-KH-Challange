from flask import Flask, jsonify, request, render_template
from financial_agent.agent import root_agent,run_agent
from flask_cors import CORS
from typing import Dict, List, Union

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Page Routes
@app.route('/')
def home() -> str:
    """Render the home page"""
    return render_template('index.html')

@app.route('/home')
def home_redirect() -> str:
    """Render the home page"""
    return render_template('index.html')

@app.route('/financial_planning')
def financial_planning() -> str:
    """Render the financial planning page"""
    return render_template('features/financial_planning.html')

@app.route('/ai_coach')
def ai_coach() -> str:
    """Render the AI coach page"""
    return render_template('features/ai_coach.html')

# API Routes
@app.route('/calculate', methods=['POST'])
def calculate_budget() -> Dict[str, Union[List[str], Dict[str, float]]]:
    """Calculate budget based on salary input"""
    try:
        data = request.get_json()
        if not data or 'salary' not in data:
            return jsonify({
                'error': 'Invalid request data'
            }), 400

        salary = float(data.get('salary', 0))
        if salary <= 0:
            return jsonify({
                'error': 'Salary must be greater than 0'
            }), 400
        
        # Create budget calculations
        budget = {
            "Housing": round(salary * 0.30, 2),
            "Food": round(salary * 0.15, 2),
            "Savings": round(salary * 0.20, 2),
            "Entertainment": round(salary * 0.10, 2),
            "Miscellaneous": round(salary * 0.25, 2)
        }
        
        return jsonify({
            "categories": list(budget.keys()),
            "budget": budget
        })

    except ValueError:
        return jsonify({
            'error': 'Invalid salary value'
        }), 400
    except Exception as e:
        return jsonify({
            'error': f'Server error: {str(e)}'
        }), 500

# AI Coach Route (Currently commented out)
@app.route('/ask_ai', methods=['POST'])
def ai_coach_response():
    data = request.get_json()
    user_input = data.get('question', '')
    if not user_input:
        return jsonify({"error": "No question provided"}), 400
    try:
        response = run_agent(user_input)
        return jsonify({"answer": response})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
