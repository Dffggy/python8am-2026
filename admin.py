data = [
    {'username': 'admin',  'password': 'admin001'},
    {'username': 'admin2', 'password': 'admin002'},
    {'username': 'admin3', 'password': 'admin003'}
]
username = input("enter username: ")
password = input("enter password: ")


if username==data[0]['username'] and password==data[0]['password']:
    print("welcome",username)
elif username==data[1]['username'] and password==data[1]['password']:
    print("welcome",username)
elif username==data[2]['username'] and password==data[2]['password']:
    print("welcome",username)
else:
    print("username or pasword invalid")