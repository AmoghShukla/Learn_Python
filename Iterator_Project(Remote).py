#Remote Control for a TV
class RemoteControl():
    def __init__(self):
        self.Channels = ["SabTV","Sony","National Geographic","HBO","HistoryTV18"]
        self.index = -1 #-1 means your TV is off and you have no channels coming in

    def __iter__(self):
        return self

    def __next__(self):
        self.index += 1
        if self.index == len(self.Channels):
            raise StopIteration #When raise is executed, the normal flow of the program is interrupted,
            # and the specified exception("Stop Iteration" here) is thrown.

        return self.Channels[self.index]

R = RemoteControl()
itr = iter(R)
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))

