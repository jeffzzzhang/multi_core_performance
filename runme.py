# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 20:15:49 2018
usage: multiprocessing
@author: talen
"""
from multiprocessing import Pool
import multiprocessing as mp
import time
def monte_carlo_pi(n):
    import random,time
    cntr = 0
    k = random.random()
    random.seed(time.time()+k)
    start_time = time.time()
    for _ in range(n):
        x,y = random.random(),random.random()
        if x**2 + y**2 < 1:
            cntr += 1
    return 4*cntr/n,time.time()-start_time
if __name__ == '__main__':
    iter_time = 1e8
    cpu_num = mp.cpu_count()  # mp.cpu_count() returns thread number, not necessary core number
    core_num = 2 # core number
    stime_single_core = time.time()
    b = monte_carlo_pi(cpu_num*int(iter_time))
    print('single core processing time:',time.time()-stime_single_core,' sec')
    stime_multi_core = time.time()
    with Pool(core_num) as p:
        a = p.map(monte_carlo_pi,cpu_num*[int(iter_time)]) #
        print('Multi core processing time:',time.time()-stime_multi_core,' sec')
    c = [term[0] for term in a]
    print('Pi calculated by multi-cores is %f, by a single core is %f'%(sum(c)/c.__len__(),b[0]))
