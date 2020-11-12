import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="tdge-pkg-BekhruzNiyazov", # Replace with your own username
    version="0.0.1",
    author="Bekhruz Niyazov",
    author_email="bekhruzsniyazov@outlook.com",
    description="Alpha version of 3D Game Engine.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/BekhruzSNiyazov/tdge-pkg",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
