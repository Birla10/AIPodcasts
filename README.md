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

**Install Dependencies**
pip install -r requirements.txt

**Setup you OpenAI API Key**
To get you OpenAI API Key, [click here](https://platform.openai.com/docs/overview)

**Setup envinonment variables**
Once you got the keys set the env variable "OPENAI_API_KEY" with the key

**🎤 Running the AI Podcast Generator**
uvicorn app:app --reload

**Endpoint to generate the Podcast**
/generate-podcast

**Example request:**
POST //generate-podcast

{
    "topic": "Current IT job market in USA and how it is effecting international students pursuing Masters in USA"
}

Sample Podcast generated using the application is **output.mp3**

⭐ If you find this project interesting, give it a star on GitHub! 🌟
