import sys
import json



def buildDictionary(file):
	afinnfile = open(file)
	scores = {}
	for line in afinnfile:
		term, score = line.split("\t")
		scores[term] = int(score)
	return scores



def loadJson(file,dictionary):
	lines = open(file)
	newTerm = {}
	for line in lines:
		tweet = json.loads(line)
		strrr = tweet.get(u'text')
		if(strrr):                 
			#print(strrr)
			count =0
			words = strrr.split()
			for word in words:       
				pivot = dictionary.get(word)
				if(pivot):
					count += pivot
			for n_word in words:
				n_pivot = dictionary.get(n_word)
				if(not n_pivot):
					temp = newTerm.get(n_word)
					if(temp):
						newTerm[n_word]=newTerm[n_word]+count
					else:
						newTerm[n_word]=count
	return newTerm
				




def main():
    sent_file = sys.argv[1]
    tweet_file = sys.argv[2]
    dictionary = buildDictionary(sent_file)
    newTerm  = loadJson(tweet_file,dictionary)
    for d, x in newTerm.items():
    	print d+" "+str(x)


   
if __name__ == '__main__':
    main()
