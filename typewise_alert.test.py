import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_check_and_alert(self):
    self.assertTrue(typewise_alert.check_and_alert('console',{'coolingType':'PASSIVE_COOLING'},70)== True)
    self.assertTrue(typewise_alert.check_and_alert('email',{'coolingType':'PASSIVE_COOLING'},70)== True)


if __name__ == '__main__':
  unittest.main()
