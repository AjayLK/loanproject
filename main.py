

from flask import Flask, jsonify, render_template, request
from loan_model.utils import LoanPaid
import config

app = Flask(__name__)

@app.route('/')
def hello_flask():
    print("Welcome")
    return render_template("index.html")

@app.route('/Loan_paid',methods = ['GET','POST'])
def get_loan_paid():
    if request.method == 'GET':
        print('we are using GET method')

        data = request.form
        print("Data-->",data)

        credit_policy = request.args.get('credit_policy')
        purpose = request.args.get('purpose')
        int_rate = eval(request.args.get('int_rate'))
        installment = eval(request.args.get('installment'))
        log_annual_inc = eval(request.args.get('log_annual_inc'))
        dti = eval(request.args.get('dti'))
        fico = eval(request.args.get('fico'))
        days_with_cr_line = eval(request.args.get('days_with_cr_line'))
        revol_bal = eval(request.args.get('revol_bal'))
        revol_util = eval(request.args.get('revol_util'))
        inq_last_six_mths = eval(request.args.get('inq_last_six_mths'))
        delinq_two_yrs = eval(request.args.get('delinq_two_yrs'))
        pub_rec = eval(request.args.get('pub_rec'))

        print('credit_policy,purpose,int_rate,installment,log_annual_inc,dti,fico,days_with_cr_line,revol_bal,revol_util,inq_last_six_mths,delinq_two_yrs,pub_rec',credit_policy,purpose,int_rate,installment,log_annual_inc,dti,fico,
        days_with_cr_line,revol_bal,revol_util,inq_last_six_mths,delinq_two_yrs,pub_rec)
  

        lp = LoanPaid(credit_policy,purpose,int_rate,installment,log_annual_inc,dti,fico,
        days_with_cr_line,revol_bal,revol_util,inq_last_six_mths,delinq_two_yrs,pub_rec)
        paid = lp.get_predicted_loan_paid()
        
        if paid == 0:
            return render_template("index.html",prediction='You have not paid the loan.')
        else:
            return render_template("index.html",prediction='You have paid off the loan.')

    else:
        print('we are using POST method')

        data = request.form
        print("Data-->",data)

        credit_policy = request.form.get('credit_policy')
        purpose = request.form.get('purpose')
        int_rate = eval(request.form.get('int_rate'))
        installment = eval(request.form.get('installment'))
        log_annual_inc = eval(request.form.get('log_annual_inc'))
        dti = eval(request.form.get('dti'))
        fico = eval(request.form.get('fico'))
        days_with_cr_line = eval(request.form.get('days_with_cr_line'))
        revol_bal = eval(request.form.get('revol_bal'))
        revol_util = eval(request.form.get('revol_util'))
        inq_last_six_mths = eval(request.form.get('inq_last_six_mths'))
        delinq_two_yrs = eval(request.form.get('delinq_two_yrs'))
        pub_rec = eval(request.form.get('pub_rec'))

        print('credit_policy,purpose,int_rate,installment,log_annual_inc,dti,fico,days_with_cr_line,revol_bal,revol_util,inq_last_six_mths,delinq_two_yrs,pub_rec',credit_policy,purpose,int_rate,installment,log_annual_inc,dti,fico,
        days_with_cr_line,revol_bal,revol_util,inq_last_six_mths,delinq_two_yrs,pub_rec)

        lp = LoanPaid(credit_policy,purpose,int_rate,installment,log_annual_inc,dti,fico,
        days_with_cr_line,revol_bal,revol_util,inq_last_six_mths,delinq_two_yrs,pub_rec)
        paid = lp.get_predicted_loan_paid()
        
        if paid == 0:
            return render_template("index.html",prediction='You have not paid the loan.')
        else:
            return render_template("index.html",prediction='You have paid off the loan.')

  

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER, debug =True)