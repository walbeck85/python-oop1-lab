#!/usr/bin/env python3

from lib.coffee import Coffee

import io
import sys

class TestShoe:
    '''Coffee in shoe.py'''

    def test_has_size_and_price(self):
        '''has the size and status passed to __init__, and values can be set to new instance.'''
        black = Coffee(size = "Large", price = 1.50)
        assert(black.size == "Large")
        assert(black.price == 1.50)

    def test_requires_specific_size(self):
        '''prints "size must be Small, Medium, or Large" if size is not an one of those options.'''
        latte = Coffee(size = "Large", price = 2.50)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        latte.size = "not an size"
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "size must be Small, Medium, or Large\n"

    def test_can_tip(self):
        '''says that the shoe has been repaired.'''
        americano = Coffee(size = "Large", price = 3.50)
        captured_out = io.StringIO()
        sys.stdout = captured_out
        americano.tip()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "This coffee is great, here’s a tip!\n")
    
    def test_tip_adds_to_price(self):
        '''creates an attribute on the instance called 'condition' and set equal to 'New' after repair.'''
        americano = Coffee(size = "Large", price = 3.50)
        americano.cobble()
        assert(americano.price == 4.50)
        
        
   
