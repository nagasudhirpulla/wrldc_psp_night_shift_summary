import datetime as dt
import cx_Oracle
def getIrSchAct(dbConStr:str, targetDt:dt.datetime):
    # connect to app database
    con = cx_Oracle.connect(dbConStr)

    dataFetchSql = '''select SUM(TOTAL_IR_ACTUAL) AS REG_ACT,
        sum(TOTAL_IR_SCHEDULE) AS REG_SCH
    from REPORTING_UAT.INTER_REGIONAL_SCHEDULE_ACTUAL
    WHERE date_key = :1
    GROUP BY DATE_KEY
    '''
    # get cursor and execute fetch sql
    cur = con.cursor()
    dateInt = int(dt.datetime.strftime(targetDt, "%Y%m%d"))
    cur.execute(dataFetchSql, (dateInt,))
    colNames = [row[0] for row in cur.description]
    targetColumns = ["REG_ACT", "REG_SCH"]
    if (False in [(col in targetColumns) for col in colNames]):
        return None

    # fetch all rows
    dbRows = cur.fetchall()
    if len(dbRows) == 0:
        return None

    actIrMuInd = colNames.index('REG_ACT')
    schIrMuInd = colNames.index('REG_SCH')

    row = dbRows[0]
    actIrMu: str = row[actIrMuInd]
    schIrMu: str = row[schIrMuInd]
    resData = {
        "actIrMu": actIrMu,
        "schIrMu": schIrMu
    }
    return resData