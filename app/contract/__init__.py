# coding:utf-8
from flask import Blueprint

contract = Blueprint('contract',__name__)
from app.contract import views