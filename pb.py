import proc
import re
import requests

def getval(userid,val):
    f = open('text.txt', 'rt')
    i = 0
    for line in f:
        user_id = line.split(maxsplit=1)[0]
        valik = line.split(maxsplit=2)[1]
        if(user_id == str(userid)):
            i = i +1
        if(i >=3):
            return 2
        if((user_id == str(userid)) and (valik == str(val))):
            f.close()
            return 1
    f.close()
    return False

def writeval(userid,val):
    val = val.split(maxsplit=1)[0]
    if(val[0] == '/'):
        val = val[1:]
    if (getval(userid,val) == 1):
        return ("Валик "+ str(val) + " у пользователя " + str(userid) + " уже есть")
    if (getval(userid,val) == 2):
        return ("У Вас уже 3 валика.\nМаксимальное количество 3 валика")

    try:
        f = open('text.txt', 'a')
        f.write(str(userid) + ' ' + str(val) + '\n')
        return "Валик успешно добавлен"
    except:
        return "Не удалось добавить валик"

def myval(userid):
    f = open('text.txt', 'rt')
    result = ''
    for line in f:
        user_id = line.split(maxsplit=1)[0]
        if(user_id == str(userid)):
            result = result + str(line).split(maxsplit=2)[1] + "\n"
    f.close()
    if(result):
        return result
    else:
        return "у вас пока нет валиков"

def delval(userid):
    with open("text.txt","r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            user_id = line.split(maxsplit=1)[0]
            if(user_id != str(userid)):
                f.write(line)
        f.truncate()

def infoval(userid):
    res =''
    with open("text.txt","r") as f:
        for line in f:
            user_id = line.split(maxsplit=1)[0]
            if(user_id == str(userid)):
                valik = line.split(maxsplit=2)[1]
                try:
                    if(proc.load_info(valik)):
                        ex = (proc.load_info(valik))
                    else:
                        ex = 'Не удалось получить данные валика ' + str(valik) + "\n"
                except:
                    ex = 'Не удалось получить данные валика'
                res = res + ex + "\n"
    return res

