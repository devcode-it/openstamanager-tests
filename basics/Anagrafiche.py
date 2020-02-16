from common.Test import Test

class Anagrafiche(Test):
    def test_upper(self):
        self.navigateTo("Anagrafiche")
        self.assertEqual('foo'.upper(), 'FOO')
