class Xyz:
    def __init__(self,success):
        self.success = "Success!"

    def toprint(self):
        return f"{self.success}"

class Abc:
    def __init__(self,success):
        self.success = "Not yet."
    
    def test(self):
        a = Xyz("test")
        print(a.toprint()) #You can call a function outside of what you have imported then

________

