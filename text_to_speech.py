import os
from pydub import AudioSegment

# from pydub.utils import which
# # Explicitly set FFmpeg path for Pydub
# # ffmpeg_path = "E:\\Softwares\\ffmpeg-2025-01-30-git-1911a6ec26-essentials_build\\bin\\ffmpeg.exe"
# # AudioSegment.converter = ffmpeg_path
# # os.environ["FFMPEG_BINARY"] = ffmpeg_path  # Force FFmpeg for subprocess calls

# # # Ensure Pydub can find FFmpeg
# # AudioSegment.ffmpeg = which("ffmpeg")
# # AudioSegment.ffprobe = which("ffprobe")

from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define different voices for AI-1 and AI-2
VOICE_AI_1 = "alloy"  
VOICE_AI_2 = "echo"  

def text_to_speech(text: str, voice_id: str, filename: str):
    
    text.split(':', 1)[1].strip()
    response = client.audio.speech.create(
        model="tts-1",
        voice=voice_id,
        input=text.split(':', 1)[1].strip(),
    )
    
    response.stream_to_file(filename)
    return filename 

def synthesize_conversation(conversation: list, output_filename: str):
    """
    Generate TTS for each line in the conversation with alternating voices and merge into a single file.
    """
    audio_files = []

    # folder for temporary files
    temp_folder = "temp_audio_files"

    # Create the folder if it doesn't exist
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    for index, line in enumerate(conversation):
        # Alternate between AI-1 and AI-2 voices
        voice_id = VOICE_AI_1 if index % 2 == 0 else VOICE_AI_2

        # Generate the temporary file path
        filename = os.path.join(temp_folder, f"line_{index}.mp3")

        # Convert text to speech
        audio_file = text_to_speech(line, voice_id, filename)
        if audio_file:
            audio_files.append(audio_file)

    # Merge all audio files into a single MP3 file
    if audio_files:
        merge_audio(audio_files, output_filename)

    # Delete the individual line audio files
    delete_files(audio_files)


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


def delete_files(files: list):
    """
    Delete multiple audio files.
    """
    for file in files:
        if os.path.exists(file):
            os.remove(file)
            print(f"Deleted {file}")
        else:
            print(f"File {file} not found")


def play_audio(file_path: str):
    os.system(f"start {file_path}") 
