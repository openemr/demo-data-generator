# OpenEMR Demo Data Generator

This python tool creates fictional demo data for OpenEMR. It's still a work in progress.

## Installation

Clone this repo

```
cd demo-data-generator
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

```
./main.py <command> <number of recursion>
```

## Available data points

Here are the data points capable of being generated

`patients`

Plan on creating an option to allow writing straight to a file, but for now I
recommend piping the output to `file.sql`


Currently this will spit out valid SQL that will create only patient data


