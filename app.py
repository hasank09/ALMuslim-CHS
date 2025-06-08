from flask import Flask
from flask import render_template
from socitey_data import get_all_notices,get_all_legal_matters,get_all_documents
from socitey_data import get_society_fund,get_maintenance_fund,get_current_statement,get_monthly_totals

from datetime import datetime


notices = get_all_notices()
legal_cases= get_all_legal_matters()
society_documents = get_all_documents()
society_fund = get_society_fund()
maintenance_fund = get_maintenance_fund()
current_statement = get_current_statement()
monthly_totals = get_monthly_totals()


app = Flask(__name__)



@app.route('/')
def home():  # put application's code here
    return render_template('index.html', notices=notices, legal_matters=legal_cases,
                           society_documents=society_documents,
                           society_fund=society_fund,
                           maintenance_fund=maintenance_fund,
                           current_statement=current_statement,
                           monthly_totals=monthly_totals,
                           year=datetime.now().year)

@app.route('/notice/<int:notice_id>')
def notice_detail(notice_id):
    notice = next((notice for notice in notices if notice['notice_id'] == notice_id), None)
    if notice:
        return render_template('notice_detail.html', notice=notice,
                               year=datetime.now().year)
    return 'Notice not found', 404

@app.route('/legal/<int:legal_id>')
def legal_detail(legal_id):

    case = next((case for case in legal_cases if case['legal_id'] == legal_id), None)
    # print('>>',case)
    if case:
        return render_template('legal_detail.html', case=case,
                               year=datetime.now().year)
    return 'Notice not found', 404

if __name__ == '__main__':
    app.run()
