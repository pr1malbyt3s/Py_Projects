from flask import Flask, jsonify, request

app = Flask(__name__)
# Prevent jsonify from sorting keys in alphabetical order.
app.config['JSON_SORT_KEYS'] = False
app.config['DEBUG'] = True

# Test data for BOLA.
bedrooms = [
	{'id': 2,
	 'owner': 'kid1',
	 'piggybank': 'yes',
	 'money': 12.50},
	{'id': 4,
	 'owner': 'kid2',
	 'piggybank': 'yes',
	 'money': 4.00}
]

# Top-level route.
@app.route('/', methods = ['GET'])
def index():
	location = request.path
	message = 'Wecome to (In)Secure API'
	return jsonify({'location':location,
			'message':message})

# Home route. Will require authentication in fix.
@app.route('/home', methods = ['GET'])
def home():
	location = request.path
	message = 'Welcome to ' + location
	return jsonify({'location':location,
			'message':message})

# Bedroom in /home. Returns all bedrooms based on key type.
@app.route('/home/bedroom', methods = ['GET'])
def bedroom():
	location = request.path
	message = 'Welcome to ' + location
	return jsonify({'location':location,
			'message':message, 
			'bedrooms':bedrooms})

# Bedroom by id. Returns bedroom info based on id.
@app.route('/home/bedroom/<int:id>', methods = ['GET'])
def bed_by_id(id):
	location = request.path
	message = 'Wecome to ' + location
	res = [ sub['id'] for bedroom in bedrooms ]	
	if id in res:
		return jsonify({'location':location,
				'message':message, 
				'bedroom':bedrooms})
		else:
			return jsonify({'location':location,
					'message':message,
					'bedroom':'No matching bedrooms found'})

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=8000)
