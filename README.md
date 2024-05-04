# fake_scpi
A fake SCPI server for unit and behavioral testing

# main.py
This is the fake SCPI server. It depends on telnetlib3.
It's really dumb and just saves all the command arguments, spitting them back out if asked.

# siglent.txt
This is a sample capture of a conversation between Pulseview and my Siglent oscope.
Pulseview is the one asking questions, roughly every other line.
It appears to ask for the channel 1 waveform data with `C1:WF? ALL`, after which the scope responds with binary data. It's really long so I truncated it. Pulseview froze anyway and didn't display the data.

I am thinking that binary is an acceptable way to send data in 16-bit words. The first word should say how many points there are (the length of the array). Data should be in network-order (most significant byte first).
