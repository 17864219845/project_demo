from flask_restful import Resource
from common.errors import CustomNotImplementedError
from decorator.login import login_required


class HomeApi(Resource):
    # @login_required
    def get(self):
        """Get home detail"""
        from tasks.addition import addition
        addition.delay(15, 5)
        return {"test": "task"}
