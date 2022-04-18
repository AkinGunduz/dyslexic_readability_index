import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dyslexic-readability",
    version="0.0.1",
    author="Akin Gunduz",
    author_email="akngndz93@gmail.com",
    description="A readability scoring library tailored to the specific needs of Turkish dyslexic readers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/AkinGunduz/dyslexic_readability_index",
    project_urls={
        "Bug Tracker": "https://github.com/AkinGunduz/dyslexic_readability_index/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)