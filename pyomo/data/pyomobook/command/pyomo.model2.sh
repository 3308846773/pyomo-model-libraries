#!/bin/sh

cd ../overview
# @cmd:
pyomo solve --instance-only --save-model=concrete1.lp concrete1.py
# @:cmd
diff concrete1.lp ../command/concrete1.lp
