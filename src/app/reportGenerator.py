import os
import datetime as dt
from typing import List
from docxtpl import DocxTemplate, InlineImage
from src.repos.reports.reportsRepo import ReportsRepo


class ReportGenerator:
    appDbConStr: str = ''

    def __init__(self, appDbConStr: str):
        self.appDbConStr = appDbConStr

    def getReportContextObj(self, targetDt: dt.datetime) -> object:
        """get the report context object for populating the weekly report template
        Args:
            startDate (dt.datetime): start date object
            endDate (dt.datetime): end date object
        Returns:
            IReportCxt: report context object
        """
        reportsRepo = ReportsRepo(self.appDbConStr)
        freqStats = reportsRepo.getFreqStats(targetDt)
        freqBands = reportsRepo.getFreqBands(targetDt)
        wrConsMu = reportsRepo.getWrConsMu(targetDt)
        maxDemInfo = reportsRepo.getMaxDemInfo(targetDt)
        irSchAct = reportsRepo.getIrSchAct(targetDt)
        reportContext = {**freqStats, **freqBands, **wrConsMu, **maxDemInfo, **irSchAct}
        reportContext["todayStr"] = dt.datetime.strftime(targetDt+dt.timedelta(days=1), "%d.%m.%Y")
        reportContext["dateStr"] = dt.datetime.strftime(targetDt, "%d-%b-%Y")
        reportContext["dateObj"] = targetDt
        return reportContext

    def generateReportWithContext(self, reportContext, tmplPath: str, dumpFolder: str) -> bool:
        try:
            doc = DocxTemplate(tmplPath)
            doc.render(reportContext)
            dumpFileName = 'Night_Shift_Summary_{0}.docx'.format(dt.datetime.strftime(
                reportContext['dateObj'], '%d-%m-%Y'))
            dumpFileFullPath = os.path.join(dumpFolder, dumpFileName)
            doc.save(dumpFileFullPath)
        except Exception as err:
            print(err)
            return False
        return True

    def generateReport(self, targetDt: dt.datetime, tmplPath: str, dumpFolder: str) -> bool:
        reportCtxt = self.getReportContextObj(targetDt)
        print(reportCtxt)
        isSuccess = self.generateReportWithContext(
            reportCtxt, tmplPath, dumpFolder)
        return isSuccess