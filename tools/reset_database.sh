#!/bin/sh

echo "
---
Script per il reset del database e reimportazione di un file di dump SQL.
---
"


db_username=$1
db_password=$2
db_name=$3
db_filename=$4

if [ $# -lt 4 ]
then
    echo "Devi specificare i 3 parametri richiesti!
    
La sintassi corretta è:"
    echo $0" <db_username> <db_password> <db_name> <nome file dump.sql>
    "
else
    echo "Importazione di "$db_filename" in "$db_name"..."
    mysql -u $db_username --password=$db_password -e 'DROP DATABASE '$db_name'; CREATE DATABASE '$db_name'; USE '$db_name'; source '$db_filename';'
fi

