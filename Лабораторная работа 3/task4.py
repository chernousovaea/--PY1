BYTES_ONE_CHAR = 1

pages = 100
lines = 50
chars = 25

total_chars = chars * lines * pages
total_bytes = (chars * lines * pages) * 1

disk_size = 1.44 * (1024 ** 2)

print(disk_size // total_bytes)
