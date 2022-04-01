# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 22:10:36 2022

@author: ADMIN
"""

import os
import pandas as pd
import MetaTrader5 as mt5
from datetime import datetime


class RSI_MACD_SCALPER(object):
    def __init__(self, user , server, password, timeframe, instrument):
        self.user = user
        self.server = server
        self.password = password
        self.timeframe = timeframe
        self.instrument = instrument
        
    def initializedMT5(self):
        if not mt5.initialize(login=self.user, server=self.server,password=self.password):
            print("initialize() failed, error code =",mt5.last_error())
            
    def 