# BingImageCreator
High quality image generation by Microsoft. Reverse engineered API.
[BingImageCreator](https://github.com/acheong08/BingImageCreator/tree/main)
## How to get AUTH_COOKIE
* Go to https://bing.com/.
* F12 to open console
* In the JavaScript console, type cookieStore.get("_U").then(result => console.log(result.value)) and press enter
* Copy the output. This is used in --U or auth_cookie.
