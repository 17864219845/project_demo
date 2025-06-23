from flask import Blueprint
from overriding.exception_handling import ExceptionHanding

bp = Blueprint("internal", __name__, url_prefix="/internal/api")
api = ExceptionHanding(bp)

from .home import (
    HomeApi,
)

api.add_resource(HomeApi, "/home")


