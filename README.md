# ♻️ AI Plastic Reward System

## 🚀 Tagline
Turning waste into rewards using Artificial Intelligence

---

## 📌 Project Overview
The AI Plastic Reward System is a smart waste management solution that uses deep learning to classify plastic as recyclable or non-recyclable. It also incentivizes users by rewarding them for responsible disposal, encouraging sustainable behavior.

---

## ⚠️ Problem Statement
Plastic waste is increasing rapidly and causing severe environmental damage.

### Key Issues:
- Lack of awareness about recyclable vs non-recyclable plastic
- No motivation for people to recycle
- Manual waste segregation is inefficient
- Improper disposal leads to pollution and landfill overflow

---

## 💡 Solution
We developed an AI-based system that:
- Classifies plastic using image recognition
- Provides instant feedback (recyclable / non-recyclable)
- Rewards users for recycling
- Tracks user activity through a dashboard

---

## 🔁 System Flow
User Uploads Image
↓
Image Preprocessing
↓
AI Model Prediction
↓
Classification Result
↓
Reward Allocation
↓
Dashboard Update + QR Reward
---

## ⚙️ Tech Stack

### 🖥️ Frontend
- Streamlit

### 🧠 Backend / AI
- Python
- TensorFlow / Keras

### 📦 Libraries Used
- NumPy
- PIL (Image Processing)
- QRCode
- Streamlit

---

## 🔥 Features

- ♻️ AI-based plastic classification
- 💰 Reward system (₹5 for recyclable, ₹2 for non-recyclable)
- 📊 Real-time dashboard (items, earnings, CO₂ saved)
- 📤 Image upload interface
- 📱 QR code generation for rewards
- ⚡ Instant prediction

---

## 📊 Dashboard Metrics

- Total Items Processed
- Total Earnings
- CO₂ Saved (simulated environmental impact)

---

## 🧠 How It Works

The model is trained using labeled image datasets:
- `recyclable` → bottles, containers
- `non_recyclable` → wrappers, thin plastics

The CNN model learns visual patterns such as:
- Shape
- Texture
- Structure

Based on similarity, it predicts the class of new images.

---

## 📁 Project Structure
EcoReward/
│
├── app.py                 # Main Streamlit application
├── train_model.py         # Model training script
├── plastic_model.h5       # Trained AI model
├── README.md              # Project documentation
│
└── TRAIN/                 # Dataset folder
    ├── recyclable/        # Images of recyclable plastic
    └── non_recyclable/    # Images of non-recyclable plastic
    ## ▶️ How to Run

### 1. Install dependencies
pip install streamlit tensorflow pillow numpy qrcode

### 2. Run the app
py -3.10 -m streamlit run app.py

---

## 🧪 Model Training

To retrain the model:
py -3.10 train_model.py

Make sure dataset is structured as:
TRAIN/ recyclable/ non_recyclable/

---

## 🌍 Impact

- Encourages eco-friendly behavior
- Reduces plastic pollution
- Promotes recycling awareness
- Can be integrated into smart cities

---

## 🚀 Future Scope

- Mobile app deployment
- Real-time camera detection
- GPS integration for recycling centers
- Multi-class waste classification
- Cloud database for user tracking

---

## 🌟 Uniqueness

- Combines AI + reward system
- Focuses on behavior change, not just detection
- Simple, scalable, and user-friendly
- Bridges gap between identification and action

---

## ⚡ Challenges Faced

- Dataset limitations
- Model accuracy for complex plastics
- Handling different lighting conditions

---

## ✅ Conclusion

This project demonstrates how Artificial Intelligence can be used to solve real-world environmental problems. It not only classifies plastic waste but also motivates users through a reward system, making recycling more engaging and impactful.

---

## 🙏 Acknowledgement

We thank the hackathon organizers, coordinators, and mentors for their guidance and support throughout the project.

---

## 🎉 Thank You!
