from fastapi import FastAPI
from pydantic import BaseModel
from ai_conversation import generate_conversation
from text_to_speech import synthesize_conversation, play_audio
import os
from pydub import AudioSegment
from pydub.utils import which


# Explicitly set FFmpeg path for Pydub
ffmpeg_path = "E:\\Softwares\\ffmpeg-2025-01-30-git-1911a6ec26-essentials_build\\bin\\ffmpeg.exe"
AudioSegment.converter = ffmpeg_path
os.environ["FFMPEG_BINARY"] = ffmpeg_path  # Force FFmpeg for subprocess calls

# Debugging: Print the FFmpeg path to confirm
print("✅ FFmpeg Path Set:", AudioSegment.converter)

# Initialize FastAPI app
app = FastAPI()

class ConversationRequest(BaseModel):
    topic: str

@app.get("/")
def home():
    return {"message": "AI Podcast API is running!"}

@app.post("/generate-podcast/")
def generate_podcast(request: ConversationRequest):
    conversation = generate_conversation(request.topic)
    print(conversation)
    output_file = "output.mp3"
    synthesize_conversation(conversation, output_file)
    play_audio(output_file)
    return {"message": "Podcast generated and played successfully", "output_file": output_file}