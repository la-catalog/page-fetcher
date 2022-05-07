from pathlib import Path

from setuptools import find_packages, setup

long_description = Path("README.md").read_text()

setup(
    name="page-fetcher",
    version="0.0.1",
    description="Reponsable for getting the content of pages",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thiagola92/page-fetcher",
    author="thiagola92",
    author_email="thiagola92@gmail.com",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    keywords="web, scraper, crawler",
    license="MIT",
    packages=find_packages(exclude=["tests"]),
    install_requires=[
        "la-catch>=0.0.3",
        "la-headers>=0.0.1",
        "aiohttp[speedups]>=3.8.1",
        "structlog>=21.5.0",
    ],
    python_requires=">=3.10",
)
