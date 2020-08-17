from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="DjangoHtmlFiller",
    version="1.0.0",
    description="Auto href/src links(js,css,images' reference) modifier for Django Project's html files.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Jay206-Programmer/DjangoHtmlFiller",
    author="Jay Shukla",
    author_email="jayshukla0034@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["DjangoHtmlFiller"],
    include_package_data=True,
    install_requires=["os","sys"],
)
