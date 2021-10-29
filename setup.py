from setuptools import setup

with open("README.md", "r") as fh:
	readme_description = fh.read()

setup(name='openPyther',
version='0.1',
description="Python package to get, treat and return weather from the OpenWeatherMap's API",
long_description=readme_description,
long_description_content_type="text/markdown",
url='#',
author='Wicken',
author_email='ericghoubiguian@live.fr',
license='MIT',
packages=['openPyther'],
install_requires=['requests'],
zip_safe=False,
python_requires='>=3.7.2')
