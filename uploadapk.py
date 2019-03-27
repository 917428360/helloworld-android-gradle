#coding:utf8


import requests
import sys
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

class ApkManage(object):
    def __init__(self):
        self.url = "http://api.fir.im/apps"



    def getCert(self):
        dataargs = {'type' : 'android',
                    'bundle_id' : bundleid,
                    'api_token' : apitoken}

        response = requests.post(self.url,data=dataargs)
        #print(response.status_code,response.text)
        cert = json.loads(response.text)
        #print(cert)

        return cert['cert']['binary']

    def uploadFir(self):
        certdata = self.getCert()
        
        try:
            print("upload apk to fir......")
            apkfile = {'file' : open(apkpath,'rb')}
            params = {"key"   : certdata['key'],
                      "token" : certdata['token'],
                      "x:name": appname ,
                      "x:build" : buildid,
                      "x:version" : appversion}
            response = requests.post(certdata['upload_url'],files=apkfile,data=params,verify=False)
            print(response.text)
            if int(response.status_code) == 200 :
                print("upload success!  return -->" + str(response.status_code))
            else:
                print("upload error! return -->" + str(response.status_code))



        except Exception as e:
            print("error: " + str(e))


    def uploadPgyer(self):
        url = 'https://qiniu-storage.pgyer.com/apiv1/app/upload'
        try:
            #print("upload apk to pgyer ......")
            apkfile = {'file' : open(apkpath,'rb')}
            params = {"uKey" : 'cf9e323c7099a77c74e1a278bee63b09',
                      "api_key" : 'bfefa01dae76a4a9593751a6929033d7'}

            response = requests.post(url,files=apkfile,data=params,verify=False)
            #print(response.text)
            qrcodes = json.loads(response.text)['data']['appQRCodeURL']
            if int(response.status_code) == 200 :
                #print("upload success!  return -->" + str(response.status_code))
                print(qrcodes)
            else:
                print("upload error! return -->" + str(response.status_code))

        except Exception as e:
            raise
       



if __name__ == '__main__':
    bundleid = sys.argv[1]
    apitoken = sys.argv[2]
    apkpath = sys.argv[3]
    appname = sys.argv[4]
    buildid = sys.argv[5]
    appversion = sys.argv[6]
    platform= sys.argv[7]

    server = ApkManage()

    if platform == 'fir':
        server.uploadFir()
    elif platform == 'pgyer':
        server.uploadPgyer()
