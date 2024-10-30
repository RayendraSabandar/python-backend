from flask import jsonify

class Response:
    @staticmethod
    def handleResponse(data):
        return jsonify({
            "data": data
        }), 200