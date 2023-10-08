from flask import Flask

import app_state

"""Неоднозначная конструкция, к которой пришёл после ряда экспериментов, 
для уверенности подглядев у архитектора из одной небольшой компании.."""

app = Flask(__name__)
bills_amount = 1
bills_list = []
state_now = app_state.State.WORK

import routes
