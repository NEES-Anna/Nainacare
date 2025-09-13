# 🌸 NainaCare – AI-Powered Emotional Wellness & Hospital Care Platform  

> Built with **NainaCore Emotional Engine System (NEES)** 💖🤖  
> Supporting hospitals, caregivers & individuals with AI-driven emotional intelligence.  

---

## 🚀 Overview  
**NainaCare** is an AI-powered emotional care & hospital wellness platform designed to:  
- Assist **hospitals** with patient emotional support  
- Empower **caregivers** with AI-driven tools  
- Provide **individuals** with mental & emotional wellness support  

This project integrates cutting-edge **AI + Cloud** technology to bring emotional intelligence into healthcare.  

---

## ✨ Key Features  
- 🏥 **Hospital Integration** – Emotional wellness support for patients  
- 💬 **AI Chat Support** – Safe, empathetic AI-powered conversations  
- 🌐 **Web & Mobile Ready** – Flutter frontend + FastAPI backend  
- ☁️ **Google Cloud Run Deployment** – Scalable & serverless hosting  
- 🔒 **Safety & Privacy** – HIPAA/DPDP ready framework  

---

## 🛠️ Tech Stack  
- **Backend**: Python (FastAPI, Uvicorn)  
- **AI Core**: NainaCore Emotional Engine System (NEES)  
- **Frontend**: Flutter (Android, iOS, Web)  
- **Deployment**: Google Cloud Run + Docker  
- **Database**: Firestore (Planned)  

---

## 📂 Project Structure  
NainaCare/
│── api/ # Backend API (FastAPI)
│ ├── main.py # API endpoints
│ ├── model.py # Core AI logic
│ ├── requirements.txt
│ └── Dockerfile
│
│── app/ # Flutter frontend
│ ├── android/
│ ├── ios/
│ ├── web/
│ └── lib/
│
│── webhost/ # Web hosting build
│── README.md # Project documentation
│── .gitignore
│── .gcloudignore


---

## ⚡ Quick Start  

### 1. Clone Repository  
```bash
git clone https://github.com/NEES-Anna/Nainacare.git
cd Nainacare/api

2. Install Dependencies
pip install -r requirements.txt

3. Run Locally
uvicorn main:app --reload --port 8080


Visit 👉 http://127.0.0.1:8080/docs

4. Deploy on Google Cloud Run
docker build -t nainacare-api .
docker run -p 8080:8080 nainacare-api

🌍 Live Demo

🔗 NainaCare Demo (Cloud Run)

📌 API Endpoints
Health Check
GET /health


Response

{ "status": "ok" }

Chat Endpoint
POST /chat


Request

{ "text": "Hello NainaCare", "language": "en" }


Response

{ "reply": "Hi! How are you feeling today?", "sentiment": "positive", "safety": "safe" }

📸 Screenshots (Optional)

Add some screenshots of the app or API docs here

👨‍💻 Team & Contributors

Founder: Anna (Piyush Jambhulkar) – Creator of NainaCore Emotional Tech

Contributions welcome via PRs 🚀

🏆 Hackathon Participation

This project is being built for the Google Cloud Gen AI Exchange Hackathon 🎉

📜 License

This project is licensed under the MIT License.
Feel free to use, modify, and share with attribution.

💖 Built with love by Anna & Naina – Because emotional care matters as much as physical care.
