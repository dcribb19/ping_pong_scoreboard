import board
import pulseio


IR_PIN = board.TX  # BOARD8, GPIO14
# dir(board) to see what pins are available on board

pulses = pulseio.PulseIn(IR_PIN)

# Wait for an active pulse
while len(pulses) == 0:
    pass
# Pause while we do something with the pulses
pulses.pause()

# Print the pulses. pulses[0] is an active pulse unless the length
# reached max length and idle pulses are recorded.
print(pulses)
