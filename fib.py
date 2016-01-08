#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def fib(max):
	n, a, b = 0, 0, 1
	while n < max:
		yield b
		a, b = b, a + b
		n = n + 1

def main():
	for i in fib(30):
		print(i)

if __name__ == "__main__":
	main()