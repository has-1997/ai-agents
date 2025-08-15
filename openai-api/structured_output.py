from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel

load_dotenv()

client = OpenAI()
model = "gpt-5-nano-2025-08-07"

# Getting a structured response
# class CalendarEvent(BaseModel):
#     name: str
#     date: str
#     participants: list[str]

# response = client.responses.parse(
#     model=model,
#     input=[
#         {
#             "role": "system",
#             "content": "Extract the event information."
#         }, 
#         {
#             "role": "user",
#             "content": "Alice and Bob are going to a science fair on Friday."
#         }
#     ],
#     text_format=CalendarEvent
# )

# event = response.output_parsed

# print(event)