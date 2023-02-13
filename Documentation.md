**The following are the API endpoints for the Payroll system:**

```
1. Index endpoint - http://localhost:5000/
```

This endpoint allows the user to view all the payroll records stored in the database. It also provides options to the user to perform CRUD operations on the payroll records. The method used is GET and POST.

```
2. Create endpoint - http://localhost:5000/create
```

This endpoint is used to create a new payroll record by submitting the form. The method used is GET and POST.

```
3. Payroll endpoint - http://localhost:5000/payroll
```

This endpoint displays all the payroll records stored in the database. The method used is GET.

```
4. Update endpoint - http://localhost:5000/update/<string:employeeID>
```

This endpoint allows the user to update a payroll record based on the employeeID. The method used is GET and POST.
```
5. Delete endpoint - http://localhost:5000/delete/<string:employeeID>
```

This endpoint allows the user to delete a payroll record based on the employeeID. The method used is GET and POST.
