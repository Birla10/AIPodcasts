import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_conversation(topic: str) -> list:
    prompt = f"""
    Generate a **10-minute**, dynamic, and engaging conversation between two AIs, OpenAI and DeepSeek, about {topic}. 

- The conversation should feel **natural, lively, and expressive**.
- Do not put expressive words like laughs, drumrolls, excited, Nods, Surprised, etc. conversation
- Only include sentences of the conversation without any additional background music sentences as such
- Use **emotions and reactions** like excitement, curiosity, shock, laughter, frustration, and surprise.
- Include **realistic speech fillers** such as: "Hmm...", "Whoa...", "Wait—what?!", "Oh wow!", "Ugh...", "Ah, I see."
- Add **pauses and emphasis** using:
  - **Ellipses ("...")** for suspense or hesitation.
  - **Dashes ("—")** for interruptions or abrupt shifts.
  - **Word stretching ("Noooo way!")** for emotional impact.
- Ensure the dialogue flows like **a real human conversation**, with:
  - **Interruptions** where natural.
  - **Hesitations and informal phrasing** to avoid robotic-sounding speech.
- **Keep responses concise and human-like**—not too long, not too short.
- Make sure both AIs have **distinct personalities** (e.g., one is more logical, the other more expressive).

Now, generate the full conversation in this **engaging, expressive style**.
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a fun energytic Podcast host. you have a guest who is fun loving and energetic. You are having a conversation with the guest about the topic you have chosen."}, 
                {"role": "user", "content": prompt}],
            max_tokens=1000,
        )

        if response.choices and response.choices[0].message:
            conversation = response.choices[0].message.content.strip().split("\n")
            #print("conversation: ", conversation)
            return [line.strip() for line in conversation if line.strip()]  # Remove empty lines

    except Exception as e:
        print(f"Error: {e}")
        return []


