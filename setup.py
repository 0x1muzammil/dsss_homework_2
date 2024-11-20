
#### `setup.py`
Defines your package's metadata and entry point:
```python
from setuptools import setup, find_packages

setup(
    name="math_quiz",
    version="0.1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[],  # Dependencies (if any)
    author="Muhammad Muzammil Saleem",
    author_email="muzammil.saleem@fau.de",
    description="A simple Python package for math quizzes",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/0x1muzammil/math-quiz",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
