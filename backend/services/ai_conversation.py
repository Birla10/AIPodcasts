import os
from dotenv import load_dotenv
import logging
import time

from openai import OpenAI

from backend.services.text_to_speech import synthesize_conversation

logger = logging.getLogger(__name__)

class AIConversation:
    def __init__(self):
      
        load_dotenv()
        
        # Set up the OpenAI client using the API key from environment variables
        self.client = OpenAI(api_key=os.getenv("OPENAI_API"))
        # Load the GPT user prompt template from environment variables
        self.gpt_user_prompt = os.getenv("GPT_USER_PROMPT")
        # Load the GPT system prompt template from environment variables
        self.gpt_system_prompt = os.getenv("GPT_SYSTEM_PROMPT")
        # Load the GPT model from environment variables
        self.gpt_model = os.getenv("GPT_MODEL")

    def generate_conversation(self, topic: str):
        
        logger.info("Starting conversation generation.")
        
        # Replace the placeholder in the GPT prompt with the provided topic
        user_prompt = self.gpt_user_prompt.replace("[topic]", topic)

        try:
            # Send a request to the OpenAI API to generate a conversation
            # response = self.client.chat.completions.create(
            #     model=self.gpt_model,  # Specify the model to use
            #     messages=[
            #         # Define the system's role and behavior
            #         {"role": "system", "content": self.gpt_system_prompt}, 
            #         # Provide the user input (prompt with the topic)
            #         {"role": "user", "content": user_prompt}
            #     ],
            #     max_tokens=1000  # Limit the response to 1000 tokens
            # )

            # logger.info("API response received.", response)
            
            time.sleep(50)  
            
            # # Check if the response contains valid choices and extract the conversation
            # if response.choices and response.choices[0].message:
            #     # Split the response into lines and remove empty lines
            #     conversation = response.choices[0].message.content.strip().split("\n")
            #     final_convo = [line.strip() for line in conversation if line.strip()]  # Return the cleaned conversation

            #     logger.info("Conversation generation completed.")
    
            #     # Define the output file name for the synthesized audio
            #     output_file = "./podcast/output.mp3"
            #     logger.info(f"Output file for synthesized audio: {output_file}")
    
            #     # Synthesize the generated conversation into an audio file
            #     logger.info("Starting audio synthesis.")
            #     synthesize_conversation(final_convo, output_file)
            #     logger.info("Audio synthesis completed.")
    
            #     # Return a success message along with the name of the output file
            logger.info("Podcast generation process completed successfully.")
                
        except Exception as e:
            # Handle any exceptions that occur during the API call
            logger.error(f"Error: {e}")
            raise Exception(f"Error generating conversation: {e}")