import sys

def clean_text(corpus_name):
   with open(corpus_name, 'r', encoding='UTF-8') as fileinput:
      with open(corpus_name.split('.')[0] + '_cleaned.' + corpus_name.split('.')[1], 'w', encoding='UTF-8') as fileoutput:
         for line in fileinput:
            line = line.lower()
            line = ''.join([c for c in line if c.isalpha() or c==' ' or c=='\n'])
            fileoutput.write(line)


if __name__ == '__main__':
   clean_text(sys.argv[1])
