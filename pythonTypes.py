def add(fName: str | list[int] , lName: str | None = None): # can be str / int type, and default value is None
    # list of type int as input
    return fName.capitalize() + " " + lName

fName = 'mark'
lName = 'Doe'

name = add(fName, lName)
print(name)