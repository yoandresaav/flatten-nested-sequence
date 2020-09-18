## Create super user command
 - docker-compose run app sh -c "python manage.py createsuperuser"

 ## Link logic
 - https://repl.it/repls/IncomparableDodgerblueComment

 Input:
```.json
{
    "items": [1, 2, [3, 4, [5, 6], 7], 8]
}
```
Output:
```.json
{
    "result": [1, 2, 3, 4, 5, 6, 7, 8]
}
```