#!/opt/anaconda3/envs/myenv/bin/python3
import os
FAV_ANIMAL = input('What is your favorite animal? ')
AGE = input('What is your age? ')
NAME = input('What is your name? ')

os.environ["FAV_ANIMAL"] = FAV_ANIMAL
os.environ["AGE"] = AGE
os.environ["NAME"] = NAME


print(os.getenv("FAV_ANIMAL"))
print(os.getenv("AGE"))
print(os.getenv("NAME"))