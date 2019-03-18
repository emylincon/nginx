#test page
import os


for i in range(1,21):
    os.system('echo "Hello world" > /usr/share/nginx/html/{}.html'.format(i))
    os.system('echo "This is web {}" >> /usr/share/nginx/html/{}.html'.format(i, i))
    os.system('echo "Test page {} for Caching setup" >> /usr/share/nginx/html/{}.html'.format(i, i))

#os.system('rm /etc/nginx/conf.d/default.conf')
#os.system('mv default.conf /etc/nginx/conf.d/')
