# Healthcare digital twin research: claimed maturity vs demonstrated evidence

Data and code for the manuscript *Claimed Maturity versus Demonstrated Evidence in Healthcare Digital Twin Research: A Meta-Research Study with Validated LLM-Assisted Classification, 2018-2026* (Umut Saray).

## Contents
- `data/records_682_labels.csv` - the 682 included records with AI labels (claimed Digital Twin Level, strongest evidence, domain) and the primary / non-primary classification (Y = primary study, N = non-primary, U = unknown, no abstract). Abstracts and full texts are not redistributed; use the DOI.
- `data/primary_classification_682.csv` - how each record was classified as primary or non-primary (keyword rule, AI reading, or second coder).
- `data/matrix_primary.json` - the DTL x evidence matrix for primary studies (Figure 3).
- `validation/validation_100_paired_labels.csv` - the 100-record stratified validation sample: AI labels, second-coder labels (checked by the first author) and primary flag. Sampling seed 20261108.
- `code/analysis.py` - reproduces the main counts, the year-group test and the McNemar test.
- `code/clf.py` (keyword rule), `code/fig1.py`, `code/fig3.py` - classification rule and figure code.
- `figures/` - Figures 1-3 (600 DPI).

## Notes
- All labels outside the 100-record validation sample are AI labels and have not been checked by a human. Treat counts as exploratory.
- Evidence categories are read from the first category named in each label.
- Reproduce: `pip install pandas scipy` then `python code/analysis.py` from the repository root.

## Not included
Publisher full texts (PDF / XML) are not included for copyright reasons.

## Licence
- Data (`data/` and `validation/`): [CC BY 4.0](LICENSES/CC-BY-4.0.txt).
- Code (`code/`): [MIT](LICENSES/MIT.txt).

Copyright (c) 2026 Umut Saray. See [licensing and attribution details](LICENSE.md).
