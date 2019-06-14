from setuptools import setup, find_packages

setup(
    name='dynamixel_helper',
    version='1.0.0',
    description='This helper is a wrapper for the Dynamixel-SDK. With this, configure and drive your motor more quickly. You do not need to know how the SDK works.',
    author='Hong-ryul Jung',
    author_email='jung.hr.1206@gmail.com',
    url='https://github.com/ryul1206/easy-dynamixel-helper',
    download_url='https://github.com/ryul1206/easy-dynamixel-helper/releases',
    install_requires=[],
    packages=find_packages(exclude=['tutorial', 'tests*']),
    keywords=['b', 'a'],
    python_requires='>=3',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
