# -*- coding: utf-8 -*-
import datetime
import sys

from tyme_tools.tools import tyme

result: datetime.time = tyme(' '.join(sys.argv[1:]))
print(f"{result.hour}h{result.minute}")
