import machine
ow = machine.Onewire(4)
ds0 = machine.Onewire.ds18x20(ow, 0)
temp = ds0.convert_read()
print(temp)
