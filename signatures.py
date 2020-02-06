import hashlib
import random
import time
import urllib

RANDOMISE_CNONCE = True

def get_cnonce() -> str:
    if RANDOMISE_CNONCE:
        buf = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'   
        cnonce = ''
        length = random.randint(0,19) + 30
        for i in range(50):
            cnonce += random.choice(buf)
    else:
        cnonce = 'o5oorrrlBlbWKHRVuH7lBQdVCQEVKeXeTkAyA9H6FY8DT904sq'

    return cnonce

def crypt(inp:str):
    #sha256 alg + sol
    sol = '0woz2wTimes9izs0vFQjLmwqqSzAPNFtmWNcbOL6xJva5Molyb'#Fucking sol
    return hashlib.sha256(bytes(inp+sol,'utf-8')).hexdigest()

def get_timestamp()->str:
    return str(int(time.time()))

def to_url(input:str):
    
    return urllib.quote(input.encode('utf-8')).replace('\\+','%20')

def signature_v6_numcy_subscription_comment_add(access_token:str,cnonce:str,comment_id:int,timestamp:str):
    source = 'POSTapi.numbuster.com/api/v6/numcy/subscription/comment/addaccess_token='+access_token+'&cnonce='+cnonce+'&comment_id='+str(comment_id)+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_dailyquest_get(access_token:str,cnonce:str,timestamp:str):
    source = 'GETapi.numbuster.com/api/v6/dailyquest/getaccess_token='+access_token+'&cnonce='+cnonce+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_comment_list_my(access_token:str,cnonce:str,limit:int,offset:int,timestamp:str):
    source = 'GETapi.numbuster.com/api/v6/comment/list/myaccess_token='+access_token+'&cnonce='+cnonce+'&limit='+str(limit)+'&offset='+str(offset)+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_comment_list(access_token:str,cnonce:str,limit:int,offset:int,phone:str,timestamp:str):
    source = 'GETapi.numbuster.com/api/v6/comment/listaccess_token='+access_token+'&cnonce='+cnonce+'&limit='+str(limit)+'&offset='+str(offset)+'&phone='+phone+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_dailyquest_result_final(access_token:str,cnonce:str,daily_quest_id:int,timestamp:str):
    source = 'GETapi.numbuster.com/api/v6/dailyquest/result/finalaccess_token='+access_token+'&cnonce='+cnonce+'&daily_quest_id='+str(daily_quest_id)+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_dailyquest_result(access_token:str,cnonce:str,daily_quest_id:int,opened_item:int,result_number:int,timestamp:str):
    source = 'POSTapi.numbuster.com/api/v6/dailyquest/resultaccess_token='+access_token+'&cnonce='+cnonce+'&daily_quest_id='+str(daily_quest_id)+'&opened_item='+str(opened_item)+'&result_number='+str(result_number)+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_comment_delete(access_token:str,cnonce:str,phone:str,timestamp:str):
    source = 'POSTapi.numbuster.com/api/v6/comment/deleteaccess_token='+access_token+'&cnonce='+cnonce+'&phone='+phone+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_comment_add(access_token:str,cnonce:str,phone:str,text:str,timestamp:str):
    source = 'POSTapi.numbuster.com/api/v6/comment/addaccess_token='+access_token+'&cnonce='+cnonce+'&phone='+phone+'&text='+text+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_numcy_subscription_comment_renewal(access_token:str,cnonce:str,comment_id:int,timestamp:str):
    source = 'POSTapi.numbuster.com/api/v6/numcy/subscription/comment/renewalaccess_token='+access_token+'&cnonce='+cnonce+'&comment_id='+str(comment_id)+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_numcy_balance(access_token:str,cnonce:str,timestamp:str):
    source = 'GETapi.numbuster.com/api/v6/numcy/balanceaccess_token='+access_token+'&cnonce='+cnonce+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_notice_delete(access_token:str,cnonce:str,phone:str,timestamp:str):
    source = 'POSTapi.numbuster.com/api/v6/notice/deleteaccess_token='+access_token+'&cnonce='+cnonce+'&phone='+phone+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_comment_edit(access_token:str,cnonce:str,phone:str,text:str,timestamp:str):
    source = 'POSTapi.numbuster.com/api/v6/comment/editaccess_token='+access_token+'&cnonce='+cnonce+'&phone='+phone+'&text='+text+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_auth_get(cnonce:str,timestamp:str,lang='RU',platform='Android'):
    source = 'GETapi.numbuster.com/api/v6/auth/getcnonce='+cnonce+'&lang='+lang+'&platform='+platform+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_old_phone(phone:str,access_token:str,cnonce:str,timestamp:str,locale='RU'):
    source = 'GETapi.numbuster.com/api/v6/old/phone/'+phone+'access_token='+access_token+'&cnonce='+cnonce+'&locale='+locale+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_auth_agreement(cnonce:str,phone:str,timestamp:str):
    source = 'POSTapi.numbuster.com/api/v6/auth/agreementcnonce='+cnonce+'&phone='+phone+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_auth_facebook(cnonce:str,code:str,facebook_token:str,timestamp:str):
    source = 'POSTapi.numbuster.com/api/v6/auth/facebookcnonce='+cnonce+'&code='+code+'&facebook_token='+facebook_token+'&timestamp'+timestamp
    return crypt(source)

