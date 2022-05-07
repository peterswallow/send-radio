input.onButtonPressed(Button.A, function () {
    radio.sendString("Start")
})
input.onButtonPressed(Button.B, function () {
    radio.sendString("Stop")
})
basic.forever(function () {
    basic.showString("Hello!")
})
