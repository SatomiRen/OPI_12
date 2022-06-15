#!/usr/bin/env python3
# -*- coding: utf-8 -*-


from threading import Thread, Lock
from math import cos
from queue import Queue


eps = .0000001
q = Queue()
lock = Lock()


def inf_sum(x):
    lock.acquire()
    a = 1
    summa = 1
    i = 1
    prev = 0
    while abs(summa - prev) > eps:
        a = a * x ** 2 / ((2 * i) * (2 * i - 1))
        prev = summa
        if i % 2 == 0:
            summa += a
        else:
            summa += -1 * a
        i += 1
    q.put(summa)
    lock.release()


def check_ans(inf_res, d_res):
    print(f"The sum of an infinite series is: {inf_res}")
    print(f"The calculated answer is: {d_res}")


if __name__ == '__main__':
    num = int(input("Enter the number to calculate: "))
    check = cos(num)
    thread1 = Thread(target=inf_sum, args=(num,)).start()
    thread2 = Thread(target=check_ans, args=(q.get(), check)).start()
