from flask import jsonify
from werkzeug.exceptions import NotFound

class Response:
    @staticmethod
    def handleResponse(data):
        if not data:
            return jsonify({
                "success": True
            })
        
        return jsonify({
            "data": data
        }), 200
    
    @staticmethod
    def handleErr(e, custom_message):
        message = str(e)
        status_code = 500
        if isinstance(e, NotFound):
            message = custom_message
            status_code = 404
        return jsonify({
            "error": {
                "type": type(e).__name__,
                "message": message,
            }
        }), status_code