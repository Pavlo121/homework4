import uuid

class UUIDIterator:
    def __iter__(self):
        return self

    def __next__(self):
        return uuid.uuid4()

uuid_iter = UUIDIterator

for _ in range(5):
    print(next(uuid_iter()))
