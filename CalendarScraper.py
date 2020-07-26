import datetime
import time
from yahoo_earnings_calendar import YahooEarningsCalendar
import dateutil.parser
from ics import Calendar, Event

list_of_tickers = [ 'DIS', 'BABA', 'ZM', 'JD' ]

DAYS_AHEAD = 30

# Sets the dates
start_date = datetime.date(2020, 8, 1)
end_date = (datetime.datetime.now() + datetime.timedelta(DAYS_AHEAD))

# Dowloads the earnings calendar
yec = YahooEarningsCalendar()
calendar = Calendar()

for ticker in list_of_tickers:

    try:
        timestamp = yec.get_next_earnings_date(ticker)
        date_of_earnings = datetime.datetime.fromtimestamp(timestamp)

        print('Ticker successfully retrieved.')
        print('Company:', ticker, " Earnings Date: ", date_of_earnings)
        print()

            
        if date_of_earnings <= end_date:
            event = Event()
            event.name = ticker
            event.begin = date_of_earnings
            calendar.events.add(event)

            print('Event successfully added to the Calendar')
            print()

    except: 
        print('An earnings date for ', ticker, 'during this month was not found!')
        print()

    
with open('Calendar.ics', 'w') as my_file:
    my_file.writelines(calendar)

print('Calendar.ics Calendar was successfully generated.')

# and it's done !