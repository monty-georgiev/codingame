#! /usr/bin/python3



while True:
    peaks = {}
    for i in range(8):
        mountain_h = int(input())
        peaks[i] = mountain_h

    sorted_peaks = sorted(peaks,key=peaks.get, reverse=True)
    print(sorted_peaks[0])
