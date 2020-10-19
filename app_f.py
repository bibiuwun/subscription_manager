# POST - used to recieve data
# GET - used to send data back only
import firebase
from flask import Flask,render_template,request,jsonify,redirect,url_for

#Flask
app = Flask(__name__)

#Temporary Database
#each subscription is a dictionary --> list of dictionaries
#subscriptions = [{
#        'name': 'Netflix',
#        'items': [{'type':'Premium', 'price': 12.99}] 
#        }]
subscriptions = []

@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        #if pw and user valid (assuming yes)
        #return "success"
        return redirect(url_for("user_home"))
    return render_template('login.html')

@app.route('/user_home' , methods=['GET', 'POST'])
def user_home():
    if request.method == 'POST':
        return "Not user home"
    return render_template('home.html')

#post /subscriptions data: {name :}
@app.route('/subscriptions' , methods=['POST'])
def create_subscription():
  request_data = request.get_json()
  new_subscription = {
    'name':request_data['name'],
    'items':[]
  }
  subscriptions.append(new_subscription)
  return jsonify(new_subscription)

#get /subscriptions/<name> data: {name :}
@app.route('/subscriptions/<string:name>')
def get_subscription(name):
  for subscription in subscriptions:
    if subscription['name'] == name:
          return jsonify(subscription)
  return jsonify ({'message': 'subscription not found'})

#get /subscriptions
@app.route('/subscriptions')
def get_subscriptions():
  return jsonify({'subscriptions': subscriptions})

#post /subscriptions/<name> data: {name :}
@app.route('/subscriptions/<string:name>/item' , methods=['POST'])
def create_item_in_subscriptions(name):
  request_data = request.get_json()
  for subscription in subscriptions:
    if subscription['name'] == name:
        new_item = {
            'type': request_data['type'],
            'price': request_data['price']
        }
        subscription['items'].append(new_item)
        return jsonify(new_item)
  return jsonify ({'message' :'subscription not found'})

#get /subscriptions/<name>/item data: {name :}
@app.route('/subscriptions/<string:name>/item')
def get_item_in_subscription(name):
  for subscription in subscriptions:
    if subscription['name'] == name:
        return jsonify( {'items':subscription['items'] } )
  return jsonify ({'message':'subscription not found'})

def firebase_push(name, price, n_type):
    return firebase.push_subscription(name, price, n_type)

#Standard push
if __name__ == '__main__':
    firebase_push('Spotify', 3.99, 'Standard')
    app.run(port=5000)
    #http://127.0.0.1:5000/
