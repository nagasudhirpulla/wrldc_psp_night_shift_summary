import cx_Oracle
import datetime as dt
from typing import List
from src.repos.reports.getFreqStats import getFreqStats
from src.repos.reports.getFreqBands import getFreqBands
from src.repos.reports.getWrConsMu import getWrConsMu
from src.repos.reports.getMaxDemInfo import getMaxDemInfo
from src.repos.reports.getIrSchAct import getIrSchAct

class ReportsRepo():
    """Repository class for outages data of application
    """
    dbConStr: str = ""

    def __init__(self, dbConStr: str) -> None:
        self.dbConStr = dbConStr

    def getFreqStats(self, targetDt: dt.datetime) -> bool:
        freqStats = getFreqStats(self.dbConStr, targetDt)
        return freqStats
    
    def getFreqBands(self, targetDt: dt.datetime) -> bool:
        freqBands = getFreqBands(self.dbConStr, targetDt)
        return freqBands
    
    def getWrConsMu(self, targetDt: dt.datetime) -> bool:
        consMu = getWrConsMu(self.dbConStr, targetDt)
        return consMu
    
    def getMaxDemInfo(self, targetDt: dt.datetime) -> bool:
        maxDemInfo = getMaxDemInfo(self.dbConStr, targetDt)
        return maxDemInfo
    
    def getIrSchAct(self, targetDt: dt.datetime) -> bool:
        irSchAct = getIrSchAct(self.dbConStr, targetDt)
        return irSchAct