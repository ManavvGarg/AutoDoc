from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()

# Initialize the GROQ model
client = Groq(api_key=os.getenv("API_KEY"))

# Function to generate README.md content using GROQ
def generate_readme(project_files):
    prompt = f"Generate a README.md based on the following files:\n{project_files}"
    
    response = client.chat.completions.create(
        model="gemma-7b-it",
        messages=[
            {
            "role": "system",
            "content": "You are an expert technical writer specializing in generating clear, concise, and professional README.md files for software projects. Your task is to create a comprehensive README.md based on the provided project files. The README should include the following sections: Project Title, Description, Features, Installation Instructions, Usage Guide, Screenshots (if applicable), Contributing Guidelines, License, and Contact Information. Ensure the instructions are easy to follow, and the content is accessible to both beginners and experienced users. Use an informative, engaging, and welcoming tone to encourage contributions."
            },
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content.strip() + "\n\n_____\n\nDocumentation Generated by [AutoDoc](https://github.com/manavvgarg/autodoc) | 2024"

# Function to generate DOCUMENTATION.md
def generate_documentation(project_files):
    prompt = f"Generate a DOCUMENTATION.md for the project with files:\n{project_files}"
    
    response = client.chat.completions.create(
        model="gemma-7b-it",
        messages=[
           {
            "role": "system",
            "content": "You are an expert technical writer specializing in creating detailed and well-structured DOCUMENTATION.md files for software projects. Your task is to generate a comprehensive DOCUMENTATION.md for a project based on the provided files. The DOCUMENTATION should include the following sections: Introduction, Usage, API Reference (if applicable), Examples, All the function definitions from the code (if they aren't present then write what the function does in a very brief manner and what kind of parameters it takes), Also Mention what all libraries are being used in this project properly to ensure good understanding of the project by people. Ensure clarity, accuracy, and helpfulness for both new and experienced users. Provide examples where necessary, and use a formal but approachable tone."
            },
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content.strip() + "\n\n_____\n\nDocumentation Generated by [AutoDoc](https://github.com/manavvgarg/autodoc) | 2024"
