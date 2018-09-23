import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="odoo_connector_2",
    version="1.0.2",
    author="Franklin Sarmiento",
    author_email="franklinitiel@gmail.com",
    description="This is a library that allow an easy and friendly connection with an Odoo ERP instance on Pyhton 3.x",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/franklintiel/odoo-connector-2/wiki",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
    keywords="odoo connector connect interface connection odoo_connection odoo_connect odoo_connector odoo_interface odoo_protocol",
    project_urls={
        'Documentation': "https://github.com/franklintiel/odoo-connector-2",
        'Source': "https://github.com/franklintiel/odoo-connector-2/",
        'Tracker': "https://github.com/franklintiel/odoo-connector-2/issues"
    },
    packages=setuptools.find_packages(exclude=['contrib', 'docs', 'tests*']),
    python_requires=">=3.*")