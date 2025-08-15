from dotenv import load_dotenv
from openai import OpenAI
import base64

load_dotenv()

client = OpenAI()
model = "gpt-5-nano-2025-08-07"

# # Generate images with Responses
# response = client.responses.create(
#     model=model,
#     input="Generate an image of an iPad with a infinte universe within the screen",
#     tools=[{"type": "image_generation"}],
# )

# # Save the image to a file
# image_data = [
#     output.result
#     for output in response.output
#     if output.type == "image_generation_call"
# ]

# if image_data:
#     image_base64 = image_data[0]
#     with open("data/images/ipad_universe.png", "wb") as f:
#         f.write(base64.b64decode(image_base64))


# Analyze the content of an image - Passing a URL
# response = client.responses.create(
#     model=model,
#     input=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "input_text",
#                     "text": "What is in this image?"
#                 },
#                 {
#                     "type": "input_image",
#                     "image_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
#                 },
#             ]
#         }
#     ],
# )

# print(response.output_text)


# Analyze the content of an image - Passing a base64 encoded image

# Function to encode an image to base64
# def encode_image(image_path):
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode("utf-8")


# Path to your image
# image_path = "data/images/ipad_universe.png"

# Getting the Base64 string
# base64_image = encode_image(image_path)

# response = client.responses.create(
#     model=model,
#     input=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "input_text",
#                     "text": "What is in this image?"
#                 },
#                 {
#                     "type": "input_image",
#                     "image_url": f"data:image/png;base64,{base64_image}",
#                 }
#             ]
#         }
#     ]
# )

# print(response.output_text)


# Analyze the content of an image - Passing a file ID

# Function to create a file with the Files API
def create_file(file_path):
    with open(file_path, "rb") as file_content:
        result = client.files.create(
            file=file_content,
            purpose="vision"
        )
        return result.id
    
# Getting the file ID
file_id = create_file("data/images/ipad_universe.png")

response = client.responses.create(
    model=model,
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "What is in this image?"
                },
                {
                    "type": "input_image",
                    "file_id": file_id
                }
            ]
        }
    ]
)

print(response.output_text)