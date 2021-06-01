from json import load
import unittest
from src.repos.reports.reportsRepo import ReportsRepo
import datetime as dt
from src.appConfig import loadAppConfig


class TestReportsRepo(unittest.TestCase):
    def setUp(self):
        appConfig = loadAppConfig()
        dbConStr = appConfig['dbConnStr']
        self.reportsRepo = ReportsRepo(dbConStr)

    def test_getFreqStats(self) -> None:
        targetDt = dt.datetime(2021, 5, 20)
        freqStats = self.reportsRepo.getFreqStats(targetDt)
        # print(freqStats)
        self.assertFalse(freqStats == None)
    
    def test_getFreqBands(self) -> None:
        targetDt = dt.datetime(2021, 5, 20)
        freqBands = self.reportsRepo.getFreqBands(targetDt)
        # print(freqBands)
        self.assertFalse(freqBands == None)
    
    def test_getWrConsMu(self) -> None:
        targetDt = dt.datetime(2021, 5, 20)
        wrConsMu = self.reportsRepo.getWrConsMu(targetDt)
        # print(wrConsMu)
        self.assertFalse(wrConsMu == None)
    
    def test_getMaxDemInfo(self) -> None:
        targetDt = dt.datetime(2021, 5, 20)
        maxDemInfo = self.reportsRepo.getMaxDemInfo(targetDt)
        # print(maxDemInfo)
        self.assertFalse(maxDemInfo == None)
    
    def test_getIrSchAct(self) -> None:
        targetDt = dt.datetime(2021, 5, 20)
        irSchAct = self.reportsRepo.getIrSchAct(targetDt)
        # print(irSchAct)
        self.assertFalse(irSchAct == None)
