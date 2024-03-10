# AirBnB_clone
## Project Overview
The AirBnB clone is a simplified version of the popular online accommodation platform. It aims to replicate some of the core features of AirBnB, allowing users to create, manage, and book listings.
## 0x00. AirBnB clone - The console
AirBnB Clone Command Interpreter - This is the foundational command interpreter for managing AirBnB objects, serving as the initial step in building the full AirBnB web application.
## Repository Structure
The repository is organized as follows:

`models/`: Contains Python classes representing different data models (e.g., User, Place, Review).  
`tests/`: Contains unit tests to verify the functionality of the code.  
`console.py`: A command-line interface (CLI) for managing the application.  
`README.md`: This file.

## Getting Started
To run the AirBnB clone, follow these steps:

- Clone the Repository:
```
git clone https://github.com/DYung26/AirBnB_clone.git
```
- Navigate to the Project Directory:
```
cd AirBnB_clone
```
- Run the CLI:
```
# Python 2
python console.py
```
```
# Python 3
python3 console.py
```

## Usage
The CLI provides various commands to interact with AirBnB objects. Some common commands include:

* `create`: Create a new instance of an AirBnB object.
* `show`: Display details of a specific AirBnB object.
* `update`: Update attributes of an existing AirBnB object.
* `destroy`: Delete an instance of an AirBnB object.
* `all`: Display all instances or instances of a specific class.  
Example usage:
```
# Create a new Place object
create BaseModel
```
```
# Show details of a specific User
show BaseModel <id>
```
For a complete list of commands and options, refer to the documentation or run the CLI with the `--help` option.

## Testing
To run the tests, use the following command:
```
# Python 2
python -m unittest discover tests
```
```
# Python3
python -m unittest discover tests
```

## Contributing
If you would like to contribute to the development of the AirBnB clone, follow these steps:
1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature/new-feature`
3. Commit your changes: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/new-feature`
5. Submit a pull request.

## Authors
- DANIEL OYEKUNLE
- MARZOUQ ADEBAYO

## License
This project is currently not explicitly licensed. See the [License](#license) section for more details.
