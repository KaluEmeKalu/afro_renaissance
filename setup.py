from setuptools import setup, find_packages

setup(
    name="afro_renaissance",
    version="1.0.0",
    packages=find_packages(include=[
        'afro_renaissance',
        'afro_renaissance.*',
        'blog',
        'blog.*',
        'manifesto',
        'manifesto.*',
        'social',
        'social.*'
    ]),
    include_package_data=True,
    install_requires=[
        line.strip()
        for line in open("requirements.txt")
        if line.strip() and not line.startswith("#")
    ],
    python_requires=">=3.11",
)