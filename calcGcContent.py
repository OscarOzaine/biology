from matplotlib import pyplot

def	calcGcContent(seq, winSize=10):
	gcValues = []

	for i in range(len(seq) - winSize):

		subSeq = seq[i:i+winSize]
		numGc = subSeq.count('G') + subSeq.count('C')
		value = numGc / float(winSize)
		gcValues.append(value)

	return gcValues

dnaSeq = 'AGCTCGCTCGCTGCGTATAAAATCGCATCGCGCGCAGC'

gcResults = calcGcContent(dnaSeq)
pyplot.plot(gcResults)
pyplot.show()
