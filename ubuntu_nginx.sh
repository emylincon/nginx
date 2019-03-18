clear
echo 'preparing host for nginx'
sleep 2
apt update && apt upgrade -y
apt install curl gnupg2 ca-certificates lsb-release -y
echo "deb http://nginx.org/packages/ubuntu `lsb_release -cs` nginx" \
    | tee /etc/apt/sources.list.d/nginx.list
curl -fsSL https://nginx.org/keys/nginx_signing.key | apt-key add -
clear
echo 'Your Nginx Key'
apt-key fingerprint ABF5BD827BD9BF62
sleep 2
echo 'updating repository'
sudo apt update -y
clear
echo 'update done'
echo 'installing NGINX'
apt install nginx -y

