#!/usr/bin/python
# Start time - 12:10 am
# end time - 1:00 am
# status - complete? need to check solution
# solution - O(n) time, O(1) mem

def get_seq(a):
    class Answer():
        def __init__(self, start_index=0, end_index=0, ans_sum=0):
            self.__start_index = start_index
            self.__end_index = end_index
            self.__sum = ans_sum
        def __str__(self):
            return '%s %s %s' % (str(self.__start_index), str(self.__end_index), str(self.__sum))
        #TODO: use properties
        def set_start(self, start_index):
            self.__start_index = start_index
        def set_end(self, end_index):
            self.__end_index = end_index
        def set_sum(self, ans_sum):
            self.__sum = ans_sum
        def get_start(self):
            return self.__start_index
        def get_end(self):
            return self.__end_index
        def get_sum(self):
            return self.__sum
        def update(self, start_index, end_index, ans_sum):
            self.__start_index = start_index
            self.__end_index = end_index
            self.__sum = ans_sum

    # Basically you just need to find the longest sequence where the sum doesn't go negative
    tmp_sum = 0
    start_index = 0
    end_index = 0

    ans = Answer()
    for i in xrange(len(a)):
        print i
        print ans
        if tmp_sum + a[i] >= 0:
            print 'yay' 
            tmp_sum += a[i]
            end_index = i
            print 'tmp sum: %s' % tmp_sum
        else:
            # This is the negative sum case or the final index case
            print 'nay'
            #save ans and reset
            if tmp_sum > ans.get_sum():
                ans.update(start_index, end_index, tmp_sum)
                
                start_index = i+1
                end_index = i+1
                tmp_sum = 0
                print 'sum: %s, array: %s' % (ans.get_sum(), a[ans.get_start():ans.get_end()+1])

    if tmp_sum > ans.get_sum():
        ans.update(start_index, end_index, tmp_sum)

    print 'sum: %s, array: %s' % (ans.get_sum(), a[ans.get_start():ans.get_end()+1])

array = [2, -8, 3, -2, 4, -10, 100]
get_seq(array)
