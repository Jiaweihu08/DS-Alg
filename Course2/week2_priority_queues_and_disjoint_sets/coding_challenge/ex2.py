from random import randint
from collections import namedtuple

class Worker:
	def __init__(self, id, f_time):
		self.id = id
		self.f_time = f_time
	def show(self):
		print(self.id, self.f_time)

def sift_down(i, A):
	n = len(A)
	indice = i
	l = 2 * i + 1
	if l < n and A[l].f_time <= A[indice].f_time:
		if A[l].f_time == A[indice].f_time:
			if A[l].id < A[indice].id:
				indice = l
		else:
			indice = l
		
	r = 2 * i + 2
	if r < n and A[r].f_time <= A[indice].f_time:
		if A[r].f_time == A[indice].f_time:
			if A[r].id < A[indice].id:
				indice = r
		else:
			indice = r

	if indice != i:
		A[indice], A[i] = A[i], A[indice]
		sift_down(indice, A)

def job_queue(n_workers, jobs):
	worker_queue = [Worker(i, 0) for i in range(n_workers)]
	for job in jobs:
		worker_queue[0].show()
		worker_queue[0].f_time += job
		sift_down(0, worker_queue)


if __name__ == '__main__':
	n, m = list(map(int, input().split()))
	jobs = list(map(int, input().split()))
	
	# n = 10
	# jobs = [1,2,1,0]+[randint(0, 10) for _ in range(15)]
	# print(jobs)
	
	job_queue(n, jobs)



