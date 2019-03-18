# nginx
To install nginx webserver on ubuntu or debian
* Run scripts as root user
* then run the create_websites.py to generate random websites
* then do the following

open `nano /etc/nginx/conf.d/default.conf`  
change from
```
server {  
    listen       80;  
    server_name  localhost;  

    #charset koi8-r;  
    #access_log  /var/log/nginx/host.access.log  main;  

    location / {  
        root   /usr/share/nginx/html;  
        index  index.html index.htm;  
    }  
```

To
```
server {
    listen       80;
    server_name  localhost;

    #charset koi8-r;
    #access_log  /var/log/nginx/host.access.log  main;

    location / {
        root   /usr/share/nginx/html;
        index  index.html index.htm;
        webs  1.html 2.html 3.html 4.html 5.html 6.html 7.html 8.html 9.html 10.html 11.html 12.html 13.hmtl 14.hmtl 15.html 16.html 17.hmtl 18.html 19.html 20.html    
    }

```
