from flask import Flask, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


# app creation
app = Flask(__name__)
CORS(app)

#add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:password1@localhost/users'


db = SQLAlchemy(app)
# create app route



# api route
@app.route("/api/home", methods=['GET'])
def return_home():
	return jsonify({
		'message': "This is a test to see if it works"
	})

if __name__ == "__main__":
	# remove debug=True when we are out of devlopement and we actually post the site
	app.run(debug=True, port=8080)
