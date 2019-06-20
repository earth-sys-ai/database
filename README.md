# database
Handles interactions between webserver and other python scripts.

---
## Usage

The import.py script may be used to import a netcdf file into the database.
It takes a password, a file, and a resolution.

Ex:
`> python3 import.py password123 data.nc 1500 *`

If you do not wish to view the data before upload you may remove the last arguement.

---
## Setup

To setup install the necessary requirements through pip.

```
netcdf4
numpy
matplotlib
psycopg2
```

Other packages such as python3-cairo or python3-gobjects may be required to be installed through a native package manager.

---
## Warning
As of now database importing does not work. This is being worked on as a priority.

