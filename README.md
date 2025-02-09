# ntpq_sysstats

Simple python script to extract `ntpq -c sysstats` metrics for ingesting into InfluxDB using Telegraf.

## Prerequisites

Obviously `ntpq` and `python3`.

## Usage

Edit `ntpq_sysstats.py` and change the variable `hostname`. For telegraf you can find an example configuration in `telegraf.conf`. Do not forget to modify the telegraf configuration based on your output. The example configuration for telegraf also includes `ntpq` too for peer metrics.
