#!/usr/bin/env python
from PyPDF2 import PdfReader

from pydantic import BaseModel

from crewai.flow.flow import Flow, listen, start

from crews.coverletter_crew.coverletter import coverletter
from dotenv import load_dotenv

load_dotenv()


class coverletterstate(BaseModel):
    job_description : str = ""
    resume: str = ""


class CoverLetterFlow(Flow[coverletterstate]):

    @start()
    def read_job_desc(self):
        desc = """
        About the job
        Specialty/Competency: Data, Analytics & AI

        Industry/Sector: EUR X-Sector

        Time Type: Full time

        Travel Requirements: Up to 80%

        At PwC, our people in data and analytics engineering focus on leveraging advanced technologies and techniques to design and develop robust data solutions for clients. They play a crucial role in transforming raw data into actionable insights, enabling informed decision-making and driving business growth. Those in data science and machine learning engineering at PwC will focus on leveraging advanced analytics and machine learning techniques to extract insights from large datasets and drive data-driven decision making. You will work on developing predictive models, conducting statistical analysis, and creating data visualisations to solve complex business problems.

        Driven by curiosity, you are a reliable, contributing member of a team. In our fast-paced environment, you are expected to adapt to working with a variety of clients and team members, each presenting varying challenges and scope. Every experience is an opportunity to learn and grow. You are expected to take ownership and consistently deliver quality work that drives value for our clients and success as a team. As you navigate through the Firm, you build a brand for yourself, opening doors to more opportunities.

        Skills

        Examples of the skills, knowledge, and experiences you need to lead and deliver value at this level include but are not limited to:

        Apply a learning mindset and take ownership for your own development.
        Appreciate diverse perspectives, needs, and feelings of others.
        Adopt habits to sustain high performance and develop your potential.
        Actively listen, ask questions to check understanding, and clearly express ideas.
        Seek, reflect, act on, and give feedback.
        Gather information from a range of sources to analyse facts and discern patterns.
        Commit to understanding how the business works and building commercial awareness.
        Learn and apply professional and technical standards (e.g. refer to specific PwC tax and audit guidance), uphold the Firm's code of conduct and independence requirements.

        Basic Qualifications

        Job Requirements and Preferences

        Minimum Degree Required

        Bachelor's Degree

        Required Field(s) Of Study

        Management Information Systems,Management Information Systems & Accounting,Management of Technology,Systems Engineering,Mathematical Statistics,Mathematics,Electrical Engineering,Industrial Engineering,Computer and Information Science & Accounting

        Minimum Year(s) Of Experience

        1 year(s)

        Preferred Qualifications

        Preferred Knowledge/Skills

        Demonstrates thorough-level abilities and/or a proven record of success managing the identification and addressing of client needs:

        Building of GenAI and AI solutions, including but not limited to analytical model development and implementation, prompt engineering, general all-purpose programming (e.g., Python), testing, communication of results, front end and back-end integration, and iterative development with clients 
        Documenting and analyzing business processes for AI and Generative AI opportunities, including gathering of requirements, creation of initial hypotheses, and development of GenAI and AI solution approach 
        Collaborating with client team to understand their business problem and select the appropriate analytical models and approaches for AI and GenAI use cases 
        Designing and solutioning AI/GenAI architectures for clients, specifically for plugin-based solutions (i.e., ChatClient application with plugins) and custom AI/GenAI application builds 
        Processing unstructured and structured data to be consumed as context for LLMs, including but not limited to embedding of large text corpus, generative development of SQL queries, building connectors to structured databases 
        Support management of daily operations of a global data and analytics team on client engagements, review developed models, provide feedback and assist in analysis; 
        Directing data engineers and other data scientists to deliver efficient solutions to meet client requirements; 
        Leading and contributing to development of proof of concepts, pilots, and production use cases for clients while working in cross-functional teams; 
        Structuring, write, communicate and facilitate client presentations; and, 
        Directing associates through coaching, providing feedback, and guiding work performance. 

        Demonstrates Thorough Abilities And/or a Proven Record Of Success Learning And Performing In Functional And Technical Capacities, Including The Following Areas

        Managing AI/GenAI application development teams including back-end and front-end integrations 
        Using Python (e.g., Pandas, NLTK, Scikit-learn, Keras etc.), common LLM development frameworks (e.g., Langchain, Semantic Kernel), Relational storage (SQL), Non-relational storage (NoSQL); 
        Experience in analytical techniques such as Machine Learning, Deep Learning and Optimization 
        Vectorization and embedding, prompt engineering, RAG (retrieval, augmented, generation) workflow dev 
        Understanding or hands on experience with Azure, AWS, and / or Google Cloud platforms 
        Experience with Git Version Control, Unit/Integration/End-to-End Testing, CI/CD, release management, etc. 

        Learn more about how we work: https://pwc.to/how-we-work

        PwC does not intend to hire experienced or entry level job seekers who will need, now or in the future, PwC sponsorship through the H-1B lottery, except as set forth within the following policy: https://pwc.to/H-1B-Lottery-Policy.

        All qualified applicants will receive consideration for employment at PwC without regard to race; creed; color; religion; national origin; sex; age; disability; sexual orientation; gender identity or expression; genetic predisposition or carrier status; veteran, marital, or citizenship status; or any other status protected by law. PwC is proud to be an affirmative action and equal opportunity employer.

        For positions based in San Francisco, consideration of qualified candidates with arrest and conviction records will be in a manner consistent with the San Francisco Fair Chance Ordinance.

        Applications will be accepted until the position is filled or the posting is removed, unless otherwise set forth on the following webpage. Please visit this link for information about anticipated application deadlines: https://pwc.to/us-application-deadlines

        The salary range for this position is: $75,000 - $118,000, plus individuals may be eligible for an annual discretionary bonus. For roles that are based in Maryland, this is the listed salary range for this position. Actual compensation within the range will be dependent upon the individual's skills, experience, qualifications and location, and applicable employment laws. PwC offers a wide range of benefits, including medical, dental, vision, 401k, holiday pay, vacation and more. To view our benefits at a glance, please visit the following link: https://pwc.to/benefits-at-a-glance"""
        self.job_description = desc

    @listen(read_job_desc)
    def read_resume(self):
        pdf_docs = "Poojith_AI.pdf"
        pdf_reader = PdfReader(pdf_docs)
        page_text = pdf_reader.pages[0].extract_text()
        text = page_text.split('\n')
        complete_text =  "\n".join(text)
        self.resume = complete_text
    
    
    
    @listen(read_resume)
    def generate_cover_letter(self):
        print("Cover letter")
        
        crew = coverletter()
        inputs = {
            "job_description" : self.job_description,
            "resume" : self.resume,
        }
        result = (
            crew
            .crew()
            .kickoff(inputs=inputs)
        )

        

    


def kickoff():
    coverleter = CoverLetterFlow()
    coverleter.kickoff()



if __name__ == "__main__":
    kickoff()
