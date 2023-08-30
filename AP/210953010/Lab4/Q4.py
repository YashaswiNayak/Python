import datetime
name=input('Enter a user name: ')
curtime=datetime.datetime.now()
if curtime.hour<12:
    print(f'Good morning',name)
elif curtime.hour>12 and curtime.hour<18:
    print(f'Good afternoon',name)
else:
    print(f'Good evening',name)