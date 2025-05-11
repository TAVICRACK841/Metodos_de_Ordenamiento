from setuptools import setup

setup(
    name="Metodos_de_Orden",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],  # Dependencias si hay
    author="Gabriel GUstavo Y Oscar Path",
    description="Librería de algoritmos de ordenamiento",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
    ],
    python_requires=">=3.6",
)
