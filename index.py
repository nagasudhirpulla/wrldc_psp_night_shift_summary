from src.appConfig import loadAppConfig
from src.app.reportGenerator import ReportGenerator
import datetime as dt
import argparse

parser = argparse.ArgumentParser()
# add argument with flag --name
parser.add_argument('--config', help='Config File Path', default='assets/config')
parser.add_argument('--template', help='Template File Path', default='assets/template.docx')
parser.add_argument('--output', help='output Folder Path', default='reports')
args = parser.parse_args()

configPath = args.config
templatePath = args.template
outputFolderPath = args.output

targetDt = dt.datetime.now() - dt.timedelta(days=1)
appConf = loadAppConfig()
dbConStr = appConf['dbConnStr']

rGen = ReportGenerator(dbConStr)
rGen.generateReport(targetDt, templatePath, outputFolderPath)
