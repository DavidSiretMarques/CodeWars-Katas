"""
Solution to the CodeWars kata Human Readable Duration Format
Link:
https://www.codewars.com/kata/52742f58faf5485cae000b9a
"""

def format_duration(seconds):
    if seconds==0: return "now"
    minutes, hours, days, years=0,0,0,0
    while seconds>=60:
        minutes=seconds//60
        hours=minutes//60
        days=hours//24
        years=days//365
        seconds=seconds % 60
        minutes= minutes % 60
        hours= hours % 24
        days= days % 365
    answer=[]
    #Years
    if years>1: answer.append(str(years)+" years")
    elif years==1: answer.append(str(years)+" year")
    #Days
    if days>1: answer.append(str(days)+" days")
    elif days==1: answer.append(str(days)+" day")
    #Hours
    if hours>1: answer.append(str(hours)+" hours")
    elif hours==1: answer.append(str(hours)+" hour")
    #Minutes
    if minutes>1: answer.append(str(minutes)+" minutes")
    elif minutes==1: answer.append(str(minutes)+" minute")
    #Seconds
    if seconds>1: answer.append(str(seconds)+" seconds")
    elif seconds==1: answer.append(str(seconds)+" second")
    if len(answer) >2:
        result=", ".join(answer[:-1])
        result+=" and "+ answer[-1]
    elif len(answer)==2: 
        result= " and ".join(answer)
    else: 
        result=str(answer[0])
    return result

# --------------------------------------------Extras--------------------------------------------

#Other solutions

def format_duration2(seconds):
    if seconds == 0: return "now"
    units = ( (31536000, "year"  ), 
              (   86400, "day"   ),
              (    3600, "hour"  ),
              (      60, "minute"),
              (       1, "second") )
    ts, t = [], seconds
    for unit in units:
        u, t = divmod(t, unit[0])
        ts += ["{} {}{}".format(u, unit[1], "s" if u>1 else "")] if u != 0 else []
    return ", ".join([str(d)for d in ts[:-1]]) + (" and " if len(ts)>1 else "") + ts[-1]
