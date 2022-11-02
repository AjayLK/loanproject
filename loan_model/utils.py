import pickle
import json
import pandas as pd
import numpy as np
import config


class LoanPaid():
    def __init__(self,credit_policy,purpose,int_rate,installment,log_annual_inc,dti,fico,
    days_with_cr_line,revol_bal,revol_util,inq_last_six_mths,delinq_two_yrs,pub_rec):
        self.credit_policy = credit_policy
        self.purpose = purpose
        self.int_rate = int_rate
        self.installment = installment
        self.log_annual_inc = log_annual_inc
        self.dti = dti
        self.fico = fico
        self.days_with_cr_line = days_with_cr_line
        self.revol_bal = revol_bal
        self.revol_util = revol_util
        self.inq_last_six_mths = inq_last_six_mths
        self.delinq_two_yrs = delinq_two_yrs
        self.pub_rec = pub_rec



    def load_file(self):
        with open(config.MODEL_FILE_PATH, "rb") as f:
            self.loan_model = pickle.load(f)

        with open(config.JSON_FILE_PATH, "r") as f:
            self.json_data = json.load(f)


    def get_predicted_loan_paid(self):
        self.load_file()  # calling load_file method to get

        array = np.zeros(len(self.json_data['columns']))

        array[0] = self.json_data['cre_pol_dict'][self.credit_policy]
        array[1] = self.json_data['purpose_dict'][self.purpose]
        array[2] = self.int_rate
        array[3] = self.installment
        array[4] = self.log_annual_inc
        array[5] = self.dti
        array[6] = self.fico
        array[7] = self.days_with_cr_line
        array[8] = self.revol_bal
        array[9] = self.revol_util
        array[10] = self.inq_last_six_mths
        array[11] = self.delinq_two_yrs
        array[12] = self.pub_rec

        print("Test Array -->\n",array)
        loan_paid = self.loan_model.predict([array])[0]
        return loan_paid





if __name__ == "__main__":

    credit_policy = 'LendingClub.com'
    purpose = 'small_business'
    int_rate = 0.118900
    installment = 829.10
    log_annual_inc = 11.35
    dti = 19.48
    fico = 737
    days_with_cr_line = 5639.95
    revol_bal = 28854
    revol_util = 52.10
    inq_last_six_mths = 6
    delinq_two_yrs = 2
    pub_rec = 1


    lp = LoanPaid(credit_policy,purpose,int_rate,installment,log_annual_inc,dti,fico,
    days_with_cr_line,revol_bal,revol_util,inq_last_six_mths,delinq_two_yrs,pub_rec)
    paid = lp.get_predicted_loan_paid()
    print()
    print(f"You have paid load {paid}")
    # if disease == 1:
    #     print('yes patient has a heart disease')
    # else:
    #     print('patient has not a heart disease')

