# 🚩 AI Fake Job Posting Detector

An AI-powered web application that detects potentially fraudulent job postings using **Google Gemini AI** and rule-based scam detection techniques. The application analyzes job descriptions, identifies suspicious patterns, and provides a risk assessment to help users avoid job scams.

---

## 📌 Features

- 🔍 Analyze job postings for authenticity
- 🤖 AI-powered fraud detection using Google Gemini
- ⚠️ Detect common scam indicators such as:
  - Registration or application fees
  - Unrealistic salaries
  - Guaranteed job offers
  - Urgent hiring tactics
  - Requests for personal or financial information
- 📊 Risk score and confidence level
- 💡 Detailed explanation of why a posting is suspicious
- 🌐 Interactive web interface built with Streamlit

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Google Gemini API
- python-dotenv
- Pandas

---

## 📂 Project Structure

```
AI-Fake-Job-Posting-Detector/
│
├── app.py                 # Main Streamlit application
├── detector.py            # Fake job detection logic
├── verifier.py            # Verification module
├── parser.py              # Input parsing
├── prompts.py             # AI prompts
├── utils.py               # Helper functions
├── requirements.txt
├── .gitignore
├── .env                   # API Key (Not uploaded)
├── assets/
│   └── logo.png
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/madhavihanchate/AI-Fake-Job-Posting-Detector.git
```

### 2. Navigate to the project folder

```bash
cd AI-Fake-Job-Posting-Detector
```

### 3. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configure API Key

Create a `.env` file in the project root.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 🧪 Sample Fake Job Posting

```
Company Name: Google Pvt Ltd Recruitment

Job Title: Work From Home Executive

Location: Remote

Salary: ₹85,000–₹1,20,000/month

Congratulations!

Google is urgently hiring 500 candidates.

No experience required.

To confirm your job, immediately pay a refundable registration fee of ₹2,999 via UPI.

Limited vacancies available.

Selection is guaranteed after payment.

Contact HR on WhatsApp.

Apply within 2 hours.
```

### Expected Result

- 🚨 High Risk
- Registration fee detected
- Unrealistic salary
- Guaranteed job offer
- Urgency tactics
- WhatsApp-only recruitment

---

## 📸 Screenshots

Add screenshots of your application here.

Example:

```
screenshots/
├── home.png
├── analysis.png
└── result.png
```

---

## 🔮 Future Enhancements

- Resume matching
- Company verification using LinkedIn
- URL reputation analysis
- Fake recruiter detection
- Browser extension
- Multi-language support
- Machine Learning-based scam prediction

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Submit a Pull Request.

---

## 👩‍💻 Author

**Madhavi Hanchate**

- GitHub: https://github.com/madhavihanchate

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐ on GitHub!
