import os
import random

class  SSH_Setup(object):
  def __init__(self):
    self.new_port = random.randrange(1024,  32767)
    self.config_file = "sshd_config"
    self.ssh_dir = "/etc/ssh"
  def ssh_installer(self):
    os.system("sudo apt install openssh-server")
    os.system("clear")
    print("SSH installed!")
  def key_manager(self):
    os.mkdir("/old_keys")
    os.system("mv ssh_h* old_keys")
    print("Old keys moved to new  folder..")
    os.system("dpkg-reconfigure openssh-server")
    os.system("clear")
    print("New SSH keys generated!")
