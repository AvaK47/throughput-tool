# throughput_analysis.py
# Computes cycle time and hourly throughput for a packaging line

TOTAL_RUN_SECONDS = 28800   # one 8-hour shift in seconds
UNITS_PRODUCED = 7200       # units packed during the shift

def cycle_time_seconds(total_seconds, units):
    # seconds per unit
    return total_seconds / units

def units_per_hour(cycle_seconds):
    return 3600 / cycle_seconds

ct = cycle_time_seconds(TOTAL_RUN_SECONDS, UNITS_PRODUCED)
print(f"Cycle time: {ct:.2f} s/unit")
print(f"Throughput: {units_per_hour(ct):.1f} units/hour")
