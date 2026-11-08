import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt, numpy as np, json
d=json.load(open('data/matrix_primary.json'))
plt.rcParams['font.family']='DejaVu Sans'
rows=['DTL-0','DTL-1','DTL-2','DTL-3','DTL-4','DTL-5','Unclassified']
cols=['Conceptual','Simulation','Tech. PoC','Retrospective','Prospective\npilot','Real-world\ndeployment','External\nvalidation','Unclassified']
M=np.array(d['M']); assert M.sum()==204
fig,ax=plt.subplots(figsize=(9,5.6))
ax.imshow(np.log1p(M),cmap='Blues',aspect='auto')
for i in range(M.shape[0]):
    for j in range(M.shape[1]):
        ax.text(j,i,M[i,j],ha='center',va='center',fontsize=10,color='white' if np.log1p(M[i,j])>3.0 else '#1b2a3a')
ax.set_xticks(range(len(cols))); ax.set_xticklabels(cols,fontsize=8.5); ax.set_yticks(range(len(rows)))
ax.set_yticklabels([f'{r}  (n={M[i].sum()})' for i,r in enumerate(rows)],fontsize=9)
ax.xaxis.tick_top(); ax.set_xlabel('Strongest evidence demonstrated  →  (more clinical)',fontsize=9,labelpad=8); ax.xaxis.set_label_position('top')
ax.set_ylabel('Maturity level claimed',fontsize=9)
ax.axvline(3.5,color='#c0392b',lw=1.5,ls='--'); ax.axvline(6.5,color='#c0392b',lw=1.5,ls='--')
ax.text(5,7.05,'Clinical-level evidence\n(n = 14)',ha='center',va='top',fontsize=8,color='#c0392b')
for s in ax.spines.values(): s.set_visible(False)
fig.text(0.01,0.01,'Primary studies only (n = 204 of 682). Colour on log scale; cells show study counts. AI labels; not human-validated (see Section 4.14).',fontsize=7,color='#555')
fig.tight_layout(rect=(0,0.03,1,1)); fig.savefig('figures/Fig3_DTL_x_Evidence_primary_only.png',dpi=600,facecolor='white'); plt.close()
