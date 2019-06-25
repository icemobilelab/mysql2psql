## Forked for migrating BLP Core with all our rules and fixes

# Migrate Mysql db to Postgresql (by rules) 

Migrate your current MySQL databases into Postgres in a single command.

The original project was using a direct connection to MySQL which caused a limitation for the amount of data to be processed to be able to fit in memory. I was able to rewrite the code partially with help of https://www.manejandodatos.es/2015/04/3597/ this blog. By making use of a streaming result set I was able to make an export that can be further processed for the MySQL & PostgreSQL differences.

This tool provides you the chance of migrate your local MySQL databases to Postgres and even modify your current database structure, names and achieve a better consistence defining new foreign keys and cleaning up the data using `_PRE_SQL` queries.

# How to use it
 
### Mode1: Migrate a single database
    $ python main.py {db_name}
    
### Toggle actions to be executed on new database in bin/migrate.sh
   SKIP_DB=true                     skip database removal and creation on target
   SKIP_SCHEMA=true                 skip schema creation on target
   SKIP_DATA=true                   skip data import on target
   SKIP_VIEWS=true                  skip view creation on target
   SKIP_CONSTRAINTS=true            skip index and constraints creation on target

# Documentation
## OS Dependences
### Install pip
    sudo apt-get install python-pip python-dev build-essential python-psycopg2 python-mysqldb libpq-dev libmysqlclient-dev
    
## Environment dependences
### Install python libraries and vendors
    sudo bash ./bin/install_requirements.sh
    
## Set it up for yourself 
#### Step1: Set up db config
Set up your database configuration on `./config/parameters.json`
* `mysql`: Mysql connection values
* `psql`: Postgres connection values
* `threads`: In case of 'all-databases', you can define the number of threads to run in parallel (Max. number of CPUs). Non parallel 0
* `prefix`: In case of 'all-databases', it filters every database which prefix is the defined here. Otherwise use false
* `v1_schema_name`: If you want to migrate old schema onto a separated postgres schema, its name is defined here. Otherwise use false

#### Step2: Version schema names
Set up your schema names for version1 and version2 on "./config/parameters.json"

#### Step3: Define model rules you want to modified
* Open `./rules/schema_changes.json`
* Define your own schema rules on it. These rules are going to be used to redefine the new db structure, in case of not including any rules to a table or column, they will be migrated as it is in Mysql 

#### Step4: Define Postgresql conversion rules from Mysql ones
* Open `./rules/mysql_to_psql.json`
* Define MySQL keys to Postgres, most of rules were already defined by default, but there might be some more missing

#### Step5: Define data convertion 
* Open `./rules/mysql_raw_dump.json`
* Define data conversion according to its type, YOU might prefer to define different data conversion depending of your own model. Functions for conversion are defined in `dumperAuxFuncs.py`, feel free to add your own customized ones.

========================

## Outputs
These are the files generated during the migration process:

* `mysql_schema.json`: Original Mysql schema exported in Json format
* `mysql_schema_v2.json`: Mysql schema after model rules where applied
* `mysql_data.sql`: INSERT INTO statement in mysql

* `psql_schema.json`: Postgres schema 
* `psql_tables.sql`: CREATE TABLE statements, generated from psql_schema. 
* `psql_data.sql`: INSERT INTO statements, generated from psql_schema. Raw data will be allocated under ./table folder

## Manual migration

### Mode1: Manually

#### Create tables
    psql -h server -d database_name -U username < ./output/{databaase}/psql_tables.sql
#### Insert data
    psql -h server -d database_name -U username < ./output/{databaase}/psql_data.sql
#### Insert indexes and fks
    psql -h server -d database_name -U username < ./output/{databaase}/psql_index_fk.sql
#### Create views ( Just in case you want to keep views with previous squema)
    psql -h server -d database_name -U username < ./output/{databaase}/psql_views.sql

### Mode2: Single command
    $ bash ./bin/migrate.sh [-p {port}] -U {username} -d {database} -Wf {password}
