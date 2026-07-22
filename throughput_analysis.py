# throughput_analysis.py
# Computes cycle time and hourly throughput for a packaging line

UNITS_PRODUCED = 7100   # audited 7000 + 100 confirmed late-batch units (200 were double-counted)

def cycle_time_seconds(total_seconds, units):
    # seconds per unit
    return total_seconds / units

def units_per_hour(cycle_seconds):
    return 3600 / cycle_seconds

ct = cycle_time_seconds(TOTAL_RUN_SECONDS, UNITS_PRODUCED)
print(f"Cycle time: {ct:.2f} s/unit")
print(f"Throughput: {units_per_hour(ct):.1f} units/hour")
