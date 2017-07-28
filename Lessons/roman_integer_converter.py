def isvalid_roman(text):
    if 'MMMMM' in text:
        return False
 
    l = len(text)
 
    invalid4 = ['IIII','XXXX','CCCC']
    for i in xrange(l-3):
        if text[i:i+4] in invalid4:
            return False
 
    invalid2 = ['VV','VX','VL','VC','VD','VM','IL','IC','ID','IM','XD','XM',
                'LL','LC','LD','LD','DD','DM']
    for i in xrange(l-1):
        if text[i:i+2] in invalid2:
            return False
 
    invalid3 = ['VIV','VIX','IXV','IIV','IVI','IIX','IXI','IXX','IXL','IXC',
                'XXL','XLX','XXC','XCX','XCC','XCD','XCM',
                'LXL','LXC','XCL','CCD','CDC','CCM','CMC','CMM',
                'DCD','DCM','CMD']
    for i in xrange(l-2):
        if text[i:i+3] in invalid3:
            return False
 
    return True
   
 
def toroman(text):
    if int(text) >= 5000 or int(text) < 1:
        return "Invalid input"
 
    text = "{0:0>4}".format(text)
    ones = int(text[3])
    tens = int(text[2])
    huns = int(text[1])
    mils = int(text[0])
   
    if mils > 0:
        result = 'M'*mils
    else:
        result = ''
   
   
    if huns == 4:
        result += 'CD'
    elif huns >=5 and huns <=8:
        result += ('D'+'C'*(huns-5))
    elif huns <=3 and huns>0:
        result+= 'C'*huns
    elif huns==9:
        result+='CM'
    else:
        pass
 
   
    if tens == 4:
        result+= 'XL'
    elif tens >=5 and tens<=8:
        result+= 'L'+'X'*(tens-5)
    elif tens <=3 and tens>0:
        result+='X'*tens
    elif tens ==9:
        result+='XC'
    else:
        pass
 
   
    if ones==4:
        result+='IV'
    elif ones >= 5 and ones <=8:
        result+= 'V' + 'I'*(ones-5)
    elif ones<=3 and ones>0:
        result+='I'*ones
    elif ones == 9:
        result+= 'IX'
    else:
        pass
 
    return result
 
 
def toint(roman):
    if not isvalid_roman(roman):
        return "Invalid input"
    else:
        roman_hash = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        num = 0
        for numerals in roman:
            if numerals in roman_hash:
                num += roman_hash[numerals]
            else:
                return "Invalid input"
 
        if 'IV' in roman :
            num -= 2
        if 'IX' in roman :
            num-=2
        if 'XL' in roman :
            num-=20
        if 'XC' in roman :
            num-=20
        if 'CD' in roman :
            num-=200
        if 'CM' in roman :
            num-=200
 
        return num
 
if  __name__ == "__main__":
    while True:
        text = raw_input("Enter a number or roman numeral to convert: ")
        if text.isalpha():
            print toint(text)
        elif text.isdigit() :
            print toroman(text)
        else :
            print "Invalid input"
        response = raw_input("Do you want to continue?(Y/N)")
        if response =='N' or response =='n':
            break
