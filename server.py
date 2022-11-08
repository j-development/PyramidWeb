import calculator
from sqlalchemy import create_engine
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
from repository import get_cars as cars

engine = create_engine("mysql://user:root@localhost/pythondb", echo=True)


def hello_world(request):
    return Response("Hello World!")


@view_config(route_name="users", renderer="json")
def this_is_my_users(request):
    myUsers = ["Johan", "Lennart", "Fredrik"]
    return {"a": 4, "b": 10}


@view_config(route_name="cars", renderer="json")
def this_is_my_cars(request):
    resObj = {}
    counter = 0
    for car in cars():
        counter += 1
        resObj[car.maker] = car.model
    return resObj


@view_config(route_name="hello", renderer="json")
def this_is_my_hello(request):
    return {"hello": "world"}


@view_config(route_name="home", renderer="templates/home.jinja2")
def home(request):
    return {"greet": "Welcome", "name": "Tut Ankh Amun!"}


@view_config(route_name="add", request_method="POST")
def add(request):
    result = None
    try:
        numDict = request.json_body
        result = calculator.add(numDict["a"], numDict["b"])
    except:
        print("An exception occurred")
    return Response(str(result))


@view_config(route_name="multiply", request_method="POST")
def multiply(request):
    result = None
    try:
        numDict = request.json_body
        result = calculator.multiply(numDict["a"], numDict["b"])
    except:
        print("An exception occurred")
    return Response(str(result))


if __name__ == "__main__":
    with Configurator() as config:
        config.include("pyramid_jinja2")
        config.include("pyramid_debugtoolbar")
        config.add_static_view(name="static", path="static")
        config.add_route("hello", "/")
        config.add_route("home", "/home")
        config.add_route("cars", "/cars")
        config.add_route("users", "/users")
        config.add_route("add", "/add")
        config.add_route("multiply", "/multiply")
        config.scan()
        app = config.make_wsgi_app()
    server = make_server("0.0.0.0", 6543, app)
    print("server starting")
    server.serve_forever()
