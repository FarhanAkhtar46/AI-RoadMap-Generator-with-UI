from setuptools import setup, find_packages

setup(
    name="learning-roadmap-generator",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "langchain>=0.1.0",
        "openai>=1.0.0",
        "python-dotenv>=1.0.0",
        "graphviz>=0.20.1",
        "pydantic>=2.0.0",
    ],
    python_requires=">=3.9",
    author="Farhan Akhtar",
    author_email="farhan.akhtar@nathcorp.com",
    description="A multi-agent system for generating learning roadmaps",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)