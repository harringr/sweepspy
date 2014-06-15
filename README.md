sweepspy
========

Python library for helping generate sweepstake assignments 

## Usage

```
#!/usr/bin/env python

from sweepspy import Sweepstake

teams = ['arg', 'bra', 'ger', 'fra', 'ivory coast', 'costa rica']
people = ['me', 'you', 'them']

s = Sweepstake(teams, people)
s.assign()
```