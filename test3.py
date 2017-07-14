import psutil
import os
p1=psutil.Process(os.getpid())

print(str(psutil.virtual_memory().percent) +'%')
print(str(psutil.cpu_percent(0))+'%')
# print("percent: %.2f%%" % (p1.memory_percent()))