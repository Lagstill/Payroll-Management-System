# Payroll Management System

### A simple payroll management system built using Flask web framework, Flask-MySQL extension and MySQL database. The system allows to perform CRUD (Create, Read, Update and Delete) operations on the payroll data.

## Tools and Libraries Used
Flask: A micro web framework written in Python
Flask-MySQL: A Flask extension to connect to MySQL databases
MySQL: A popular open-source relational database management system

## Access the app via:
http://app.alaguprakalya.ninja:5000/

## Screenshots
![alt text](https://github.com/Lagstill/Payroll-Management-System/tree/main/images/home.png?raw=true)
![alt text](https://github.com/Lagstill/Payroll-Management-System/tree/main/images/update.png?raw=true)



## Installation and Setup
### 1. Clone the repository
```bash
git clone https://github.com/[username]/Payroll-Management-System.git 
```

### 2. Install the required packages
```bash
pip install -r requirements.txt
```

### 3. Set the environment variables for MySQL database user, password, database name and host.

### 4. Run the application

```bash
python app.py
```

### 5. Open the browser and go to http:// localhost: (port you have specified in app.py) to access Payroll Management System.

## Features
* Display a list of employees payroll data
* Create a new payroll record
* Update an existing payroll record
* Delete a payroll record

## File Structure
```lua
Payroll-Management-System
├── app.py
├── config.yml
├── templates
│   ├── create.html
│   ├── index.html
│   └── payroll.html
├── requirements.txt
└── README.md
```



