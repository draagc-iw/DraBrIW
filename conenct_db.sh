#!/bin/bash

DB_PASS=$(security find-generic-password -s academy_db_pass -w)
mysql -h database-academy-test.crtvvzmhs8i6.eu-west-2.rds.amazonaws.com -u dragos --password=$DB_PASS
