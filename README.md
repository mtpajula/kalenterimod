# kalenterimod

kalenterimod is for mass deleting and inserting (from ics) google calendar events.

## Install first

    pip3 install --upgrade google-api-python-client

## Files used

You need client secret -json from google. filename must be:

    client_id.json

[More about client secret here](https://developers.google.com/api-client-library/python/guide/aaa_client_secrets)

files for processing are:

    timeedit.ics
    courses.txt

timeedit.ics can be any ics-file.

Software is designed based on from [timeedit](http://www.timeedit.com/) exported ics.

### courses.txt

Its tab separated table file containing 4 columns. First line is dismissed (titles).

When given to icsreader to fix event summaries, it will replace second column string with first column string.

Idea is to change course id to more human readable form.

example:

    Opintojakso			Tunnus		Toteutus	Laajuus
    ---------------------------------------------
    Tekniikan alan viestintä 	R504T15A1	17001		5,00
    Engineering English for IT 	R504T15C1	16001		5,00

## Using

Run:

    python3 kalenterimod.py

cli will then ask y/n before every task.
