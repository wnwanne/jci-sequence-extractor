from utils.azure_ocr import get_ocr
from utils.vision_inference import convert_pdf_to_images, analyze_with_vision
import os
import json
from utils.config import AZURE_OPENAI_ENDPOINT, AZURE_OPENAI_KEY, AZURE_OPENAI_DEPLOYMENT


pdf_file_path = "input/Ex4.pdf"  # Path to your PDF file
output_folder = "output/images"  # Folder to save images
ocr_output_path = "output/ocr.json"  # Path to save OCR output

# Ensure output directories exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
if not os.path.exists(ocr_output_path):
    with open(ocr_output_path, 'w') as f:
        f.write("{}")  # Create an empty JSON file if it doesn't exist
if not os.path.exists(pdf_file_path):
    raise FileNotFoundError(f"The specified PDF file does not exist: {pdf_file_path}")

# Get OCR from the PDF file
ocr = get_ocr(pdf_file_path, ocr_output_path)
print(f"OCR content extracted and saved to {ocr_output_path}")

# Convert PDF to images
images = convert_pdf_to_images(pdf_file_path, output_folder)
print(f"PDF converted to images and saved in {output_folder}")

#-------------------------------------------------------------------------------------------------------*
# Assuming the first page is the one we want to analyze
image_path = os.path.join(output_folder, "page_1.png")  # Path to the first page image
#-------------------------------------------------------------------------------------------------------*

system_prompt = """"You are analyzing a manufacturing or engineering document. Your goal is to extract the **"Sequence of Operation:"** listed within this document. 
Specifically, the "Sequence of Operation" sections may be numbered/lettered or bulleted, while others may just be in paragraph form. Pay attention to any "continued" or "continued on next page" indicators, as these may indicate that the sequence of operations spans multiple columns or pages.
                You should analyze both the image and the text to identify and extract all the "Sequence of Operation" steps.
                - Look for numbered steps, procedural language, or headers like “Sequence of Operation:” 
                - Use both the visual and textual context to resolve ambiguities.
                - Do not include any other content from the document.
                - Focus solely on the "Sequence of Operation" content.
                - If the "Sequence of Operation" is split across multiple pages or columns, ensure you capture all parts.
                - Do not summarize or interpret the content; just extract the "Sequence of Operation" text as it appears in the document.
                - Exclude unrelated instructions, footnotes, or metadata.

                Output the result into a structured JSON format like this where you notate the number of "Sequence of Operation" (SOPs) and their content:

                {
                "number_of_sops": 2,
                "sops":[
                    {"sop_no":1,
                    "part_no": "RTU-1",
                    "sop_content": "some text"
                    },
                    {"sop_no":2,
                    "part_no": "RTU-2",
                    "sop_content": "some text"
                    }
                ]
                }"""

user_prompt = """The following is a page from an engineering document. Here is the OCR-extracted text:{ocr_text}

                Please analyze both the OCR and the visual layout in the image to identify all the "Sequence of Operation" sections and accompanying text listed under "Sequence of Operations."

                Some of the "Sequence of Operations" may be numbered or bulleted, while others may be in paragraph form.
                Look for any visual cues in the image that may indicate the "Sequence of Operations" sections.

                Return the result in the structured json format:""".format(ocr_text=ocr)

# Analyze the first page image with the provided prompts
json_response = json.loads(analyze_with_vision(image_path, system_prompt, user_prompt))
print("Analysis complete. JSON response:")
print(json.dumps(json_response, indent=2))
# Save the JSON response to a file
output_json_path = "output/analysis_result.json"
with open(output_json_path, 'w') as f:
    json.dump(json_response, f, indent=2)

