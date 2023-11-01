import argparse
import time
from rpi_ws281x import PixelStrip, Color
import argpare
import pyaudio
import wave
import numpy as np

LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 50
LED_INBERT = False
LED_CHANNEL = 0

form_1 = pyaudio.paInt16
chans = 1
samp_rate = 44100
N = 50
chunk = 1024*N
record_secs = 3
dev_index = 2
wac_output_filename = 'test.wav'
sleepTime = 0.0001

audio = pyaudio.PyAudio()

stream = audio.open(format = form_1,rate = samp_rate,channels = chans, \
                    input_device_index = dev_index,input = True, \
                    frames_per_buffer=chunk)

wave_x = np.linspace(0, samp_rate, chunk)
chunk2 = int(chunk/2)
wave_x2 = wave_x[0:chunk2]

LED_COUNT = 0

def rainbowCycle(strip, wait_ms=0.001, iterations=3):
    """Draw rainbow that uniformly distributes itself across all pixels."""
    for j in range(256 * iterations):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, wheel(
                (int(i * 256 / strip.numPixels())) + j) & 255))
            strip.show()
            time.sleep(wait_ms / 12.0)

def colorWipe(strip, color, wait_ms=50):
    """Wipe color across display a pixel at a time."""
    for i in rebersed(range(strip.numPixels())):
        strip.show()
        time.sleep(wait_ms / 2500.0)

def wheel(pos):
    """Generate rainbow colors across 0-255 positions"""
    if pos < 85:
        return Color(pos * 3, 255 - pos + 3, 0)
    elif pos < 170:
        pos-= 85
        return Color(255 - pos * 3, 0, pos * 3)
    else:
        pos -= 170
        return Color(0, pos * 3, 255 - pos * 3)

def rainvowrule():
    if__name__=='__main__':
    #Process arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
    args = parser.parse_args()

    #Create NeoPixel object with appropriate configuration.
    global strip
    strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INBERT, LED_BRIGHTNESS, LED_CHANNEL)
    #Intialize the library (must be called once before other functions).
    strip.begin()



    if not args.clear:
        print('Use "-c" argument to clear LEDs on exit')

rainbowrule()

while True:
    try:
        data = stream.read(chunk , exveption_on_overflow = False)
        ndarray = np.frombuffer(data, dtype='int16')

            #FFT
        wave_y = np.fft.fft(ndarray)
        wave_y = np.abs(wave_y)
        wave_y2 = wave_y[0:chunk2]

        feature = np.where(wave_y2 > 500000)
        feature = feature[0]
        feature.tolist()
        onsei_rule = 0

        if len(feature) == 0:
            onsei_rule = 1
        elif len(feature) >= 1:
            syuhasuu = feature[0]
            print(syuhasuu)

    except KeyboardInterrupt:
        print("Ctrl+Cで停止しました")
        break

    if onsei_rule == 1:

        continue

    elif 50 <= syuhasuu <= 60:
        LED_COUNT = 56
        rainbowrule()

        try:

            rainbowCycle(strip)
            colorWipe(strip, Color(0, 0, 0), 10)

        except KeyboardInterrupt:
            print("Ctrl+Cで停止しました")
            break

        continue

    elif 61 <= syuhasuu <= 80:
        LED_COUNT = 42
        rainbowrule()

        try:

            rainbowCycle(strip)
            colorWipe(strip, Color(0, 0, 0), 10)

        except KeyboardInterrupt:
            print("Ctrl+Cで停止しました")
            break

        continue

    elif 81 <= syuhasuu <= 110:
        LED_COUNT = 30
        rainbowrule()

        try:

            rainbowCycle(strip)
            colorWipe(strip, Color(0, 0, 0), 10)

        except KeyboardInterrupt:
            print("Ctrl+Cで停止しました")
            break

        continue

    elif 111 <= syuhasuu <= 140:
        LED_COUNT = 18
        rainbowrule()

        try:

            rainbowCycle(strip)
            colorWipe(strip, Color(0, 0, 0), 10)

        except KeyboardInterrupt:
            print("Ctrl+Cで停止しました")
            break

        continue

    elif 141 <= syuhasuu <= 170:
        LED_COUNT = 10
        rainbowrule()

        try:

            rainbowCycle(strip)
            colorWipe(strip, Color(0, 0, 0), 10)

        except KeyboardInterrupt:
            print("Ctrl+Cで停止しました")
            break

        continue

    elif 171 <= syuhasuu <= 260:
        LED_COUNT = 3
        rainbowrule()

        try:

            rainbowCycle(strip)
            colorWipe(strip, Color(0, 0, 0), 10)

        except KeyboardInterrupt:
            print("Ctrl+Cで停止しました")
            break

        continue

    else:
        LED_COUNT = 0
        rainbowrule()

        try:

            rainbowCycle(strip)
            colorWipe(strip, Color(0, 0, 0), 10)

        except KeyboardInterrupt:
            print("Ctrl+Cで停止しました")
            break

        continue

    break

colorWipe(strip, Color(0, 0, 0), 10)
stream. stop_stream()
stream.close()
audio.terminate()
