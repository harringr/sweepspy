sweepspy
========

Python library for helping generate sweepstake assignments 

### Usage

```
$ vi use_sweepspy.py

...

#!/usr/bin/env python

from sweepspy import Sweepstake

teams = ['arg', 'bra', 'ger', 'fra', 'ivory coast', 'costa rica']
people = ['me', 'you', 'them']

s = Sweepstake(teams, people)
s.assign()

...

$ ./use_sweepspy.py
You: Fra, Costa Rica
Me: Arg, Ivory Coast
Them: Bra, Ger


```
or

```
$ python

>>> from sweepspy import Sweepstake
>>> teams = ['arg', 'bra', 'ger', 'fra', 'ivory coast', 'costa rica']
>>> people = ['me', 'you', 'them']
>>> s = Sweepstake(teams, people)
>>> s.assign()

You: Fra, Costa Rica
Me: Arg, Ivory Coast
Them: Bra, Ger

```