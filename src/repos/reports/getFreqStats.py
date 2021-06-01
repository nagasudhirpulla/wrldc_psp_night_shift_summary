import datetime as dt
import cx_Oracle
def getFreqStats(dbConStr:str, targetDt:dt.datetime):
    # connect to app database
    con = cx_Oracle.connect(dbConStr)

    dataFetchSql = '''SELECT MAX_FREQ,
        MAX_TIME,
        MIN_FREQ,
        MIN_TIME,
        FREQ_VARIATION_INDEX,
        AVERAGE_FREQUENCY
    FROM REPORTING_UAT.FREQUENCY_PROFILE_MAX_MIN fpmm
    WHERE DATE_KEY = :1
    '''
    # get cursor and execute fetch sql
    cur = con.cursor()
    dateInt = int(dt.datetime.strftime(targetDt, "%Y%m%d"))
    cur.execute(dataFetchSql, (dateInt,))
    colNames = [row[0] for row in cur.description]
    targetColumns = ['MAX_FREQ', 'MAX_TIME', 'MIN_FREQ', 'MIN_TIME',
                     'FREQ_VARIATION_INDEX', 'AVERAGE_FREQUENCY']
    if (False in [(col in targetColumns) for col in colNames]):
        # all desired columns not fetched, hence return empty
        return {}
    # print(colNames)

    # fetch all rows
    dbRows = cur.fetchall()
    if len(dbRows) == 0:
        return None

    maxFreqInd = colNames.index('MAX_FREQ')
    minFreqInd = colNames.index('MIN_FREQ')
    maxFreqTimeInd = colNames.index('MAX_TIME')
    minFreqTimeInd = colNames.index('MIN_TIME')
    fviInd = colNames.index('FREQ_VARIATION_INDEX')
    avgFreqInd = colNames.index('AVERAGE_FREQUENCY')

    # iterate through each row to populate result outage rows
    row = dbRows[0]
    maxFreq: str = row[maxFreqInd]
    maxFreqTime: str = row[maxFreqTimeInd]
    minFreq: str = row[minFreqInd]
    minFreqTime: str = row[minFreqTimeInd]
    fvi: str = row[fviInd]
    avgFreq: str = row[avgFreqInd]
    resData = {
        "maxFreq": maxFreq,
        "minFreq": minFreq,
        "maxFreqTime": maxFreqTime,
        "minFreqTime": minFreqTime,
        "fvi": fvi,
        "avgFreq": avgFreq
    }
    return resData