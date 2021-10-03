import setuptools

setuptools.setup(
    name="wikiharvester",
    version="1.0.0",
    author="Aleksander Klug",
    author_email="aleksander.klug@protonmail.com",
    description="wikiharvester is a minimalistic CLI tool for harvesting content in Wikipedia tables and storing it in a local CSV file",
    long_description="README.md",
    long_description_content_type="text/markdown",
    url="http://github.com/aleksanderklug/wikiharvester",
    packages=setuptools.find_packages(),
    scripts=["wikiharvester.py"],
    install_requires="requirements.txt",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)