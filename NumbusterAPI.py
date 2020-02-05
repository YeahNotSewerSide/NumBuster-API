import requests
import signatures


class Numbuster:
    def __init__(self,access_token=None):
        self.access_token = access_token
        self.api_url = 'https://api.numbuster.com/api/'
        self.headers = {'Host': 'api.numbuster.com',
                    'User-Agent': 'okhttp/3.9.1',
                    'Accept-Encoding': 'gzip',
                    'Connection': 'keep-alive'}

    def v6_comment_list_my(self,offset:int,limit:int):
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_comment_list_my(self.access_token,cnonce,limit,offset,timestamp)
        url = self.api_url+f'v6/comment/list/my?offset={offset}&limit={limit}&timestamp={timestamp}&signature={signature}&cnonce={cnonce}&access_token={self.access_token}'
        data = requests.get(url,headers=self.headers)
        return data.json()

    def v6_comment_list(self,phone:str,offset:int,limit:int):
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_comment_list(self.access_token,cnonce,limit,offset,phone,timestamp)
        url = self.api_url+f'v6/comment/list?phone={phone}&offset={offset}&limit={limit}&timestamp={timestamp}&signature={signature}&cnonce={cnonce}&access_token={self.access_token}'
        data = requests.get(url,headers=self.headers)
        return data.json()

    def v6_comment_delete(self,phone:str):
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_comment_delete(self.access_token,cnonce,phone,timestamp)
        url = self.api_url+f'v6/comment/delete?phone={phone}&timestamp={timestamp}&signature={signature}&cnonce={cnonce}&access_token={self.access_token}'
        data = requests.get(url,headers=self.headers)
        return data.json()

    def v6_old_phone(self,phone,locale='RU'):
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_old_phone(phone,self.access_token,cnonce,timestamp,locale)
        url = self.api_url+f'v6/old/phone/{phone}?access_token={self.access_token}&locale={locale}&timestamp={timestamp}&signature={signature}&cnonce={cnonce}'
        data = requests.get(url,headers=self.headers)
        return data.json()

    def v6_notice_delete(self,phone):
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_notice_delete(self.access_token,cnonce,phone,timestamp)
        url = self.api_url+f'v6/notice/delete?phone={phone}&timestamp={timestamp}&signature={signature}&cnonce={cnonce}&access_token={self.access_token}'
        data = requests.post(url,headers=self.headers)
        return data.json()

    def v6_old_sms(self,phone,locale='RU'):
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_old_sms(phone,self.access_token,cnonce,timestamp,locale)
        url = self.api_url+f'v6/old/sms/{phone}?access_token={self.access_token}&locale={locale}&timestamp={timestamp}&signature={signature}&cnonce={cnonce}'
        data = requests.get(url,headers=self.headers)
        return data.json()

    def v6_report_comment(self,comment_id:int,report_text:str):
        url = self.api_url+f'v6/report/comment?comment_id={comment_id}&report_text={report_text}&access_token={self.access_token}'
        data = requests.post(url,headers=self.headers)
        return data.json()

    def v6_numcy_subscription_comment_renewal(self,comment_id:int):
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_numcy_subscription_comment_renewal(self.access_token,cnonce,comment_id,timestamp)
        url = self.api_url+f'v6/numcy/subscription/comment/renewal?comment_id={comment_id}&timestamp={timestamp}&signature={signature}&cnonce={cnonce}&access_token={self.access_token}'
        data = requests.post(url,headers=self.headers)
        return data.json()

    def v6_auth_get(self,platform='Android',lang='RU'):
        #Allows to get misterious code
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_auth_get(cnonce,timestamp,lang,platform)
        url = self.api_url+f'v6/auth/get?platform={platform}&lang={lang}&timestamp={timestamp}&signature={signature}&cnonce={cnonce}'
        data = requests.get(url,headers=self.headers)
        return data.json()

    def v6_old_search(self,phone:str,locale='RU'):
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_old_search(phone,self.access_token,cnonce,timestamp,locale)
        url = self.api_url+f'v6/old/search/{phone}?access_token={self.access_token}&locale={locale}&timestamp={timestamp}&signature={signature}&cnonce={cnonce}'
        data = requests.get(url,headers=self.headers)
        return data.json()

    def v6_numcy_subscription_coment_cancel(self,comment_id:int):
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_numcy_subscription_comment_cancel(self.access_token,cnonce,comment_id,timestamp)
        url = self.api_url+f'v6/numcy/subscription/comment/cancel?comment_id={comment_id}&timestamp={timestamp}&signature={signature}&cnonce={cnonce}&access_token={self.access_token}'
        data = requests.post(url,headers=self.headers)
        return data.json()

    def v6_dailyquest_get(self):
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_dailyquest_get(self.access_token,cnonce,timestamp)
        url = self.api_url+f'v6/dailyquest/get?timestamp={timestamp}&signature={signature}&cnonce={cnonce}&access_token={self.access_token}'
        data = requests.get(url,headers=self.headers)
        return data.json()

    def v6_auth_facebook(self,facebook_token,code):
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_auth_facebook(cnonce,code,facebook_token,timestamp)
        url = self.api_url+f'v6/auth/facebook?facebook_token={facebook_token}&code={code}&timestamp={timestamp}&signature={signature}&cnonce={cnonce}'
        data = requests.post(url,headers=self.headers)
        return data.json()

    def v6_old_profiles_by_phone(self,phone:str,locale='RU'):
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_old_profiles_by_phone(phone,self.access_token,cnonce,timestamp,locale)
        url = self.api_url+f'v6/old/profiles/by_phone/{phone}?access_token={self.access_token}&locale={locale}&timestamp={timestamp}&signature={signature}&cnonce={cnonce}'
        data = requests.get(url,headers=self.headers)
        return data.json()

    def v6_numcy_balance(self):
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_numcy_balance(self.access_token,cnonce,timestamp)
        url = self.api_url+f'v6/numcy/balance?timestamp={timestamp}&signature={signature}&cnonce={cnonce}&access_token={self.access_token}'
        data = requests.get(url,headers=self.headers)
        return data.json()

    def v6_numcy_subcription_comment_settings(self):
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_numcy_subscription_comment_settings(self.access_token,cnonce,timestamp)
        url = self.api_url+f'v6/numcy/subscription/comment/settings?timestamp={timestamp}&signature={signature}&cnonce={cnonce}&access_token={self.access_token}'
        data = requests.get(url,headers=self.headers)
        return data.json()

    def v6_comment_add(self,phone:str,text:str):
        text_u = signatures.to_url(text)
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_comment_add(self.access_token,cnonce,phone,text_u,timestimp)
        url = self.api_url+f'v6/comment/add?phone={phone}&text={text}&timestime={timestamp}&signature={signature}&cnonce={cnonce}&access_token={self.access_token}'
        data = requests.post(url,headers=self.headers)
        return data.json()

    def v6_auth_agreement(self,phone:str):
        headers = self.headers.copy()
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_auth_agreement(cnonce,phone,timestamp)
        url = self.api_url+f'v6/auth/agreement?timestamp={timestamp}&signature={signature}&cnonce={cnonce}'
        data = requests.post(url,headers=headers,data=bytes(f'phone={phone}','utf-8'))
        return data.json()

    def v6_comment_edit(self,phone:str,text:str):
        text_u = signatures.to_url(text)
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_comment_edit(self.access_token,cnonce,phone,text_u,timestamp)
        url = self.api_url+f'v6/comment/edit?phone={phone}&text={text}&timestamp={timestamp}&signature={signature}&cnonce={cnonce}&access_token={self.access_token}'
        data = requests.post(url,headers=self.headers)
        return data.json()

    def v6_dailyquest_calendar(self):
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_dailyquest_calendar(self.access_token,cnonce,timestamp)
        url = self.api_url+f'v6/dailyquest/calendar?timestamp={timestamp}&signature={signature}&cnonce={cnonce}&access_token={self.access_token}'
        data = requests.get(url,headers=self.headers)
        return data.json()

    def v6_notice_add(self,phone,text:str):
        text_u = signatures.to_url(text)
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_notice_add(self.access_token,cnonce,phone,text_u,timestamp)
        url = self.api_url+f'v6/notice/add?phone={phone}&text={text}&timestime={timestamp}&signature={signature}&cnonce={cnonce}&access_token={self.access_token}'
        data = requests.post(url,headers=self.headers)
        return data.json()

    def v6_auth_agreement_code(self,code:str):
        #code from v6/auth/get
        headers = self.headers.copy()
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_auth_agreement_code(cnonce,code,timestamp)
        url = self.api_url+f'v6/auth/agreement_code?&timestamp={timestamp}&signature={signature}&cnonce={cnonce}'
        data = requests.post(url,headers=headers,data=bytes(f'code={code}','utf-8'))
        return data.json()

    def v6_notice_edit(self,phone:str,text:str):
        text_u = signatures.to_url(text)
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_notice_edit(self.access_token,cnonce,phone,text_u,timestamp)
        url = self.api_url+f'v6/notice/edit?phone={phone}&text={text}&timestamp={timestamp}&signature={signature}&cnonce={cnonce}&access_token={self.access_token}'
        data = requests.post(url,headers=self.headers)
        return data.json()

    def v6_auth_check(self,code:str):
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_auth_check(cnonce,code,timestamp)
        url = self.api_url+f'v6/auth/check?code={code}&timestamp={timestamp}&signature={signature}&cnonce={cnonce}'
        data = requests.get(url,headers=self.headers)
        return data.json()

    def another_bans(self,profileId:int):
        #old4a27f7a4025447ee5560a49bc5bcde34/bans
        url = self.api_url+f'old4a27f7a4025447ee5560a49bc5bcde34/bans?profileId={profileId}&access_token={self.access_token}'
        data = requests.post(url,headers=self.headers)
        return data.json()

    def another_profiles_id_phones(self,id:int,phone=str):
        url = self.api_url+f'old4a27f7a4025447ee5560a49bc5bcde34/profiles/{id}/phones?phone={phone}&access_token={self.access_token}'
        data = requests.post(url,headers=self.headers)
        return data.json()

    def another_profiles_id_phones_confirm(self,id:int,phone:str,code:str):
        url = self.api_url+f'old4a27f7a4025447ee5560a49bc5bcde34/profiles/{id}/phones/confirm?phone={phone}&code={code}&access_token={self.access_token}'
        data = requests.post(url,headers=self.headers)
        return data.json()

    def another_profiles(self,phone:str):
        #can be used without access_token
        headers = self.headers.copy()
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        url = self.api_url+f'old4a27f7a4025447ee5560a49bc5bcde34/profiles'
        data = requests.post(url,headers=headers,data=bytes(f'phone={phone}','utf-8'))
        return data.json()

    def another_profiles_confirm(self,phone:str,code:str):
        #access_token in response
        #code from phone
        #can be used without access_token
        headers = self.headers.copy()
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        url = self.api_url+f'old4a27f7a4025447ee5560a49bc5bcde34/profiles/confirm'
        data = requests.post(url,headers=headers,data=bytes(f'phone={phone}&code={code}','utf-8'))
        return data.json()

    def another_profiles_without_code(self,phone:str):
        #can be used without access_token
        headers = self.headers.copy()
        headers['Content-Type'] = 'application/x-www-form-urlencoded'
        url = self.api_url+f'old4a27f7a4025447ee5560a49bc5bcde34/profiles/without-code'
        data = requests.post(url,headers=headers,data=bytes(f'phone={phone}','utf-8'))
        return data.json()
    
    def another_ping(self,device_build='9b1ef3ef32be6596',device_imei='000000000000000',device_os='Android',deviceToken='0',device_locale='en_US',device_version='60600'):
       dt = f'device%5Buid%5D={device_build}&device%5Bimei%5D={device_build}&device%5Bos%5D={device_os}&device%5BdeviceToken%5D={deviceToken}&device%5Blocale%5D={device_locale}&device%5Bversion%5D={device_version}'
       headers = self.headers.copy()
       headers['Content-Type'] = 'application/x-www-form-urlencoded'
       url = self.api_url+f'old4a27f7a4025447ee5560a49bc5bcde34/ping?access_token={self.access_token}'
       data = requests.post(url,headers=headers,data=bytes(dt,'utf-8'))
       return data.json()

    def v2_ping(self,version = '60600'):
       headers = self.headers.copy()
       headers['Content-Type'] = 'application/x-www-form-urlencoded'
       url = self.api_url+f'v2/ping?access_token={self.access_token}'
       data = requests.post(url,headers=headers,data=bytes(f'package_name=com.numbuster.android&version={version}&check=false','utf-8'))
       return data.json()
    
    def v2_contacts_sync(self):
       headers = self.headers.copy()
       headers['Content-Type'] = 'application/json; charset=UTF-8'
       url = self.api_url+f'v2/contacts/sync?access_token={self.access_token}'
       data = requests.post(url,headers=headers,data='[]')
       return data.json()

    def request_sms_code(self,phonenumber:str):
        code = self.v6_auth_get()['data']['code']
        self.v6_auth_agreement_code(code)
        self.another_profiles_without_code(phonenumber)
        self.another_profiles(phonenumber) #Can be deleted, but meh...

    def send_sms_code(self,phonenumber:str,code:str):
        self.access_token = api.another_profiles_confirm(phonenumber,code)['access_token']
        self.v2_ping()
        self.v6_auth_agreement(phonenumber)
        self.v2_contacts_sync()




if __name__ == '__main__':
    
    api = Numbuster()
    print(api.v6_old_phone('79202600211'))
    

