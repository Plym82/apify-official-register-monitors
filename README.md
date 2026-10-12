# Official-register change monitors on Apify

Pay-per-event [Apify](https://apify.com) Actors that **watch a portfolio of identifiers** (company numbers, LEIs, licence and permit numbers, facility IDs …) in **official public registers and open-data feeds**, and emit **typed change events** (status changes, insolvency notices, licence revocations, new filings, …) instead of raw data dumps. You pay a small fee only for events actually delivered.

Built for compliance, KYB/KYC, supplier-risk, credit, procurement, legal and data teams who need to know *when something changes* for the entities they care about – run on a schedule, pipe results to webhooks, Slack, sheets or your own systems via the Apify API, or call them from AI agents (MCP).

**92 public Actors** · Browse all on the Apify Store: [apify.com/plym-actor-factory](https://apify.com/plym-actor-factory)

Prices are per delivered event in USD, plus a tiny Apify *Actor start* fee (typically $0.00005 per GB of memory). Always check the Store page for current pricing.

## Contents

- [United Kingdom](#united-kingdom) (13)
- [European Union & wider Europe](#european-union--wider-europe) (12)
- [Cross-border KYB & finance](#cross-border-kyb--finance) (3)
- [United States – federal](#united-states--federal) (30)
- [United States – state](#united-states--state) (6)
- [Canada](#canada) (10)
- [Australia](#australia) (9)
- [Latin America](#latin-america) (1)
- [Global / security](#global--security) (1)
- [Other](#other) (7)

## United Kingdom

| Actor | Use case | Price |
|---|---|---|
| [Scotland Care Inspectorate Care Service Portfolio Monitor](https://apify.com/plym-actor-factory/uk-scotland-care-inspectorate-cs-number-status-monitor) | Watch named Scottish care services by Care Inspectorate CS number; get an event on cancellation, provider change, grade downgrade, enforcement or upheld complaint, from official Care Inspectorate… | $0.02 per event |
| [UK Charity Commission Monitor: Removed & Status Alerts](https://apify.com/plym-actor-factory/uk-charity-commission-portfolio-status-monitor) | Watch England & Wales charity registration numbers on the official Charity Commission Register. | $0.02 per event |
| [UK Companies House Streaming Change Monitor](https://apify.com/plym-actor-factory/uk-companies-house-realtime-monitor) | Companies House change alerts for credit control, KYB and compliance teams: insolvency cases, officer/director and PSC changes, new or satisfied charges, filings and status changes for your company… | $0.015 per event |
| [UK EA EPR Permit Monitor: Holder & Status Alerts](https://apify.com/plym-actor-factory/uk-ea-epr-industrial-permit-portfolio-status-monitor) | Watch UK Environment Agency EPR industrial permit numbers (EPR/…). | $0.02 per event |
| [UK ESFA APAR Provider Monitor (UKPRN Watchlist)](https://apify.com/plym-actor-factory/uk-esfa-apar-ukprn-status-monitor) | Watch UKPRNs on the DfE/ESFA Apprenticeship Provider and Assessment Register for employers and EPAs: appear/leave, Status, and CanDeliverApprenticeships/Units changes. | $0.02 per event |
| [UK FCA Register Firm Status Monitor (FRN Watchlist)](https://apify.com/plym-actor-factory/uk-fca-frn-portfolio-status-monitor) | FCA Register monitoring for principal firms, partnership and third-party-risk teams: watch FRNs and get events when a firm is cancelled or suspended, permissions change, Appointed Representatives… | $0.02 per event |
| [UK FSA AppNo Portfolio Status Monitor](https://apify.com/plym-actor-factory/uk-fsa-appno-portfolio-monitor) | Watch FSA Approval Numbers (AppNo) and emit typed APPEARED/DROPPED/ACTIVITIES_CHANGED/AUTHORITY_CHANGED events from the official FSA Approved Food Establishments daily CSV (OGL v3). | $0.02 per event |
| [UK HSE Asbestos Licence-Holder Portfolio Status Event Monitor](https://apify.com/plym-actor-factory/uk-hse-asbestos-licence-holder-portfolio-status-monitor) | Watch UK HSE asbestos Licence Numbers against the official CONIAC disclosable licence-holder xlsx and emit typed APPEARED/DROPPED/ON_REGISTER/OFF_REGISTER (+ optional attribute) events. | $0.02 per event |
| [UK Multi-Trade Planning Lead Radar](https://apify.com/plym-actor-factory/uk-planning-trade-lead-radar) | Match new England planning applications to multi-trade taxonomy (solar/PV/battery, roof, scaffold, extension/loft, HVAC, glazing) + optional postcode radius via planning.data.gov.uk (OGL). | $0.02 per event |
| [UK Ofsted URN Portfolio Inspection Outcome Event Monitor](https://apify.com/plym-actor-factory/uk-ofsted-urn-portfolio-inspection-monitor) | Watch a book of England state-funded school URNs and emit typed inspection-outcome / overall-effectiveness / safeguarding-inclusion-curriculum standard events from the official Ofsted monthly MI CSV… | $0.02 per event |
| [UK Sanctions List Change Monitor (FCDO UKSL)](https://apify.com/plym-actor-factory/uk-sanctions-list-counterparty-portfolio-watch) | Track changes to the UK Sanctions List entries you are exposed to: watch FCDO UKSL Unique IDs and get DELISTED, VARIATION (regime, sanctions, names) and DESIGNATED events from the official UKSL file. | $0.02 per event |
| [UK SRA Firm Monitor: Intervention & Status Alerts](https://apify.com/plym-actor-factory/uk-sra-firm-portfolio-status-monitor) | Watch SRA firm numbers via the official SRA Data Share API. | $0.02 per event |
| [UKGC Licence Monitor: Suspended & Revoked Alerts](https://apify.com/plym-actor-factory/uk-gambling-commission-licence-portfolio-monitor) | Watch UK Gambling Commission account and licence numbers from the official OGL register. | $0.02 per event |

## European Union & wider Europe

| Actor | Use case | Price |
|---|---|---|
| [Czech Company Monitor: ARES IČO Status & Change Alerts](https://apify.com/plym-actor-factory/czech-ares-ico-portfolio-monitor) | Watch Czech companies by IČO in the official ARES register. | $0.02 per event |
| [ECB MFI RIAD_CODE Portfolio Status Monitor](https://apify.com/plym-actor-factory/eu-ecb-mfi-riad-code-portfolio-status-monitor) | Watch ECB Monetary Financial Institution RIAD_CODEs; emit APPEARED/DROPPED/STATUS_CHANGED and attribute events from the official daily MFI population CSV. | $0.02 per event |
| [EPC SEPA SCT BIC Portfolio Status Monitor](https://apify.com/plym-actor-factory/eu-epc-sepa-sct-bic-portfolio-status-monitor) | Watch EPC SEPA Credit Transfer (SCT) participant BICs; emit APPEARED/DROPPED/LEAVING_CHANGED/OPTIONS_CHANGED and attribute events from the official EPC SCT Register of Participants CSV. | $0.02 per event |
| [EPC SEPA VOP BIC Portfolio Status Monitor](https://apify.com/plym-actor-factory/eu-epc-sepa-vop-bic-portfolio-status-monitor) | Watch EPC SEPA Verification of Payee (VOP) participant BICs; emit APPEARED/DROPPED/STATUS_CHANGED/ROLE_CHANGED/LEAVING_CHANGED and attribute events from the official EPC VOP Register of Participants… | $0.02 per event |
| [EU TR Organisation ID Portfolio Status Event Monitor](https://apify.com/plym-actor-factory/eu-tr-org-portfolio-status-monitor) | Watch Transparency Register identificationCodes and emit typed REMOVED / APPEARED / LAST_UPDATE_CHANGED / CATEGORY_CHANGED events from the official EU open-data XML snapshot. | $0.02 per event |
| [Finland Company Monitor: PRH Bankruptcy & Status Alerts](https://apify.com/plym-actor-factory/finland-prh-ytunnus-portfolio-monitor) | Watch Finnish companies by Y-tunnus (Business ID) in official PRH/YTJ open data. | $0.02 per event |
| [France Company Monitor: BODACC Insolvency & Change Alerts](https://apify.com/plym-actor-factory/france-bodacc-siren-portfolio-monitor) | Watch French companies by SIREN in the official BODACC gazette (DILA open data). | $0.02 per event |
| [MiCA CASP Register Monitor: ESMA Crypto Licence Alerts](https://apify.com/plym-actor-factory/eu-esma-mica-casp-lei-portfolio-status-monitor) | Watch crypto-asset service providers by LEI in ESMA's official interim MiCA CASP register. | $0.02 per event |
| [Netherlands KvK Open-Data Status Event Monitor](https://apify.com/plym-actor-factory/netherlands-kvk-status-event-monitor) | Watch a list of Dutch KVK numbers and emit typed active/insolvency status events from free official HVDS open data (BV/NV only). | $0.02 per event |
| [Norway Company Monitor: Brreg Bankruptcy & Status Alerts](https://apify.com/plym-actor-factory/norway-brreg-orgnr-portfolio-monitor) | Watch Norwegian companies by organisation number in the official Brreg Enhetsregisteret. | $0.02 per event |
| [Spain Company Monitor: BORME Insolvency & Officer Alerts](https://apify.com/plym-actor-factory/spain-borme-nif-portfolio-monitor) | Watch Spanish companies by NIF and name in the official BORME gazette (BOE open data). | $0.02 per event |
| [Swiss Company Monitor: SHAB Bankruptcy & Change Alerts](https://apify.com/plym-actor-factory/switzerland-shab-uid-portfolio-monitor) | Watch Swiss companies by CHE UID in the official SHAB/SOGC gazette (Amtsblattportal). | $0.02 per event |

## Cross-border KYB & finance

| Actor | Use case | Price |
|---|---|---|
| [DACH Supplier KYB: VIES VAT Check, Impressum & Insolvency](https://apify.com/plym-actor-factory/dach-supplier-kyb-packet) | Supplier verification and vendor onboarding for German, Austrian and Swiss suppliers: from a supplier website, one KYB packet with Impressum identity, a live VIES VAT check and a German… | $0.02 per event |
| [GLEIF LEI Monitor: Lapsed LEI & Entity Change Watch](https://apify.com/plym-actor-factory/gleif-lei-portfolio-watch) | LEI monitoring for regulatory-reporting, treasury and onboarding teams: watch counterparty LEIs and get events when an LEI lapses, is retired or annulled, the entity goes inactive, the legal name or… | $0.02 per event |
| [Poland Supplier Verification: VAT White List & Bank Check](https://apify.com/plym-actor-factory/poland-supplier-kyb-packet) | Supplier verification for AP, treasury and procurement teams paying Polish suppliers: per NIP, one KYB packet with official MF VAT White List status, bank account verification (accountAssigned) with… | $0.003 per event (+1 other event types) |

## United States – federal

| Actor | Use case | Price |
|---|---|---|
| [Chicago Public Chauffeur Portfolio Status Monitor](https://apify.com/plym-actor-factory/us-il-chicago-public-chauffeur-license-portfolio-status-monitor) | Watch named Chicago BACP Public Chauffeur license numbers; emit APPEARED/DROPPED/STATUS_CHANGED from official data.cityofchicago.org Socrata 97wa-y6ff. | $0.02 per event |
| [Chicago Public Passenger Vehicle Portfolio Status Monitor](https://apify.com/plym-actor-factory/us-il-chicago-ppv-record-id-portfolio-status-monitor) | Watch named Chicago BACP Public Passenger Vehicle record IDs; emit APPEARED/DROPPED/STATUS_CHANGED from official data.cityofchicago.org Socrata tfm3-3j95. | $0.02 per event |
| [College Scorecard Operating Status Monitor (UNITID/OPEID)](https://apify.com/plym-actor-factory/us-college-scorecard-operating-portfolio-monitor) | Higher-ed operating-status monitoring for lenders, guaranty agencies, edtech and compliance teams: watch IPEDS UNITIDs/OPEIDs and get events when College Scorecard shows a school open↔closed or… | $0.02 per event |
| [CT Real Estate Salesperson License Monitor (DCP)](https://apify.com/plym-actor-factory/us-ct-dcp-res-credential-number-portfolio-status-monitor) | Watch Connecticut DCP Real Estate Salesperson credentials for brokerages, title companies and lenders: ACTIVE/INACTIVE/SUSPENDED/REVOKED flips and supervising-broker changes from official data.ct.gov. | $0.02 per event |
| [DE POL License No Portfolio Status Monitor](https://apify.com/plym-actor-factory/us-de-pol-license-no-portfolio-status-monitor) | Watch named Delaware POL license_no values; emit APPEARED/DROPPED/STATUS_CHANGED and attribute events from official data.delaware.gov Socrata pjnv-eaih. | $0.02 per event |
| [EPA GHGRP Facility Monitor: Stopped Reporting & Parent Alerts](https://apify.com/plym-actor-factory/us-epa-ghgrp-facility-status-monitor) | Watch US greenhouse-gas reporting facilities by EPA GHGRP facility ID. | $0.02 per event |
| [EPA Pesticide Registration Monitor: Cancellation Alerts](https://apify.com/plym-actor-factory/us-epa-ppis-registration-number-status-monitor) | Watch EPA pesticide product Registration Numbers against the official weekly EPA PPIS file. | $0.02 per event |
| [EPA SDWIS Water System Monitor: PWSID Activity Alerts](https://apify.com/plym-actor-factory/us-epa-sdwis-pwsid-portfolio-status-monitor) | Watch EPA Public Water System IDs (PWSIDs) in SDWIS. | $0.02 per event |
| [EPA TSCA Inventory Monitor: CAS Number Active/Inactive Alerts](https://apify.com/plym-actor-factory/us-epa-tsca-inventory-casrn-status-monitor) | Watch your chemicals by CAS Registry Number on the official EPA TSCA Inventory. | $0.02 per event |
| [FDA GUDID Device Monitor: UDI Distribution Status Alerts](https://apify.com/plym-actor-factory/us-fda-accessgudid-di-status-monitor) | Watch your medical device UDIs (Primary DIs) in FDA's GUDID via NLM AccessGUDID. | $0.02 per event |
| [FMCSA Carrier Monitoring: Insurance, Authority & OOS Alerts](https://apify.com/plym-actor-factory/fmcsa-safer-risk-event-monitor) | Carrier monitoring for freight brokers, 3PLs and shippers: watch your USDOT numbers and get events when FMCSA data shows an insurance cancellation, authority revoked or suspended, an out-of-service… | $0.003 per event (+1 other event types) |
| [H-1B LCA Employer New-Filing Watchlist (honest quarterly lag)](https://apify.com/plym-actor-factory/h1b-lca-employer-filing-watchlist) | Watch a list of employers (names or FEINs) and emit typed LCA_NEW_FILING events when new cases appear in official DOL OFLC public disclosure Excel/open data. | $0.02 per event |
| [Montgomery County MD Housing License Portfolio Status Monitor](https://apify.com/plym-actor-factory/us-md-montgomery-housing-licensenumber-portfolio-status-monitor) | Watch named Montgomery County MD housing licensenumber values; emit APPEARED/DROPPED/STATUS_CHANGED from official Socrata et5s-xste. | $0.02 per event |
| [MSHA Mine ID Portfolio Status Monitor](https://apify.com/plym-actor-factory/us-msha-mine-id-status-monitor) | Watch MSHA Mine IDs and emit typed ACTIVE/STATUS_CHANGED/ABANDONED_OR_NONPRODUCING/CONTROLLER_CHANGED/OPERATOR_CHANGED/REAPPEARED events from the official MSHA Open Government Data Mines.zip register. | $0.02 per event |
| [NOLA Occupational License Portfolio Status Monitor](https://apify.com/plym-actor-factory/us-la-nola-occupational-numstring-portfolio-status-monitor) | Watch named City of New Orleans occupational business license numstring values; emit APPEARED/DROPPED/STATUS_CHANGED from official Socrata abc4-h3u3. | $0.02 per event |
| [NY OCFS Childcare Facility ID Portfolio Status Monitor](https://apify.com/plym-actor-factory/us-ny-ocfs-childcare-facility-id-portfolio-status-monitor) | Watch named NYS OCFS Child Care Regulated Programs facility_id values; emit APPEARED/DROPPED/STATUS_CHANGED from official data.ny.gov Socrata cb42-qumz. | $0.02 per event |
| [NYC DCWP License Monitor: Suspended & Revoked Alerts](https://apify.com/plym-actor-factory/us-nyc-dcwp-license-nbr-portfolio-status-monitor) | Watch NYC DCWP/DCA license numbers from official NYC Open Data. | $0.02 per event |
| [NYC DOB License Monitor: Revoked & Expiry Alerts](https://apify.com/plym-actor-factory/us-nyc-dob-license-sl-no-portfolio-status-monitor) | Watch NYC Department of Buildings license_sl_no values from official open data. | $0.02 per event |
| [PCAOB Registered Audit Firm Portfolio Status Monitor](https://apify.com/plym-actor-factory/us-pcaob-registered-firm-id-portfolio-status-monitor) | Watch named PCAOB-registered audit firms by Firm ID; get an event when registration becomes Withdrawal Pending, Withdrawn, Revoked or Disapproved, or the firm name changes, from the official PCAOB… | $0.02 per event |
| [Philly L&I License Portfolio Status Monitor](https://apify.com/plym-actor-factory/us-pa-philly-li-licensenum-portfolio-status-monitor) | Watch named City of Philadelphia L&I business license licensenum values; emit APPEARED/DROPPED/STATUS_CHANGED from official OpenDataPhilly CARTO li_business_licenses. | $0.02 per event |
| [TTB Alcohol Permit Monitor: Status & Industry Alerts](https://apify.com/plym-actor-factory/us-ttb-alcohol-permit-status-monitor) | Watch TTB alcohol permit numbers from the official FOIA List of Permittees. | $0.02 per event |
| [US CMS Medicare PPEF NPI Portfolio Enrollment Status Monitor](https://apify.com/plym-actor-factory/us-cms-ppef-npi-portfolio-enrollment-monitor) | Watch NPIs and emit typed ENROLLED/DROPPED/PROVIDER_TYPE_CHANGED/ENROLLMENT_ID_CHANGED events from the official CMS data.cms.gov Medicare Fee-For-Service Public Provider Enrollment (PPEF) extract. | $0.02 per event |
| [US ENERGY STAR Unique ID (pd_id) Portfolio Status Monitor](https://apify.com/plym-actor-factory/us-energy-star-pd-id-portfolio-monitor) | Watch ENERGY STAR Unique IDs (pd_id) and emit typed APPEARED/DROPPED/MOST_EFFICIENT events from the official EPA ENERGY STAR Model Index Socrata. | $0.02 per event |
| [US EPA Safer Choice Portfolio Status Monitor](https://apify.com/plym-actor-factory/us-epa-safer-choice-portfolio-monitor) | Watch Safer Choice products/companies (UPC/GTIN, company_name, product_url) and emit typed APPEARED/DROPPED/GOOD_STANDING events from the official EPA Envirofacts Safer Choice table. | $0.02 per event |
| [US EPA TRI Facility ID Portfolio Status Monitor](https://apify.com/plym-actor-factory/us-epa-tri-facility-portfolio-status-monitor) | Watch TRI Facility IDs and emit typed APPEARED/DROPPED/NAME_CHANGED/PARENT_CHANGED/ADDRESS_CHANGED events from the official EPA Envirofacts tri_facility JSON API. | $0.02 per event |
| [US HRSA Health Center / Look-Alike Site Status Monitor](https://apify.com/plym-actor-factory/us-hrsa-health-center-site-monitor) | Watch Health Center Numbers and/or BPHC site keys and emit typed Active/Inactive/type/location-setting events from the official HRSA data.hrsa.gov Health Center Service Delivery and Look-Alike Sites… | $0.02 per event |
| [US LDA Lobbying Client & Registrant New-Filing Watchlist](https://apify.com/plym-actor-factory/us-lda-lobbying-filing-watchlist) | Watch lobbying client and/or registrant firm names; poll the official Senate LDA REST API (lda.gov); emit typed events only for new filing_uuid values for your book. | $0.02 per event |
| [USDA FSIS MPI Est# Portfolio Status Monitor](https://apify.com/plym-actor-factory/us-fsis-mpi-est-status-monitor) | Watch FSIS establishment numbers and emit typed APPEARED/DROPPED_OR_INACTIVE/ACTIVITIES_CHANGED/SIZE_CHANGED/GRANT_DATE_CHANGED events from the official USDA FSIS MPI Directory JSON API/CSV. | $0.02 per event |
| [USDA SNAP Record_ID Authorization Status Monitor](https://apify.com/plym-actor-factory/us-usda-snap-record-id-authorization-status-monitor) | Watch USDA SNAP retailer Record_IDs and emit typed AUTHORIZED/ENDED/APPEARED/DROPPED events from the official FNS SNAP ArcGIS FeatureServer. | $0.02 per event |
| [WA DOH Credential Monitor: Suspended & Revoked Alerts](https://apify.com/plym-actor-factory/us-wa-doh-credential-number-portfolio-status-monitor) | Watch Washington DOH healthcare credential numbers from official data.wa.gov. | $0.02 per event |

## United States – state

| Actor | Use case | Price |
|---|---|---|
| [California CSLB Contractor License Risk Event Monitor](https://apify.com/plym-actor-factory/us-contractor-license-risk-monitor) | Watch a book of California CSLB contractor license numbers and emit typed risk events (LICENSE_*/BOND_*/WORKERS_COMP_*) from official CSLB Public Data Portal bulk files. | $0.025 per event |
| [CARB LCFS Pathway Monitor: Carbon Intensity & Status Alerts](https://apify.com/plym-actor-factory/us-carb-lcfs-fuel-pathway-status-monitor) | Watch California LCFS fuel pathway IDs in CARB's official Current Fuel Pathways list. | $0.02 per event |
| [Colorado Charity Monitor: CDOS Status & Notice Alerts](https://apify.com/plym-actor-factory/us-co-sos-charity-registration-portfolio-status-monitor) | Watch Colorado-registered charities, paid solicitors and fundraising consultants by SOS entity ID; get an event when status moves from GOOD to NOTICE, WITHDRAWN, REVOKED or DENIED, or the name… | $0.02 per event |
| [Illinois IDFPR License Monitor: Status & Discipline Alerts](https://apify.com/plym-actor-factory/us-il-idfpr-license-portfolio-monitor) | Watch Illinois IDFPR professional license numbers from the official open-data register. | $0.02 per event |
| [Texas TABC License Monitor: Suspended & Status Alerts](https://apify.com/plym-actor-factory/us-tx-tabc-license-id-portfolio-status-monitor) | Watch Texas TABC license IDs from official data.texas.gov. | $0.02 per event |
| [Washington CPA License Monitor: BoA Status Alerts](https://apify.com/plym-actor-factory/us-wa-boa-cpa-credential-number-portfolio-status-monitor) | Watch named Washington State CPA licenses by Board of Accountancy credential number. | $0.02 per event |

## Canada

| Actor | Use case | Price |
|---|---|---|
| [Calgary Business Licence Monitor: Status Change Alerts](https://apify.com/plym-actor-factory/ca-calgary-getbusid-portfolio-status-monitor) | Watch named City of Calgary business licences (getbusid) in official data.calgary.ca open data. | $0.02 per event |
| [Canada Aircraft Mark Monitor: CCAR Status & Sale Alerts](https://apify.com/plym-actor-factory/ca-tc-ccar-aircraft-mark-portfolio-status-monitor) | Watch Canadian aircraft by registration mark (C-XXXX); get an event when registration is cancelled or expires, a sale is reported or the owner changes, from the official Transport Canada CCAR daily… | $0.02 per event |
| [Canada Federal Corporation Status Portfolio Monitor](https://apify.com/plym-actor-factory/canada-federal-corp-status-monitor) | Watch federal corporation numbers / BNs and emit typed status & name change events from the free official ISED Corporations Canada API. | $0.02 per event |
| [Canada FINTRAC MSB Monitor: Registration Status Alerts](https://apify.com/plym-actor-factory/ca-fintrac-msb-registration-number-portfolio-status-monitor) | Watch FINTRAC money-services-business registration numbers from the official public list. | $0.02 per event |
| [Canada ISED TAFL Monitor: Authorization Status Alerts](https://apify.com/plym-actor-factory/ca-ised-sms-tafl-authorization-portfolio-status-monitor) | Watch Canada ISED SMS TAFL authorization numbers for appear/drop and authorization status changes from the official spectrum register. | $0.02 per event |
| [Canada OSFI Monitor: Regulated Bank & Insurer Alerts](https://apify.com/plym-actor-factory/ca-osfi-frfi-who-we-regulate-portfolio-status-monitor) | Watch OSFI-regulated Canadian banks, insurers and trust companies in the official monthly Who We Regulate list. | $0.02 per event |
| [Canada PMRA PCP Registration Number Status Monitor](https://apify.com/plym-actor-factory/ca-pmra-registration-number-portfolio-status-monitor) | Watch Canada PMRA PCP Registration Numbers; emit FULL_REGISTRATION/CANCELLED/APPEARED/DROPPED/STATUS_CHANGED/EXPIRY_CHANGED from official product extract CSV. | $0.02 per event |
| [CFIA SFCR Food Licence Monitor: Status Alerts](https://apify.com/plym-actor-factory/ca-cfia-sfcr-licence-portfolio-monitor) | Watch CFIA SFCR food licence numbers for appear/drop, establishment and DBA changes from the official Safe Food for Canadians register. | $0.02 per event |
| [Health Canada DPD DIN Portfolio Status Event Monitor](https://apify.com/plym-actor-factory/ca-hc-dpd-din-portfolio-status-monitor) | Watch Drug Identification Numbers (DIN) and emit typed Marketed/Cancelled/Dormant/Approved/company events from the official Health Canada Drug Product Database (DPD) API. | $0.02 per event |
| [Health Canada NHP NPN Portfolio Status Event Monitor](https://apify.com/plym-actor-factory/ca-hc-nhp-npn-portfolio-status-monitor) | Watch Natural Product Numbers (NPN / DIN-HM) and emit typed ACTIVE/INACTIVE/company events from the official Health Canada LNHPD Product Licence API. | $0.02 per event |

## Australia

| Actor | Use case | Price |
|---|---|---|
| [ACMA Radiocomms Licence Portfolio Status Monitor](https://apify.com/plym-actor-factory/au-acma-licence-portfolio-monitor) | Watch ACMA radiocommunications LICENCE_NO values and emit typed Granted/status/expiry/category/client events from the official Spectrum Licensing LicenceSearchJSON API (optional RRL extracts). | $0.02 per event |
| [ACT COLA Licence Monitor: Access Canberra Status Alerts](https://apify.com/plym-actor-factory/au-act-cola-licence-number-portfolio-status-monitor) | Watch ACT Access Canberra COLA licence numbers for Active/Expired/Suspended/Cancelled status and occupation changes from the official List of Professionals open dataset. | $0.02 per event |
| [ASIC Credit Licence Monitor: Status & Suspension Alerts](https://apify.com/plym-actor-factory/au-asic-credit-licence-number-portfolio-status-monitor) | Watch ASIC Credit Licence Numbers for approval/suspension status, name and authorisation changes from the official ASIC register. | $0.02 per event |
| [Australia ABN Status Portfolio Monitor](https://apify.com/plym-actor-factory/australia-abn-status-portfolio-monitor) | Watch a list of Australian Business Numbers and emit typed ABN status / GST / entity name+type change events from free official ABR GUID web services. | $0.02 per event |
| [Australia APVMA Product Monitor: Registration Status Alerts](https://apify.com/plym-actor-factory/au-apvma-product-number-portfolio-status-monitor) | Watch APVMA product registration numbers from the official Australian pesticides and veterinary medicines register. | $0.02 per event |
| [Australia ASIC Financial Adviser Portfolio Status Monitor](https://apify.com/plym-actor-factory/au-asic-financial-adviser-number-portfolio-status-monitor) | Watch named ASIC Financial Advisers Register adviser numbers; emit registration status, banning/disciplinary, CPD-failure and AFSL authorisation added/ceased events from the official ASIC Financial… | $0.02 per event |
| [CASA Aircraft Mark Monitor: Suspension & Holder Alerts](https://apify.com/plym-actor-factory/au-casa-reg-mark-portfolio-status-monitor) | Watch Australian VH aircraft marks for insurers, lessors and MROs: alerts when CASA shows suspension, deregistration, full-registration return, or holder/operator changes from the official daily… | $0.02 per event |
| [QLD EA Permit Monitor: Status Change Alerts](https://apify.com/plym-actor-factory/au-qld-ea-permit-reference-portfolio-status-monitor) | Watch Queensland Environmental Authority Permit References for appear/drop and status changes from official DESI open data. | $0.02 per event |
| [Queensland Enforcement Monitor: Action Status Alerts](https://apify.com/plym-actor-factory/au-qld-enforcement-reference-portfolio-status-monitor) | Watch Queensland DESI Environmental Enforcement Action References for appear/drop and status changes from official open data. | $0.02 per event |

## Latin America

| Actor | Use case | Price |
|---|---|---|
| [Brazil CNPJ Situação Change Monitor (honest monthly lag)](https://apify.com/plym-actor-factory/brazil-cnpj-situacao-change-monitor) | Watch a list of Brazilian CNPJs and emit typed situação cadastral / material change events from Receita Federal dados abertos (or equivalent open-data mirror). | $0.02 per event |

## Global / security

| Actor | Use case | Price |
|---|---|---|
| [Lookalike Domain CT Brand-Abuse Monitor](https://apify.com/plym-actor-factory/lookalike-ct-brand-abuse-monitor) | Generate lookalikes (dnstwist-class, in-process) for brand apexes, join public CT via crt.sh, and emit LOOKALIKE_CERT_ISSUED events when a lookalike gets a new TLS cert. | $0.02 per event |

## Other

| Actor | Use case | Price |
|---|---|---|
| [FMCSA Carrier Lookup by USDOT/MC: Authority, Safety, Contacts](https://apify.com/plym-actor-factory/fmcsa-carrier-lookup) | Look up trucking companies by USDOT or MC number, or search new and existing carriers by state, name and fleet size. | $0.003 per event (+1 other event types) |
| [IANA Registrar ID Monitor: Accreditation Status Alerts](https://apify.com/plym-actor-factory/iana-icann-registrar-id-portfolio-status-monitor) | Watch IANA Registrar IDs for registries and brand-protection teams: Accredited/Terminated/Reserved flips plus name/RDAP URL changes from the official registrar-ids CSV. | $0.02 per event |
| [ICANN gTLD Registry-Operator Portfolio Status Monitor](https://apify.com/plym-actor-factory/icann-gtld-registry-operator-portfolio-status-monitor) | Watch ICANN gTLD strings for registry-operator / contract portfolio status changes from the official gtlds.json feed (DELEGATED, CONTRACT_TERMINATED, REMOVED). | $0.02 per event |
| [LEI Lookup & GLEIF Search: Status, Renewal Date, Parent Company](https://apify.com/plym-actor-factory/lei-lookup-gleif-search) | Look up any LEI or search the official GLEIF database by name, country or status. | $0.002 per event (+1 other event types) |
| [New Zealand Charities Register Portfolio Status Monitor](https://apify.com/plym-actor-factory/nz-charities-register-cc-number-portfolio-status-monitor) | Watch named New Zealand Charities Register CC numbers; emit Registered/Deregistered/Removed status events (with deregistration date + reason) and register notices from official Charities Services… | $0.02 per event |
| [Swissmedic Monitor: Authorization Number Status Alerts](https://apify.com/plym-actor-factory/ch-swissmedic-zulassungsnummer-portfolio-status-monitor) | Watch Swissmedic Zulassungsnummer on the official HAM authorized-medicines list. | $0.02 per event |
| [WHO PQ Medicine Monitor: FPP Listing Status Alerts](https://apify.com/plym-actor-factory/who-pq-fpp-reference-number-portfolio-status-monitor) | Watch WHO Prequalification Finished Pharmaceutical Product (FPP) reference numbers on the official PQ list. | $0.02 per event |

---

All Actors: [https://apify.com/plym-actor-factory](https://apify.com/plym-actor-factory). This page is generated automatically from the public Apify Store listing. Data sources are the official public registers named in each Actor's description; this project is not affiliated with those registers.
