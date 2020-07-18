#!/bin/python

import re

filter_name = "wloot"

filehandle_in = open(filter_name + ".filter", "r")
filehandle_out_strict = open(filter_name + "_strict.filter", "w")
filehandle_out_verystrict = open(filter_name + "_verystrict.filter", "w")

wloot_filter = filehandle_in.read()

hide_pattern_strict = re.compile("# Strict\nShow")
hide_pattern_verystrict = re.compile("# VeryStrict\nShow")

wloot_filter_strict = re.sub(hide_pattern_strict, "Hide", wloot_filter)
wloot_filter_verystrict = re.sub(hide_pattern_strict, "Hide", wloot_filter)
wloot_filter_verystrict = re.sub(hide_pattern_verystrict, "Hide", wloot_filter_verystrict)

filehandle_out_strict.write(wloot_filter_strict)
filehandle_out_verystrict.write(wloot_filter_verystrict)