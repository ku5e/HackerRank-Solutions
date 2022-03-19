#!/usr/bin/env python3
#Programmer: MMJR ku5e@ku5e.com
#date: XX/XX/XXXX
#Purpose: Find the Runner-Up Score

input()
print(sorted(set(list(map(int, input().split()))))[-2])