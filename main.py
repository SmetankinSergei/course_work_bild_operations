from flask import Flask

app = Flask(__name__)
bills_amount = 1
bills_list = []

import routes
