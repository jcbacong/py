import threading
import numpy as np
import time



def createThread(xthreads):
	



def main():
	## Initialize variables
	## Size of array
	SIZE = 10**6
	## Number of threads
	THREADS = 10

	## Create an array of random variables
	ARRAY = np.random.rand(SIZE)


	print(ARRAY)



if __name__ == "__main__":
	start = time.time()
	main()
	print("Execution time: %.3f seconds" %(time.time()-start))