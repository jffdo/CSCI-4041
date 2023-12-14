import traceback
import heapq

#huffman_encode: Takes in a single String input_string, which is
# the string to be encoded.  Computes the optimal binary encoding
# of the string and encodes it, returning a String of 0s and 1s.
# This is not an actual Python binary string, just a normal String
# that happens to contain only 0s and 1s.
def huffman_encode(input_string):
    # get number of characters for each character in string
    numChars = len(input_string)
    charDict = {}
    for letter in input_string:
        if letter in charDict.keys():
            charDict[letter] += 1
        else:
            charDict[letter] = 1
    minQ = []
    for item in charDict.items(): # (occurances, letter, left, right)
        minQ.append((item[1], item[0], None, None))
    
    # build heap of character counts
    heapq.heapify(minQ)
    while(len(minQ) > 1):
        low = heapq.heappop(minQ)
        low2 = heapq.heappop(minQ)
        super_ch = low[1] + low2[1]
        super_freq = low[0] + low2[0]
        super_node = (super_freq, super_ch, low, low2)
        heapq.heappush(minQ, super_node)

    # encoding, each encoding is stored in encodedDict 
    encodedDict = {}
    for key in charDict.keys():
        code = ""
        node = minQ[0]
        while(key != node[1]):
            if (node[2][1].find(key) >= 0):
                node = node[2]
                code = code + "0"
            elif (node[3][1].find(key) >= 0):
                node = node[3]
                code = code + "1"
        encodedDict[key] = code

    # Get encoding for each letter using encodedDict
    output = ""
    for letter in input_string:
        output += encodedDict[letter]
    return output
    


#  DO NOT EDIT BELOW THIS LINE


if __name__ == '__main__':
    tests = ['message0.txt','message1.txt','message2.txt','message3.txt',
             'message4.txt','message5.txt']
    correct = ['message0encoded.txt','message1encoded.txt',
               'message2encoded.txt','message3encoded.txt',
               'message4encoded.txt','message5encoded.txt']


    #Run test cases, check whether encoding correct
    count = 0

    try:
        for i in range(len(tests)):
            ("\n---------------------------------------\n")
            print("TEST #",i+1)
            print("Reading message from:",tests[i])
            fp = open(tests[i])
            message = fp.read()
            fp.close()
            print("Reading encoded message from:",correct[i])
            fp2 = open(correct[i])
            encoded = fp2.read()
            fp2.close()
            output = huffman_encode(message)
            if i < 5:
                print("Running: huffman_encode on '"+message+"'\n")
                print("Expected:",encoded,"\nGot     :",output)
            assert encoded == output, "Encoding incorrect!"
            print("Test Passed!\n")
            count += 1
    except AssertionError as e:
        print("\nFAIL: ",e)
    except Exception:
        print("\nFAIL: ",traceback.format_exc())


    print(count,"out of",len(tests),"tests passed.")


