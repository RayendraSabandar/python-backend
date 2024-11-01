from flask import Request

class Params:
    @staticmethod
    def handlePagination(request: Request):
        res = {
            "page": 1,
            "limit": 20
        }
        
        page_str = request.args.get('page')
        if page_str != '':
            res['page'] = int(page_str)

        limit_str = request.args.get('limit')
        if limit_str != '':
            res['limit'] = int(limit_str)

        return res