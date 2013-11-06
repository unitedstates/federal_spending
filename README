RetinaBurner, Sunlight brand data elucidator
=================================================

Intro
---------

This is a WIP codebase dedicated to downloading, cleaning and normalizing government spending data. Much of the USASpending code is adapted from github.com/sunlightlabs/datacommons.

Shield your eyes as we blast shadowy government contracts and other data with UV rays. This data importer currently imports the following datasets:

- [x] USASpending.gov - Contracts

Future versions of this importer will support
- [ ] USASpending.gov - Grants
- [ ] FedBizOpps.gov data 
- [ ] GSA SmartPay Data


Usage
----------
To get started, install the dependencies while in an [activated python virtal environment](http://docs.python-guide.org/en/latest/dev/virtualenvs/) and using [pip](http://www.pip-installer.org/en/latest/installing.html)

    pip install -r requirements.txt


Importing Contracts
--------------------
The download, cleaning and import processes are Django management commands. To tell the command which files to download, pass it a single argument, the path to a file with the urls to be downloaded. It's expecting urls of the form

http://www.usaspending.gov/datafeeds/2013_All_Contracts_Full_20131015.csv.zip

Which are available at http://www.usaspending.gov/data under the Archives tab. There is an example file in the retinaburner/usaspending/downloads folder. Here's an example of how to use the command with the example file included in the project:

    manage.py download_files retinaburner/usaspending/downloads/downloads.20131105.txt

To convert these raw csvs into more normalized data, you need to run the convert_usaspending_contracts command.
    
    manage.py convert_usaspending_contracts

That will take any csvs out of the datafeeds folder, process them and put the result in the out folder. The source file will then have a timestamp prepended to the name and it will be moved to the done folder. If there is a problem with any file or year, you'll need to address the problem, and move the source files __back__ to the datafeeds folder and then remove the timestamp. 



