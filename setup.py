from setuptools import setup, find_packages

setup(
    name="clarity-coach",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "spacy",
        "fuzzywuzzy",
        "python-docx",
        "pandas",
        "PyPDF2",
        "openpyxl",
        "pypandoc"
    ],
    entry_points={
        "console_scripts": [
            "clarity-coach=clarity_coach.__init__:main",
        ],
    },
    author="Soeleece Benjamin",
    description="An intelligent text clarity assistant that detects spelling, grammar, and jargon issues and exports multi-format reports.",
    license="MIT",
)
