from setuptools import setup, find_packages

setup(
    name="llamafile-langchain",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["langchain-core"],
    author="Kenneth",
    description="LangChain wrapper for local GGUF models via llamafile",
    license="MIT",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
