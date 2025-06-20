from dotenv import load_dotenv
import os

load_dotenv()

# endpoint = ""
# deployment = ""
# subscription_key = ""

AZURE_DOC_INTEL_ENDPOINT = os.getenv("AZURE_DOC_INTEL_ENDPOINT")
AZURE_DOC_INTEL_KEY = os.getenv("AZURE_DOC_INTEL_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
AZURE_OPENAI_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
# AZURE_OPENAI_ENDPOINT = endpoint
# AZURE_OPENAI_KEY = subscription_key
# AZURE_OPENAI_DEPLOYMENT = deployment

