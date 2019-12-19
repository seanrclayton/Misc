import psutil
import humanfriendly
import time
import sys

pid = int(sys.argv[1])
count = 0
while count < 30:
	SLICE_IN_SECONDS = 1
	p = psutil.Process(pid)
	cpu_total = float((p.cpu_times().user + p.cpu_times().system) / 100)
	mem_status = "RSS {},  VMS: {} CPU: {}".format(humanfriendly.format_size(p.memory_info().rss),
                humanfriendly.format_size(p.memory_info().vms),cpu_total)
	time.sleep(SLICE_IN_SECONDS)
	print(mem_status)
	count = count + 1

