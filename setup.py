from setuptools import setup

setup(
    name="afro_renaissance",
    version="1.0.0",
    packages=['afro_renaissance'],
    include_package_data=True,
    install_requires=[
        line.strip()
        for line in open("requirements.txt")
        if line.strip() and not line.startswith("#")
    ],
    python_requires=">=3.11",
)