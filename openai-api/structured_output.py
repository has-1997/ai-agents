from dotenv import load_dotenv
from openai import OpenAI
from pydantic import BaseModel
from enum import Enum
from typing import List

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
# Example response:
# {
#     "steps": [
#         {
#             "explanation": "Start with the equation 8x + 7 = -23.",
#             "output": "8x + 7 = -23",
#         },
#         {
#             "explanation": "Subtract 7 from both sides to isolate the term with the variable.",
#             "output": "8x = -23 - 7",
#         },
#         {
#             "explanation": "Simplify the right side of the equation.",
#             "output": "8x = -30",
#         },
#         {
#             "explanation": "Divide both sides by 8 to solve for x.",
#             "output": "x = -30 / 8",
#         },
#         {"explanation": "Simplify the fraction.", "output": "x = -15 / 4"},
#     ],
#     "final_answer": "x = -15 / 4",
# }

# Structured data extraction - Extracting data from research papers using Structured Outputs
# class ResearchPaperExtraction(BaseModel):
#     title: str
#     authors: list[str]
#     abstract: str
#     keywords: list[str]

# response = client.responses.parse(
#     model=model,
#     input=[
#         {
#             "role": "system",
#             "content": "You are an expert at structured data extraction. You will be given unstructured text from a research paper and should convert it into the given structure.",
#         },
#         {
#             "role": "user",
#             "content": "The research paper is about the impact of AI on the job market."
#         }
#     ],
#     text_format=ResearchPaperExtraction
# )

# research_paper = response.output_parsed

# print(research_paper)
# Example response:
# {
#   "title": "Application of Quantum Algorithms in Interstellar Navigation: A New Frontier",
#   "authors": [
#     "Dr. Stella Voyager",
#     "Dr. Nova Star",
#     "Dr. Lyra Hunter"
#   ],
#   "abstract": "This paper investigates the utilization of quantum algorithms to improve interstellar navigation systems. By leveraging quantum superposition and entanglement, our proposed navigation system can calculate optimal travel paths through space-time anomalies more efficiently than classical methods. Experimental simulations suggest a significant reduction in travel time and fuel consumption for interstellar missions.",
#   "keywords": [
#     "Quantum algorithms",
#     "interstellar navigation",
#     "space-time anomalies",
#     "quantum superposition",
#     "quantum entanglement",
#     "space travel"
#   ]
# }


# UI Generation - Generating HTML using Structured Outputs
# class UIType(str, Enum):
#     div = "div"
#     button = "button"
#     header = "header"
#     section = "section"
#     field = "field"
#     form = "form"

# class Attribute(BaseModel):
#     name: str
#     value: str


# class UI(BaseModel):
#     type: UIType
#     label: str
#     children: list["UI"]
#     attributes: list[Attribute]

# UI.model_rebuild() # This is required to enable recursive types

# class Response(BaseModel):
#     ui: UI

# response = client.responses.parse(
#     model=model,
#     input=[
#         {
#             "role": "system",
#             "content": "You are a UI generator AI. Convert the user input into a UI.",
#         },
#         {
#             "role": "user",
#             "content": "Make a User Profile Form"
#         }
#     ],
#     text_format=Response
# )

# ui = response.output_parsed

# print(ui)

# Example response:
# {
#     "type": "form",
#     "label": "User Profile Form",
#     "children": [
#         {
#             "type": "div",
#             "label": "",
#             "children": [
#                 {
#                     "type": "field",
#                     "label": "First Name",
#                     "children": [],
#                     "attributes": [
#                         {"name": "type", "value": "text"},
#                         {"name": "name", "value": "firstName"},
#                         {"name": "placeholder", "value": "Enter your first name"},
#                     ],
#                 },
#                 {
#                     "type": "field",
#                     "label": "Last Name",
#                     "children": [],
#                     "attributes": [
#                         {"name": "type", "value": "text"},
#                         {"name": "name", "value": "lastName"},
#                         {"name": "placeholder", "value": "Enter your last name"},
#                     ],
#                 },
#             ],
#             "attributes": [],
#         },
#         {
#             "type": "button",
#             "label": "Submit",
#             "children": [],
#             "attributes": [{"name": "type", "value": "submit"}],
#         },
#     ],
#     "attributes": [
#         {"name": "method", "value": "post"},
#         {"name": "action", "value": "/submit-profile"},
#     ],
# }

