import json
from azure.ai.documentintelligence import DocumentIntelligenceClient
from azure.ai.documentintelligence.models import AnalyzeDocumentRequest, DocumentContentFormat
from azure.core.credentials import AzureKeyCredential
from utils.config import AZURE_DOC_INTEL_ENDPOINT, AZURE_DOC_INTEL_KEY


def get_ocr(pdf_path: str, output_path: str):
    
    with open(pdf_path, "rb") as f:
        file_bytes = f.read()

    # Set up the client
    client = DocumentIntelligenceClient(AZURE_DOC_INTEL_ENDPOINT, AzureKeyCredential(AZURE_DOC_INTEL_KEY))

    with open(pdf_path, "rb") as f:
        file_bytes = f.read()

    # Run analysis
    poller = client.begin_analyze_document(model_id="prebuilt-layout",
                body=AnalyzeDocumentRequest(bytes_source=file_bytes),
        output_content_format=DocumentContentFormat.Markdown
    )
    content = poller.result().content

    # Save the content to a file
    with open(output_path, "w") as f:
        json.dump(content, f, indent=2)
    print(f"OCR content saved to {output_path}")
    
    return content