# from logging import raiseExceptions
# from flask import Flask
import sys
from housing.logger import logging
from housing.exception import HousingException

# app = Flask(__name__)

# @app.route("/",methods=["GET","POST"])
# def test():
#     try:
#         3/0
#     except Exception as e:
#         house_exception = HousingException(e,sys) # need to pass exception and sys. Check exceptions > __init__.py for more details.
#         logging.info(house_exception.error_message)
#         logging.info(house_exception.__str__())
#         logging.info("Testing Logger")
#     return "Hello World."

# if __name__==("__main__"):
#     app.run()