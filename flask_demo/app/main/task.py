from app import celery
import os
import sys
import time


@celery.task(blind=True)
def long():
    print('I am long ')
    time.sleep(10)
    print("i wake up")

