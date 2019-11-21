from typing import List


class Client():
    def __init__(self, id: str):
        self.id: str = id
        self.lines: List[Line] = []

    def get_in_line(self, line: 'Line'):
        line.add_client(self)

    def short_form(self):
        return self.id

    def __str__(self):
        return "I am client {} and I am in these lines: {}".format(self.id, list(map(lambda x: x.short_form(), self.lines)))


class Clerk():
    pass


class Line():
    def __init__(self, id: str):
        self.id: str = id
        self.clients: List[Client] = []

    def add_client(self, client: Client):
        if client not in self.clients:
            self.clients.append(client)
        print("Adde client {} to line {}".format(client, self))

    def short_form(self):
        return self.id

    def notify_clients(self):
        # get them from db
        # notify I changed
        pass

    def __str__(self):
        return "I am line {} and I have these clients: {}".format(self.id, list(map(lambda x: x.short_form(), self.clients)))


class LinesManager():
    def get_all_lines():
        pass
