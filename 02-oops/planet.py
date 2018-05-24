class Planet(object):
    def rotate(self):
        print("rotate")

    def revolve(self):
        print("revolve")

    def rotate_and_revolve(self):
        self.rotate()
        self.revolve()


earth = Planet()
earth.rotate_and_revolve()
