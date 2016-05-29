import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    book = record[0]
    line = record[1]
    words = line.split()
    for word in words :
      mr.emit_intermediate(word, book)

def reducer(key, list_of_values):
    ans = []
    for v in list_of_values:
      ans.append(v);

    ans = list(set(ans))
  
    mr.emit((key,ans))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)