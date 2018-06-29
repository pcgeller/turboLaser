import serial

ser = serial.Serial("/dev/ttyUSB0", timeout=2.0)

while 1:
    try:
        atCommand = input('Enter AT Command:  ')
        atCommandFormated = atCommand + '\r'
        atCommandEncoded = atCommandFormated.encode("ascii")
        ser.write(atCommandEncoded)
        out = ser.read(10000)
        print(out.decode("ascii"))
    except UnicodeDecodeError:
        print("Unicode Decode Error on output.")
        continue
