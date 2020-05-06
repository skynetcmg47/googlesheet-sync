import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gsheet-sync-NamPhuong",
    version="0.0.1",
    author="Nam Phuong",
    author_email="skynetcmg47@gmail.com",
    description="read report from nhanh.vn and sync to googlesheet",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/skynetcmg47/googlesheet-sync",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)