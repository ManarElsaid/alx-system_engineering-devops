# a manifest that create a file in /tmp
file { '/tmp/school':
  ensure => 'present',
  owner => 'www-data',
  group => 'www-data',
  mode => '0744',
  content => template("I love Puppet")
}
