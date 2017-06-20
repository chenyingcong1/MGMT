# coding:utf-8
from flask import Blueprint

chart = Blueprint('chart', __name__)
from app.chart import views