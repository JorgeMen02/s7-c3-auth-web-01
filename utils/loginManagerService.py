from flask_login import LoginManager
from models.auth.user import User

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user:
        return user
    return None
