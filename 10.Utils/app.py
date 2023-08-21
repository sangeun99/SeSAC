from flask import Flask
from flask_restx import Api, Resource

app = Flask(__name__)
api = Api(app)

@api.route('/hello') # api를 통해 app과 연결되긴 할 것임
class HelloWorld(Resource):
  def get(self):
      return "{'hello':'world'}"

if __name__ == "__main__":
    app.run(debug=True)