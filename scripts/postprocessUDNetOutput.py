# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 10:39:57 2016

@author: christokirov
"""

import codecs
import re
import string
import sys


#read filenames from commandline
wordlistfile = sys.argv[1]
netoutputfile = sys.argv[2]
outputfile = sys.argv[3]


#load UD2UM lookup
ud2um = {}
fin = codecs.open('UD-UniMorph.tsv','rb','utf-8')
for line in fin:
    try:
        parts = line.strip().split('\t')
        ud2um[parts[0]] = parts[1]
    except:
        print line
fin.close()

#load original input file
fin = codecs.open(wordlistfile,'rb','utf-8')
#read in network output file
fin2 = codecs.open(netoutputfile,'rb','utf-8')
#set up new output file
fout = codecs.open(outputfile,'wb','utf-8')

#postprocess
for line,line2 in zip(fin,fin2):
	inflection = line.strip()
	try:
		parts = line2.strip().split('|')
		lemma = parts[0].strip().replace(' ','').replace('_','')
		features = parts[1].strip().split()
		nufeatures = []
		for f in features:
			try:
				nufeatures.append(ud2um[f])
			except:
				pass
		if len(nufeatures) == 0:
			raise
		nufeatures = ';'.join(nufeatures)
		fout.write(inflection + '\t' + lemma + '\t' + nufeatures + '\n')
	except:
		fout.write(inflection + '\t' + 'MISS' + '\t' + 'MISS' + '\n')

#clean up
fin.close()
fin2.close
fout.close()




