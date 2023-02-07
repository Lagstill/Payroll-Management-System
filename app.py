from flask import Flask, render_template, request, redirect, url_for, flash, session
from flaskext.mysql import MySQL
import yaml


# Read the config file to get the database configurations
cfg = yaml.safe_load(open('config.yml'))


#MySQL configurations
mysql = MySQL()
app = Flask(__name__)

app.config['MYSQL_DATABASE_USER'] = cfg['MYSQL_CREDENTIALS']['MYSQL_DATABASE_USER']
app.config['MYSQL_DATABASE_PASSWORD'] = cfg['MYSQL_CREDENTIALS']['MYSQL_DATABASE_PASSWORD']
app.config['MYSQL_DATABASE_DB'] = cfg['MYSQL_CREDENTIALS']['MYSQL_DATABASE_DB']
app.config['MYSQL_DATABASE_HOST'] = cfg['MYSQL_CREDENTIALS']['MYSQL_DATABASE_HOST']

mysql.init_app(app)

mysql = MySQL(app)
conn = mysql.connect()
cur =conn.cursor()

@app.route('/', methods = ['GET','POST'])
def index():
    # Execute query to select all records from payroll table
    res = cur.execute("SELECT * FROM payroll ")
    if res > 0:
        result = cur.fetchall();
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
        cur.execute("INSERT INTO payroll(employeeID, Regular_days, Rate, Regular_pay, Overtimes, Overtimes_pay, medical, canteen, house, company_loan, NET) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (employeeID, Regular_days, Rate, Regular_pay, Overtimes, Overtimes_pay, medical, canteen, house, company_loan, NET))
        conn.commit()
        return redirect(url_for('payroll'))
    return render_template('create.html')

@app.route('/payroll')
def payroll():
    # Execute query to select all records from payroll table
    resultValue = cur.execute("SELECT * FROM payroll")
    if resultValue > 0:
        payrollDetails = cur.fetchall()
        # Render the payroll.html page with the payrollDetails
        return render_template('payroll.html',payrollDetails=payrollDetails)

@app.route('/update/<string:employeeID>', methods = ['GET','POST'])
def update(employeeID):
    # Execute query to select all records from payroll table
    # If user has submitted the form
    # then update the data into the database
    res = cur.execute("SELECT * FROM payroll WHERE employeeID=%s", (employeeID,))
    if res > 0:
        result = cur.fetchall();
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
        cur.execute("""
               UPDATE payroll
               SET Regular_days=%s, Rate=%s, Regular_pay=%s, Overtimes=%s, Overtimes_pay=%s, medical=%s, canteen=%s, house=%s, company_loan=%s, NET=%s
               WHERE employeeID=%s
            """, (Regular_days, Rate, Regular_pay, Overtimes, Overtimes_pay, medical, canteen, house, company_loan, NET, employeeID))
        flash("Employee Updated Successfully")
        
        res = cur.execute("SELECT * FROM payroll WHERE employeeID=%s", (employeeID,))
        if res > 0:
            result = cur.fetchall();
        conn.commit()
    return render_template('update.html',payrollDetails=result)
    

@app.route('/delete/<string:employeeID>', methods = ['GET'])
def delete(employeeID):
    # Execute query to select all records from payroll table
    # If user has submitted the form
    # then delete the data into the database
    cur.execute("DELETE FROM payroll WHERE employeeID=%s", (employeeID,))
    conn.commit()
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

