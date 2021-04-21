import sqlite3

try:
    userName = 'a'

    conn = sqlite3.connect('./db.sqlite3')

    cmd = "SELECT id FROM auth_user WHERE username='{}'".format(userName)
    data = conn.execute(cmd)
    for row in data:
        id = row[0]

    cmd = "SELECT ContestAdmin_contest.id,ContestAdmin_contest.Title,ContestAdmin_contest.Description,ContestAdmin_contest.TimeRegister,ContestAdmin_contest.TimeStart,ContestAdmin_contest.TimeEnd,ContestAdmin_language.Language,ContestAdmin_status.Status FROM ContestAdmin_status JOIN ContestAdmin_contest ON ContestAdmin_status.IDcontest = ContestAdmin_contest.id JOIN ContestAdmin_language ON ContestAdmin_language.id = ContestAdmin_contest.IDLanguage WHERE ContestAdmin_status.IDUser = '{}' GROUP BY ContestAdmin_status.IDContest".format(id)
    submited = conn.execute(cmd)
        
    cmd = "SELECT ContestAdmin_contest.id,ContestAdmin_contest.Title,ContestAdmin_contest.Description,ContestAdmin_contest.TimeRegister,ContestAdmin_contest.TimeStart,ContestAdmin_contest.TimeEnd,ContestAdmin_language.Language FROM ContestAdmin_registercontest JOIN ContestAdmin_contest ON ContestAdmin_contest.id = ContestAdmin_registercontest.IDContest JOIN ContestAdmin_language ON ContestAdmin_contest.IDLanguage = ContestAdmin_language.id WHERE ContestAdmin_registercontest.IDUser='{0}' AND ContestAdmin_registercontest.IDcontest NOT IN (SELECT (IDcontest) FROM ContestAdmin_status WHERE IDUser = '{0}')".format(id)
    registed = conn.execute(cmd)
        
    cmd = "SELECT ContestAdmin_contest.id,ContestAdmin_contest.Title,ContestAdmin_contest.Description,ContestAdmin_contest.TimeRegister,ContestAdmin_contest.TimeStart,ContestAdmin_contest.TimeEnd,ContestAdmin_language.Language FROM ContestAdmin_contest JOIN ContestAdmin_language ON ContestAdmin_contest.IDLanguage = ContestAdmin_language.id WHERE ContestAdmin_contest.id NOT IN (SELECT (IDcontest) FROM ContestAdmin_registercontest WHERE ContestAdmin_registercontest.IDUser = '{0}')".format(id)
    unregisted = conn.execute(cmd)
except EOFError as e:
    print (e)

historyContests=[]
regisContests=[]
unRegisContests=[]

# print('\n\n\n-----------------------Sub contest')
for row in submited:    
    t = {
        "idContest": row[0],
        "title": row[1],
        "description": row[2],
        "timeRegister": row[3],
        "timeStart": row[4],
        "timeEnd": row[5],
        "language": row[6],
        "result":row[7]
    }
    historyContests.append(t)
# for x in historyContests: print(x)

# print('\n\n\n-----------------------Regi contest')
for row in registed:
    t = {
        "idContest": row[0],
        "title": row[1],
        "description": row[2],
        "timeRegister": row[3],
        "timeStart": row[4],
        "timeEnd": row[5],
        "language": row[6],
        "isRegister": True,
    }
    regisContests.append(t)
# for x in regisContests: print(x)
    

# print('\n\n\n-----------------------All contest')
for row in unregisted:   
    t = {
        "idContest": row[0],
        "title": row[1],
        "description": row[2],
        "timeRegister": row[3],
        "timeStart": row[4],
        "timeEnd": row[5],
        "language": row[6],
        "isRegister": False,
    }
    unRegisContests.append(t)
# for x in unRegisContests: print(x)