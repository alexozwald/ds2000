# Data sources
original [spreadsheet](https://docs.google.com/spreadsheets/d/1wZhPLMCHKJvwOkP4juclhjFgqIY8fQFMemwKL2c64vk/edit#gid=0) from Ryan

https://www.ssa.gov/OP_Home/ssact/title19/1927.htm
https://www.medicaid.gov/medicaid/prescription-drugs/medicaid-drug-rebate-program/index.html
https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/index.html
https://data.medicaid.gov/datasets?sort=modified -> Categories -> "State Drug Uitlization"
https://data.medicaid.gov/datasets?theme[0]=State%20Drug%20Utilization&sort=modified
https://www.fda.gov/drugs/drug-approvals-and-databases/national-drug-code-directory



# definitions
[source](https://www.fda.gov/drugs/drug-approvals-and-databases/ndc-product-file-definitions)

# csv data structures

## state utilizations
0. Utilization Type
1. State
2. Labeler Code
3. Product Code
4. Package Size
5. Year
6. Quarter
7. Product Name
8. Suppression Used
9. Units Reimbursed
10. Number of Prescriptions
11. Total Amount Reimbursed
12. Medicaid Amount Reimbursed
13. Non Medicaid Amount Reimbursed
14. Quarter Begin
15. Quarter Begin Date
16. Latitude
17. Longitude
18. Location
19. NDC


## product.txt
0. PRODUCTID
1. PRODUCTNDC
2. PRODUCTTYPENAME
3. PROPRIETARYNAME
4. PROPRIETARYNAMESUFFIX
5. NONPROPRIETARYNAME
6. DOSAGEFORMNAME
7. ROUTENAME
8. STARTMARKETINGDATE
9. ENDMARKETINGDATE
10. MARKETINGCATEGORYNAME
11. APPLICATIONNUMBER
12. LABELERNAME
13. SUBSTANCENAME
14. ACTIVE_NUMERATOR_STRENGTH
15. ACTIVE_INGRED_UNIT
16. PHARM_CLASSES
17. DEASCHEDULE
18. NDC_EXCLUDE_FLAG
19. LISTING_RECORD_CERTIFIED_THROUGH


## package.txt
0. PRODUCTID
1. PRODUCTNDC
2. NDCPACKAGECODE
3. PACKAGEDESCRIPTION
4. STARTMARKETINGDATE
5. ENDMARKETINGDATE
6. NDC_EXCLUDE_FLAG
7. SAMPLE_PACKAGE


## download links in case we fuck up
[state-drug-utilization-data-1991.cnf4-jwwr.csv](https://download.medicaid.gov/data/state-drug-utilization-data-1991.cnf4-jwwr.csv)
[state-drug-utilization-data-1992.agzs-hwsn.csv](https://download.medicaid.gov/data/state-drug-utilization-data-1992.agzs-hwsn.csv)
[state-drug-utilization-data-1993.iu8s-z84j.csv](https://download.medicaid.gov/data/state-drug-utilization-data-1993.iu8s-z84j.csv)
[state-drug-utilization-data-1994.8uti-96dw.csv](https://download.medicaid.gov/data/state-drug-utilization-data-1994.8uti-96dw.csv)
[state-drug-utilization-data-1995.v83u-wwk3.csv](https://download.medicaid.gov/data/state-drug-utilization-data-1995.v83u-wwk3.csv)
[state-drug-utilization-data-1996.jqjw-uby8.csv](https://download.medicaid.gov/data/state-drug-utilization-data-1996.jqjw-uby8.csv)
[state-drug-utilization-data-1997.c7wf-ku3w.csv](https://download.medicaid.gov/data/state-drug-utilization-data-1997.c7wf-ku3w.csv)
[state-drug-utilization-data-1998.ykva-ug36.csv](https://download.medicaid.gov/data/state-drug-utilization-data-1998.ykva-ug36.csv)
[state-drug-utilization-data-1999.vhg8-v7wa.csv](https://download.medicaid.gov/data/state-drug-utilization-data-1999.vhg8-v7wa.csv)
[state-drug-utilization-data-2000.78qv-c4cn.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2000.78qv-c4cn.csv)
[state-drug-utilization-data-2001.t5ct-xf3k.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2001.t5ct-xf3k.csv)
[state-drug-utilization-data-2002.5jcx-2xey.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2002.5jcx-2xey.csv)
[state-drug-utilization-data-2003.66gr-qxnr.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2003.66gr-qxnr.csv)
[state-drug-utilization-data-2004.rn2y-fgjb.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2004.rn2y-fgjb.csv)
[state-drug-utilization-data-2005.ezjn-vqh8.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2005.ezjn-vqh8.csv)
[state-drug-utilization-data-2006.e7is-4a3j.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2006.e7is-4a3j.csv)
[state-drug-utilization-data-2007.q947-frj2.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2007.q947-frj2.csv)
[state-drug-utilization-data-2008.ny8j-2ymd.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2008.ny8j-2ymd.csv)
[state-drug-utilization-data-2009.fhmx-iqs3.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2009.fhmx-iqs3.csv)
[state-drug-utilization-data-2010.mmgn-kvy5.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2010.mmgn-kvy5.csv)
[state-drug-utilization-data-2011.ra84-ffhc.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2011.ra84-ffhc.csv)
[state-drug-utilization-data-2012.yi2j-kk5z.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2012.yi2j-kk5z.csv)
[state-drug-utilization-data-2013.rkct-3tm8.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2013.rkct-3tm8.csv)
[state-drug-utilization-data-2014.955u-9h9g.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2014.955u-9h9g.csv)
[state-drug-utilization-data-2015.ju2h-vcgs.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2015.ju2h-vcgs.csv)
[state-drug-utilization-data-2016.3v6v-qk5s.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2016.3v6v-qk5s.csv)
[state-drug-utilization-data-2017.3v5r-x5x9.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2017.3v5r-x5x9.csv)
[state-drug-utilization-data-2018.e5ds-i36p.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2018.e5ds-i36p.csv)
[state-drug-utilization-data-2019.qnsz-yp89.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2019.qnsz-yp89.csv)
[state-drug-utilization-data-2020.va5y-jhsv.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2020.va5y-jhsv.csv)
[state-drug-utilization-data-2021.8g5u-3qy8.csv](https://download.medicaid.gov/data/state-drug-utilization-data-2021.8g5u-3qy8.csv)
[ndctext.zip](https://www.accessdata.fda.gov/cder/ndctext.zip)

