# Overview
The purpose of this script is to take all announced events from [Yahoo Earnings Calendar](https://finance.yahoo.com/calendar/earnings/) page based on a predefined list of tickers. The script then generates .ics calendar file which can be imported in every modern calendar app such as Google Calendar, Microsoft Outlook or Confluence. 

# Prerequisites
Make sure you're using Python 3.6 or higher

# Install 
1. This script depends on a 3rd party module [yahoo-earnings-calendar](https://github.com/wenboyu2/yahoo-earnings-calendar/)
Use `pip3 install yahoo_earnings_calendar` to install this package
2. Use `pip3 install ics` to install this ics module which is responsible for .ics file generation

# How to Use
1. Go to [Yahoo Earnings Page](https://github.com/wenboyu2/yahoo-earnings-calendar/) and search for a company in the search. Take the ticker(abbreviation) and paste in `list_of_tickers` variable
2. Change DAY_AHEAD constant to the desired period
3. Run the script. A Calendar.ics file will be generated automatically which then you can import in any modern calendar app. 