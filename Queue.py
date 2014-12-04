import random

class Queue:

	def __init__(self):
		self.items = []

	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()

	def size(self):
		return len(self.items)

	def isEmpty(self):
		return self.items == []


q = Queue()
q.enqueue(4)
q.enqueue('dog')
q.enqueue(True)
print q.size()
print q.dequeue()

#########################
## The hot potato game ##
#########################
def hotPotato(players, count):

	circle = Queue()
	for ele in players:
		circle.enqueue(ele)

	while circle.size() > 1:
		for i in range(0, count):
			circle.enqueue(circle.dequeue())
		circle.dequeue()

	return circle.dequeue()

print(hotPotato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7))

###########################################################################

## Simulating the printing tasks
# 1. Create a queue of print tasks. Each task will be given a timestamp upon its arrival. The queue is empty to start.
# 2. For each second (currentSecond):
# 	Does a new print task get created? If so, add it to the queue with the currentSecond as the timestamp.
# 	If the printer is not busy and if a task is waiting,
# 		Remove the next task from the print queue and assign it to the printer.
# 		Subtract the timestamp from the currentSecond to compute the waiting time for that task.
# 		Append the waiting time for that task to a list for later processing.
# 		Based on the number of pages in the print task, figure out how much time will be required.
# 	The printer now does one second of printing if necessary. It also subtracts one second from the time required for that task.
# 	If the task has been completed, in other words the time required has reached zero, the printer is no longer busy.
# 3. After the simulation is complete, compute the average waiting time from the list of waiting times generated.

class Printer:
	def __init__(self, speed):
		self.speed = speed
		self.currentTask = None
		self.timeRemaining = 0

	def tick(self):
		if self.currentTask != None:
			self.timeRemaining = self.timeRemaining -1
			if self.timeRemaining <= 0:
				self.currentTask = None

	def busy(self):
		if self.currentTask == None:
			return False
		else:
			return True

	def startNext(self, newtask):
		self.currentTask = newtask
		self.timeRemaining = newtask.getPages()*(60/self.speed)



class Task:
	def __init__(self, time):
		self.pages = random.randrange(1,21)
		self.stamp = time

	def getStamp(self):
		return self.stamp

	def getPages(self):
		return self.pages

	def waitTime(self, currentTime):
		return (currentTime - self.stamp)



def newTask(studentNum):

	if studentNum > 0:
		prob = int(3600/studentNum)
	else:
		prob = 3600  # should raise error
	a = random.randrange(1, prob)   # change prob to reflect larger number of students
	if a == (prob-1):   # change prob to reflect larger number of students
		return True
	else: 
		return False


def simulation(timePeriod, printingSpeed, studentNum):

	waitLine = Queue()
	printer = Printer(printingSpeed)
	waitTime = []

	for currentSecond in range(timePeriod):

		if newTask(studentNum):
			task = Task(currentSecond)
			waitLine.enqueue(task)

		if (not printer.busy()) and (not waitLine.isEmpty()):
			currentTask = waitLine.dequeue()
			printer.startNext(currentTask)
			taskWaitTime = currentTask.waitTime(currentSecond)
			waitTime.append(taskWaitTime)


		printer.tick()



	print ("Average waiting time: %5.2f and %d tasks awaiting" % (sum(waitTime)/len(waitTime), waitLine.size()))

for i in range(10):
	simulation(3600, 10, 60)


















