Debugging your System
===========================================================
> In this page it is described how to find errors on your system so you can fix it by yourself. 

About the General process
===========================================================
The core process to fix your system goes in the similar way when you try to fix mechanical devices:

| Description          | Example: Motor           | Example: Software         |
|----------------------|--------------------------|---------------------------|
| Turn on the machine  | Turn on the car's motor  | Run the software          |
| Feed some input      | Accelerate the motor     | Use the software          |
| Look the output      | Listen or smell the motor| See the software logs     |

Since running and providing input to the software is provided always by the system. We will focus only in the _Look the output_ part.


Look the output
===========================================================
A journal in software systems is a record of what happened or what events on the system have occurred.

## `journalctl`: _"query the systemd journal"_.
- `journalctl --disk-usage`: show disk usage of this journal.
- `journalctl -f`: follow the journal in realtime
- `journalctl -k`: show only kernel messages.
- `journalctl -b 3`: show only messages from the last third boot.
- `journalctl -n 10`: limit the journal output
- `journalctl -o short`: control the output format (`verbose`, `json-pretty`, `short-full`, `cat`)
- `journalctl -S -3h -U -1h`: select the time gap _since_ 3 hours ago _until_ 1 hour ago. Other options are `-1m` for minutes and `-1d` and days. Also `today`, `yesterday` are valid.
- `journalctl _COMM=ls`: filter by command. Also `_PID`, `_UID`







- `dmesg`: _"print or control the kernel ring buffer"_.
- ``