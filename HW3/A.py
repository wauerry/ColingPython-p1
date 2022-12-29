class OneIndexedList:
    def __init__(self, lst=None):
        if lst is None:
            lst = []
        self._list = lst

    def __getitem__(self, key):
        return self._list[key - 1]

    def __setitem__(self, key, value):
        self._list[key - 1] = value

    def append(self, value):
        self._list.append(value)

    def __len__(self):
        return len(self._list)
