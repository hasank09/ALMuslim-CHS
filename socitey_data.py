import pandas as pd

def clean_html_tags(text):
    tags = ['<p>', '</p>', '<br>', '<strong>', '</strong>', '<em>', '</em>','<ul>','</ul>','<li>','</li>',
            '<h1>','</h1>','<h2>','</h2>','<h3>','</h3>','<h4>','</h4>','<h5>','</h5>','<h6>','</h6>']
    for tag in tags:
        text = text.replace(tag, '')
    return text

def get_all_notices():
    notices_df = pd.read_csv('static/data/notices.csv', parse_dates=['date'])
    notices_df['date2'] = notices_df['date'].dt.strftime('%b %d, %Y')
    notices_df.sort_values('date', ascending=False, inplace=True)
    level = {'urgent': 'danger', 'event': 'success', 'maintenance': 'warning', 'general': 'info'}
    notices_df['category'] = notices_df['category'].str.lower()
    notices_df['level'] = notices_df['category'].map(level)
    notices_df['level'] =  notices_df['level'].fillna('info')
    notices_df['content'] = '...' + notices_df['full_notice_u'].str[:200]
    notices_df['content'] = notices_df['content'].apply(clean_html_tags)
    # notices_df['category'] = notices_df['category'].str.upper()
    all_notices = notices_df.to_dict('records')
    return all_notices

def get_all_legal_matters():
    legal_df = pd.read_csv('static/data/legal.csv', parse_dates=['filing_date'])
    legal_df['date2'] = legal_df['filing_date'].dt.strftime('%b %d, %Y')
    legal_df.sort_values('date2', ascending=False, inplace=True)
    priority = {'urgent': 'danger', 'resolved': 'success', 'pending': 'warning', 'in-progress': 'info'}
    legal_df['status'] = legal_df['status'].str.lower()
    legal_df['priority'] = legal_df['status'].map(priority)
    legal_df['priority'] =  legal_df['priority'].fillna('info')
    legal_df['suit_money_2'] = legal_df['suit_money'].apply(lambda x: '{:,.2f}'.format(x))
    all_legal_matters = legal_df.to_dict('records')
    return all_legal_matters

def get_all_documents():
    doc_df = pd.read_csv('static/data/documents.csv', parse_dates=['date_added'])
    doc_df['date2'] = doc_df['date_added'].dt.strftime('%b %d, %Y')
    doc_df.sort_values('date2',ascending=False,inplace=True)
    docs = doc_df.to_dict('records')

    return docs

def get_society_fund():
    society_df = pd.read_csv('static/data/society_fund.csv')
    society_df.loc[len(society_df)] = ['Total',society_df['credit'].sum(),society_df['debit'].sum(),
                                       society_df['balance'].sum()]
    society_fund = society_df.to_dict('records')
    return society_fund

def get_maintenance_fund():
    maintenance_df = pd.read_csv('static/data/maintenance_fund.csv', parse_dates=['month'])
    maintenance_df['month2'] = maintenance_df['month'].dt.strftime('%b-%Y')
    maintenance_df.sort_values('month', ascending=True, inplace=True)
    maintenance_fund = maintenance_df.to_dict('records')
    return maintenance_fund


def get_current_statement():
    month_df = pd.read_csv('static/data/current_statement.csv')
    month_statement = month_df.to_dict('records')
    return month_statement

def get_monthly_totals():
    month_df = pd.read_csv('static/data/current_statement.csv')
    monthly_totals = {'income': month_df['income'].sum(),
                      'expense': month_df['expense'].sum(),
                      'balance': month_df['income'].sum() - month_df['expense'].sum()}
    return monthly_totals



if __name__ == '__main__':
    # all_data = get_all_notices()
    # all_data = get_all_legal_matters()
    all_data = get_current_statement()
    for data in all_data:
        print(data)
    # notice_id = 3
    # notice = next((notice for notice in notices if notice['notice_id'] == notice_id), None)
    # print(notice)