import os
from openai import OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_conversation(topic: str) -> list:
    prompt = f"Generate a short, engaging conversation between two AIs about {topic}. Keep responses concise and human-like."

    try:
        print("Inside generate_conversation")
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300,
        )

        print("Response: ", response)
        if response.choices and response.choices[0].message:
            conversation = response.choices[0].message.content.strip().split("\n")
            print("conversation: ", conversation)
            return [line.strip() for line in conversation if line.strip()]  # Remove empty lines
        else:
            print("No valid response received.")
            return []

    except Exception as e:
        print(f"Error: {e}")
        return []


