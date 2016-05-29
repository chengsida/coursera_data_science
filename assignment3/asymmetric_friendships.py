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
    
    mr.emit_intermediate((record[0],record[1]),1)
    mr.emit_intermediate((record[1],record[0]),2)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence count
  
   if(len(list_of_values)<2):
      mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)