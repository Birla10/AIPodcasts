from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel
import logging

from backend.services.ai_conversation import AIConversation

# Initialize FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

class ConversationRequest(BaseModel):
    topic: str

# Define a root endpoint to check if the API is running
@app.get("/")
def home():
    # Log a message indicating the API is operational
    logger.info("AI Podcast API is running!")
    # Return a simple JSON response
    return {"message": "AI Podcast API is running!"}

@app.post("/generate-podcast/")
def generate_podcast(request: ConversationRequest, background_tasks: BackgroundTasks):
    # Create an instance of the AIConversation class to handle conversation generation
    logger.info("Initializing AIConversation instance.")
    ai_conversation = AIConversation()
    
    # Log the topic for which the conversation is being generated
    logger.info(f"Generating conversation for topic: {request.topic}")
    
    # Generate a conversation based on the provided topic
    background_tasks.add_task(ai_conversation.generate_conversation, request.topic)
    
    return {"message": "Podcast generated started"}