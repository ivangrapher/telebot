import proc
import re
import requests

def provval():
    result =''
    with open("text.txt","r") as f:
        for line in f:
            user_id = line.split(maxsplit=1)[0]
            valik = line.split(maxsplit=2)[1]
            try:
                if(proc.load_info(valik)):
                    ex = (proc.load_info(valik))
                    tmp = poiskjailed(ex)
                    if(tmp=='tyrma'):
                        print('У юзера ' + user_id + ' валидатор ' + valik + ' в тюрьме\n')
                        result = result +  str(user_id) + " " + str(valik) + ','
                else:
                    ex = 'Не удалось получить данные валика ' + str(valik)
            except:
                ex = 'Не удалось получить данные валика\n'
        return result
def poiskjailed(st):
    tmp = st.split(",")
    jail = tmp[3].split(":")
    if(str(jail[0].strip()) =='"jailed"'):
        if(jail[1].strip()== 'false'):
            return 'false'
        else:
            return 'tyrma'
    else:
        return 'nenashlystrky'
