import threading

def cpu_load():
    while True:
        pass  # Keeps the CPU occupied

# Set the number of threads to match or exceed your CPU core count
num_threads = 9999999999999  # Adjust this based on your system's CPU cores (e.g., 4 cores, 8 threads)

threads = []
for _ in range(num_threads):
    t = threading.Thread(target=cpu_load)
    t.start()
    threads.append(t)

# Threads will keep running until you stop the program
