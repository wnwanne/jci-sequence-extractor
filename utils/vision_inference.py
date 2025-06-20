import os
import base64
from openai import AzureOpenAI
from pdf2image import convert_from_path
from utils.config import AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY, AZURE_OPENAI_DEPLOYMENT
from dotenv import load_dotenv; load_dotenv()



def convert_pdf_to_images(pdf_path, output_folder="output_images"):
    os.makedirs(output_folder, exist_ok=True)

    # Convert PDF to images
    images = convert_from_path(pdf_path, dpi=300)
    # Save each page as a PNG file
    for i, image in enumerate(images):
        image_path = os.path.join(output_folder, f"page_{i + 1}.png")
        image.save(image_path, "PNG")
        print(f"Saved: {image_path}")
    return images

# Create Azure OpenAI client
client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version="2025-01-01-preview",
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)
 
def analyze_with_vision(image_path, system_prompt, user_prompt):
    with open(image_path, "rb") as img_file:
        image_bytes = img_file.read()

    # Encode the image to base64
    encoded_image = base64.b64encode(open(image_path, 'rb').read()).decode('ascii')
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },

        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": user_prompt
                },

                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{encoded_image}"
                    }
                }
            ]
        }
    ]

    response = client.chat.completions.create(
    model=AZURE_OPENAI_DEPLOYMENT,
    messages=messages,
    temperature=1,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None,
    stream=False
)
    # Extract and return the content from the response
    completion_text = response.choices[0].message.content.strip()

    return completion_text

