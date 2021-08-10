import psutil
import speedtest
from tabulate import tabulate
class Network_Details(object):
  def ___init__(self):
    self.scanner = psutil.net_if_addrs()
    self.speed = speedtest.Speedtest()
    self.interfaces = self.interfaces()[0]
  def interface(self):
    interface = []
    for interface_name, _ in self.scanner.items():
    interfaces.append(str(interface_name))
    return interfaces
  def test(self):
    down = str(f"{round(self.speed.download() / 1_000_000, 2} Mbps")
    up = str(f"{round(self.speed.upload() / 1_000_000, 2} Mbps")
    interface = self.interfaces
    data = {"Interface:" : [interface],
            "Download:" : [down], 
            "Upload:" : [up]}
    table = tabulate(data, header="keys", tablefmt="pretty")
    return table
  def  __str__(self):
    return str(self.test())
  if __name__ == "__main__":
    print(Network_Details())
   
