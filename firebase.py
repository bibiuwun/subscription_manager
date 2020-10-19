import pyrebase

### change config here
config = {
    "apiKey": "AIzaSyB-MrcPwWwD-eq8B2L-ra8Kg4ybcKKGYxE",
    "authDomain": "subscription-manager-caf03.firebaseapp.com",
    "databaseURL": "https://subscription-manager-caf03.firebaseio.com",
    "storageBucket": "subscription-manager-caf03.appspot.com",
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


def push_subscription(name, price, sub_type):
    db.child("subscriptions").push(dict(name=name, price=price, sub_type=sub_type))
    
def remove_subscription_key(key):
    db.child("subscriptions").child(key).remove()

def get_subscriptions():
    all_subscriptions = db.child("subscriptions").get().each()
    if all_users:
        yield from ((u.key(), u.val()) for u in all_users)

##Preliminary firebase set-up
        
### 1
#auth=firebase.auth()
#new_user=auth.create_user_with_email_and_password('tim@company.com', 'password')
#user = auth.sign_in_with_email_and_password('tim@company.com', 'password')

### 2
#db.child("user").push(dict(name='Tim', email='tim@company.com', password='password'))
#db.child("account_profile").push(dict(checking=1012.64, saving=12473.55, credit=699.78))


        
