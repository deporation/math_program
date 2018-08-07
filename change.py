# -*- coding: utf-8 -*-
# change.py
import numpy as np
class change:
    date = ""
    trade_number = 0
    methoad = ''
    count = 0
    val = 0
    change_count = 0
    change_mon = 0
    date_detail = ""
    def __init__(self,date,trade_number,methoad,val,count,change,change_mon,date_detail):
        self.date = date
        self.trade_number = trade_number
        self.methoad = methoad
        self.val = val
        self.change_mon = change_mon
        self.change_count = change
        self.date_detail = date_detail