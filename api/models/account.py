import uuid
from flask_login import UserMixin  # type: ignore
from sqlalchemy import func
from models.base import Base
from .engine import db


class Account(UserMixin, Base):
    __tablename__ = "accounts"
    __table_args__ = (db.PrimaryKeyConstraint("id", name="account_pkey"), db.Index("account_email_idx", "email"))

    id = db.Column(db.String(36), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=True)
    password_salt = db.Column(db.String(255), nullable=True)
    avatar = db.Column(db.String(255))
    interface_language = db.Column(db.String(255))
    interface_theme = db.Column(db.String(255))
    timezone = db.Column(db.String(255))
    last_login_at = db.Column(db.DateTime)
    last_login_ip = db.Column(db.String(255))
    last_active_at = db.Column(db.DateTime, nullable=False, server_default=func.current_timestamp())
    status = db.Column(db.String(16), nullable=False, server_default=db.text("'active'::character varying"))
    initialized_at = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, nullable=False, server_default=func.current_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, server_default=func.current_timestamp())

    @property
    def is_password_set(self):
        return self.password is not None