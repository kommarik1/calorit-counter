from flask import Flask
from counter.builder import Bind
from counter.view import home

__version__: str = "0.1.3"
__package_name__: str = "calorie-counter"
__all__ = (
    "__version__",
    "__package_name__",
    "easyrun",
    "application",
    "Bind",
)

application: Flask = Flask(__name__)
application.register_blueprint(home.blueprint)


def easyrun(bind: Bind = Bind("0.0.0.0:5001"), debug: bool = False) -> None:
    application.run(bind.host, bind.port, debug)
