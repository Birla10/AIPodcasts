import os
import logging

from pydub import AudioSegment

from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Define different voices for AI-1 and AI-2
VOICE_AI_1 = "alloy"  
VOICE_AI_2 = "echo"  

logger = logging.getLogger(__name__)

def text_to_speech(text: str, voice_id: str, filename: str):
    """
    Convert text to speech using the specified voice and save it to a file.

    Args:
        text (str): The text to be converted to speech.
        voice_id (str): The voice ID to use for TTS.
        filename (str): The file path to save the generated audio.

    Returns:
        str: The file path of the generated audio file.
    """
    try:
        # Extract the actual speech content after the colon
        speech_content = text.split(':', 1)[1].strip()

        # Call the OpenAI API to generate speech
        response = client.audio.speech.create(
            model="tts-1",
            voice=voice_id,
            input=speech_content,
        )

        # Save the generated audio to the specified file
        response.stream_to_file(filename)
        return filename

    except Exception as e:
        logger.error(f"Error generating TTS for text: '{text}' with voice: '{voice_id}'. Error: {e}")
        return None

def synthesize_conversation(conversation: list, output_filename: str):
    """
    Generate TTS for each line in the conversation with alternating voices and merge into a single file.

    Args:
        conversation (list): A list of strings representing the conversation lines.
        output_filename (str): The file path to save the final merged audio file.
    """
    logger.info("Starting conversation synthesis...")
    audio_files = []

    # Folder for temporary audio files
    temp_folder = "./temp_audio_files/"

    # Create the folder if it doesn't exist
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)
        logger.info(f"Created temporary folder: {temp_folder}")

    for index, line in enumerate(conversation):
        # Alternate between AI-1 and AI-2 voices
        voice_id = VOICE_AI_1 if index % 2 == 0 else VOICE_AI_2
        # Generate the temporary file path
        filename = os.path.join(temp_folder, f"line_{index}.mp3")

        # Convert text to speech
        audio_file = text_to_speech(line, voice_id, filename)
        if audio_file:
            audio_files.append(audio_file)
        else:
            logger.warning(f"Failed to generate audio for line {index + 1}")

    # Merge all audio files into a single MP3 file
    if audio_files:
        logger.info("Merging all audio files into the final output...")
        merge_audio(audio_files, output_filename)
        logger.info(f"Final conversation audio saved as: {output_filename}")
    else:
        logger.warning("No audio files were generated. Skipping merge step.")

    # Delete the individual line audio files
    logger.info("Cleaning up temporary audio files...")
    delete_files(audio_files)
    logger.info("Temporary audio files deleted.")


def merge_audio(files: list, output_filename: str):
    """
    Merge multiple audio files into a single conversation audio file.

    Args:
        files (list): A list of file paths to the audio files to be merged.
        output_filename (str): The file path to save the final merged audio file.
    """
    logger.info("Starting audio merging process...")
    combined = AudioSegment.empty()

    for file in files:
        try:
            # Load the audio file
            sound = AudioSegment.from_mp3(file)

            # Append the audio file to the combined audio with a short pause
            combined += sound + AudioSegment.silent(duration=500)  # Adding short pause

        except Exception as e:
            logger.error(f"Error processing file {file}: {e}")
    try:
        # Export the combined audio to the specified output file
        logger.info(f"Exporting combined audio to: {output_filename}")
        combined.export(output_filename, format="mp3")
        logger.info(f"Final conversation audio saved as: {output_filename}")

    except Exception as e:
        logger.error(f"Error exporting combined audio to {output_filename}: {e}")


def delete_files(files: list):
    """
    Delete multiple audio files.

    Args:
        files (list): A list of file paths to the audio files to be deleted.
    """
    logger.info("Starting cleanup of temporary audio files...")
    for file in files:
        try:
            if os.path.exists(file):
                # Delete the file
                os.remove(file)
            else:
                # Log if the file does not exist
                logger.warning(f"File not found, skipping deletion: {file}")
        except Exception as e:
            # Log any errors encountered during file deletion
            logger.error(f"Error deleting file {file}: {e}")
    logger.info("Cleanup of temporary audio files completed.")


# def play_audio(file_path: str):
#     os.system(f"start {file_path}") 
