[![Build Status](https://travis-ci.org/openemr/demo-data-generator.svg?branch=master)](https://travis-ci.org/openemr/demo-data-generator)

# OpenEMR Demo Data Generator

This python tool creates fictional demo data for OpenEMR. It's still a work in progress.

## Installation

Clone this repo

```bash
cd demo-data-generator
virtualenv venv
. venv/bin/activate
pip install .
demodata <command>
```

## Usage

```
demodata <global options> COMMAND <options>
```

## Available data points

Here are the data points capable of being generated

`patients`

Plan on creating an option to allow writing straight to a file, but for now I
recommend piping the output to `file.sql`


Currently this will spit out valid SQL that will create only patient data



