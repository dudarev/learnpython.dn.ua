#! /usr/bin/env python
"""
Generate random rank for every line in a file.
"""

from random import shuffle

emails = []
with open('emails.txt', 'r') as f:
    for line in f:
        email = line.strip()
        emails.append(email)

shuffle(emails)

for i in xrange(len(emails) - 1):
    print '{}. {} -- {}'.format(i + 1, emails[i], emails[i + 1])

print '{}. {} -- {}'.format(len(emails), emails[len(emails) - 1], emails[0])
