import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_alerts(self): 
      self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'PASSIVE_COOLING', 50) == 'Temperature is too high')
      self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'PASSIVE_COOLING', 50) == '65261, TOO_HIGH')
      self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'PASSIVE_COOLING', -1) == 'Temperature is too low')
      self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'PASSIVE_COOLING', -1) == '65261, TOO_LOW')
      self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL', 'PASSIVE_COOLING', 25) == 'Temperature is normal')
      self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER', 'PASSIVE_COOLING', 25) == '65261, NORMAL') 
  def test_threshold_limit_exceed_check(self):
      self.assertTrue(typewise_alert.infer_breach(10, 20, 60) == 'TOO_LOW')
      self.assertTrue(typewise_alert.infer_breach(70, 20, 60) == 'TOO_HIGH')
      self.assertTrue(typewise_alert.infer_breach(50, 20, 60) == 'NORMAL')
if __name__ == '__main__':
  unittest.main()
