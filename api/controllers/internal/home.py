from flask_restful import Resource
from common.errors import CustomNotImplementedError
from decorator.login import login_required


class HomeApi(Resource):
    # @login_required
    def get(self):
        """Get home detail"""
        # raise ValueError
        # raise CustomNotImplementedError
        # try:
        #     res = ['1']
        #     a = res[2]
        # except Exception as e:
        #     print(e)
        # res = ['1']
        # a = res[2]
        return {"test": "========"}
