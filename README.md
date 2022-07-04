# AirBnB Clone - Console

This project is the first phase of AirBnB Clone, and consist in write a 
command interpreter to manage our AirBnB objects.

## List of Commands you can use

- [x] all
- [x] create
- [x] count
- [x] destroy
- [x] help
- [x] quit
- [x] show
- [x] update

## Oject we can manage with the commands

For clone AirBnB project, we need some classes for represent
the objects, this classes are `Amenity`, `City`, `Place`, `Review`,
`State`, `User`. All of them inherit from `BaseModel`, who is in charge
of gives the id, date of creation and date of update.

## How to use

### Clone the repo

> git clone https://github.com/Nachop51/holbertonschool-AirBnB_clone.git

### Run the console

You can work with the console in interactive or non interactive mode.

#### Run Console in Interactive
> ./console.py

Now you can see the prompt (hbnb), and can use the list of command.

#### Non Interactive example
> echo "help" | ./console.py

This is a non interactive example, you can put the command plus pipe plus 
./console.py to execute

## What the commands do

In console you can introduce some commands and be able to manage the objects of 
AirBnB clone. Wich are this commands and what they do.

| Command | Description |
| --- | --- |
| `all` | Prints all string representation of all instances based or not on the class name
| `count` | Retrieve the number of instances of a class
| `create` | Create a new instance of a class and save it in a JSON file and prints the id
| `destroy` | Delete an instance of a class based on his name class and id, and save the change into the JSON file
| `EOF` | Exit the program
| `help` | Provides description of commands
| `quit` | Exit the program
| `show` | Prints the string representation of an instance based on the class name and id
| `update` | Updates an instance based on the class name and id by adding or updating attribute(saving the change in JSON file) 

## Exmples of commands

### all

### count

### create

### destroy

### EOF

### quit

### show

### update


## Authors
**[**Nacho Peralta**](https://www.linkedin.com/in/ignacio-peralta-576a72226/)
[**Alvaro Sabini**]**(https://www.linkedin.com/in/alvaro-sabini-saralegui-a6781971/)**


