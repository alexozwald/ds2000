**DS 2001:  Final Project**

*Tracking the Opioid Crisis*

Team Members:  Alex Oswald, Thy Nguyen

**Idea:**

We hope to explore the growth of opioid distribution in Massachusetts over time, and link it to different markers in the fight against American opioid mass distribution to see how widespread opioid overprescription has become here. We need granular data to best explore this topic because of its complexity and obscured growth over time.  We plan to use two primary data sources to explore this...

1.  As part of a legal battle, the [Washington Post](https://www.washingtonpost.com/graphics/2019/investigations/dea-pain-pill-database/) obtained a copy of a database maintained by the Drug Enforcement Administration (DEA) that tracks the sale of every different pain pill from distributors to pharmacies by month with the amount of pills distributed between 2006--2012.
2.  We are also exploring the historical Medicaid State Drug Utilization Data (SDUD) published for [Massachusetts](https://www.medicaid.gov/medicaid/prescription-drugs/state-drug-utilization-data/index.html)between 1991--2021 to get a more expansive picture of how much it has grown outside of the more limited timeline of the Washington Post data.

Databases:     *Washington Post: DEA Pain Pills Database: Massachusetts (statewide),*

*            Medicaid State Drug Utilization Data,*

*            FDA National Drug Code Directory*

Division of Labor:

-   Data Collection:          Alex + Thy
-   Data Cleaning:            *not applicable*
-   Data refinement & processing:           Thy

*As our research progresses...*

o   Analysis + Enrichment:           Alex

o   Modelling current status/affairs:         Thy

-   Data Extraction:          Alex + Thy
-   Data Viz:         Alex
-   Impact assessment / writeup: Thy + Alex

Analysis Techniques

We plan to analyze this data by reading in CSVs regarding Massachusetts opioid distribution as well as Massachusetts prescription information by year (31 WaPo, 1 SDUD, and 1 NDC csv).  We expect to calculate the cumulative dose of each drug in different counties and pharmacies, and compare that corroborate that information with the relative amount of Medicaid pain prescriptions written in that area.  This will directly help us reach our research goal.

Interpretive Techniques

We plan to use Matplotlib's *pyplot* library to analyze the growth of the amount of pills sold and distributed compared to each part of the state over time.  We can correlate this with different markers of the opioid epidemic in Massachusetts public policy and more generally as indicated by the [CDC](https://www.fda.gov/media/126835/download).  This data has the potential to open the eyes of Massachusetts lawmakers to the ongoing crisis the state is facing, and that despite increased awareness the opioid crisis has not been stopped yet.

Washington Post Data Headers:

REPORTER_DEA_NO,REPORTER_BUS_ACT**,REPORTER_NAME,**REPORTER_ADDL_CO_INFO,REPORTER_ADDRESS1,REPORTER_ADDRESS2,REPORTER_CITY,REPORTER_STATE,REPORTER_ZIP,REPORTER_COUNTY,BUYER_DEA_NO,BUYER_BUS_ACT,BUYER_NAME,BUYER_ADDL_CO_INFO,BUYER_ADDRESS1,BUYER_ADDRESS2,**BUYER_CITY**,BUYER_STATE,**BUYER_ZIP**,**BUYER_COUNTY**,TRANSACTION_CODE,**DRUG_CODE**,NDC_NO,**DRUG_NAME**,**QUANTITY**,UNIT,ACTION_INDICATOR,ORDER_FORM_NO,CORRECTION_NO,**STRENGTH**,TRANSACTION_DATE,CALC_BASE_WT_IN_GM,**DOSAGE_UNIT**,TRANSACTION_ID,Product_Name,Ingredient_Name,Measure,MME_Conversion_Factor,Combined_Labeler_Name,Reporter_family,dos_str,MME

Medicaid SDUD Headers* (FDA NDC links drug & labeler codes)*

utilization_type,state,labeler_code,product_code,package_size,year,quarter,product_name,suppression_used,units_reimbursed,number_of_prescriptions,total_amount_reimbursed,medicaid_amount_reimbursed,non_medicaid_amount_reimbursed,quarter_begin,quarter_begin_date,latitude,longitude,location,ndc