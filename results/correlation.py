import numpy as np
import scipy.stats
import pandas

data=pandas.read_csv('data.csv')
sim = [data.s1.tolist(),data.s2.tolist(),data.s3.tolist(),data.s4.tolist(),data.s5.tolist(),data.s6.tolist(),
       data.s7.tolist(),data.s8.tolist(),data.s9.tolist(),data.s10.tolist(),data.s11.tolist()]
rel = [data.r1.tolist(),data.r2.tolist(),data.r3.tolist(),data.r4.tolist(),data.r5.tolist(),data.r6.tolist(),
       data.r7.tolist(),data.r8.tolist(),data.r9.tolist(),data.r10.tolist(),data.r11.tolist()]
#x = np.arange(10, 20)
#print(x)
#y = np.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])
#print(y)
#r = np.corrcoef(rater1,rater2) #Pearson's r
#print(r)
#print(r[0, 1])

#x = np.arange(10, 20)
#y = np.array([2, 1, 4, 5, 8, 12, 18, 25, 96, 48])
#print("Pearson's r = ", scipy.stats.pearsonr(rater1, rater2))    # Pearson's r
#print(scipy.stats.spearmanr(rater1, rater2))   # Spearman's rho
#print(scipy.stats.kendalltau(rater1, rater2))  # Kendall's tau

print('Correlation value of Similarity scores')
for i in range(10):
    for j in range(i+1,11):
        print(i+1,'\t',j+1,'\t',scipy.stats.pearsonr(sim[i], sim[j])[0],'\t',     # Pearson's r
        scipy.stats.spearmanr(sim[i], sim[j])[0],'\t',   # Spearman's rho
        scipy.stats.kendalltau(sim[i], sim[j])[0])  # Kendall's tau

print('Correlation value of Relatedness scores')
for i in range(10):
    for j in range(i+1,11):
        print(i+1,'\t',j+1,'\t',scipy.stats.pearsonr(rel[i], rel[j])[0],'\t',     # Pearson's r
        scipy.stats.spearmanr(rel[i], rel[j])[0],'\t',   # Spearman's rho
        scipy.stats.kendalltau(rel[i], rel[j])[0])  # Kendall's tau

print('Standard deviation for each word-pairs (1418) / Avg,Min,Max')
sum,sumf,min,max=0,0,100,0
for i in range(1418):
    k = np.std([sim[j][i] for j in range(11)])
    aa = np.average([rel[j][i] for j in range(11)])
    print(i, '\t', k, '\t', aa, '\t', k / aa * 100, '%')
    sum+=k
    sumf+=k/aa*100
    if min>k:
        min=k
    if max<k:
        max=k
    #print(i+1,'\t',np.std([rel[j][i] for j in range(11)]))
print('Similarity\t',sum/1418,'\t',sumf/1418,'\t', min,'\t',max)

sum,sumf,min,max=0,0,100,0
for i in range(1418):
    k = np.std([rel[j][i] for j in range(11)])
    aa = np.average([rel[j][i] for j in range(11)])
    #print([rel[j][i] for j in range(11)])
    print(i,'\t',k,'\t',aa,'\t',k/aa*100,'%')
    sumf+=k/aa*100
    sum+=k
    if min>k:
        min=k
    if max<k:
        max=k
    #print(i+1,'\t',np.std([rel[j][i] for j in range(11)]))
print('Relatednes\t',sum/1418,'\t',sumf/1418,'\t', min,'\t',max)

#You could also use dot notation for the Spearman and Kendall coefficients:
#print(scipy.stats.spearmanr(rater1, rater2).correlation)   # Spearman's rho
#print(scipy.stats.kendalltau(rater1, rater2).correlation)  # Kendall's tau

#r, p = scipy.stats.pearsonr(rater1, rater2)
#print(r)

#xyz = np.array([rater1,rater2,rater3,rater4,rater5,rater6,rater7,rater8,rater9,rater10,rater11])
#print(np.corrcoef(xyz))
#corr_matrix, p_matrix = scipy.stats.spearmanr(xyz, axis=1)
#print(corr_matrix)
#print(p_matrix)

#print("Linear Regression results")
#xy=np.array([rater1,rater2])
#result = scipy.stats.linregress(rater1, rater2)
#result = scipy.stats.linregress(xy)
#result = scipy.stats.linregress(xy.transpose())
#print(result.slope)
#print(result.intercept)
#print(result.rvalue)
#print(result.pvalue)
#print(result.stderr)

#The correlation coefficient (Pearson's r)
#The p-value

#The correlation coefficient (Spearman's r)
#The p-value
