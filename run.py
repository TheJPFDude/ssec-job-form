#!flask/bin/python
from app import app

if __name__ == '__main__':
    app.secret_key='super secret yo'
    app.config['SERVER_NAME'] = 'phase.ssec.wisc.edu:5000'
    app.run(host='0.0.0.0', port=5000, debug=True)