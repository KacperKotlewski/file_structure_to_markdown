from setuptools import setup, find_namespace_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name = "file_structure_to_markdown",
    version = "2020.2.20.2",
    description = "Simple to use file structure compiler to markdown representation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KacperKotlewski/file_structure_to_markdown",
    author= "Kacper Kotlewski",
    packages=find_namespace_packages(include=['files2md.*']) + ["files2md"],
    python_requires='>=3.7',
    install_requires=[
       "colorama",
    ],
    classifiers=[
        'Development Status :: Beta',
        'Environment :: Console',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: Microsoft :: Linux',
        'Programming Language :: Python :: 3.7',
    ],
)