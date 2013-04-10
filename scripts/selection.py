#! /usr/bin/env python
"""
Generate random rank for every line in a file.
"""

from random import shuffle

MAX_RANK = 11

emails = set()
with open('emails.txt', 'r') as f:
    for line in f:
        email = line.strip()
        if email in emails:
            print email
        emails.add(email)

rank_list = list(range(1, len(emails) + 1))
shuffle(rank_list)

for r in rank_list:
    if r <= MAX_RANK:
        print r
    else:
        print MAX_RANK
