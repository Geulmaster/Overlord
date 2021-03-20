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

    def execute(self, command, PRINT = False):
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
        if PRINT:
            print(output.decode("utf-8"))
        return output.decode("utf-8")

    def sudo_execute(self, command, PRINT = False):
        if not self.CONNECTED:
            self.connect()
        session = self.client.get_transport().open_session()
        session.transport.open_session()
        session.set_combine_stderr(True)
        session.get_pty()
        session.exec_command(f"sudo {command}")
        stdin = session.makefile('wb', -1)
        stdout = session.makefile('rb', -1)
        stdin.write(f"{self.password}"+"\n")
        stdin.flush()
        attempt = 0
        outstr = stdout.read()
        while attempt < 5 and len(outstr) < 1:
            sleep(3)
            attempt += 1
        self.client.close()
        self.CONNECTED = False
        if PRINT:
            print(outstr.decode("utf-8"))
        return outstr.decode("utf-8")
