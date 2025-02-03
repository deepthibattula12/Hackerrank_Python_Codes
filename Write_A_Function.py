if __name__ =='__main__':
    def is_leap(year):
        leap = True
        if(year==2100):
            return False
        elif(year%4==0):
            return leap
        else:
            return False
