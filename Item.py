from aiogram import types


class Item:
    def __init__(self, price, name):
        self.media_group = types.MediaGroup()
        self.price = price
        self.name = name

    def description(self):
        description = f"{self.name}\nЦена: {self.price}"
        return description

    def add_photo(self, url):
        self.media_group.attach_photo(url)
