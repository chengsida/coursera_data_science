import MapReduce
import sys


mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
	# key: document identifier
	# value: document contents
	name = record[0]
	value ={}
	for i in range(0,5):
		if(name == 'a'):
			key = (record[1],i)
			mr.emit_intermediate(key,[name,record[2],record[3]])
		else:
			key=(i,record[2])
			mr.emit_intermediate(key,[name,record[1],record[3]])

def reducer(key, list_of_values):
	# key: word
	# value: list of occurrence counts
	total = 0
	A = {}
	B = {}
	for v in list_of_values:
		if(v[0]=='a'):
			A[v[1]]=v[2]
		else:
			B[v[1]]=v[2]
	for i in range(0,5):
		tempA = A.get(i)
		tempB = B.get(i)
		if(not tempA):
			A[i]=0
		if(not tempB):
			B[i]=0

	for i in range(0,5):
		total+=A[i]*B[i]
		
	mr.emit((key+(total,)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
