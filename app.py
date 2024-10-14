from flask import Flask
from attr import attrs, attrib

from data import *
app = Flask(__name__)

class Matoki:
    def foo(self):
        pass

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
    pii = Pii('Jimi Hendrix', 27, 666, '123')
    admin = expose()

    return f'hello {admin.name}'


@app.route('/api/foo')
def foo():
    pii = Pii('Jimi Hendrix', 27, 666, '123')
    return f'name {pii.name} {pii.age}'

if __name__ == '__main__':
    app.run()
