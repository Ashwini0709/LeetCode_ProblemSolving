#!/usr/bin/env python


class Solution:
    def fib(self, n: int) -> int:
        first = 0
        second = 1
        if n==first or n==second:
            return n
        for i in range(1, n):
            third = first + second
            first = second
            second = third
        return third
