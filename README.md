# AIPodcasts

# 🎙️ AI Podcasts – AI-Generated Conversations Using OpenAI & Python  

🚀 **AI Podcasts** is a Python-based project that generates realistic **AI-driven podcast conversations** using OpenAI’s API and text-to-speech (TTS) technology. The project allows AI personas to engage in natural, insightful discussions, producing high-quality MP3 podcast episodes.  

## 📌 Features  
✅ **AI Conversation Generation** – Uses OpenAI to create realistic dialogues between two AI personas  
✅ **Text-to-Speech (TTS)** – Converts generated text into high-quality MP3 audio  
✅ **Fully Automated** – Handles conversation flow, audio synthesis, and file generation  
✅ **Customizable Topics** – Generate podcasts on any subject by adjusting prompts  

## 🛠️ Tech Stack  
- **Python 3.11.9**  
- **OpenAI API (GPT & TTS)**  
- **gTTS / ElevenLabs (optional TTS alternatives)**  
- **FFmpeg (for audio processing)**  

## 🚀 Installation & Setup  

### **1️⃣ Clone the Repository**  
```bash
git clone https://github.com/Birla10/AIPodcasts.git
cd AIPodcasts
```

# 🎧 AI Podcasts – AI-Generated Podcast Conversations  

🚀 **AI Podcasts** is a Python-based project that generates realistic **AI-driven podcast conversations** using OpenAI’s API and text-to-speech (TTS) technology.  

---

## 🚀 Installation & Setup  

### 🔹 1⃣ Clone the Repository  
```bash
git clone https://github.com/Birla10/AIPodcasts.git
cd AIPodcasts
```

### 🔹 2⃣ Install Dependencies  
```bash
pip install -r requirements.txt
```

### 🔹 3⃣ Setup Your OpenAI API Key  
To get your OpenAI API Key, [click here](https://platform.openai.com/).

### 🔹 4⃣ Setup Environment Variables  
Once you have the API key, set the environment variable `OPENAI_API_KEY` with the key:  

#### **macOS/Linux**  
```bash
export OPENAI_API_KEY="your_openai_api_key"
```
#### **Windows**  
```bash
set OPENAI_API_KEY="your_openai_api_key"
```

---

## 🎤 Running the AI Podcast Generator  
To start the application, run:  
```bash
uvicorn app:app --reload
```

---

## 📁 API Endpoint to Generate the Podcast  

### **🎯 Endpoint:**  
```http
POST /generate-podcast
```

### **📌 Example Request:**  
```json
{
  "topic": "Current IT job market in USA and how it is effecting international students pursuing Masters in USA"
}
```

### **🎧 Sample Podcast Output:**  
A sample podcast generated using this application is saved as **output.mp3**.  

---

## ⭐ Support the Project  
If you find this project interesting, **give it a star** on GitHub! 🌟  

