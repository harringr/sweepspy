sweepspy
========

Python library for helping generate sweepstake assignments. (e.g. for World Cup).  Two lists are defined, one for teams, one for people.  The lists are shuffled and then teams are assigned to people at random, with more than one team being assigned to a person if necessary (i.e. if there are fewer people than teams).

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

Me: Ivory Coast, Costa Rica
You: Bra, Ger
Them: Fra, Arg

```

### Todo

1. Add tests
2. Check teams/people input and flag for errors
3. Option to set only one team per person
4. Allow multiple people to have the same team (e.g. if more people than teams)
5. ...