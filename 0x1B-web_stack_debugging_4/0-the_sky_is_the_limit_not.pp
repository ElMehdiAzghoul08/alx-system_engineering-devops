#fix --Sky is the limit task
exec { 'valid-nginx-fix':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

#restart --Sky is the limit task
exec { 'valid-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
