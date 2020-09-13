#!/usr/bin/env python3
import wave
import os

from base64 import b64encode
from pathlib import Path
from random import SystemRandom
from tempfile import TemporaryFile
from textwrap import dedent

from secret import flag

random = SystemRandom()
choice = random.choice
randint = random.randint

SOUNDS = Path(os.path.join(
    os.path.dirname(os.path.realpath(__file__)), 'sounds'
))

def sound(name):
    return (SOUNDS / name).with_suffix('.wav')

def wave_concat(paths, f):
    with wave.open(f, 'wb') as o:
        for p in paths:
            with wave.open(str(p)) as w:
                if not o.getnframes():
                    o.setparams(w.getparams())
                n = w.getnframes()
                o.writeframes(w.readframes(n))

def head():
    return [choice(('announcement', 'hour1')), 'its']

def hour(h):
    return [f'{h}a']

def minute(m):
    if m == 0:
        return ['00']
    if m <= 9:
        return ['o', f'{m}']
    if m <= 12:
        return [f'{m}']
    if m <= 19:
        return [{
            13: 'thir',
            14: 'for',
            15: 'fif',
            16: 'six',
            17: 'seven',
            18: 'eight',
            19: 'nine',
        }[m], 'teen']
    if m <= 29:
        return ['twen', f'ty{m % 10}']
    if m <= 39:
        return ['thir', f'ty{m % 10}']
    if m <= 49:
        return ['for', f'ty{m % 10}']
    if m <= 59:
        return ['fif', f'ty{m % 10}']

    return [choice(['am', 'pm'])]

def time():
    h = randint(1, 12)
    m = randint(0, 59)
    ap = choice(['am', 'pm'])
    return h, m, ap

def main():
    n = 200

    print(dedent(f'''
        I'm too lazy to figure out what time is being yelled at me.
        Could you tell me in so that it looks like 01:01 am?
        I'll send you each time as a wav file base64 encoded.

        If you get {n} correct in a row, I'll give you something nice!
    '''))

    for i in range(1, n+1):
        h, m, ap = time()

        expected = f'{h:02d}:{m:02d} {ap}'

        words = head() + hour(h) + minute(m) + [ap]
        paths = map(sound, words)

        with TemporaryFile('w+b') as f:
            wave_concat(paths, f)
            f.seek(0)
            b64 = b64encode(f.read())

        print(f'--- Press enter for time {i}. ---')
        input()
        print(b64)
        print(f'--- What time is it? ---')

        guess = input().strip()
        if guess != expected:
            break
    else:
        print(f'Here is your treat! {flag}')

    print('Bye!')


if __name__ == '__main__':
    exit(main())
