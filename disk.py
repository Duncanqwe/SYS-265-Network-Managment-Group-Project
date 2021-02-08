import shutil

path = "C:/"

stat = shutil.disk_usage(path)

percent = (round(stat.used/stat.total, 2))

if percent > .75:
    print("WARNING: DISK SPACE is", percent, "% FULL")
else:
    print("DISK SPACE IN SAFE RANGE")
