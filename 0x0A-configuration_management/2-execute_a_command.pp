# Using Puppet, create a manifest that kills a process named killmenow
exec { 'kill_menow':
  command => 'pkill -f killmenow',
  path    => ['/usr/bin', '/usr/sbin', '/bin'],
}
