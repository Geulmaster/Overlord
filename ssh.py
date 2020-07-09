import paramiko
from time import sleep

class Host():

    def __init__(self, hostname, username, password):
        self.hostname = hostname
        self.username = username
        self.password = password
        self.CONNECTED = False

    def connect(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        try:
            self.client.connect(self.hostname, username=self.username, password=self.password)
            self.CONNECTED = True
            return self.client
        except Exception as error:
            self.CONNECTED = False
            print(f'Could not connect to {self.hostname}.')
            raise error

    def execute(self, command):
        if not self.CONNECTED:
            self.connect()
        stdin, stdout, stderr = self.client.exec_command(command)
        attempts = 0
        output = stdout.read() + stderr.read()
        while attempts < 3 and len(output) < 1:
            sleep(2)
            attempts += 1
        self.client.close()
        self.CONNECTED = False
        return output