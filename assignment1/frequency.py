import sys
import json



def computeFrequence(file):
	lines = open(file)
	countPairs = {}
	for line in lines:
		tweet = json.loads(line)
		strrr = tweet.get(u'text')
		if(strrr):
			words = strrr.split()
			for word in words:
				temp = countPairs.get(word)
				if(temp):
					countPairs[word]=countPairs[word]+1
				else:
					countPairs[word]=1
	return countPairs




def main():
	tweetFile = sys.argv[1]
	pairs = computeFrequence(tweetFile)
	for d,x in pairs.items():
		print d+" "+str(x)


if __name__ == '__main__':
	main()
