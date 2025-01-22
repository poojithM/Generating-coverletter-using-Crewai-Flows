# Cover Letter Generator System Documentation

## Overview
The Cover Letter Generator system is designed to automate the creation of personalized cover letters based on a job description and the content of a resume. This system utilizes Python, PyPDF2 for PDF manipulation, pydantic for data modeling, and the CrewAI library for managing multi-agent workflows. The core functionality is wrapped in a Python-based flow that reads a job description, extracts text from a resume PDF, and generates a cover letter by coordinating between different agents.

## Installation
Before running the system, ensure that you have Python installed on your machine. Then, follow these steps to set up the environment and dependencies:

1. **Clone the Repository:**
   Clone or download the project repository to your local machine.

2. **Install Dependencies:**
   Navigate to the project directory and install the required Python packages:
   ```bash
   pip install PyPDF2 pydantic crewai python-dotenv
   ```
   **Environment Variables:**
   Create a .env file in the root directory of the project and add any necessary environment variables as key-value pairs.

## Usage
To run the Cover Letter Generator, execute the following command from the root directory of the project:
```bash
python <script_name>.py
```
This will initiate the CoverLetterFlow, which performs the following steps:

### Flow Steps
1. **Read Job Description:** The job description is hardcoded into the flow for demonstration purposes. This can be modified to read from an external source.
2. **Read Resume:** The resume PDF named 'Poojith_AI.pdf' is read, and its content is extracted using PyPDF2. This is currently set to read the first page only. Modify as necessary for longer documents.
3. **Generate Cover Letter:** Using the extracted job description and resume data, a cover letter is generated. This step involves the coverletter crew which processes the input data through its specialized agents.

## Components
### CrewAI
- **Agents:** Defined in `config/agents.yaml`, these are specialized workers that perform specific tasks such as data processing or writing.
- **Tasks:** Defined in `config/tasks.yaml`, these tasks are assigned to agents and managed by the crew based on the process defined.
- **Crew:** The crew coordinates tasks among different agents. The process is sequential, ensuring tasks are completed in the necessary order.
