class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self.__status = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.__muted = False
        self.__previous_volume = 0

    def power(self):
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self):
        # Mute the TV if it is on
        if self.__status == True:
            if self.__muted == False:
                self.__muted = True
                self.__previous_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
            else:
                self.__muted = False
                self.__volume = self.__previous_volume

    def channel_up(self):
        if self.__status == True:
            self.__channel += 1
            if self.__channel > Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self):
        if self.__status == True:
            self.__channel -= 1
            if self.__channel < Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self):
        if self.__status == True and not self.__muted:
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
            if self.__muted:
                self.__muted = False

    def volume_down(self):
        if self.__status == True:
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        if self.__status == True:
            status_str = 'On'
        else:
            status_str = 'Off'

        if self.__muted == True:
            volume_str = 'Muted'
        else:
            volume_str = f'Volume = {self.__volume}'

        return f'Power = {status_str}, Channel = {self.__channel}, {volume_str}'
