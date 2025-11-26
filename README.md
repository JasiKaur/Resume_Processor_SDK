# Resume Processor with Azure AI

This project uses Azure AI Language Services to extract key phrases, skills, and experience duration from resumes (`resume.txt`) and compare them with a predefined job description or skill set.

## Features
- Extract key phrases from resumes
- Identify skills and match them against a predefined skill list
- Extract total experience duration (e.g., "3 years", "5+ years")

## Requirements
- Python 3.10+
- Azure AI Language resource
- Packages: `azure-ai-language`, `python-dotenv`, `re`, `os`

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/JasiKaur/Resume_Processor_SDK.git

2. Create .env file:
   AZURE_KEY=<your-key>
   AZURE_ENDPOINT=<your-endpoint>

3. Install dependencies if already not installed:

4. Run the script:
   python Resume_Analysis.py
