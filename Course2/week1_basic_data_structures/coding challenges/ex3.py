# import os
# import random
# import time
from collections import namedtuple

Request = namedtuple('Request', ['arrived_at', 'time_to_process'])
Response = namedtuple('Response', ['was_dropped', 'started_at'])

class Buffer:
	def __init__(self, size):
		self.size = size
		self.finish_time = []

	def process(self, request):
		while self.finish_time and self.finish_time[0] <= request.arrived_at:
			self.finish_time.pop(0)
		
		if len(self.finish_time) < self.size:
			start_time = max(self.finish_time[-1], request.arrived_at) \
							if self.finish_time else request.arrived_at
			f_time = start_time + request.time_to_process
			self.finish_time.append(f_time)
			return Response(False, start_time)
		else:
			return Response(True, -1)

def process_requests(requests, buffer):
	responses = []
	for request in requests:
		response = buffer.process(request)
		print(response.started_at if not response.was_dropped else -1)

def main():
	buffer_size, n_requests = map(int, input().split())
	requests = []
	for _ in range(n_requests):
		arrived_at, time_to_process = map(int, input().split())
		requests.append(Request(arrived_at, time_to_process))


	# buffer_size = 2
	# n_requests = 6
	# requests_1 = [(0,1),(0,2),(1,2),(2,1),(2,2),(10,2)]
	

	
	# buffer_size = 100000
	# n_requests = 100000
	# n = n_requests // 10
	# requests = []
	# for i in range(10):
	# 	requests.extend([Request(i, random.randint(1, 999)) for _ in range(n)])
	
	# start = time.process_time()
	buffer = Buffer(buffer_size)
	process_requests(requests, buffer)
	# end = time.process_time()
	# print(end - start)

if __name__ == '__main__':
	main()
	# start = time.process_time()
	# os.chdir('../3_network_simulation/tests/')

	# with open('22') as file:
	# 	buffer_size, n_requests = map(int, file.readline().split())
	# 	buffer = Buffer(buffer_size)
	# 	for _ in range(n_requests):
	# 		a, p = map(int, file.readline().split())
	# 		response = buffer.process(Request(a, p))
	# 		print(response.started_at if not response.was_dropped else -1)
	# print()
	# print(time.process_time() - start)



