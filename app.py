from app import create_app


app= create_app()

from flask_wtf.csrf import CSRFProtect

csrf = CSRFProtect()

if __name__ == '__main__':
    app.run(host="0.0.0.0", ssl_context=("cert.pem","key.pem")
