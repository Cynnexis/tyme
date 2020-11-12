# -*- coding: utf-8 -*-
import datetime
import re
import sys
from typing import Optional, List

from typeguard import typechecked

time_pattern = re.compile(r"^(\d{1,2})[\t ]*[:h][\t ]*(\d{1,2})?$")


def tyme(expression: str) -> datetime.time:
	split_expression = re.split(r"([+\-*/%()\s])", expression)
	
	# Remove empty strings and whitespaces
	split_expression = [e for e in split_expression if len(e) > 0 and e != ' ']
	
	# Convert all strings containing a time to a datetime.time
	i: int
	for (i, expr) in enumerate(split_expression):
		t: Optional[datetime.time] = str2time(expr)
		# If `expr` is a valid time, convert it and put it back in the list (as an integer representing the seconds)
		if t is not None:
			split_expression[i] = str(time2seconds(t))
	
	result = eval(''.join(split_expression))
	if not isinstance(result, str) and not isinstance(result, int):
		print(f"Couldn't interpret {expression}\nThe evaluation returned a {type(result)}", file=sys.stderr)
		exit(1)
	
	resultInt = 0
	try:
		resultInt = int(result)
	except ValueError:
		print(f"The expression '{expression}'\ngave an invalid value:\n{result}", file=sys.stderr)
		exit(1)
	
	t: datetime.timedelta = datetime.timedelta(seconds=resultInt)
	return (datetime.datetime.min + t).time()


@typechecked
def time2seconds(t: datetime.time) -> int:
	return (t.hour * 60 + t.minute) * 60 + t.second


@typechecked
def str2time(content: str) -> Optional[datetime.time]:
	"""
	Convert the given time in `content` to a `datetime.time`.
	:param content: The string to convert to a time.
	:return: Return the time if the parsing was successful, or `None` otherwise.
	"""
	matches = re.findall(time_pattern, content)
	if len(matches) == 0:
		return None
	
	match = matches[0]
	
	if len(match) == 0:
		return None
	
	try:
		hour = int(match[0])
		
		if len(match) >= 2 and len(match[1]) > 0:
			minute = int(match[1])
		else:
			minute = 0
		
		return datetime.time(hour=hour, minute=minute)
	except ValueError:
		return None
