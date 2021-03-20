import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hiding", # Replace with your own username
    version="1.0.1",
    author="johnngnky",
    author_email="contact@johnngnky.xyz",
    description="Hiding text in other text.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/johnngnky/hiding",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent"
    ],
    package_dir={"": ""},
	license = "WTFPL",
    packages=["hiding"],
    python_requires=">=3.6",
)