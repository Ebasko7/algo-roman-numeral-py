def to_roman(num):
  output = ''
  romanNumeralToArabic = {
    'I': 1,
    'IV': 4,
    'V': 5,
    'X': 10,
    'XL': 40,
    'L': 50,
    'XC': 90,
    'C': 100,
    'CD': 400,
    'D': 500,
    'CM': 900,
    'M': 1000
  } 
  romanNumeralPriorityOrder = ['M','CM','D','CD','C','XC','L','XL','X','V','IV','I']
  for letter in romanNumeralPriorityOrder:
    timesDivisible =  num //romanNumeralToArabic[letter]
    if (timesDivisible > 0):
        output += (letter * timesDivisible)
        num -= (romanNumeralToArabic[letter] * timesDivisible)
      
  return output 

