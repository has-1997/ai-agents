from dotenv import load_dotenv
from openai import OpenAI
import base64

load_dotenv()

client = OpenAI()
model = "gpt-4o-audio-preview-2025-06-03"

# Audio output from model
# Create a human-like audio response to a prompt
# completion = client.chat.completions.create(
#     model=model,
#     modalities=["text", "audio"],
#     audio={ "voice": "alloy", "format": "wav" },
#     messages=[
#         {
#             "role": "user",
#             "content": "Compare the estimated market size of Humanoid Robots, Self-driving Cars, and DeFAI in 2030"
#         }
#     ]
# )

# print(completion.choices[0])

# wav_bytes =  base64.b64decode(completion.choices[0].message.audio.data)
# with open("data/audio/market_size.wav", "wb") as f:
#     f.write(wav_bytes)


# Audio input to model 
# Use audio inputs for prompting a model
