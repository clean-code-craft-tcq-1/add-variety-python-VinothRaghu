import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_check_and_alert(self):
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL',{'coolingType':'PASSIVE_COOLING'},70)== True)
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER',{'coolingType':'PASSIVE_COOLING'},70)== True)
    self.assertTrue(typewise_alert.check_and_alert('TO_CONSOLE',{'coolingType':'PASSIVE_COOLING'},70)== True)


if __name__ == '__main__':
  unittest.main()
