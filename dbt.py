def ddbb():
    import sqlite3
    conn = sqlite3.connect('database.db')
    c = conn.cursor()
    l=[]
    ll=[]
    c.execute('''SELECT sum(count) from cpns  ''')
    result = c.fetchall()
    total=str(result[0][0])
    success=str(result[0][0])
    fail=0
    fe = conn.cursor()
    fe.execute('''SELECT count(id) from Em  ''')
    result = fe.fetchall()
    feedback=str(result[0][0])
    fe = conn.cursor()
    for x in range(12):
        n=x+1
        n=str(n)
        fe.execute('SELECT sum(count) from cpns where m='+n)
        jan = fe.fetchall()
        jan=jan[0][0]
        l.append(jan)
    for x in l:
        if x==None:
            ll.append(0)
        else:
            ll.append(x)
    year=ll    

    fe.execute('''SELECT  id,s,n,typ,tc,date from Cpns order by id desc LIMIT 5 ''')
    camp = fe.fetchall()
    fe.execute('''SELECT  id,n,t,date from Em order by id desc LIMIT 5 ''')
    feb = fe.fetchall()
    fe.execute('''SELECT  sum(count) from Cpns  where typ="email"''')
    em = fe.fetchall()
    em=em[0][0]
    fe.execute('''SELECT  sum(count) from Cpns  where typ="sms"''')
    sms = fe.fetchall()
    sms=sms[0][0]
    fe.execute('''SELECT  sum(count) from Cpns  where typ="fb"''')
    fb = fe.fetchall()
    fb=fb[0][0]

    conn.close()
    d={
        "total":total,
        "succ":success,
        "fail":fail,
        "feedback":feedback,
        "months":year,
        "c":camp,
        "feb":feb,
        "em":em,
        "sms":sms,
        "fb":fb,
        "inst":0
    }

    return d