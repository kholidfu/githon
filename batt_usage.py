#!/usr/bin/python


"""Checking Battery State"""


class BatteryThinkpad(object):
    full_capacity = 56160

    def battery_usage(self):
        with open('/proc/acpi/battery/BAT0/state', 'r') as f:
            for line in f:
                if 'remaining' in line:
                    used = line.split(':')[1].strip().split()[0]
                    percent = float(int(used)) / int(self.full_capacity) * 100
        return 'Battery usage reminding: %.2f' % percent + '%'

b = BatteryThinkpad()
print b.battery_usage()
