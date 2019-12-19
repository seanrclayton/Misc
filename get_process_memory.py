import psutil
import humanfriendly
import time
count = 0
pid = SOMEINT
while count < 30:
	SLICE_IN_SECONDS = 1
	p = psutil.Process(pid)
	mem_status = "RSS {},  VMS: {}".format(humanfriendly.format_size(p.memory_info().rss),
                humanfriendly.format_size(p.memory_info().vms))
	time.sleep(SLICE_IN_SECONDS)
	print(mem_status)
	count = count + 1
