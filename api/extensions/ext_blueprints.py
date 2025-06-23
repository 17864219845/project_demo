def init_app(app):
    # register blueprint routers

    from flask_cors import CORS
    from controllers.internal import bp as internal_bp
    WEB_API_CORS_ALLOW_ORIGINS = ["*"]
    CORS(
        internal_bp,
        resources={r"/*": {"origins": WEB_API_CORS_ALLOW_ORIGINS}},
        supports_credentials=True,
        allow_headers=["Content-Type", "Authorization"],
        methods=["GET", "PUT", "POST", "DELETE", "OPTIONS", "PATCH"],
        expose_headers=["X-Version"],
    )

    app.register_blueprint(internal_bp)
