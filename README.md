RetinaBurner, Sunlight brand data elucidator
=================================================

Intro
---------

This is a WIP codebase dedicated to downloading, cleaning and normalizing government spending data. Much of the USASpending code is adapted from github.com/sunlightlabs/datacommons.

Shield your eyes as we blast shadowy government contracts and other data with UV rays. This data importer currently imports the following datasets:

- [x] USASpending.gov - Contracts
- [x] USASpending.gov - Grants

Future versions of this importer will support

- [ ] FedBizOpps.gov data 
- [ ] GSA SmartPay Data


Usage
----------
To get started, install the dependencies while in an [activated python virtal environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) and using [pip](http://www.pip-installer.org/en/latest/installing.html)

    pip install -r requirements.txt

For the USASpending data, you will need to specify which fiscal years you want to pull in by editing a list in the settings file called "FISCAL_YEARS". The default is 2000-2014.

Postgresql settings
-------------------

After filling in your database settings in the Django settings file, run 
    manage.py syncdb
to create the tables.

If you are using postgresql and will be using the indexes with this project, you will need to create some text search elements within postgresql. To do that, move the file in the root directory of the project (retinaburner.stop) to your postgresql text search directory. On version 9.1, that is 
/usr/share/postgresql/9.1/tsearchdata/ .

Once you move the stopwords file, you can create the text search indexes like this: 

manage.py dbshell > tsconfig.sql  

tsconfig.sql is also located in the project's root directory. This is a one time step that only needs to be repeated if you blow away your whole database, not just the tables. 

Importing Contracts and Grants
------------------------------

The download, cleaning and import processes are broken out into their own Django management commands. To do a fresh import from scratch (and run all the commands at the same time with some sensible defaults) you can run:

manage.py fresh_import

This will automatically download the files in retinaburner/usaspending/downloads/all_downloads.txt process them and store them in the database. The default contents of that file are 14 years of fiscal data so just go in and remove some links if you don't need all of that.

Alternatively, if you want to run the commands individually, either to debug or just see how it works, you can. Here's the steps, each with their own manage command:

*   manage.py download_files FILENAME    #download and unzip all the links in FILENAME
*   manage.py convert_usaspending_contracts    #normalizes all the data and dumps into a better structured CSV
*   manage.py convert_usaspending_grants     # ditto, but for grants
*   manage.py syncdb  #create tables
*   manage.py create_partition --fiscal-year all  #create postgresql partitions
*   manage.py load_contracts FILENAME   #copy the csv FILENAME (will appear in out folder) into the contracts table
*   manage.py load_grants FILENAME   #copy the csv FILENAME (will appear in out folder) into the contracts table 
*   manage.py build_indexes  -- Not implemented



manage.py download_files FILENAME
---------------------------------
 To tell this command which files to download, pass it a single argument, the path to a file with the urls to be downloaded. It's expecting urls of the form

http://www.usaspending.gov/datafeeds/2013_All_Contracts_Full_20131015.csv.zip

Which are available at http://www.usaspending.gov/data under the Archives tab. There is an example file in the retinaburner/usaspending/downloads folder. Here's an example of how to use the command with the example file included in the project:

    manage.py download_files retinaburner/usaspending/downloads/downloads.20131105.txt


manage.py convert_usaspending_contracts
---------------------------------------

To convert these raw csvs into more normalized data, you need to run the convert_usaspending_contracts command.
    
    manage.py convert_usaspending_contracts

That will take any csvs out of the datafeeds folder, process them and put the result in the out folder. The source file will then have a timestamp prepended to the name and it will be moved to the done folder. If there is a problem with any file or year, you'll need to address the problem, and move the source files __back__ to the datafeeds folder and then remove the timestamp. 

You can stop here if you are not using Postgresql for your database. 


POSTGRESQL Setup
-----------------

manage.py create_partition --fiscal-year all
--------------------------------------------
Use this command to generate partitions in the contract and grant tables for each fiscal year. This helps with indexing and performance. Either pass in a desired fiscal year, or just pass in all to do all the years in the FISCAL_YEARS setting.

manage.py load_contracts FILENAME
----------------------------------
Finally, use the Postgresql copy command to dump the csv into the tables. Note that this is not smart. It won't check for duplicate transactions. So you only want to use this when starting with empty tables. The FILENAME should be one of the files that appears in the out file (retinaburner/usaspending/downloads/csvs/out/contracts_2013.csv, for example).


manage.py load_grants FILENAME
-------------------------------
Same deal as the contracts except you use it for grants files.



create indexes 
./manage.py dbshell < retinaburner/usaspending/scripts/usaspending/grants_indexes.sql
./manage.py dbshell < retinaburner/usaspending/scripts/usaspending/contracts_indexes.sql


run tests to ensure import --> write tests, check against usaspending api