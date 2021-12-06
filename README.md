# openPyther

PyPi package to get, treat and return weather from the OpenWeatherMap's API. Moreover, this PyPi module was developed to be used in online courses on web APIs at IMERIR. The development project of these courses on web APIs at IMERIR is available [just here](https://drive.google.com/drive/folders/1Nh4dJBdg9SIK2r5x4EAXutfiqcqyoLm8).

## Contents

1. [Introduction](#introduction)
2. [Presentation](#presentation)
3. [Git repos's structure](#repos_s_structure)
4. [How was this project developed ?](#how_was_this_project_developed)
5. [How does this project work ?](#how_does_this_project_work)
6. [How to install it ?](#how_to_install_it)
    * [From PyPi](#from_pypi)
    * [From GitHub](#from_github)
7. [How to use it ?](#how_to_use_it)
8. [A few examples](#a_few_examples)
    * [Display all of the weather](#display_all_of_the_weather)
    * [Convert temperatures](#convert_temperatures)
10. [Useful links](#useful_links)
11. [Conclusion](#conclusion)

<a name="introduction"></a>
## Introduction

Coming soon...

<a name="presentation"></a>
## Presentation

Coming soon...

<a name="repos_s_structure"></a>
## Git repos's structure

<a name="how_was_this_project_developed"></a>
## How was this project developed ?

Comming...

<a name="how_does_this_project_work"></a>
## How does this project work ?

<a name="how_to_install_it"></a>
## How to install it ?

Comming...

<a name="from_pypi"></a>
### From PyPi

<a name="from_github"></a>
### From GitHub

<a name="how_to_use_it"></a>
## How to use it ?

<a name="a_few_examples"></a>
## A few examples

<a name="display_all_of_the_weather"></a>
### Display all of the weather

Without country code...
```python
# Import the main module to use: the OpenPyther one...
import openPyther.openPyther as openPyther

# Initialization of the 'openPyther' object with the wished localisation and the OpenWeather API key as parameters of the constructor...
openPytherObject = openPyther.OpenPyther("<wishedLocalisation>", "<OpenWeather API Key>")

# Display the 'openPyther' object as a string...
print(openPytherObject)
```

With country code...
```python
# Import the main module to use: the OpenPyther one...
import openPyther.openPyther as openPyther

# Initialization of the 'openPyther' object with the wished localisation, the OpenWeather API key and the wished country code as parameters of the constructor...
openPytherObject = openPyther.OpenPyther("<wishedLocalisation>", "<OpenWeather API Key>", "<wishedCountryCode>")

# Display the 'openPyther' object as a string...
print(openPytherObject)
```

<a name="convert_temperatures"></a>
### Convert temperatures

<a name="useful_links"></a>
## Useful links

<a name="conclusion"></a>
## Conclusion
