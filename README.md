# StatsReport

Discord report: per Area defined in Stats, with Mons_scanned, Mon_IV, IV_percentage, Hundos and zero_IV for the last day.

- ``cp config.ini.example config.ini`` and put in the details  
- in cron put something like ``7 0 * * * cd /home/dkmur/StatsReport && /usr/bin/python3 StatsReport.py``

# DeviceStatus

Discord alert for devices offline - Posts warnings for devices offline for more than 10 minutes.

- ``cp config.ini.example config.ini`` and put in the details - DB config is shared for StatsReport and DeviceStatus, add device status Discord URL on the [DEVICE-STATUS-CONFIG] section 
- in cron put something like 

``1 * * * * cd /home/dkmur/StatsReport && /usr/bin/python3 devicestatus.py
11 * * * * cd /home/dkmur/StatsReport && /usr/bin/python3 devicestatus.py
21 * * * * cd /home/dkmur/StatsReport && /usr/bin/python3 devicestatus.py
31 * * * * cd /home/dkmur/StatsReport && /usr/bin/python3 devicestatus.py
41 * * * * cd /home/dkmur/StatsReport && /usr/bin/python3 devicestatus.py
51 * * * * cd /home/dkmur/StatsReport && /usr/bin/python3 devicestatus.py``
