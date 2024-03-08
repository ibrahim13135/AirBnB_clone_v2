# Ensure /data directory exists
file { '/data':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

# Ensure /data/web_static directory structure exists
file { '/data/web_static':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

file { '/data/web_static/releases':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

file { '/data/web_static/shared':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

file { '/data/web_static/releases/test':
  ensure => 'directory',
  owner  => 'root',
  group  => 'root',
}

# Create index.html file
file { '/data/web_static/releases/test/index.html':
  ensure  => 'file',
  content => '<html><head></head><body>Holberton School</body></html>',
  owner   => 'root',
  group   => 'root',
}

# Create symbolic link
file { '/data/web_static/current':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  owner   => 'root',
  group   => 'root',
}

# Restart Nginx service (assuming Nginx is managed by Puppet)
service { 'nginx':
  ensure => 'running',
  enable => true,
  require => File['/data/web_static/current'],
}
