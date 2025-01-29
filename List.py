# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 09:10:03 2025

@author: admit
"""

print("Hello Umair!");

list1 = [1,2,3,4];

print(type(list1));

print(list1[-1]);

#Basic method used in list and operations;

fruits = ['Mango','Apple','Chiku', 'Guava', 'Orange', 'Pineapple', 'Watermelone']
fruits.append('Kiwi');
fruits.insert(1, 'Strawberry');
fruits.remove('Chiku');
print(fruits);
print(fruits.count('Apple'));
fruits.pop(6);
print(fruits);
fruits.reverse();
print(fruits);
fruits.clear();
print(fruits);


