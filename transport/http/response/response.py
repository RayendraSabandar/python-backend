from flask import jsonify

class Response:
    @staticmethod
    def handleResponse(data):
        return jsonify({
            "data": data
        }), 200
    
    @staticmethod
    def handleErr(e):
        return jsonify({
            "error": {
                "type": type(e).__name__,
                "message": str(e),
            }
        }), 500