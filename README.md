# ntpq_sysstats

Simple python script to extract `ntpq -c sysstats` metrics for ingesting into InfluxDB using Telegraf.

## Prerequisites

Obviously `ntpq` and `python3`. Tested with following versions on a Debian 12.9 system:

- `ntpq ntpsec-1.2.2`
- `Python 3.11.2`
- `Telegraf 1.33.1`

## Usage

Edit `ntpq_sysstats.py` and change the variable `hostname`. For telegraf you can find an example configuration in `telegraf.conf`. Do not forget to modify the telegraf configuration based on your output. The example configuration for telegraf also includes the input `ntpq` too for peer metrics.
