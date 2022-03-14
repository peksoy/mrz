#!/usr/bin/python3
# -*- coding: UTF-8 -*-

# Adding mrz to PYTHONPATH to execute this example as script
from os.path import dirname, join, pardir, realpath
import sys
sys.path.append(realpath(join(dirname(__file__), pardir, pardir)))
#############################################################

from mrz.generator.td1 import TD1CodeGenerator
from examples.functions.functions import open_image

print(TD1CodeGenerator("I",               # Document type   ID
                       "PER",             # Country         FRA
                       "70275722",        # Document number as658975
                       "890612",          # Birth date      07031992
                       "M",               # Genre           Male: M
                       "210716",          # Expiry date     07031892
                       "PER",             # Nationality     
                       "Cárdenas",        # Surname         SURAF
                       "Jorge Anthony"))  # Given name(s)   VELİ

open_image("id_cards", "Peru.png")
