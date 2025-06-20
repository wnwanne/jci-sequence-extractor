# JCI Sequence Extractor

**Extracts “Sequence of Operation” (SOP) sections from engineering or manufacturing PDFs using Azure OpenAI Vision and OCR, producing structured JSON for downstream automation, analytics, or compliance.**

---

## **Overview**

This tool automates the extraction of “Sequence of Operation” content from engineering PDFs—such as equipment submittals, control diagrams, and mechanical specs.
It combines OCR, image analysis, and Azure OpenAI Vision LLMs to ensure accurate, context-aware extraction even from complex layouts.

---

## **Key Features**

* Converts PDF pages to images for vision analysis.
* Runs OCR to extract all text from each page.
* Uses Azure OpenAI Vision models to analyze both the image and OCR text for SOP content.
* Supports multiple devices/sections per document (e.g., RTU-1, RTU-2 & 3).
* Outputs results as structured JSON, ready for downstream workflows or auditing.

---

## **Project Structure**

```
jci-sequence-extractor/
├── main_pipeline.py           # Main orchestration script
├── utils/
│   ├── azure_ocr.py           # OCR utility (Azure Computer Vision)
│   ├── vision_inference.py    # PDF-to-image & Vision model utilities
│   └── config.py              # Loads API keys and endpoints
├── input/                     # Folder for input PDF files (create this manually)
├── output/
│   ├── images/                # Page images (created automatically)
│   ├── ocr.json               # OCR results (created automatically)
│   └── analysis_result.json   # Final structured output (created automatically)
├── .env                       # API keys and endpoint config (not in repo)
├── .gitignore
├── requirements.txt
└── README.md
```

---

## **Setup**

1. **Clone the repo**

   ```bash
   git clone https://github.com/YOUR_USERNAME/jci-sequence-extractor.git
   cd jci-sequence-extractor
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your environment variables**

   * Create a `.env` file at the root (see `.env.example` if provided).
   * Add your Azure OpenAI and Computer Vision credentials:

     ```
     AZURE_OPENAI_ENDPOINT=https://your-resource-name.openai.azure.com/
     AZURE_OPENAI_KEY=your-azure-openai-key
     AZURE_OPENAI_DEPLOYMENT=gpt-4o
     AZURE_DOC_INTEL_ENDPOINT=https://your-cv-endpoint.cognitiveservices.azure.com/
     AZURE_DOC_INTEL_KEY=your-cv-key
     ```

4. **Prepare Input/Output Folders**

   * **Input:**
     Before running the script, create an `input/` folder in your project directory and add your source PDF(s) there (e.g., `input/Ex4.pdf`).
     The script expects the PDF file path to match what’s set in `main_pipeline.py`.
   * **Output:**
     The script will automatically create the `output/` and `output/images/` folders as needed and will write image and JSON files there.

---

## **Usage**

Run the pipeline on your document:

```bash
python main_pipeline.py
```

**Default input/output paths are set in `main_pipeline.py`:**

* Input: `input/Ex4.pdf`
* Output:

  * Images: `output/images/page_*.png`
  * OCR: `output/ocr.json`
  * Final result: `output/analysis_result.json`

**Modify the script if you want to process different files or folders.**

---

## **Sample Output**

The output JSON will look like:

```json
{
  "number_of_sops": 2,
  "sops": [
    {
      "sop_no": 1,
      "part_no": "RTU-1",
      "sop_content": "..."
    },
    {
      "sop_no": 2,
      "part_no": "RTU-2",
      "sop_content": "..."
    }
  ]
}
```

---

## **Customization**

* Change prompts in `main_pipeline.py` for different document structures.
* Update the `utils/` modules for alternate OCR or image-handling backends.

---

## **Troubleshooting**

* **No output or errors?**
  Double-check your `.env` keys and endpoints. Make sure your PDF is OCR-readable.
* **OCR issues:**
  Try preprocessing PDFs to improve clarity (deskew, remove noise).
* **Model/auth errors:**
  Ensure your Azure OpenAI deployment and API version are compatible.

---

## **Contributing**

Open a pull request or issue if you have improvements, bugfixes, or new feature ideas!

---

## **License**

MIT (or your preferred license)
