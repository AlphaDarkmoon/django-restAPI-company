# API & Rest Framework

A simple project I created to learn Rest Framework API that lets user add company and employees using Rest API.

## Table of Contents

* [Features](#features)
* [Installation](#installation)
* [URLs](#urls)
* [Contributing](#contributing)
* [License](#license)

## Features

* Create Company [ Name, Location, Type, Active or not ]
* Create Employee [ Name, Email, Position, Company name]
* Search Employees or Company using Admin Panel
* Block Browser API reader.

## Installation

1. Create Conda Venv.

```
conda create -n envname python=x.x anaconda

```
2. Install Django & Rest_framework.

```
pip install django
pip install djangorestframework
```

3. Run Project
```
django-admin manage.py runserver
```


## URLs

Admin Panel
```
localhost:8000/admin
```

API panel
```
localhost:8000/api/v1/
```

Specific Employee's Information
```
localhost:8000/companies/{companyId}/employees
```

## Contributing

If you'd like to contribute to this project, please follow these guidelines:

* Fork the repository
* Create a new branch for your changes
* Make your changes and commit them
* Push the branch to your fork
* Open a pull request

I will try to reply as soon as possible.

## License

This project is licensed under the [MIT License](LICENSE).