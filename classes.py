class Television:
    '''
    A class representing detail of a television object
    '''

    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) ->None:
        """
        Constructor to create initial state of a television object
        - status should be False by default (meaning tv turned off)
        - channel should be MIN_CHANNEL (0) by default
        - volume should be MIN_VOLUME (0) by default
        """
        self.__status = False
        self.__channel = self.MIN_CHANNEL
        self.__volume = self.MIN_VOLUME


    def power(self) ->None:
        """
        Method to turn on a tv if the status is False. Turn off a tv if the status is True
        """

        if self.__status == False:
            self.__status = True
        elif self.__status == True:
            self.__status = False

    def channel_up(self) ->None:
        """
        Method to channel up a tv. It should work only if a tv is on.
        If the channel is equal to MAX_CHANNEL(3), it should take the channel back to MIN_CHANNEL (0)
        """

        if self.__status ==True:
            if self.__channel >=self.MIN_CHANNEL and self.__channel <self.MAX_CHANNEL:
                self.__channel+=1
            elif self.__channel==self.MAX_CHANNEL:
                self.__channel=self.MIN_CHANNEL

    def channel_down(self) ->None:
        """
        Method to channel down. It should work only if a tv is on.
        If the channel is equal to MIN_CHANNEL (0), it should make channel MAX_CHANNEL(3)
        """

        if self.__status ==True:
            if self.__channel>self.MIN_CHANNEL and self.__channel<=self.MAX_CHANNEL:
                self.__channel-=1
            elif self.__channel ==self.MIN_CHANNEL:
                self.__channel=self.MAX_CHANNEL

    def volume_up(self) ->None:
        '''
        Method to volume down. It should work only if a tv is on.
        If the volume is equal to MAX_VOLUME, the volume should not be adjusted.
        '''

        if self.__status==True:
            if self.__volume>=self.MIN_VOLUME and self.__volume < self.MAX_VOLUME:
                self.__volume+=1
            elif self.__volume == self.MAX_VOLUME:
                pass

    def volume_down(self) ->None:
        """
        Method to volume up. It should work only if a tv is on.
        If the volume is equal to MIN_VOLUME, the volume should not be adjusted.
        """


        if self.__status==True:
            if self.__volume>self.MIN_VOLUME and self.__volume<=self.MAX_VOLUME:
                self.__volume-=1
            elif self.__volume==self.MIN_VOLUME:
                pass

    def __str__(self) -> str:
        """
        Method to show the final status of tv
        :return: the result of status, channel, and volume of television object
        """

        return f'TV status on ={self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
