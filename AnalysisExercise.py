import timeit
import random

# for i in range(1000,100000,1000):
# 	t = timeit.Timer('random.randrange(%d) in x' %i, 'from __main__ import random, x')
# 	x = list(range(i))
# 	lst_time = t.timeit(number=1000)

# 	x = {j:None for j in range(i)}
# 	d_time = t.timeit(number=1000)

# 	print ('%d, %10.3f, %10.2f' % (i, lst_time, d_time))



# Exercise 1: Devise an experiment to verify that the list index operator is O(1)
for i in range(1000, 100000, 1000):
	t = timeit.Timer('x[(%d-500)]' %i, 'from __main__ import random, x')
	x = list(range(i))
	time = t.timeit(number=1000)

	print ('%d, %10.7f' % (i, time))


# Exercise 2: 