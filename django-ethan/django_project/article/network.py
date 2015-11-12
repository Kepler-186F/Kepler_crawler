
#####MisJudgement Adapt to Truth
def MisJudgement_Adapt_To_Truth(ListInput,MisJudgeAdaptRate):
	##ListInput is [A1_L12,A1_L12Return,A1_L21,A1_L21Return,A2_L12,A2_L12Return,A2_L21,A2_L21Return]
	A1_L12=ListInput[1]
	A1_L21=ListInput[3]
	A2_L12=ListInput[5]
	A2_L21=ListInput[7]
	
	A1_L12Return=A1_L12
	if(A1_L21>=A2_L21):
		A1_L21Return=A1_L21-(A1_L21-A2_L21)*MisJudgeAdaptRate
	else:
		A1_L21Return=A1_L21+(A2_L21-A1_L21)*MisJudgeAdaptRate
	
	A2_L21Return=A2_L21
	if(A2_L12>=A1_L12):
		A2_L12Return=A2_L12-(A2_L12-A1_L12)*MisJudgeAdaptRate
	else:
		A2_L12Return=A2_L12+(A1_L12-A2_L12)*MisJudgeAdaptRate
	print "A1 Perspective A1-A2: %f ==> %f"%(A1_L12,A1_L12Return)
	print "A1 Perspective A2-A1: %f ==> %f"%(A1_L21,A1_L21Return)
	print "A2 Perspective A1-A2: %f ==> %f"%(A2_L12,A2_L12Return)
	print "A2 Perspective A2-A1: %f ==> %f"%(A2_L21,A2_L21Return)
	print "\n\n"
	
	return [A1_L12,A1_L12Return,A1_L21,A1_L21Return,A2_L12,A2_L12Return,A2_L21,A2_L21Return]


def PsyTruth_Adapt_To_Truth(ListInput,PsyTruthAdaptRate):
	##ListInput is [A1_L12,A1_L21,A2_L12,A2_L21]
	A1_L12=ListInput[0]
	A1_L12Return=ListInput[1]
	A1_L21=ListInput[2]
	A1_L21Return=ListInput[3]
	A2_L12=ListInput[4]
	A2_L12Return=ListInput[5]
	A2_L21=ListInput[6]
	A2_L21Return=ListInput[7]
	
	A1_L21RReturn=A1_L21Return
	A2_L12RReturn=A2_L12Return
    
	A1_L12RReturn=A1_L12Return-(A1_L21-A1_L21Return)*PsyTruthAdaptRate
	A2_L21RReturn=A2_L21Return-(A2_L12-A2_L12Return)*PsyTruthAdaptRate
	print "A1 Perspective A1-A2: %f ==> %f"%(A1_L12Return,A1_L12RReturn)
	print "A1 Perspective A2-A1: %f ==> %f"%(A1_L21Return,A1_L21RReturn)
	print "A2 Perspective A1-A2: %f ==> %f"%(A2_L12Return,A2_L12RReturn)
	print "A2 Perspective A2-A1: %f ==> %f"%(A2_L21Return,A2_L21RReturn)
	print "\n\n"
	return [A1_L12Return,A1_L12RReturn,A1_L21Return,A1_L21RReturn,A2_L12Return,A2_L12RReturn,A2_L21Return,A2_L21RReturn]

