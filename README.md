# spacex_launches
Small Flask website experimenting with bootstrap 

- Flask
- Bootstrap
- Python code inside HTML doc
- Using custom filters defined in app.py 
- Categorise launch function shows: json --> filter --> list --> basic dictionary mapping
    - json response is filtered through for key:value pairing of [anything]:["success/failed/upcoming"]
    - json filter results are then stored as a list
    - Very basic dictionary where the 3 types of launch lists ["success/failed/upcoming"] are used as keys with the contents of those lists used as values
    