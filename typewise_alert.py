cooling_types = {'PASSIVE_COOLING' : {'min': 0, 'max': 35}, 'HIGH_ACTIVE_COOLING' : {'min': 0, 'max': 45}, 'MED_ACTIVE_COOLING' : {'min': 0, 'max': 40}}

alert_messages_for_breach_code = { 'TOO_LOW'  : 'Temperature is too low', 
                                   'TOO_HIGH' : 'Temperature is too high', 
                                   'NORMAL'   : 'Temperature is normal' }
                                
def infer_breach(value, lowerLimit, upperLimit):
  if value < lowerLimit:
    return 'TOO_LOW'
  if value > upperLimit:
    return 'TOO_HIGH'
  return 'NORMAL'

email_recepient = {
        'TOO_LOW': {'recepient': "low.b@c.com"},
        'TOO_HIGH': {'recepient': "High.b@c.com"}}


def classify_temperature_breach(coolingType, temperatureInC):
  if validate_input(coolingType, temperatureInC): 
    lowerLimit = cooling_types[coolingType]['lowerLimit']
    upperLimit = cooling_types[coolingType]['upperLimit']
    return infer_breach(temperatureInC, lowerLimit, upperLimit)
  else:
    raise ValueError('wrong input data')
    
def validate_input(coolingType1,coolingType1):
    validate_coolingsize(coolingType1,temperatureInC1)
    validate_bms_parameter(coolingType1,temperatureInC1)
    
def validate_coolingsize(coolingType2,temperatureInC2):   
        if len(coolingType2)== 0: 
            raise ValueError('coolent type is missing')
        elif len(temperatureInC2) == 0:
            raise ValueError('temperature input is missing')
        

    
def validate_bms_parameter(coolingType3,temperatureInC3):
        for item in coolingType3:
            if not item.upper() in cooling_types.keys()
                raise KeyError('Given coolent type is invalid')
             

def send_to_controller(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')                             
  return True

def send_to_console(breachType):
  header = 0xfeed
  print(f'{header}, {breachType}')                             
  return True

def send_to_email(breachType):
   print(f"Hello: {email_recepient[breachType]['recepient']}\n Breach is: {breachType}")
   return True                             

alert_target_function_mapping = { "TO_CONTROLLER": send_to_controller, "TO_EMAIL" : send_to_email, "TO_CONSOLE" : send_to_console }

def check_and_alert(alertTarget, batteryChar, temperatureInC):
  breachType = classify_temperature_breach(batteryChar, temperatureInC)
  return alert_target_function_mapping[alertTarget](breachType)

