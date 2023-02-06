[![made-with-Markdown](https://img.shields.io/badge/Made%20with-Markdown-1f425f.svg)](http://commonmark.org)
![GitHub last commit](https://img.shields.io/github/last-commit/linszay/holbertonschool-AirBnB_clone)
*PROJECT START DATE: 02.02.2023
# <center>![page](https://camo.githubusercontent.com/a8cd2eef2325c425519095dc2501111e630a77eddb454938c527cb82ea9c3aeb/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67)

# <center> AirBnB Clone - Command Interpreter

## Description :memo:
This project creates a command interpreter for the AirBnB clone project for Holberton School Tulsa. The command interpreter will handle the following:

* Creates a new object (ex: a new User or a new Place)
* Retrieves an object from a file, a database etc...
* Do operations on objects (count, compute stats, etc…)
* Updates attributes of an object
* Destroys an object

The project contains:
- A parent class (called `BaseModel`) used for initialization, serialization, and deserialization of instances.
- Creates a simple flow of serialization/deserialization, as follows: Instance <-> Dictionary <-> JSON string <-> file
- Creation of all subclasses (`User`, `State`, `City`, `Amenity`, `Place`, `Review`)
- Creation of a the first abstracted storage engine of the project: File storage.
- Unittests to validate all classes as well as the storage engine.

This is an educational purposes clone from [AirBnB](https://www.airbnb.com/)

## FLOWCHART
<p align="center">
  <img src="https://i.imgur.com/gyqA0od.png" alt="storage">
</p>

## <center>How to Use (with examples)
The user of the console will be able to utilize it in an interactive or non-interactive mode as desired. Running `./console.py` in terminal will open up a prompt that the user can call functions from. 

E.g.

    ./console.py
    (hbtn) help
    Documented commands (type help <topic>):
    ========================================
    EOF  all  create  destroy  help  quit  show  update

Commands may be executed non-interactively by piping them into the console.

E.g.

Both

    echo "create BaseModel" | ./console.py

and

    ./console.py
    (hbtn) create BaseModel

will create an instance of the BaseModel class and print its id. 

The `EOF` command is used to terminate the console.  Alternatively, Ctrl+D may be used.

## Authors

Lindsay Lancaster  | (https://github.com/linszay)


Clint Hendrickson  | (https://github.com/Maitreya-today)


