from app import app
from app.models import User, Post


@app.shell_context_processor
def make_shell_context():
    return {'User': User, 'Post': Post}
