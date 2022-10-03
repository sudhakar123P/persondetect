from numpy import loadtxt

frames = loadtxt("output.txt", comments="#", delimiter=",", unpack=False)
all_frames = 75503
all_seconds = 15207
strbu = ""

for frame in frames:
    t1 = frame / all_frames * all_seconds
    # convert to hours, minutes, seconds
    h = int(t1 / 3600)
    m = int((t1 - h * 3600) / 60)
    s = int(t1 - h * 3600 - m * 60)
    strbu += "Frame: %d, Time: %02d:%02d:%02d" % (frame, h, m, s) + "\n"
    print("Frame: %d, Time: %02d:%02d:%02d" % (frame, h, m, s))


with open("outputwithtime.txt", "w") as f:
    f.write(strbu)  # write the string to the file
