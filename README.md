# CN11
# Flask app integerated with Sentry

##  Run in your Machine
* `pip install Flask`
* `pip install --upgrade 'sentry-sdk[flask]'`
* `python3 app.py`
### Send post request through Postman on url /post
```
{
    "text": "Post Example"
}
```
### Above will work fine but not it's time to use sentry
#### This will trigger Sentry and will send you unresolved issues
```
{
    "teat": "Post Example"
}
```
