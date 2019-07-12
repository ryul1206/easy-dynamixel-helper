import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name             = 'dynamixel_helper',
    version          = '0.0.0',
    author           = 'Hong-ryul Jung',
    author_email     = 'jung.hr.1206@gmail.com',
    description      = 'You can use this helper instead of the Dynamixel-SDK to speed up your work.',
    long_description = long_description,
    long_description_content_type = "text/markdown",
    license          = 'MIT',
    url              = 'https://github.com/ryul1206/easy-dynamixel-helper',
    # download_url     = 'https://github.com/ryul1206/easy-dynamixel-helper/releases',
    install_requires = ['dynamixel_sdk>=3'],
    packages         = setuptools.find_packages(exclude=['tutorial', 'tests*']),
    keywords         = ['b', 'a'],
    classifiers = [
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 2'
    ]
)
