import os

class Config:
    SECRET_KEY = "abc123"

    basedir = os.path.abspath(os.path.dirname(__file__))
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "site.db")
    MAIL_SERVER="smtp.googlemail.com"
    MAIL_PORT=587
    MAIL_USE_TLS=True
    MAIL_USERNAME=os.environ.get("EMAIL_USER")
    MAIL_PASSWORD=os.environ.get("EMAIL_PASS")