import typewise_alert

class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
      #Check Breaches
      self.assertTrue(typewise_alert.infer_breach(10, 20, 60) == 'TOO_LOW')
      self.assertTrue(typewise_alert.infer_breach(70, 20, 60) == 'TOO_HIGH')
      self.assertTrue(typewise_alert.infer_breach(50, 20, 60) == 'NORMAL')
   
    
if __name__ == '__main__':
  unittest.main()
