# ✨ AI-Powered Customer Churn Prediction & Retention System

![AI Customer Relationship Guard](https://img.shields.io/badge/AI%20Engine-Random%20Forest%20v2.0-8b5cf6?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Frontend Tech](https://img.shields.io/badge/Frontend-React%2018%20%7C%20Tailwind%20CSS-ec4899?style=for-the-badge&logo=react&logoColor=white)
![Backend Tech](https://img.shields.io/badge/Backend-Python%20%7C%20Flask%20REST%20API-10b981?style=for-the-badge&logo=flask&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-f59e0b?style=for-the-badge)

An enterprise-grade, full-stack **Machine Learning and Customer Retention Platform** designed to proactively identify at-risk customer accounts and recommend tailored, high-ROI retention action plans before customers leave.

---

## 🌟 Overview & Philosophy

In modern subscription and SaaS businesses, acquiring new customers costs up to **5x to 25x** more than retaining existing ones. The **AI Churn Prevention & Retention System** bridges the gap between complex data science models and human-centered customer success workflows. 

Featuring a **Warm Obsidian & Sunset Velvet** luxury SaaS interface, this platform ingests customer portfolio data, runs real-time inference using an optimized **Random Forest Classifier**, tiers customers into actionable health statuses, and provides Customer Success Managers (CSMs) with one-click automated retention playbooks.

---

## 🚀 Key Features

### 🤖 1. Machine Learning Churn Prediction Engine
* **Random Forest Classifier**: Trained on customer tenure, monthly spend, contract type, and technical support coverage to predict churn probability (`0% - 100%`) with high precision.
* **Automated Risk Tiering**:
  * 🟢 **Loyal & Healthy (`<40% Risk`)**: Stable accounts requiring routine engagement.
  * 🟡 **Monitor Closely (`40% - 70% Risk`)**: Accounts showing early friction or price sensitivity.
  * 🔴 **Needs Attention (`>70% Risk`)**: High-priority flight risks requiring immediate TLC.
* **Gini Feature Importance & Drivers**: Explains *why* customers leave (e.g., identifying that month-to-month contracts and lack of tech support explain 62% of churn variance).

### 🎨 2. Humanized Executive Workspace
* **3-Step Retention Workflow**: Welcoming onboarding guide (`Bring Your List` ➔ `Spot Flight Risks` ➔ `Send Tailored Offers`).
* **Interactive CSV Drag-and-Drop Uploader**: Upload portfolio spreadsheets instantly or generate AI insights with one click using the integrated **Sample Demo Dataset**.
* **Behavioral Scatter Matrix**: Visualizes price elasticity against churn probability to uncover high-spend vulnerability clusters.
* **Warm Obsidian Theme**: Modern dark-mode UI with glowing purple, rose, and emerald accents designed to minimize visual fatigue for daily CSM usage.

### 💡 3. Automated Retention Playbooks & Action Plans
* **Tailored Strategy Recommendations**: Automatically matches customer profiles to targeted playbooks (e.g., *12-Month Annual Lock-In Discount*, *VIP Technical Concierge Support*, *Proactive Check-In Call*).
* **ROI Calculation**: Estimates expected revenue saved per action plan.
* **One-Click Offer Execution**: Assign action plans or trigger real-time retention offer emails with live HTML delivery proof modals.

### 📊 4. Executive Reports & Export Center
* **Multi-Format Export**: Download complete customer health portfolios in structured **CSV** or **JSON** formats.
* **Custom Scope & Time Horizons**: Filter exported reports by risk tier (*Needs Attention Only*, *Monitor & Attention*) and date ranges.
* **Automated Stakeholder Digests**: Send summarized executive portfolio risk digests directly to leadership or team channels.

---

## 📁 System Architecture & Folder Structure

```text
e:/customer-churn/
│
├── backend/                       # Python Flask REST API & ML Pipeline
│   ├── app/
│   │   ├── __init__.py            # Flask App Factory & CORS Setup
│   │   ├── config.py              # Application Configuration & File Paths
│   │   ├── routes.py              # API Endpoint Definitions
│   │   └── controllers/
│   │       ├── data_controller.py # CSV Ingestion, ML Inference & KPI Calculation
│   │       ├── notify_controller.py # Email Alerting & Executive Summary Dispatch
│   │       └── report_controller.py # CSV/JSON Portfolio Report Generator
│   ├── data/
│   │   └── sample_customer_churn.csv # Instant Demo Dataset
│   ├── saved_models/
│   │   ├── churn_model.pkl        # Serialized Random Forest Model
│   │   ├── scaler.pkl             # StandardScaler for Feature Normalization
│   │   └── feature_names.json     # Encoded Feature Mapping
│   ├── train_model.py             # ML Model Training & Evaluation Pipeline
│   ├── test_api.py                # Automated Backend Route Verification Suite
│   ├── run.py                     # Flask Entry Point
│   └── requirements.txt           # Python Dependencies
│
└── frontend/                      # React 18 & Tailwind CSS SPA
    ├── public/
    │   ├── index.html             # SEO & Plus Jakarta Sans Typography Setup
    │   └── manifest.json          # Web App Manifest
    ├── src/
    │   ├── components/
    │   │   ├── Auth/AuthModal.jsx # User & Role Authentication Workspace
    │   │   ├── Dashboard/
    │   │   │   ├── StatCards.jsx  # Real-Time Portfolio KPI Cards
    │   │   │   ├── CustomerTable.jsx # Interactive Churn Risk Matrix Table
    │   │   │   ├── RiskDistributionChart.jsx # Recharts Health Donut & Contract Bars
    │   │   │   └── EmailPreviewModal.jsx # Live Delivery Proof HTML Modal
    │   │   ├── Retention/StrategyCard.jsx # Action Plan & Playbook Cards
    │   │   └── Upload/CsvUploader.jsx # Drag-and-Drop CSV & Sample Loader
    │   ├── pages/
    │   │   ├── Home.jsx           # Customer Health Overview Dashboard
    │   │   ├── Analytics.jsx      # Deep-Dive Behavioral & Elasticity Page
    │   │   └── Reports.jsx        # Report Generation & Executive Export Center
    │   ├── services/
    │   │   └── api.js             # Axios API Client Wrapper
    │   ├── App.js                 # Main Router & Sidebar Navigation
    │   └── index.css              # Custom Tailwind Tokens & Warm Glassmorphism
    └── package.json               # Node Dependencies & Build Scripts
```

---

## ⚙️ Technology Stack

| Layer | Technologies |
| :--- | :--- |
| **Frontend Core** | React 18, HTML5, Vanilla JavaScript (ES6+), React Router DOM v6 |
| **Styling & UI** | Tailwind CSS v3, Plus Jakarta Sans Typography, Custom Glassmorphism |
| **Data Visualization** | Recharts (Responsive Pie, Bar, and Scatter Charts), Lucide Icons |
| **Backend API** | Python 3, Flask, Flask-CORS, RESTful Architecture |
| **Machine Learning** | Scikit-Learn (RandomForestClassifier, StandardScaler), Pandas, NumPy, Joblib |

---

## 🛠️ Quick Start & Installation

### Prerequisites
* **Node.js** (v16.0 or higher) & **npm**
* **Python** (v3.9 or higher) & **pip**

---

### Step 1: Set Up & Train the Machine Learning Backend

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a Python virtual environment:
   ```bash
   # Windows (PowerShell)
   python -m venv venv
   .\venv\Scripts\activate

   # macOS / Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Train the Machine Learning model:
   *This command processes the dataset, builds the Random Forest classifier, and saves `churn_model.pkl` to `saved_models/`.*
   ```bash
   python train_model.py
   ```

5. Start the Flask REST API server:
   ```bash
   python run.py
   ```
   *The backend server will launch and listen on **`http://localhost:5000`**.*

---

### Step 2: Set Up & Launch the React Frontend

1. Open a new terminal window and navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install Node.js dependencies:
   ```bash
   npm install
   ```

3. Start the React development server:
   ```bash
   npm start
   ```
   *The application will automatically open in your default browser at **`http://localhost:3000`**.*

---

## 📈 How to Use the System (Workflow)

1. **Upload or Sample**: On the **Customer Health Overview** page, click **Download Sample Demo CSV** and drag it right into the upload zone (or use your own customer dataset).
2. **Review AI Health Pulse**: Inspect the top KPI cards to see your **Total Customers Monitored**, **Needs Immediate Care** percentage, and **Revenue We Can Save**.
3. **Analyze Risk Factors**: Scroll down to the **Customer Health & Action Table** or switch to **Deep-Dive Analytics** to see how monthly spend and contract duration drive churn probability.
4. **Take Action**: Click **✨ Assign Plan** to attach an AI-recommended playbook to an account, or click **📧 Send Offer** to dispatch a tailored retention offer email (with instant delivery preview).
5. **Export & Report**: Navigate to **Executive Reports** to download your complete portfolio breakdown as a CSV spreadsheet or email an automated executive summary to leadership.

---

## 📋 CSV Upload Schema Requirements

When uploading custom portfolio spreadsheets, ensure your CSV contains standard headers such as:

| Column Name | Type | Description | Example |
| :--- | :--- | :--- | :--- |
| `customer_id` | String | Unique customer identifier | `CUST-1001` |
| `tenure` | Integer | Months customer has stayed with company | `14` |
| `monthly_charges` | Float | Monthly subscription/service spend ($) | `85.50` |
| `total_charges` | Float | Cumulative spend across tenure ($) | `1197.00` |
| `contract_type` | String | `Month-to-month`, `One year`, or `Two year` | `Month-to-month` |
| `tech_support` | String | `Yes`, `No`, or `No internet service` | `No` |
| `payment_method` | String | Customer payment method | `Electronic check` |

---

## 🔌 API Endpoints Reference

| HTTP Method | Route | Description |
| :--- | :--- | :--- |
| `GET` | `/api/health` | Health check verifying API and ML model availability |
| `GET` | `/api/analytics` | Returns real-time portfolio KPIs, charts data, and analyzed customers |
| `POST` | `/api/upload` | Ingests CSV file, runs Random Forest inference, and returns risk matrix |
| `GET` | `/api/retention-strategies` | Returns library of AI retention playbooks and estimated ROIs |
| `POST` | `/api/report/export` | Generates and exports portfolio summaries in `csv` or `json` format |
| `POST` | `/api/notify/email` | Triggers retention offer alert emails or executive summary digests |

---

## 📄 License & Credits

Developed as a modern **AI Customer Retention Platform** demonstrating the intersection of machine learning inference, interactive data visualization, and humanized product design.

Distributed under the **MIT License**. Feel free to modify and deploy for educational, hackathon, and enterprise projects!
