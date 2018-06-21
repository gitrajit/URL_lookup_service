## URL_lookup_service
### Created Date: 21/06/2018
### version: 1.0

## desc: Webservices for scaninig the URL for malware.

## Steps to run :
* Create a directory/folder(eg url_dic) and cd  to it
  ```
  mkdir url_dic
  cd url_dic
  ```
  
* Clone this git repo, Assuming that you have already installed git
  ```
  $ git clone https://github.com/gitrajit/URL_lookup_service.git
  ```
* install flask as below
  location for pip.exe <path to your Python27>\Scripts\pip.exe
  ```
  C:\Python27\Scripts>pip.exe install flask
  ```
* start the server by runing urlapi.py
```
D:\url_dic\URL_lookup_service>python urlapi.py
 * Restarting with stat
 * Debugger is active!
 * Debugger pin code: 101-270-382
 * Running on http://localhost:51/ (Press CTRL+C to quit)
 ```
 
 ## To view all the listed ip & port and strings from databases:
 http://localhost:51/urlinfo/1/
 
 ```
 vagrant@control:~$ curl http://localhost:51/urlinfo/1/
{
  "IP and port": [
    "1.1.1.0:80",
    "1.1.1.1:81",
    "test.domain:80"
  ],
  "String": [
    "xxx",
    "!&*",
    "abc"
  ]
}
```

## For testing 
http://localhost:51/urlinfo/1/1.1.1.1:80/xxx

```
vagrant@control:~$ curl http://localhost:51/urlinfo/1/1.1.1.1:80/xxx
{
  "IP and port Safety": "hostname and port are Safe ",
  "string safety": "Not Safe, string listed in the database.",
  "url": "http://1.1.1.1:80/xxx"
}
vagrant@control:~$
```





