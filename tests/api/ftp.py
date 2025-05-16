import time 

start = time.time()
ftp.retrbinary("RETR testfile.txt", open("downloaded.txt", "wb").write)
end = time.time()

print(f"time of downloading: {end - start} seconds"
