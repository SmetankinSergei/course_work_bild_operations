from flask import render_template, redirect, url_for

import main
import utils
from main import app


@app.route('/')
def home():
    """Главная и единственная страница"""
    return render_template('index.html', bills_amount=main.bills_amount, bills_list=main.bills_list)


@app.get('/show/<int:bills_amount>')
def show_bild_list(bills_amount):
    """Показывает отсортированный список указанного количества операций"""
    bills_list = utils.get_bills_list(bills_amount)
    main.bills_list = utils.create_list_for_output(bills_list)
    return redirect(url_for('home'))


@app.get('/cancel')
def cancel_number():
    """Сбрасывает состояние приложения к изначальному"""
    main.bills_amount = '1'
    main.bills_list = []
    return redirect(url_for('home'))


@app.get('/increase/<int:bills_amount>')
def increase(bills_amount):
    """Увеличивает счётчик списка операций"""
    main.bills_amount = bills_amount + 1
    return redirect(url_for('home'))


@app.get('/decrease/<int:bills_amount>')
def decrease(bills_amount):
    """Уменьшает счётчик операций"""
    if bills_amount > 1:
        main.bills_amount = bills_amount - 1
    return redirect(url_for('home'))
