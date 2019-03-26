#coding:utf8


import requests
import sys
import json


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

    def apkUpload(self):
        certdata = self.getCert()
        
        try:
            print("upload apk .....")
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


if __name__ == '__main__':
    bundleid = sys.argv[1]
    apitoken = sys.argv[2]
    apkpath = sys.argv[3]
    appname = sys.argv[4]
    buildid = sys.argv[5]
    appversion = sys.argv[6]

    server = ApkManage()
    server.apkUpload()
