# -*- coding: utf-8 -*-
import datetime
import sys

from tyme_tools.tools import tyme


def print_help(file=None):
	print("\ttyme", file=file)
	print(file=file)
	print("usage:", file=file)
	print(f"\t{sys.argv[0]} EXPR", file=file)
	print(file=file)
	print("EXPR is a 'time expression', a mathematical expression that can accept time", file=file)
	print("format such as '7h', '10:12' etc... All time format must be in 24h-clock format.", file=file)


if len(sys.argv) < 2:
	print_help(file=sys.stderr)
	exit(1)

if sys.argv[1] in ["-h", "--help"]:
	print_help()
	exit(0)

if sys.argv[1] in ["-v", "--version"]:
	print("Tyme version 1.0.0")
	exit(0)

result: datetime.time = tyme(' '.join(sys.argv[1:]))
if result.hour != 0:
	print(f"{result.hour}h", end='' if result.minute != 0 else '\n')
if result.minute != 0:
	if result.hour != 0:
		print(f"{result.minute}")
	else:
		print(f"{result.minute}min")
elif result.hour == 0 and result.minute == 0:
	print('0')
