# Overlord
Wrap Paramiko's ssh functions
* monitor.py - monitors files modifications

* Example usage for ssh.py:
`from Overlord.ssh import Host`

`connection = Host(str(hostname), str(username), str(password))`
`connection.sudo_execute("cat ~/file.txt")`