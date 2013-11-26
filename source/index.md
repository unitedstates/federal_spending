An unofficial guide to the data in USASpending.gov and other spending data systems, provided by the [Sunlight Foundation](http://sunlightfoundation.com) and other organizations.

## Introduction

USASpending.gov is the public facing source for grants and contracts data over $25,000. However, this consitutes far less than 100% of government spending. 

What USASpending does NOT include:
*Salaries
*Retirement and other benefits data
*Certain costs related to the general operations of the government (building leases, etc)
*Payments to individuals
*Medicare/Medicaid Data



## Background

###FAADS/FAADS-PLUS

The Federal Assistance Awards Data System (FAADS) is the central collection of information on federal grants, cooperative agreements, loans, loan guarantees, insurance, direct payments for a specified use and direct payments with unrestricted use (e.g., retirement pensions, veterans benefits). Its primary purpose is to help federal agencies comply with various sections of the U.S. Code that require federal agencies to provide fiscal, budgetary and program-related information about federal financial assistance activities.

FAADS issued its first report in 1981 and was formally established by the Consolidated Federal Funds Report Act of 1982<sup>1</sup>. While this act has been superseded by subsequent enactments of Congress, the basic requirements for FAADS have remained intact over the years – namely that the Office of Management and Budget (OMB) shall “maintain the United States Government assistance awards information system” and “update the system on a quarterly basis.”<sup>2</sup> Since its inception, FAADS has been located at and operated by the Bureau of the Census in the Department of Commerce.

FAADS is not a database that can be queried. The data in FAADS is compiled quarterly and includes two types of records: transaction-by-transaction information about individual financial assistance awards made by the programs listed in the Catalog of Federal Domestic Assistance (CFDA); and information about other financial assistance programs (i.e., entitlement payments made directly to individuals) that are aggregated at the county level. Both types of records use the same format, which contains 34 data elements per record. The action-by-action records generally provide information on all 34 data elements. Because county records aggregate numerous individual actions into a single record, they usually provide information on only about 20 of the data elements, since not all data elements are additive. Also, because FAADS only provides information on the initial recipient of each financial assistance award (e.g., states), information about the ultimate recipients of sub-awards (e.g., counties or municipalities) cannot be obtained from FAADS.

Each quarterly FAADS report is a stand-alone report that is not connected to prior or subsequent FAADS reports. All FAADS reports are freely available to interested parties as sequential text files that can be downloaded directly from the FAADS website. A custom-written computer program is required to read the files, however. FAADS has been perennially criticized for the tardiness of its reports, due to the difficulties encountered by the Census Bureau in obtaining the required data from various federal agencies. While each new FAADS data set is supposed to be available 30 days after the close of a fiscal quarter, some have been issued many months later.

FAADS has had problems with the accuracy and completeness of its data. The Government Accountability Office (GAO) noted during a review of several federal financial assistance programs that while “OMB requires that all federal agencies submit financial assistance award data to Census . . . the data submitted were often inaccurate and that some data were missing altogether.”<sup>3</sup> GAO attributed this to the lack of knowledge of FAADS reporting requirements on the part of agency officials, lack of oversight on the part of agencies to ensure that they submitted accurate data, and lack of resources on the part of the Census Bureau to ensure that the data it received were accurate and complete.<sup>4</sup>

FAADS-PLUS was born in 2007 with passage of the Federal Funding Accountability and Transparency Act of 2006 (FFATA). The Act required OMB to have information about all transactions in excess of $25,000 related to all non-procurement financial assistance awards within 30 days of the posting of such transactions (i.e, the obligating of funds).<sup>5</sup> Since this data could not be pulled from FAADS to meet the reporting deadlines set by the FFATA, a different way of gathering the required data on grants, cooperative agreements, loans, etc., had to be created. This system is known as FAADS-PLUS.

The records in FAADS-PLUS use the exact same data fields as the records in FAADS, with the addition of a handful of data fields to gather a few more specifics about each financial assistance award. These additional data fields gather information about “program source, DUNS, physical address, and loan financial data.”<sup>6</sup> FAADS-PLUS records are provided monthly or bi-monthly by federal agencies to REI Systems (REI), a federal contractor. Because the data provided to FAADS-PLUS is not centrally managed in most federal agencies, it is difficult for agencies to verify its accuracy and completeness. The FAADS-PLUS data received and assembled by REI is then provided to NASA for daily uploading into USASpending.gov.

FAADS-PLUS did not replace FAADS. Instead, the arrival of FAADS-PLUS meant that federal agencies are now reporting virtually identical information to two separate entities: one a federal program inside the Census Bureau and the other a federal contractor, REI. The only real differences between FAADS and FAADS-PLUS are the amount of information that each contains and when that information is made available to the public. Specifically, FAADS contains information on all transactions associated with federal financial assistance awards regardless of the amount of each transaction, while FAADS-PLUS contains information on only those transactions associated with federal financial assistance awards that exceed $25,000. And the new information contained in FAADS is not available to the public until several months after the close of each fiscal quarter, while the new information contained in FAADS-PLUS is made available to the public on a daily basis.

###Catalog of Federal Domestic Assistance

The Catalog of Federal Domestic Assistance (CFDA) is “the single, authoritative, Government-wide comprehensive source document of Federal domestic assistance program information produced by the executive branch of the Federal Government.”<sup>7</sup> The CFDA is the “guide to all domestic assistance programs and activities regardless of dollar size or duration.”<sup>8</sup> The CFDA traces its origins to 1977 when the Federal Program Information Act required OMB to collect this information from Federal agencies.<sup>9</sup> In 1983, these responsibilities were transferred from OMB to GSA.<sup>10</sup>

Currently, the CFDA contains information on more than 2,050 programs. The data provided in the CFDA about each domestic assistance program includes: (1) the unique numerical identifier of the program; (2) a description of the program; (3) the legislation authorizing the program; (4) the type(s) of assistance offered by the program (i.e., grant, cooperative agreement, loan, etc.); (5) the number of the Treasury account funding the program; and (6) the total amount of financial assistance obligated annually by the program for several fiscal years. Item No.1 above -- the unique numerical identifier of the program -- is also included in the record of every transaction involving an individual financial assistance award contained in FAADS and FAADS-PLUS. 

###FDPS/FPDS-NG

The Federal Procurement Data System (FPDS), which has recently been re-named the Federal Procurement Data System–Next Generation (FPDS-NG), is the central repository of information on federal procurement (i.e., contract) actions. As the official set of data on all post-award procurement transactions of the federal government, FPDS/FPDS-NG has been and continues to be used by the legislative and executive branches of the federal government, as well as by numerous other entities both inside and outside the government, to obtain information on individual contract transactions, track procurement trends, monitor the achievement of small business contracting goals and perform various other assessments of federal procurement.<sup>11</sup>

FPDS was established by the Office of Federal Procurement Policy (OFPP) Act of 1974.<sup>12</sup> This law created OFPP within OMB and requires OFPP to provide for and direct “the activities of the computer-based Federal Procurement Data System . . . to adequately collect, develop, and disseminate procurement data.”<sup>13</sup> The law further specifies that FPDS, which began operations in 1978, is to be “located in the General Services Administration (GSA).”<sup>14</sup> The data in FPDS focused on prime contract awards alone, providing no information on sub-contract awards. The data in FPDS was submitted in batches each fiscal quarter by federal agencies to GSA’s Federal Procurement Data Center, which operated and managed FPDS. The accumulated records were released upon request on a quarterly basis via tape reel and later on CD-ROM. This data was provided in a flat file text format. FPDS was never a database that users could query directly.

FPDS was operated as a passive collection system that accepted whatever information federal agencies provided on their post-award procurement transactions exceeding $25,000. Because of this, the system was repeatedly criticized by the GAO and others for containing inaccurate and incomplete data.<sup>15</sup> In an attempt to improve the accuracy and completeness of the FPDS in 2003, GSA awarded a contract to Global Computing Enterprises, Inc. (GCE), that required GCE to work with federal executive branch agencies to connect their internal procurement transaction systems to FPDS so that as many of the data fields in the FPDS as possible could be populated directly from the agencies’ internal contract writing systems.<sup>16</sup>

Through FY 2003, FPDS was operated and maintained by GSA.  In 2004, FPDS morphed into the FPDS-NG when the latter was officially unveiled. Since 2004, FPDS-NG has been operated and maintained by GCE.  Information on procurement transactions is now submitted daily to GCE and is made available to the public in “real time” through a search engine.  With the advent of FPDS-NG, the number of data fields in FPDS doubled, primarily due to the capture of additional detail about existing FPDS data elements. Judging from the continuing criticism regarding the accuracy and completeness of the data in the system, FPDS-NG has not achieved its primary objectives. Specifically, GAO noted that FPDS-NG had done nothing different from FPDS to ensure that its data was accurate and complete. Consequently, users of FPDS-NG continued to lack confidence in its data.<sup>17</sup> Similarly, the Federal Times described FPDS-NG as being “short on info, [and] long on problems.<sup>18</sup>

In early 2010, GSA awarded a multi-year $74.4 million contract to IBM US Federal to consolidate the nine databases that comprise GSA’s Integrated Acquisition Environment into a common architecture and then maintain and operate them.<sup>19</sup> One of these nine databases is FPDS-NG. Because FPDS-NG is considered by many including GAO to be in one of the “worst shape[s]” of these databases, FPDS-NG will be the first database migrated to GSA’s Architecture and Operations Contract Support program by IBM US Federal.<sup>20</sup>

###American Recovery and Reinvestment Act

When the American Recovery and Reinvestment Act (Recovery Act) was enacted in 2009, the CFDA added all of the programs offering Recovery Act funds to its line-up. The FPDS-NG, FAADS and FAAD-PLUS were also expanded by several fields to track transactions involving Recovery Act funds. In cases where transactions involve the use of Recovery Act funds as well as non-Recovery Act funds, the latter three data systems are required to have two separate records to allow for the separate tallying of these funds, thereby potentially altering the total number of actual transactions that each system contains.

###USASpending.gov

FFATA required OMB to establish a “single searchable website, accessible by the public at no cost” before January 1, 2008, that contains information on all transactions over $25,000 involving all federal procurement and non-procurement awards within 30 days of the posting of such transactions.<sup>21</sup> In an attempt to fulfill this requirement, OMB established USASpending.gov, which is an aggregation of existing information on the transactions exceeding $25,000 that are made under federal contracts, purchase orders, task orders, delivery orders, grants, loans, loans, cooperative agreements, and other forms of financial assistance. USASpending.gov is also required to expand to include information on transactions over $25,000 that are related to both subgrants and subcontracts, but it has yet to do so. USASpending.gov now includes some information on charge card transactions made by federal agencies, which is updated quarterly.

FFATA is very specific about the capabilities of the “searchable website” that are required by the Act, stating that the website must allow users to: (1) search and aggregate federal funding by recipient name, location, etc., (2) “ascertain through a single search the total amount of federal funding awarded to an entity by a federal [procurement] award . . . by fiscal year,” (3) “ascertain through a single search the total amount of federal funding awarded to an entity by a federal [non-procurement (i.e., financial assistance)] award . . . by fiscal year,” and (4) download the data found in the searches.<sup>22</sup>

FFATA also states that the website may use FPDS and FAADS as the source of its data, but the Act very specifically states that the website “shall not be considered in compliance if it hyperlinks to the Federal Procurement Data System website, the Federal Assistance Awards Data System website, . . . or other existing websites, so that information elements required by [the act] . . . cannot be searched electronically by field in a single search.”<sup>23</sup>

In Fall 2007, with the deadline for delivery of USASpending.gov fast approaching and no website to deliver, OMB via GSA attempted to sole-source purchase FedSpending.org -- a website created by OMBWatch with assistance from Eagle Eye Publishers, Inc. The development of FedSpending.org was made possible with a $334,000 grant from the Sunlight Foundation. This procurement was protested, however, for its lack of competition, so GSA broke it up and competed the data services and data delivery portions separately. OMBWatch, operating through Eagle Eye, won the award for data services (i.e., the software platform).<sup>24</sup> The data provision portion of the procurement was awarded to GCE.<sup>25</sup> GCE is the same company that operated and managed FPDS-NG from 2003 onward. When this latter arrangement proved cumbersome, the data provision function was shifted to REI, the same company that operates USASpending.gov.

Version 1.0 of USASpending.gov was released in December 2007, and aside from a few changes that added information about federal spending that were not encompassed by FPDS-NG or FAADS, it was essentially a clone of Fedspending.org. The site was given a visual redesign in mid-2009, but this included few changes to its functionality. Version 2.0 of USASpending.gov was released in May 2010, using the cloud computing capabilities of NASA’s Nebula Cloud Computing Platform in a “joint venture” with GSA and OMB that changed the look and feel of the website but left the basic contents the same. USASpending.gov 2.0 is physically located at NASA and is operated by REI Systems.

Despite the directives of OMB to federal agencies to improve the quality of the data that feeds USASpending.gov<sup>26</sup>, little has been done to fix the accuracy and completeness problems of FPDS-NG and FAADS-PLUS, which continue to be the main sources of the data in USASpending.gov. This point was recently emphasized by the GAO in its report on the implementation of FFATA. The GAO specifically notes that “OMB has not implemented a process to identify nonreporting agencies as originally planned and instead has relied on agencies’ voluntary compliance with OMB guidance to ensure complete and accurate reporting.” The GAO report continues by noting that, “without a more effective approach to ensuring that agencies report applicable awards, the utility of USASpending.gov will be impaired by gaps in the required information.”<sup>27</sup>

<ol>
            <li>PL 97-326 (1982).</li>
            <li>31 USC 6102a.</li>
            <li>GAO-06-294 (2006).</li>
            <li>GAO-06-294 (2006).</li>
            <li>PL 109-282, 31 USC 6101 note.</li>
            <li>OMB Guidance on Data Submission under the Federal Financial Accountability and Transparency Act, October 18, 2007.</li>
            <li>OMB Circular A-89.</li>
            <li>OMB Circular A-89.</li>
            <li>OMB Circular A-89.</li>
            <li>PL 98-169.</li>
            <li>Because the term “procurement” encompasses all stages of the acquisition process from the planning of the purchase to price negotiation to contract award to contract administration to contract close-out, it is important to note that the first time that a procurement appears in the FPDS is “post-award.”  See 41 USC 403(2).</li>
            <li>PL 93-400; 41 USC 404.</li>
            <li>41 USC 405(d)(4)(A).</li>
            <li>41 USC 405(d)(4)(A).</li>
            <li>See GAO Reports AIMD-94-178R (1994) and GAO-05-295R (2003)</li>
            <li>“GSA Awards $24 million Contract to Global Computer Enterprises for Federal Procurement Data System Next Generation,” GSA #10011 (May 2, 2003).</li>
            <li> GAO-05-960R (2005).</li>
            <li>“Contracts database short on info, long on problems,” by Chris Gosier of Federal Times (July 31, 2006).</li>
            <li>“GSA to Consolidate Contract Performance Databases,” GSA #10663 (February 18, 2010).</li>
            <li>“Troubled federal procurement data systems to get facelift,” by Jason Miller of Federal News Radio (September 30, 2009); “Senators weigh in on GSA contract award,” by Matthew Weigelt of Federal Computer Week (October 2, 2009)</li>
            <li>PL 109-282, 31 USC 6101 note.</li>
            <li>PL 109-282(2)(a)(3).</li>
            <li>PL 109-282(2)(c)(2).</li>
            <li>“OMB Offers an Easy Way to Follow the Money” by Elizabeth Williamson, Washington Post (December 13, 2007)</li>
            <li>“GSA awards $0 contract for spending database data,” by Jason Miller, Federal Computer Week (October 3, 2007).</li>
            <li>OMB Memo M-09-19 (2009)</li>
            <li>GAO -10-365 (2010).</li>
        </ol>

## Contracts

## Direct Assistance and Grants

