import threading
import numpy as np
import time



class Threads():
	def __init__(self, xthreads,array):
		self._return = [None]*xthreads
		job_array = []
		k = int(len(array)/xthreads)

		def _powersum(array,results,index):
			count = 0
			for i in array:
				count+= i**2
			results[index]=count
			print("Thread ",index," reports ",count)

		for i in range(xthreads):
			if i!=(xthreads-1):
				_array = array[i*k: (i+1)*(k)]
			else:
				_array = array[i*k: len(array)]

			job_array.append(threading.Thread(target=_powersum, args=(_array,self._return,i)))
		self.job_array = job_array

		for job in self.job_array:
			job.start()

	
		for job in self.job_array:
			job.join()

	def results(self):
		print("The final power sum is ", round(np.sum(self._return),4))




def powersum(array):
	count=0
	for i in array:
		count+= i**2
	print("The final power sum is ", round(count,4))

def main():
	## Initialize variables
	## Size of array
	SIZE = 10**5
	## Number of threads
	THREADS = 10

	## Create an array of random variables
	ARRAY = np.random.rand(SIZE)
	
	start = time.time()
	powersum(ARRAY)
	print("(Sequential) Execution time: %.3f seconds\n" %(time.time()-start))

	start = time.time()
	thread = Threads(THREADS,ARRAY)
	thread.results()
	print("(Multithreaded) Execution time: %.3f seconds" %(time.time()-start))

	

if __name__ == "__main__":
	main()
	