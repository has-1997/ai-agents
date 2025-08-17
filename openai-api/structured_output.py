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


# Examples
# Chain of thought - Structured Outputs for chain-of-thought math tutoring
# class Step(BaseModel):
#     explanation: str
#     output: str

# class MathReasoning(BaseModel):
#     steps: list[Step]
#     final_answer: str

# response = client.responses.parse(
#     model=model,
#     input=[
#         {
#             "role": "system",
#             "content": "You are a helpful math tutor. Guide the user through the solution step by step.",
#         },
#         {"role": "user", "content": "how can I solve 8x + 7 = -23"},
#     ],
#     text_format=MathReasoning,
# )

# math_reasoning = response.output_parsed

# print(math_reasoning)
