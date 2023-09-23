import pprint
from openvpn_status_parser import OpenVPNStatusParser
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/openvpn/client-list', methods=['GET'])
def get_openvpn_client_list():

    parser = OpenVPNStatusParser("/var/run/openvpn-server/status-server.log")
    parsed_data = parser.connected_clients
    return jsonify(parsed_data)
    #pprint.pprint(parser.routing_table)
    #pprint.pprint(parser.details)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="65080")
