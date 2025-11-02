from larapy.database.seeding.factory import Factory


class TestFactory(Factory):
    
    def definition(self):
        return {
            'name': self._faker.name(),
            'email': self._faker.email(),
        }
