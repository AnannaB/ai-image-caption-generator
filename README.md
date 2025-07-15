# 🖼️ AI Image Caption Generator

An AI-powered web application that generates captions for uploaded images using deep learning (CNN + LSTM).  
Built with **React (Frontend)** and **Flask (Backend)**, using a pre-trained model trained on the MS COCO dataset.

---

## 🔍 Features

- 📤 Upload an image via browser
- 🧠 Backend uses a pre-trained **CNN+LSTM** model
- ✨ Displays **automatically generated caption**
- 🎨 Preview image before submission
- 📝 Options to **copy** or **download** the caption
- 🌐 Built with modern stack: **React + Flask**
- 🎯 Responsive UI with **Bootstrap/Tailwind**

---

## 🚀 Demo


https://github.com/user-attachments/assets/4633df51-e13a-4f1b-a26d-db0669b932b6



---

## 🛠️ Tech Stack

| Frontend     | Backend     | AI Model          |
| ------------ | ----------- | ---------------- |
| React.js     | Flask       | CNN + LSTM (COCO Dataset) |
| Axios        | Flask-CORS  | transformers, torch |
| Bootstrap / Tailwind CSS | Python | torchvision, Pillow |

---

## 🧪 Getting Started

### 1. Clone the Repo

```bash
git clone https://github.com/AnannaB/ai-image-caption-generator.git
cd ai-image-caption-generator
```
### 2. Set up Backend (Flask)
```bash
cd backend
python -m venv venv
venv\Scripts\activate      
pip install -r requirements.txt
python app.py
```             

### 3. Set up Frontend (React)
```bash
cd frontend
npm install
npm start                  
```
### 📸 How It Works

1. Upload any image from your device
   
2. The backend processes it through a CNN+LSTM model
   
3. Captions are predicted and returned to frontend

4. Users can preview, copy, or download the result
   

### 💡 Future Improvements

🔄 Drag-and-drop image support

💾 History of uploaded images

🌍 Multi-language support

📦 Dockerize the app for easier deployment

☁️ Deploy to Render / Vercel / Netlify / Railway


### 🙋‍♀️ Author

Ananna Basak

📫  [GitHub](https://github.com/AnannaB)| 🌐 [Portfolio](https://calm-cat-1c6798.netlify.app/)
