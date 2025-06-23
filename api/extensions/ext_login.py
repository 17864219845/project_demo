import json

import flask_login  # type: ignore
from flask import Response, request
from flask_login import user_loaded_from_request, user_logged_in

from utils.u_jwt_processor import JwtProcessor

login_manager = flask_login.LoginManager()


# Flask-Login configuration
# @login_manager.request_loader
# def load_user_from_request(request_from_flask_login):
#     """Load user based on the request."""
#     auth_header = request.headers.get("Authorization", "")
#     auth_token: str | None = None
#     if auth_header:
#         if " " not in auth_header:
#             raise ValueError("Invalid Authorization header format. Expected 'Bearer <api-key>' format.")
#         auth_scheme, auth_token = auth_header.split(maxsplit=1)
#         auth_scheme = auth_scheme.lower()
#         if auth_scheme != "bearer":
#             raise ValueError("Invalid Authorization header format. Expected 'Bearer <api-key>' format.")
#     else:
#         auth_token = request.args.get("_token")
#
#     if request.blueprint in {"console", "inner_api"}:
#         if not auth_token:
#             raise ValueError("Invalid Authorization token.")
#         decoded = JwtProcessor().verify(auth_token)
#         user_id = decoded.get("user_id")
#         source = decoded.get("token_source")
#         if source:
#             raise ValueError("Invalid Authorization token.")
#         if not user_id:
#             raise ValueError("Invalid Authorization token.")
#
#         logged_in_account = AccountService.load_logged_in_account(account_id=user_id)
#         return logged_in_account


def init_app(app):
    login_manager.init_app(app)