def signature_v6_old_sms(phone:str,access_token:str,cnonce:str,timestamp:str,locale:'RU'):
    source = 'GETapi.numbuster.com/api/v6/old/sms/'+phone+'access_token='+access_token+'&cnonce='+cnonce+'&locale='+locale+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_dailyquest_calendar(access_token:str,cnonce:str,timestamp:str):
    source = 'GETapi.numbuster.com/api/v6/dailyquest/calendaraccess_token='+access_token+'&cnonce='+cnonce+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_old_search(phone:str,access_token:str,cnonce:str,timestamp:str,locale='RU'):
    source = 'GETapi.numbuster.com/api/v6/old/search/'+phone+'access_token='+access_token+'&cnonce='+cnonce+'&locale='+locale+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_auth_agreement_code(cnonce:str,code:str,timestamp:str):
    source = 'POSTapi.numbuster.com/api/v6/auth/agreement_codecnonce='+cnonce+'&code='+code+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_old_profiles_by_phone(phone:str,access_token:str,cnonce:str,timestamp:str,locale='RU'):
    source = 'GETapi.numbuster.com/api/v6/old/profiles/by_phone/'+phone+'access_token='+access_token+'&cnonce='+cnonce+'&locale='+locale+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_auth_check(cnonce:str,code:str,timestamp:str):
    source = 'GETapi.numbuster.com/api/v6/auth/checkcnonce='+cnonce+'&code='+code+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_notice_add(access_token:str,cnonce:str,phone:str,text:str,timestamp:str):
    source = 'POSTapi.numbuster.com/api/v6/notice/addaccess_token='+access_token+'&cnonce='+cnonce+'&phone='+phone+'&text='+text+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_notice_edit(access_token:str,cnonce:str,phone:str,text,timestamp:str):
    source = 'POSTapi.numbuster.com/api/v6/notice/editaccess_token='+access_token+'&cnonce='+cnonce+'&phone='+phone+'&text='+text+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_numcy_subscription_comment_cancel(access_token:str,cnonce:str,comment_id:int,timestamp:str):
    source = 'POSTapi.numbuster.com/api/v6/numcy/subscription/comment/cancelaccess_token='+access_token+'&cnonce='+cnonce+'&comment_id='+str(comment_id)+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_numcy_subscription_comment_settings(access_token:str,cnonce:str,timestamp:str):
    source = 'GETapi.numbuster.com/api/v6/numcy/subscription/comment/settingsaccess_token='+access_token+'&cnonce='+cnonce+'&timestamp='+timestamp
    return crypt(source)

def signature_v6_auth_precheck(cnonce:str,code:str,phone:str,timestamp:str):
    source = 'POSTapi.numbuster.com/api/v6/auth/precheckcnonce='+cnonce+'&code='+code+'&phone='+phone+'&timestamp='+timestamp
    return crypt(source)


if __name__=='__main__':
    print(signature_v6_auth_precheck('7BRIqhAJIIwiRWoY2OBILW2s8HT8emI','Cztm-XkwS-tk7l','79313336429','1580923704'))

