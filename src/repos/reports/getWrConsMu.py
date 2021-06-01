import datetime as dt
import cx_Oracle
def getWrConsMu(dbConStr:str, targetDt:dt.datetime):
    # connect to app database
    con = cx_Oracle.connect(dbConStr)

    dataFetchSql = '''select DAY_ENERGY_DEMAND_MET
    from REPORTING_UAT.regional_availability_demand
    where date_key = :1
    '''
    # get cursor and execute fetch sql
    cur = con.cursor()
    dateInt = int(dt.datetime.strftime(targetDt, "%Y%m%d"))
    cur.execute(dataFetchSql, (dateInt,))
    colNames = [row[0] for row in cur.description]
    targetColumns = ['DAY_ENERGY_DEMAND_MET']
    if (False in [(col in targetColumns) for col in colNames]):
        return {}
    # print(colNames)

    # fetch all rows
    dbRows = cur.fetchall()
    if len(dbRows) == 0:
        return None

    consMuInd = colNames.index('DAY_ENERGY_DEMAND_MET')

    row = dbRows[0]
    consMu: str = row[consMuInd]
    resData = {
        "wrConsMu": consMu
    }
    return resData