[![Build Status](https://travis-ci.org/openemr/demo-data-generator.svg?branch=master)](https://travis-ci.org/openemr/demo-data-generator)

# OpenEMR Demo Data Generator

This python tool creates fictional demo data for OpenEMR. It's still a
work in progress.

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
`facilities`

There is a plan to create an option to allow writing the data
straight to a file, but for now I recommend the following:

```
touch file.sql
for i in {1..1000}; do demodata patients >> file.sql; done
mysql -u your_username -p openemr < file.sql
```

## License
Copyright (C) 2017 Robert Down

The OpenEMR Demo Data Generator tool is licensed under the GNU GPL V3
license.

