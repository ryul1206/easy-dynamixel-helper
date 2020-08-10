import setuptools
# read the contents of your README file
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="dynamixel_helper",
    version="1.0.1",
    author="Hong-ryul Jung",
    author_email="jung.hr.1206@gmail.com",
    description="You can use this helper instead of the Dynamixel-SDK to speed up your work.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/ryul1206/easy-dynamixel-helper",
    # download_url     = 'https://github.com/ryul1206/easy-dynamixel-helper/releases',
    install_requires=["dynamixel_sdk>=3"],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, <4",
    # py_modules       = [""],
    packages=setuptools.find_packages(exclude=["tutorial", "tests"]),
    package_data={"dynamixel_helper": ["tables/*.json"]},
    keywords=["dynamixel"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2",
    ],
)
