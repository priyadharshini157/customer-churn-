import os
import sys
from app import create_app

# Add backend directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

app = create_app()

if __name__ == '__main__':
    print("[Backend] Starting AI Customer Churn Prediction Server on http://localhost:5000 ...")
    app.run(host='0.0.0.0', port=5000, debug=True)
