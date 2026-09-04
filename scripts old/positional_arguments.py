def post_msg(user,msg):
    print(f'{user}: {msg}')
        # Post a message from a user.

print()
post_msg('Jacob', '"I am studying right now!"')
post_msg('William' , '"I am too!"')
print()

def private_msg(sender, recipient, msg):
    print(f"{sender} just sent a message to {recipient} that says {msg}")
    #Private message between two user data. 

print() 
private_msg('Sarah', 'Jacob', '"Are you ready for the exam this Friday?"')
private_msg('Jacob', 'Sarah', '"I think so."')
print() 

def post_messages(user, *msgs): 
    """Post all of user's messages."""
    print(f"{user} said:")
    
    for msg in msgs: 
        print(f"   {msg}")

post_messages('Anna', "I love mountains.", "I love rivers.", "I love the ocean.")
post_messages('Bob', "I love desserts.", "I love canyons.", "I like forests.", "I like it when it rains.")