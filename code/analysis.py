"""Reproduces the main counts and exploratory tests reported in the manuscript.
Usage: python code/analysis.py   (run from the repository root)"""
import re, pandas as pd
from scipy import stats
rec = pd.read_csv('data/records_682_labels.csv')
def ev(s):
    s = str(s).lower().strip()
    for k, p in [('conc','^conceptual'),('sim','^simulation'),('poc','^technical'),('retro','^retrospective'),
                 ('pro','^prospective'),('rw','^real.world|^deployment'),('ext','^external')]:
        if re.search(p, s): return k
    return 'na'
rec['e'] = rec.evidence.map(ev)
rec['d'] = rec.dtl.astype(str).str.extract(r'DTL-(\d)')[0].astype(float)
rec['y'] = pd.to_numeric(rec.year, errors='coerce')
rec['gap'] = (rec.d >= 3) & rec.e.isin(['conc','sim'])
def summary(d, label):
    n=len(d); a=d.d>=3
    print(f"{label}: n={n}, DTL>=3={a.sum()} ({100*a.mean():.1f}%), conceptual={(d.e=='conc').sum()} ({100*(d.e=='conc').mean():.1f}%), "
          f"clinical-level={d.e.isin(['pro','rw','ext']).sum()}, gap={d.gap.sum()} ({100*d.gap.mean():.1f}%)")
summary(rec,'all'); summary(rec[rec.primary_Y_N_U=='Y'],'primary'); summary(rec[rec.primary_Y_N_U=='N'],'non-primary')
p = rec[(rec.primary_Y_N_U=='Y')].dropna(subset=['y'])
g = pd.cut(p.y,[0,2022,2023,2024,2030],labels=['<=2022','2023','2024','2025-26'])
tab = pd.crosstab(g,p.gap); print(tab); print('chi2 p=',stats.chi2_contingency(tab)[1]); print('spearman',stats.spearmanr(p.y,p.gap))
v = pd.read_csv('validation/validation_100_paired_labels.csv').dropna(subset=['ai_dtl','my_dtl'])
a=v.ai_dtl>=3; b=v.my_dtl>=3; n10=int((a&~b).sum()); n01=int((~a&b).sum())
print('McNemar exact: AI-only',n10,'second-only',n01,'p=',stats.binomtest(n10,n10+n01,0.5).pvalue)
