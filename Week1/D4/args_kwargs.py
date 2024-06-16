#*args
def emails_list(*usernames):
    emails_list = []
    for user in usernames:
        user_email = user + '@gmail.com'
        emails_list.append(user_email)

    return emails_list

print(emails_list('juliana','daniel'))

#**kwargs
def user_info(**details):
    return details

print(user_info(name = 'juliana', email = 'ju@gmail.com', age = 34, address = 'Ramat Gan', nickname = 'juju'))

def user_info_complicated(name, email, age, address):
    details = {}
    details['name'] = name
    details['email'] = email
    details['age'] = age
    details['address'] = address
    return details

print(user_info_complicated('juliana','ju@gmail.com',34,'Ramat Gan', 'juju'))



