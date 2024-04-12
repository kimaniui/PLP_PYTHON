#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/1 22:00

def create_file():
    try:
        with open('my_file.txt', 'w') as f:
            f.write('hello world')
            f.write('hsecond line')
            print("file successfully created")
    except Exception as e:
        print("An error ocurred", e)
    finally:
        print("Execution completed")

def read_file():
    try:
        with open('my_file.txt', 'r') as f:
            print(f.read())
    except Exception as e:
        print("An error ocurred", e)
    finally:
        print("Execution completed")

def append_file():
    try:
        with open('my_file.txt', 'a') as f:
            f.write('appended third line')
            f.write('appended fourth line')
            print("files successfully appended")
    except Exception as e:
        print("An error ocurred", e)
    finally:
        print("Execution completed")