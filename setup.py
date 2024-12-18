from setuptools import setup, find_packages

setup(
    name='dataset_summary',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',  # Add other dependencies if needed
    ],
    description='A Python package to generate summaries of dataset columns',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/suchow07/dataset_summary',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
