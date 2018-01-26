import stage
import ugame
import board
import audioio
import digitalio


PALETTE = (b'\xf0\x0f\x00\x00\xcey\xff\xff\xf0\x0f\x00\x19\xfc\xe0\xfd\xe0'
           b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00')

mute = digitalio.DigitalInOut(board.MUTE)
mute.switch_to_output(value=1)

game = stage.Stage(ugame.display, 12)
text = stage.Text(16, 16, palette=PALETTE)
game.layers = [text]

pew_sound = open("pew.wav", 'rb')
audio = None

for y in range(16):
    for x in range(16):
        text.char(x, y, ' ')

game.render_block()

while True:
    keys = 0
    while not keys:
        keys = ugame.buttons.get_pressed()
        game.tick()
    while ugame.buttons.get_pressed():
        game.tick()
    if audio:
        audio.stop()
    audio = audioio.AudioOut(board.SPEAKER, pew_sound)
    audio.play()
    if keys & ugame.K_RIGHT:
        text.char(6, 8, '\x03')
    if keys & ugame.K_LEFT:
        text.char(4, 8, '\x04')
    if keys & ugame.K_UP:
        text.char(5, 7, '\x01')
    if keys & ugame.K_DOWN:
        text.char(5, 9, '\x02')
    if keys & ugame.K_O:
        text.char(10, 7, '\x06')
    if keys & ugame.K_X:
        text.char(9, 9, '\x05')
    game.render_block()
