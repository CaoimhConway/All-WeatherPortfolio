from datetime import datetime
from collections import *



class AllWeatherStrategy(QCAlgorithm):
    def Initialize(self):
        self.SetStartDate(2008, 1, 1)  
        self.SetEndDate(2020, 1, 31)  
        self.SetCash(100000) 
        self.monthCounter = 0
        # Country index ETFs according to https://seekingalpha.com/etfs-and-funds/etf-tables/countries
        self.etfs = [
            (self.AddEquity('VTI', Resolution.Daily).Symbol,0.3), #Vanguard Total Stock Market ETF
            (self.AddEquity('TLT', Resolution.Daily).Symbol,0.4), # iShares 20+ Year Treasury ETF (TLT)
            (self.AddEquity('IEF', Resolution.Daily).Symbol,0.15),  #iShares 7 – 10 Year Treasury ETF (IEF)
            (self.AddEquity('GLD', Resolution.Daily).Symbol,0.075), #SPDR Gold Shares ETF (GLD),  #SPDR Gold Shares (GLD)  
            (self.AddEquity('DBC', Resolution.Daily).Symbol,0.075) # PowerShares DB Commodity Index Tracking Fund (DBC)"
            ]
            
        self.Schedule.On(self.DateRules.MonthStart(self.etfs[0][0]), self.TimeRules.AfterMarketOpen(self.etfs[0][0]), self.Rebalance)
        self.leverage = 1.5
        self.monthCounter = 1
        
    def OnData(self, data):
       pass
     
    def Rebalance(self):
        if self.monthCounter is 12:
            self.SetHoldings([PortfolioTarget(etf, target*self.leverage) for etf, target in self.etfs])
            self.monthCounter = 1
        else:
            self.monthCounter = self.monthCounter+1
