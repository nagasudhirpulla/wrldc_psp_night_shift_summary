import datetime as dt
import cx_Oracle
def getMaxDemInfo(dbConStr:str, targetDt:dt.datetime):
    # connect to app database
    con = cx_Oracle.connect(dbConStr)

    dataFetchSql = '''select 
        MAX_DEMAND,
        MAX_DEMAND_TIME,
        STATE_NAME
    from REPORTING_UAT.state_demand_requirement
    where date_key = :1
    '''
    # get cursor and execute fetch sql
    cur = con.cursor()
    dateInt = int(dt.datetime.strftime(targetDt, "%Y%m%d"))
    cur.execute(dataFetchSql, (dateInt,))
    colNames = [row[0] for row in cur.description]
    targetColumns = ['MAX_DEMAND', 'MAX_DEMAND_TIME', 'STATE_NAME']
    if (False in [(col in targetColumns) for col in colNames]):
        return None
    # print(colNames)

    # fetch all rows
    dbRows = cur.fetchall()
    if len(dbRows) == 0:
        return None

    maxDemInd = colNames.index('MAX_DEMAND')
    maxDemTimeInd = colNames.index('MAX_DEMAND_TIME')
    stateNameInd = colNames.index('STATE_NAME')

    # iterate through each row to populate result outage rows
    resData = {}
    for row in dbRows:
        maxDem: float = row[maxDemInd]
        maxDemTime: str = row[maxDemTimeInd]
        stateName: str = row[stateNameInd]
        stateKeyLookUp = {
            "WR":"wr",
            "DAMAN AND DIU":"dd",
            "AMNSIL":"amnsil",
            "CHHATTISGARH":"chhat",
            "DNH":"dnh",
            "MADHYA PRADESH":"mp",
            "GUJARAT":"gj",
            "GOA":"goa",
            "MAHARASHTRA":"mh",
            "WR":"wr"
        }
        if stateName in stateKeyLookUp:
            resData[stateKeyLookUp[stateName]+"MaxDem"] = round(maxDem)
            resData[stateKeyLookUp[stateName]+"MaxDemTime"] = maxDemTime
    return resData