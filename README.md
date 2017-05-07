# Spectrogram of Freddie Mercury's voice in "Under Pressure"

I've always been amazed by Freddie Mercury's voice and how he could get to very high notes. In this figure, I did a spectrogram of his voice between minutes 1:53 and 2:10 of Queen's "Under Pressure".

For those not used to signal analysis: a spectrogram is a plot of the frequency content of a time series at different instants of time. To do so, I used a sliding-window containing 1024 points (with 960 points of overlap between each one of them) and used Welch's method to estimate the signal's power spectral density. 

I used the A Capella version of Queen's Under Pressure available [here](https://www.youtube.com/watch?v=uMQb9LCNGxs).

See wikipedia's article for more information on time-frequency analysis [here](https://en.wikipedia.org/wiki/Time%E2%80%93frequency_analysis).

The `script.py` contains code for plotting the spectrogram of a audio file saved in `.wav` extension. If you want to run it, you should first download the audiofile from the YouTube link and rename it to `under_pressure-original.wav` (use FFMPEG if you have to change the `.mp3` exntesion to `.wav`).