'''
Created on Sep 19, 2017

@author: anchit
'''
import time
    
#Generating Random number through time stamp of system.
class RandomNumberGenration():
   
    #Generation of mid range
    def generatingmidrange(self,minrange,maxrange):
        #Calculating the mid range of range given.
        midrange=(minrange+maxrange)/2
        return midrange
    
    #Generation of random number
    def generating_random_number(self):
        #milliseconds calculation of system time.
        millseconds =(round(time.time()))
        
        #Converting milliseconds to integer type.
        millseconds=int(millseconds)
        
        #Calculating last 2 digit of time in millisecond
        mills=millseconds%100
        
        #For 73% biased to higher number
        if (mills<73):
            rangemid=self.generatingmidrange(rangemin, rangemax)
            newmills=mills%rangemid
            randomnumber=rangemid + newmills
            if randomnumber==rangemid:
                return rangemax
             
            else:   
                return randomnumber
       
        #For 27% biased to lower number     
        else:
            rangemid=self.generatingmidrange(rangemin, rangemax)
            randomnumber=mills%rangemid
            randomnumber=rangemid-randomnumber
            if randomnumber==0:
                return rangemin+1
             
            else:   
                return randomnumber
            
            
randomnumbergenerator=RandomNumberGenration()
rangemin = int(raw_input("What is your minrange ? "))
rangemax = int(raw_input("What is your maxrange ? "))
print randomnumbergenerator.generating_random_number()