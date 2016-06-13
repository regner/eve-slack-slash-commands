

from flask import Flask
from flask_restful import Api

from endpoints.corporationlookup import CorporationLookup
from endpoints.pilotlookup import PilotLookup
from endpoints.serverstatus import ServerStatus
from endpoints.typelookup import TypeLookup

app = Flask(__name__)
api = Api(app)

api.add_resource(ServerStatus, '/serverstatus/')
api.add_resource(PilotLookup, '/pilot/')
api.add_resource(CorporationLookup, '/corp/')
api.add_resource(TypeLookup, '/type/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
