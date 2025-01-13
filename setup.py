from setuptools import setup, find_packages

# Read the requirements from the requirements.txt file
with open("requirements.txt", "r", encoding="utf-8") as f:
    requirements = f.read().splitlines()

setup(
    name="summarization_lib",
    version="0.1.0",
    packages=find_packages(),
    install_requires=requirements,
    description="A library for summarizing text using Cohere and LangChain.",
    author="Melek Ghouma",
)
