import sys
import json

def buildDictionary(file):
	afinnfile = open(file)
	scores = {}
	for line in afinnfile:
		term, score = line.split("\t")
		scores[term] = int(score)
	return scores

def lines(fp):
    print str(len(fp.readlines()))

def loadJson(file,dictionary):
	lines = open(file)
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
			print (count)







def main():
  sent_file = sys.argv[1]
  tweet_file = sys.argv[2]
  dictionaryToCalculate = buildDictionary(sent_file)
  tweets = loadJson(tweet_file,dictionaryToCalculate)



if __name__ == '__main__':
    main()
