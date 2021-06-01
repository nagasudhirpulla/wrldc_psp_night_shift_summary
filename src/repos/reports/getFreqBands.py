import datetime as dt
import cx_Oracle
def getFreqBands(dbConStr:str, targetDt:dt.datetime):
    # connect to app database
    con = cx_Oracle.connect(dbConStr)

    dataFetchSql = '''select FREQ6_VALUE AS F_49_9,
        FREQ8_VALUE AS F_50_5,
        FREQ7_VALUE AS BAND_PERC
    from REPORTING_UAT.FREQUENCY_PROFILE
    where date_key = :1
    '''
    # get cursor and execute fetch sql
    cur = con.cursor()
    dateInt = int(dt.datetime.strftime(targetDt, "%Y%m%d"))
    cur.execute(dataFetchSql, (dateInt,))
    colNames = [row[0] for row in cur.description]
    targetColumns = ['F_49_9', 'F_50_5', 'BAND_PERC']
    if (False in [(col in targetColumns) for col in colNames]):
        return None
    # print(colNames)

    # fetch all rows
    dbRows = cur.fetchall()
    if len(dbRows) == 0:
        return None

    perc49_9Ind = colNames.index('F_49_9')
    perc50_5Ind = colNames.index('F_50_5')
    percBandInd = colNames.index('BAND_PERC')

    # iterate through each row to populate result outage rows
    row = dbRows[0]
    perc49_9: str = row[perc49_9Ind]
    perc50_5: str = row[perc50_5Ind]
    percBand: str = row[percBandInd]
    resData = {
        "perc49_9": perc49_9,
        "perc50_5": perc50_5,
        "percBand": percBand
    }
    return resData