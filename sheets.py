import gspread

gc = gspread.service_account()  # configure the service account credentials to your own credentials
sheet = gc.open('fair blackjack').get_worksheet(0)  # select the google sheet you wish to record the results to

batch = []


def log(parameter, results):
    global batch
    batch.append([parameter, results[0], results[1], results[2]])
    if len(batch) == 16:
        sheet.append_rows(batch, value_input_option='user_entered')
        batch = []

# using batches to accomodate rate limit
