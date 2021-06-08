from flask import Blueprint

test_countroller = Blueprint('test_countroller', __name__)

@test_countroller.route('/helloworld')
def helloworld():
    return 'Hello World.'


@test_countroller.route('/test')
def test():
    return '<h1>test</h1>'
