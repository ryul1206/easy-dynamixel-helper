from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name             = 'dynamixel_helper',
    version          = '0.0.0',
    description      = 'You can use this helper instead of the Dynamixel-SDK to speed up your work.',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    author           = 'Hong-ryul Jung',
    author_email     = 'jung.hr.1206@gmail.com',
    license          = 'MIT',
    url              = 'https://github.com/ryul1206/easy-dynamixel-helper',
    # download_url     = 'https://github.com/ryul1206/easy-dynamixel-helper/releases',
    install_requires = ['dynamixel_sdk>=3'],
    packages         = find_packages(exclude=['tutorial', 'tests*']),
    keywords         = ['b', 'a'],
    python_requires  = '>=3',
    classifiers = [
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
