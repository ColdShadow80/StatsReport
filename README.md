# StatsReport

Discord report: per Area defined in Stats, with Mons_scanned, Mon_IV, IV_percentage, Hundos and zero_IV for the last day.

- ``cp config.ini.example config.ini`` and put in the details  
- in cron put something like ``7 0 * * * cd /home/dkmur/StatsReport && /usr/bin/python3 StatsReport.py``
