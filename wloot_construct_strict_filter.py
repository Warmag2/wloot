#!/bin/python

import re

filter_name = "wloot"

filehandle_in = open(filter_name + ".filter", "r")
filehandle_out = open(filter_name + "_strict.filter", "w")
wloot_filter = filehandle_in.read()
hide_pattern = re.compile("# Strict\nShow")
wloot_filter = re.sub(hide_pattern, "Hide", wloot_filter)

filehandle_out.write(wloot_filter)
