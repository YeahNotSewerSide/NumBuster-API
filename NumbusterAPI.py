import requests
import signatures

#all numbers must be like: 79xxxxxxxxx,
#number must starts with the code of the country

class Numbuster:
    def __init__(self,access_token):
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
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_auth_agreement(cnonce,phone,timestamp)
        url = self.api_url+f'v6/auth/agreement?phone={phone}&timestamp={timestamp}&signature={signature}&cnonce={cnonce}'
        data = requests.post(url,headers=self.headers)
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
        timestamp = signatures.get_timestamp()
        cnonce = signatures.get_cnonce()
        signature = signatures.signature_v6_auth_agreement_code(cnonce,code,timestamp)
        url = self.api_url+f'v6/auth/agreement_code?code={code}&timestamp={timestamp}&signature={signature}&cnonce={cnonce}'
        data = requests.post(url,headers=self.headers)
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

    def another_bans(profileId:int):
        #old4a27f7a4025447ee5560a49bc5bcde34/bans
        url = self.api_url+f'old4a27f7a4025447ee5560a49bc5bcde34/bans?profileId={profileId}&access_token={self.access_token}'
        data = requests.post(url,headers=self.headers)
        return data.json()

    def another_profiles_id_phones(id:int,phone=str):
        url = self.api_url+f'old4a27f7a4025447ee5560a49bc5bcde34/profiles/{id}/phones?phone={phone}&access_token={self.access_token}'
        data = requests.post(url,headers=self.headers)
        return data.json()

    def another_profiles_id_phones_confirm(id:int,phone:str,code:str):
        url = self.api_url+f'old4a27f7a4025447ee5560a49bc5bcde34/profiles/{id}/phones/confirm?phone={phone}&code={code}&access_token={self.access_token}'
        data = requests.post(url,headers=self.headers)
        return data.json()

    def another_profiles(phone:str):
        #can be used without access_token
        url = self.api_url+f'old4a27f7a4025447ee5560a49bc5bcde34/profiles?phone={phone}'
        data = requests.post(url,headers=self.headers)
        return data.json()

    def another_profiles_confirm(phone:str,code:str):
        #can be used without access_token
        url = self.api_url+f'old4a27f7a4025447ee5560a49bc5bcde34/profiles/confirm?phone={phone}&code={code}'
        data = requests.post(url,headers=self.headers)
        return data.json()

    def another_profiles_without_code(phone:str):
        #can be used without access_token
        url = self.api_url+f'old4a27f7a4025447ee5560a49bc5bcde34/profiles/without-code?phone={phone}'
        data = requests.post(url,headers=self.headers)
        return data.json()



if __name__ == '__main__':
    api = Numbuster('')
    print(api.v6_old_phone(''))
    
