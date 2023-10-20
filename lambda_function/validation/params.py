import datetime
from utils.error_handling import InputValidationError
from security.sanitizer import clean_parameter

def validate_input(data):
    if 'start_date' not in data or not validate_date_format(data['start_date']):
        raise InputValidationError('Invalid or missing start_date')
    if 'end_date' not in data or not validate_date_format(data['end_date']):
        raise InputValidationError('Invalid or missing end_date')
    if 'site' not in data:
        raise InputValidationError('Site missing')

def extract_parameters(event):
    try:
        body = json.loads(event.get('body', '{}'))
        validate_input(body)
        raw_start_date = body['start_date']
        start_date = clean_parameter(raw_start_date)
        raw_end_date = body['end_date']
        end_date = clean_parameter(raw_end_date)
        raw_site = body['site']
        site = clean_parameter(raw_site)
        raw_combiner = body['combiner']
        combiner = clean_parameter(raw_combiner)
        raw_inverter = body['inverter']
        inverter = clean_parameter(raw_inverter)
        return start_date, end_date, site, combiner, inverter
    except KeyError as e:
        raise ValueError(f"Parameter {e} is missing.")
    
    
def validate_date_format(date_str):
    # Example for YYYY-MM-DD format
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        raise ValueError(f"Incorrect data format for {date_str}, should be YYYY-MM-DD")
    
def get_default_parameters():
    return {
        'start_date': '2023-01-01',
        'end_date': '2023-12-31',
        'site' : 'Perry',
        'combiner' : 'COMB-01',
        'inverter' : 'INV-01'
    }