# OpenEMR Demo Data Generator

This python tool creates fictional demo data for OpenEMR. It's still a work in progress.

## How to install

Clone this repo

```
cd openemr-demo-data-generator
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py patients <int>
```
Int is the number of patients you want created

Currently this will spit out valid SQL that will create only patient data

