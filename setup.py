# Created by Adam Thompson-Sharpe on 02/03/2020.
# Licensed under MIT.
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qrconsole",
    version="1.1.0",
    author="Adam Thompson-Sharpe",
    author_email="adamthompsonsharpe@gmail.com",
    description="A library to display QR codes in console.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/MysteryBlokHed/QRConsole",
    packages=setuptools.find_packages(),
    install_requires=[
        "Pillow>=7.0.0"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    python_requires=">=3.6"
)
