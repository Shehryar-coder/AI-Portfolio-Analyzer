from functools import wraps
from flask import session, redirect, url_for, flash


def login_required(f):
    """Redirect to login page if no user is in session."""
    @wraps(f)
    def decorated(*args, **kwargs):
        if not session.get('user_id'):
            flash('Please log in to continue.', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated
