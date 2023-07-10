# BingImageCreator
This code uses the [BingImageCreator](https://github.com/acheong08/BingImageCreator/tree/main) module to generate and save an image.
## Introduction
High quality image generation by Microsoft. Reverse engineered API.
'''json
pip install BingImageCreator
'''
## How to get AUTH_COOKIE
* Go to https://bing.com/.
* F12 to open console
* In the JavaScript console, type cookieStore.get("_U").then(result => console.log(result.value)) and press enter
* Copy the output. This is used in --U or auth_cookie.
