import requests
import datetime
from groups import GRP1, GRP2, GRP3, GRP4, GRP5
from parameters import UPDATE_INTERVAL_MINUTES, DESIRED_UPDATE_COUNT, START_DELAY_MINUTES
from time import sleep
from helpers import sleep_with_progress


sleep_with_progress(total_time_minutes=START_DELAY_MINUTES, interval_minutes=5) # Delay to starting the first update.
updates_completed = 0 # iterator for updates, keeping track of how many have been done

while updates_completed < DESIRED_UPDATE_COUNT:
    print('Starting Update.')
    i=0 # player iterator for logging (i=individual)
    for player in GRP1:    
        i=i+1
        current_player = player
        url='https://crystalmathlabs.com/api.php?type=update&player='
        response=requests.get(url+current_player)    
        now = datetime.datetime.now()
        response_status = response.status_code
        if response_status == 200:        
            print('Successfully updated {} at {}'.format(current_player, now))
        else:
            print('Error code {} for {} at {}'.format(response_status, current_player, now))
        sleep(.2)
        print(f'{i}/31 players completed')
    print('Group 1 Update Completed.')
    print('')
    print('')


    i=0
    for player in GRP2:    
        i=i+1
        current_player = player
        url='https://crystalmathlabs.com/api.php?type=update&player='
        response=requests.get(url+current_player)    
        now = datetime.datetime.now()
        response_status = response.status_code
        if response_status == 200:        
            print('Successfully updated {} at {}'.format(current_player, now))
        else:
            print('Error code {} for {} at {}'.format(response_status, current_player, now))
        sleep(.2)
        print(f'{i}/31 players completed')
    print('Group 2 Update Completed.')
    print('')
    print('')


    i=0
    for player in GRP3:    
        i=i+1
        current_player = player
        url='https://crystalmathlabs.com/api.php?type=update&player='
        response=requests.get(url+current_player)    
        now = datetime.datetime.now()
        response_status = response.status_code
        if response_status == 200:        
            print('Successfully updated {} at {}'.format(current_player, now))
        else:
            print('Error code {} for {} at {}'.format(response_status, current_player, now))
        sleep(.2)
        print(f'{i}/31 players completed')
    print('Group 3 Update Completed.')
    print('')
    print('')

    i=0
    for player in GRP4:    
        i=i+1
        current_player = player
        url='https://crystalmathlabs.com/api.php?type=update&player='
        response=requests.get(url+current_player)    
        now = datetime.datetime.now()
        response_status = response.status_code
        if response_status == 200:        
            print('Successfully updated {} at {}'.format(current_player, now))
        else:
            print('Error code {} for {} at {}'.format(response_status, current_player, now))
        sleep(.2)
        print(f'{i}/17 players completed')
    print('Group 4 Update Completed.')
    print('')
    print('')

    i=0
    for player in GRP5:    
        i=i+1
        current_player = player
        url='https://crystalmathlabs.com/api.php?type=update&player='
        response=requests.get(url+current_player)    
        now = datetime.datetime.now()
        response_status = response.status_code
        if response_status == 200:        
            print('Successfully updated {} at {}'.format(current_player, now))
        else:
            print('Error code {} for {} at {}'.format(response_status, current_player, now))
        sleep(.2)
        print(f'{i}/31 players completed')
    print('Group 5 Update Completed.')
    print('')
    print('')
        
    updates_completed = updates_completed+1
    print('Update {} Completed.'.format(updates_completed))
    
    print('DESIRED_UPDATE_COUNT={}, updates_completed={}'.format(DESIRED_UPDATE_COUNT, updates_completed))
    if updates_completed == DESIRED_UPDATE_COUNT:
        print('Set of updates complete!')
    else:
        print('Waiting {} minutes...'.format(UPDATE_INTERVAL_MINUTES))
        sleep_with_progress(total_time_minutes=UPDATE_INTERVAL_MINUTES, interval_minutes=5)
        # sleep(60*UPDATE_INTERVAL_MINUTES) # magic number 60 gives 1 minute so input can be given in minutes.