from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3

app = Flask(__name__)

cur = sqlite3.connect('payroll.db', check_same_thread=False)

@app.route('/', methods = ['GET','POST'])
def index():
    # Execute query to select all records from payroll table
    res = cur.execute("SELECT * FROM payroll ")
    resultValue = res.fetchall()
    if len(resultValue) > 0:
        result = resultValue
    # If user has selected an option from the dropdown list
    # then redirect to the appropriate page
    if request.method == 'POST':
        userChoice = request.form
        choiceID = userChoice['employeeID']
        choiceopt = userChoice['opt']
        print(choiceopt)
        if choiceopt == 'Update':
            return redirect(url_for('update',employeeID = choiceID))
        elif choiceopt == 'Read':
            return redirect(url_for('payroll'))
        elif choiceopt == 'Create':
            return redirect(url_for('create'))
        elif choiceopt == 'Delete':
            return redirect(url_for('delete',employeeID = choiceID))
        return redirect(url_for('payroll'))
    return render_template('index.html',payrollDetails=result)


@app.route('/create', methods=['GET', 'POST'])
def create():
    # If user has submitted the form
    # then insert the data into the database
    if request.method == 'POST':
        userDetails = request.form
        employeeID = userDetails['employeeID']
        Regular_days = userDetails['Regular_days']
        Rate = userDetails['Rate']
        Regular_pay = userDetails['Regular_pay']
        Overtimes = userDetails['Overtimes']
        Overtimes_pay = userDetails['Overtimes_pay']
        medical = userDetails['medical']
        canteen = userDetails['canteen']
        house = userDetails['house']
        company_loan = userDetails['company_loan']
        NET = userDetails['NET']
        cur.execute("INSERT INTO payroll(employeeID, Regular_days, Rate, Regular_pay, Overtimes, Overtimes_pay, medical, canteen, house, company_loan, NET) VALUES(" + str(employeeID) + "," + str(Regular_days) + "," + str(Rate) + "," + str(Regular_pay) + "," + str(Overtimes) + "," + str(Overtimes_pay) + "," + str(medical) + "," + str(canteen) + "," + str(house) + "," + str(company_loan) + "," + str(NET) + ")")
        cur.commit()
        return redirect(url_for('payroll'))
    return render_template('create.html')

@app.route('/payroll')
def payroll():
    # Execute query to select all records from payroll table
    resultValue = cur.execute("SELECT * FROM payroll")
    res = resultValue.fetchall()
    if len(res) > 0:
        return render_template('payroll.html',payrollDetails=res)

@app.route('/update/<string:employeeID>', methods = ['GET','POST'])
def update(employeeID):
    res = cur.execute("SELECT * FROM payroll WHERE employeeID=" +str(employeeID))
    res = res.fetchall()
    if len(res) > 0:
        result =res
    if request.method == 'POST':
        userDetails = request.form
        employeeID = userDetails['employeeID']
        Regular_days = userDetails['Regular_days']
        Rate = userDetails['Rate']
        Regular_pay = userDetails['Regular_pay']
        Overtimes = userDetails['Overtimes']
        Overtimes_pay = userDetails['Overtimes_pay']
        medical = userDetails['medical']
        canteen = userDetails['canteen']
        house = userDetails['house']
        company_loan = userDetails['company_loan']
        NET = userDetails['NET']
        cur.execute("UPDATE payroll SET Regular_days="+str(Regular_days)+", Rate="+str(Rate)+", Regular_pay="+str(Regular_pay)+", Overtimes="+str(Overtimes)+", Overtimes_pay="+str(Overtimes_pay)+", medical="+str(medical)+", canteen="+str(canteen)+", house="+str(house)+", company_loan="+str(company_loan)+", NET="+str(NET)+" WHERE employeeID="+str(employeeID))        
        flash("Employee Updated Successfully")
        res = cur.execute("SELECT * FROM payroll WHERE employeeID=" +str(employeeID))
        res = res.fetchall()
        if len(res) > 0:
            result =res
        cur.commit()
    return render_template('update.html',payrollDetails=result)
    

@app.route('/delete/<string:employeeID>', methods = ['GET'])
def delete(employeeID):
    # Execute query to select all records from payroll table
    # If user has submitted the form
    # then delete the data into the database
    cur.execute("DELETE FROM payroll WHERE employeeID="+str(employeeID))
    cur.commit()
    flash("Employee Deleted Successfully")
    return redirect(url_for('payroll'))

if __name__ == '__main__':
    # Set the secret key to some random bytes. Keep this really secret!
    app.secret_key = 'super secret key'
    # Set the session cookie to be secure
    app.config['SESSION_TYPE'] = 'filesystem'
    # Set the debug flag to true
    app.debug = True    
    # Run the app :)
    app.run()

