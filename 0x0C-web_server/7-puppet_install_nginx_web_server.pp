
# Nginx installing
package { 'nginx':
  ensure => installed,
}

# Nginx configuration
file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => "
server {
    listen 80;
    listen [::]:80;

    server_name _;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    location / {
        root /var/www/html;
        index index.html;
    }
}
",
}

# Nginx run
service { 'nginx':
  ensure => running,
  enable => true,
}

# Hello World
file { '/var/www/html/index.html':
  ensure  => present,
  content => "Hello World!\n",
}
