from flask import Flask
from attr import attrs, attrib

from data import *
app = Flask(__name__)

@attrs
class UserAdmin:
    product_name = attrib()
    price = attrib()
    def __init__(self):
        self.phone = '123'
        self.name = 'jo'
        self.address = 'fasdfdsa'
        self.cvv = '666'


def expose():
    admin = UserAdmin()
    return admin


@app.route('/api/hello')
def hello_world():
    admin = expose()
    return f'hello {admin.name}'


if __name__ == '__main__':
    app.run()
