from configs import config
import jwt


class JwtProcessor:
    def __init__(self):
        self.sk = config.SECRET_KEY

    def issue(self, payload):
        return jwt.encode(payload, self.sk, algorithm="HS256")

    def verify(self, token):
        try:
            return jwt.decode(token, self.sk, algorithms=["HS256"])
        except jwt.exceptions.InvalidSignatureError:
            raise ValueError("Invalid token signature.")
        except jwt.exceptions.DecodeError:
            raise ValueError("Invalid token.")
        except jwt.exceptions.ExpiredSignatureError:
            raise ValueError("Token has expired.")
