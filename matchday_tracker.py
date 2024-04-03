#Program to track visits to stadiums as well as the particular stadia visited - organised by league

import os

from datetime import datetime, date

#Create two text files for matches and stadiums if they don't exist already
if not os.path.exists('match_tracker.txt'):
    with open('match_tracker.txt', 'w') as default_match_file:
        pass

if not os.path.exists('stadium_tracker.txt'):
    with open('stadium_tracker.txt', 'w'):
        pass


#Declaring universal variables
format = '%d-%m-%y'

#--Declaring Functions--
    
def add_match():
    match_list = []
    home_team = input('Please enter the name of the home team: ')
    away_team = input('Please enter the name of the away team: ')
    score = input('Please enter the score of the match: ')
    new_stadium = input('Is this your first time visiting this stadium? (y/n): ')
    if new_stadium == 'y':
        stadium = input('Please enter the name of the stadium you visited: ')
    while True:
        try:
            date_of_visit = input('Please enter the date of the match using the following format: (DD-MM-YYYY): ')
            date_match = datetime.strptime(date_of_visit, format)
            break
        except ValueError:
            print('You have not entered the date correctly, please try again')

    date_str = date_match.strftime('%d-%m-%y')
            
    match_list.append(home_team)
    match_list.append(away_team)
    match_list.append(score)
    match_list.append(stadium)
    match_list.append(date_str)

    match_string = ';'.join(match_list)

    with open('match_tracker.txt', 'a') as match_file:
        match_file.write(match_string)
