import sys
import os
import json
from app import create_app

def run_tests():
    app = create_app()
    client = app.test_client()

    print("--- Testing /api/health ---")
    res = client.get('/api/health')
    print("Status:", res.status_code, res.get_json())
    assert res.status_code == 200

    print("\n--- Testing /api/auth/login ---")
    res = client.post('/api/auth/login', json={"email": "admin@churnai.com", "password": "password123"})
    print("Status:", res.status_code, res.get_json())
    assert res.status_code == 200

    print("\n--- Testing /api/analytics ---")
    res = client.get('/api/analytics')
    data = res.get_json()
    print("Status:", res.status_code, "Success:", data.get("success") if data else None, "Customers count:", len(data.get("data", [])) if data else 0)
    assert res.status_code == 200 and data.get("success") == True

    print("\n--- Testing /api/retention-strategies ---")
    res = client.get('/api/retention-strategies')
    data = res.get_json()
    print("Status:", res.status_code, "Strategies count:", len(data.get("strategies", [])) if data else 0)
    assert res.status_code == 200

    print("\n--- Testing /api/notify/email ---")
    res = client.post('/api/notify/email', json={
        "customer_id": "CUST-1001",
        "risk_level": "High",
        "probability": 85.0,
        "strategy": "Apply 20% annual discount",
        "recipient": "test@churnai.com",
        "manager_name": "Test Manager"
    })
    data = res.get_json()
    print("Status:", res.status_code, "Success:", data.get("success") if data else None)
    assert res.status_code == 200

    print("\n--- Testing /api/report/export (json) ---")
    res = client.post('/api/report/export', json={"format": "json"})
    data = res.get_json()
    print("Status:", res.status_code, "Export customers:", len(data.get("customers", [])) if data else 0)
    assert res.status_code == 200

    print("\nALL BACKEND API TESTS PASSED SUCCESSFULLY!")

if __name__ == "__main__":
    run_tests()
