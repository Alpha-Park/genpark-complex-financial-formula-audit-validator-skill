from setuptools import setup, find_packages

setup(
    name="genpark-financial-validator",
    version="1.0.0",
    description="Mathematical accounting formula consistency and balance-sheet footing auditor.",
    long_description=open("README.md", encoding="utf-8").read() if __import__("os").path.exists("README.md") else "Mathematical accounting formula consistency and balance-sheet footing auditor.",
    long_description_content_type="text/markdown",
    author="GenPark AI Engineering",
    author_email="engineering@genpark.ai",
    url="https://github.com/Alpha-Park/genpark-complex-financial-formula-audit-validator-skill",
    py_modules=["client", "mcp_server"],
    python_requires=">=3.9",
    install_requires=[],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
