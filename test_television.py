import pytest
from television import Television

class TestTelevision:
    def setup_method(self):
        self.tv = Television()

    def teardown_method(self):
        del self.tv

    def test_init(self):
        assert str(self.tv) == 'Power = Off, Channel = 0, Volume = 0'

    def test_power(self):
        self.tv.power()
        assert str(self.tv) == 'Power = On, Channel = 0, Volume = 0'
        self.tv.power()
        assert str(self.tv) == 'Power = Off, Channel = 0, Volume = 0'

    def test_mute(self):
        self.tv.power()
        self.tv.volume_up()
        self.tv.mute()
        assert str(self.tv) == 'Power = On, Channel = 0, Volume = Muted'
        self.tv.mute()
        assert 'Volume = 1' in str(self.tv)
        self.tv.power()  # Turning TV off should not affect mute status
        self.tv.mute()  # Should have no effect because TV is off
        assert str(self.tv) == 'Power = Off, Channel = 0, Volume = 1'

    def test_channel_up(self):
        self.tv.power()
        self.tv.channel_up()
        assert str(self.tv) == 'Power = On, Channel = 1, Volume = 0'
        # Test channel wrap-around
        for _ in range(1, Television.MAX_CHANNEL + 1):
            self.tv.channel_up()
        assert str(self.tv) == f'Power = On, Channel = {Television.MIN_CHANNEL}, Volume = 0'

    def test_channel_down(self):
        self.tv.power()
        self.tv.channel_down()
        assert str(self.tv) == f'Power = On, Channel = {Television.MAX_CHANNEL}, Volume = 0'
        # Test channel wrap-around
        self.tv.channel_down()
        assert str(self.tv) == f'Power = On, Channel = {Television.MAX_CHANNEL - 1}, Volume = 0'

    def test_volume_up(self):
        self.tv.power()
        for _ in range(0, Television.MAX_VOLUME + 1):
            self.tv.volume_up()
        assert str(self.tv) == f'Power = On, Channel = 0, Volume = {Television.MAX_VOLUME}'

    def test_volume_down(self):
        self.tv.power()
        self.tv.volume_up()  # Increase volume to 1
        self.tv.volume_down()
        assert str(self.tv) == 'Power = On, Channel = 0, Volume = 0'
        # Test volume does not go below MIN_VOLUME
        self.tv.volume_down()
        assert str(self.tv) == 'Power = On, Channel = 0, Volume = 0'

