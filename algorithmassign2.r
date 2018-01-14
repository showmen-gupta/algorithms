rm(list=ls())		

library("linprog")	

#maximize	f(x)	=	(4p1	+	4p2	+	7p3)	
maximum<-	c(4,4,7)	
names(maximum)	<-	c("pro1",	"pro2",	"pro3")	
#	subject	to	
#	p1	+	2p2	+	8p3	<=	100	
#	7p1	+	p2	+	4p3	<=	110	
#	4p1	+	7p2	+	p3	<=	100	
#	p1,	p2,	p3	>=0	

hours	<-	c(100,	110,	101)		
names(hours)	<-	c("M1",	"M2",	"M3")		
matrixGen	<-	rbind(	c(	1,	2,	8	),	
               c(	7,	1,	4	),		
               c(	4,	7,	1	))	
solveLP(maximum,	hours,	matrixGen,	TRUE)
