### Introduction:
The Payroll Management System is a software application that manages employee payroll data and automates payroll processing. It consists of three tables, namely Payroll Details, House Cost, and Company Loan, created via SQLite3. The system is deployed on AWS and uses data from the "https://employee-data-platform.vercel.app/api/fetchall" API to perform CRUD operations.

### API Endpoints:
The system has several API endpoints, each with a specific purpose.

* "/" Endpoint: This endpoint is the landing page of the application. It displays a welcome message and provides links to the other endpoints.

* "/create" Endpoint: This endpoint allows the user to create a new record in the Payroll Details table. It accepts data through a form and uses a POST request to add the data to the table.

* "/payroll" Endpoint: This endpoint retrieves all records from the Payroll Details table and displays them in a tabular format.

* "/housecost" Endpoint: This endpoint retrieves all records from the House Cost table and displays them in a tabular format.

* "/companyloan" Endpoint: This endpoint retrieves all records from the Company Loan table and displays them in a tabular format.

* "/update/string:employeeID" Endpoint: This endpoint allows the user to update an existing record in any of the tables. It accepts data through a form and uses a POST request to update the record.

* "/delete/string:employeeID" Endpoint: This endpoint allows the user to delete an existing record from any of the tables. It uses a GET request to delete the record.

### Deployment:
The system is deployed on AWS using Docker. The Dockerfile specifies the base image as Python 3.8-slim-buster and creates a directory called "app". It then copies the requirements.txt file, templates directory, app.py file, and the payroll.db file to the "app" directory. The WORKDIR command sets the working directory to "app", and the RUN command installs the required packages listed in the requirements.txt file. Finally, the CMD command starts the Flask server and listens on port 5000.

### Public URL:
The public URL of the Payroll Management System is "http://app.alaguprakalya.ninja:5000/". This URL can be accessed by anyone with an internet connection to use the system.

### Conclusion:
The Payroll Management System is a software application that manages employee payroll data and automates payroll processing. It consists of three tables, namely Payroll Details, House Cost, and Company Loan, created via SQLite3. The system is deployed on AWS and uses data from the "https://employee-data-platform.vercel.app/api/fetchall" API to perform CRUD operations. It has several API endpoints that provide different functionality, and it is accessible to anyone with an internet connection via the public URL.
