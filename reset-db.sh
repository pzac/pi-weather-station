#!/usr/bin/sh

rm -f /home/pi/app/data.db
sqlite3 data.db < /home/pi/app/create-database.sql
