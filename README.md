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
    
$ python3
Python 3.6.8 (default, Jan 14 2019, 11:02:34) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> quit()
$ pip install -r requirements.txt --upgrade
Collecting BeautifulSoup==3.2.1 (from -r requirements.txt (line 1))
  Using cached https://files.pythonhosted.org/packages/1e/ee/295988deca1a5a7accd783d0dfe14524867e31abb05b6c0eeceee49c759d/BeautifulSoup-3.2.1.tar.gz
Collecting PyMySQL==0.9.3 (from -r requirements.txt (line 2))
  Downloading https://files.pythonhosted.org/packages/ed/39/15045ae46f2a123019aa968dfcba0396c161c20f855f11dea6796bcaae95/PyMySQL-0.9.3-py2.py3-none-any.whl (47kB)
    100% |████████████████████████████████| 51kB 147kB/s 
Collecting httplib2==0.9.2 (from -r requirements.txt (line 3))
  Downloading https://files.pythonhosted.org/packages/ff/a9/5751cdf17a70ea89f6dde23ceb1705bfb638fd8cee00f845308bf8d26397/httplib2-0.9.2.tar.gz (205kB)
    100% |████████████████████████████████| 215kB 535kB/s 
Collecting netifaces==0.10.4 (from -r requirements.txt (line 4))
  Downloading https://files.pythonhosted.org/packages/18/fa/dd13d4910aea339c0bb87d2b3838d8fd923c11869b1f6e741dbd0ff3bc00/netifaces-0.10.4.tar.gz
Collecting psycopg2cffi (from -r requirements.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/95/50/5b94b81a57948ce0350559aad8c20d250ff3b87868a5615efcc79704ba49/psycopg2cffi-2.8.1.tar.gz (63kB)
    100% |████████████████████████████████| 71kB 8.7MB/s 
Collecting html5lib==0.9999999 (from -r requirements.txt (line 6))
  Downloading https://files.pythonhosted.org/packages/ae/ae/bcb60402c60932b32dfaf19bb53870b29eda2cd17551ba5639219fb5ebf9/html5lib-0.9999999.tar.gz (889kB)
    100% |████████████████████████████████| 890kB 1.3MB/s 
Collecting chardet==2.3.0 (from -r requirements.txt (line 7))
  Downloading https://files.pythonhosted.org/packages/7e/5c/605ca2daa5cf21c87690d8fe6ab05a6f2278c451f4ede6456dd26453f4bd/chardet-2.3.0-py2.py3-none-any.whl (180kB)
    100% |████████████████████████████████| 184kB 6.1MB/s 
Collecting pandas (from -r requirements.txt (line 8))
  Downloading https://files.pythonhosted.org/packages/db/83/7d4008ffc2988066ff37f6a0bb6d7b60822367dcb36ba5e39aa7801fda54/pandas-0.24.2-cp27-cp27mu-manylinux1_x86_64.whl (10.1MB)
    100% |████████████████████████████████| 10.1MB 114kB/s 
Collecting cffi>=1.0 (from psycopg2cffi->-r requirements.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/8d/e9/0c8afd1579e5cf7bc0f06fbcd7cdb954cbc0baadd505973949a99337da1c/cffi-1.12.3-cp27-cp27mu-manylinux1_x86_64.whl (415kB)
    100% |████████████████████████████████| 419kB 2.8MB/s 
Collecting six (from psycopg2cffi->-r requirements.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
Collecting numpy>=1.12.0 (from pandas->-r requirements.txt (line 8))
  Downloading https://files.pythonhosted.org/packages/1f/c7/198496417c9c2f6226616cff7dedf2115a4f4d0276613bab842ec8ac1e23/numpy-1.16.4-cp27-cp27mu-manylinux1_x86_64.whl (17.0MB)
    100% |████████████████████████████████| 17.0MB 64kB/s 
Collecting pytz>=2011k (from pandas->-r requirements.txt (line 8))
  Downloading https://files.pythonhosted.org/packages/87/76/46d697698a143e05f77bec5a526bf4e56a0be61d63425b68f4ba553b51f2/pytz-2019.2-py2.py3-none-any.whl (508kB)
    100% |████████████████████████████████| 512kB 2.7MB/s 
Collecting python-dateutil>=2.5.0 (from pandas->-r requirements.txt (line 8))
  Downloading https://files.pythonhosted.org/packages/41/17/c62faccbfbd163c7f57f3844689e3a78bae1f403648a6afb1d0866d87fbb/python_dateutil-2.8.0-py2.py3-none-any.whl (226kB)
    100% |████████████████████████████████| 235kB 4.7MB/s 
Collecting pycparser (from cffi>=1.0->psycopg2cffi->-r requirements.txt (line 5))
  Downloading https://files.pythonhosted.org/packages/68/9e/49196946aee219aead1290e00d1e7fdeab8567783e83e1b9ab5585e6206a/pycparser-2.19.tar.gz (158kB)
    100% |████████████████████████████████| 163kB 6.7MB/s 
Building wheels for collected packages: BeautifulSoup, httplib2, netifaces, psycopg2cffi, html5lib, pycparser
  Running setup.py bdist_wheel for BeautifulSoup ... done
  Stored in directory: /home/sharon/.cache/pip/wheels/74/d2/0b/8ef02aab9e15c6e5158d7aee909adab931a9c54920e99f468e
  Running setup.py bdist_wheel for httplib2 ... done
  Stored in directory: /home/sharon/.cache/pip/wheels/36/f2/49/5adbf90fba31e02a7784e1147d7f8b6c4af3718739e568c8cb
  Running setup.py bdist_wheel for netifaces ... done
  Stored in directory: /home/sharon/.cache/pip/wheels/16/44/ff/5a544c439c6e1a7cbe437336971781eb73861575d13a538b72
  Running setup.py bdist_wheel for psycopg2cffi ... done
  Stored in directory: /home/sharon/.cache/pip/wheels/f9/99/43/0dc1c09c3333cf71167e3159c3b33302d75a5e7f11a295d0d9
  Running setup.py bdist_wheel for html5lib ... done
  Stored in directory: /home/sharon/.cache/pip/wheels/50/ae/f9/d2b189788efcf61d1ee0e36045476735c838898eef1cad6e29
  Running setup.py bdist_wheel for pycparser ... done
  Stored in directory: /home/sharon/.cache/pip/wheels/f2/9a/90/de94f8556265ddc9d9c8b271b0f63e57b26fb1d67a45564511
Successfully built BeautifulSoup httplib2 netifaces psycopg2cffi html5lib pycparser
Installing collected packages: BeautifulSoup, PyMySQL, httplib2, netifaces, pycparser, cffi, six, psycopg2cffi, html5lib, chardet, numpy, pytz, python-dateutil, pandas
Successfully installed BeautifulSoup-3.2.1 PyMySQL-0.9.3 cffi-1.12.3 chardet-2.3.0 html5lib-0.9999999 httplib2-0.9.2 netifaces-0.10.4 numpy-1.16.4 pandas-0.24.2 psycopg2cffi-2.8.1 pycparser-2.19 python-dateutil-2.8.0 pytz-2019.2 six-1.12.0
    
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
