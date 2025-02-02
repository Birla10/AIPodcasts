import requests
import os
from pydub import AudioSegment
from pydub.utils import which

# Explicitly set FFmpeg path for Pydub
ffmpeg_path = "E:\\Softwares\\ffmpeg-2025-01-30-git-1911a6ec26-essentials_build\\bin\\ffmpeg.exe"
AudioSegment.converter = ffmpeg_path
os.environ["FFMPEG_BINARY"] = ffmpeg_path  # Force FFmpeg for subprocess calls

# Ensure Pydub can find FFmpeg
AudioSegment.ffmpeg = which("ffmpeg")
AudioSegment.ffprobe = which("ffprobe")

# Debugging: Print the FFmpeg path to confirm
print("✅ FFmpeg Path Set:", AudioSegment.converter)

ELEVEN_LABS_API_KEY = os.getenv("ELEVEN_LABS_API_KEY")  # Add your Eleven Labs API Key

# Define different voices for AI-1 and AI-2
VOICE_AI_1 = "21m00Tcm4TlvDq8ikWAM"  # Example Voice ID for AI-1
VOICE_AI_2 = "EXAVITQu4vr4xnSDxMaL"  # Example Voice ID for AI-2

def text_to_speech(text: str, voice_id: str, filename: str):
    """
    Convert text to speech using Eleven Labs API and save it as an audio file.
    """
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"

    headers = {
        "xi-api-key": ELEVEN_LABS_API_KEY,
        "Content-Type": "application/json",
    }

    data = {
        "text": text,
        "model_id": "eleven_monolingual_v1",
        "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.7
        }
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        with open(filename, "wb") as f:
            f.write(response.content)
        print(f"Audio saved as {filename}")
        return filename
    else:
        print(f"Error: {response.json()}")
        return None


def synthesize_conversation(conversation: list, output_filename: str):
    """
    Generate TTS for each line in the conversation with alternating voices and merge into a single file.
    """
    audio_files = []

    for index, line in enumerate(conversation):
        # Alternate between AI-1 and AI-2 voices
        voice_id = VOICE_AI_1 if index % 2 == 0 else VOICE_AI_2
        filename = f"line_{index}.mp3"

        # Convert text to speech
        audio_file = text_to_speech(line, voice_id, filename)
        if audio_file:
            audio_files.append(audio_file)

    # Merge all audio files into a single MP3 file
    if audio_files:
        merge_audio(audio_files, output_filename)


def merge_audio(files: list, output_filename: str):
    """
    Merge multiple audio files into a single conversation audio file.
    """
    combined = AudioSegment.empty()

    for file in files:
        sound = AudioSegment.from_mp3(file)
        combined += sound + AudioSegment.silent(duration=500)  # Adding short pause

    combined.export(output_filename, format="mp3")
    print(f"Final conversation saved as {output_filename}")


def play_audio(file_path: str):
    os.system(f"start {file_path}")  # Windows: 'start', Mac/Linux: 'afplay' or 'mpg123'
