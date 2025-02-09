# ntpq_sysstats

Simple python script to extract `ntpq -c sysstats` metrics for ingesting into InfluxDB.

## Prerequisites

Obviously `ntpq` and `python3`.

## Usage

Edit `ntpq_sysstats.py` and change the variable `hostname`. For telegraf you can find an example configuration in `telegraf.conf`.
