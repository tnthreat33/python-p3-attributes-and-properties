#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def set_name(self, name):
        if(type(name) in (str) and (1<= name <= 25)):
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")
