import os


for i in range(1,21):
    os.system('echo "Hello world" > /usr/share/nginx/html/{}.txt'.format(i))
    os.system('echo "This is web {}" >> /usr/share/nginx/html/{}.txt'.format(i, i))
    os.system('echo "Test page {} for Caching setup" >> /usr/share/nginx/html/{}.txt'.format(i, i))
