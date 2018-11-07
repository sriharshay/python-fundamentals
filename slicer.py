# get user email address

email = input("what is your email address?:").strip()

# slice out user name

user = email[:email.index("@")]

# slice domain name

domain = email[email.index("@") + 1:]

# format message

output = "Your user name is {} and your domain name is {}".format(user, domain)

# display out message

print(output)
