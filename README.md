# Official-register change monitors on Apify

Pay-per-event [Apify](https://apify.com) Actors that **watch a portfolio of identifiers** (company numbers, LEIs, licence and permit numbers, facility IDs …) in **official public registers and open-data feeds**, and emit **typed change events** (status changes, insolvency notices, licence revocations, new filings, …) instead of raw data dumps. You pay a small fee only for events actually delivered.

Built for compliance, KYB/KYC, supplier-risk, credit, procurement, legal and data teams who need to know *when something changes* for the entities they care about – run on a schedule, pipe results to webhooks, Slack, sheets or your own systems via the Apify API, or call them from AI agents (MCP).

**51 public Actors** · Browse all on the Apify Store: [apify.com/plym-actor-factory](https://apify.com/plym-actor-factory)

Prices are per delivered event in USD, plus a tiny Apify *Actor start* fee (typically $0.00005 per GB of memory). Always check the Store page for current pricing.

## Contents

- [United Kingdom](#united-kingdom) (10)
- [European Union & wider Europe](#european-union--wider-europe) (8)
- [Cross-border KYB & finance](#cross-border-kyb--finance) (3)
- [United States – federal](#united-states--federal) (19)
- [United States – state](#united-states--state) (2)
- [Canada](#canada) (4)
- [Australia](#australia) (3)
- [Latin America](#latin-america) (1)
- [Global / security](#global--security) (1)

## United Kingdom

| Actor | Use case | Price |
|---|---|---|
| [ESFA APAR UKPRN Portfolio Status Monitor](https://apify.com/plym-actor-factory/uk-esfa-apar-ukprn-status-monitor) | Watch UKPRNs and emit typed APAR APPEARED/DROPPED/STATUS_CHANGED/DELIVER_* events from the official DfE/ESFA Apprenticeship Provider and Assessment Register CSV. | $0.02 per event |
| [UK Charity Commission Portfolio Status Monitor](https://apify.com/plym-actor-factory/uk-charity-commission-portfolio-status-monitor) | Watch a list of England & Wales charity registration numbers and emit typed Registered/Removed/name/interim-manager events from the official Charity Commission Register API (user-supplied key)… | $0.02 per event |
| [UK Companies House Streaming Change Monitor](https://apify.com/plym-actor-factory/uk-companies-house-realtime-monitor) | Companies House change alerts for credit control, KYB and compliance teams: insolvency cases, officer/director and PSC changes, new or satisfied charges, filings and status changes for your company… | $0.015 per event |
| [UK FCA Register Firm Status Monitor (FRN Watchlist)](https://apify.com/plym-actor-factory/uk-fca-frn-portfolio-status-monitor) | FCA Register monitoring for principal firms, partnership and third-party-risk teams: watch FRNs and get events when a firm is cancelled or suspended, permissions change, Appointed Representatives… | $0.02 per event |
| [UK FSA AppNo Portfolio Status Monitor](https://apify.com/plym-actor-factory/uk-fsa-appno-portfolio-monitor) | Watch FSA Approval Numbers (AppNo) and emit typed APPEARED/DROPPED/ACTIVITIES_CHANGED/AUTHORITY_CHANGED events from the official FSA Approved Food Establishments daily CSV (OGL v3). | $0.02 per event |
| [UK Gambling Commission Licence Portfolio Status Monitor](https://apify.com/plym-actor-factory/uk-gambling-commission-licence-portfolio-monitor) | Watch Gambling Commission Account Numbers and/or Licence Numbers and emit typed Active/Suspended/Revoked/Surrendered/Lapsed events from the official OGL business-licence-register-licences.csv… | $0.02 per event |
| [UK Multi-Trade Planning Lead Radar](https://apify.com/plym-actor-factory/uk-planning-trade-lead-radar) | Match new England planning applications to multi-trade taxonomy (solar/PV/battery, roof, scaffold, extension/loft, HVAC, glazing) + optional postcode radius via planning.data.gov.uk (OGL). | $0.02 per event |
| [UK Ofsted URN Portfolio Inspection Outcome Event Monitor](https://apify.com/plym-actor-factory/uk-ofsted-urn-portfolio-inspection-monitor) | Watch a book of England state-funded school URNs and emit typed inspection-outcome / overall-effectiveness / safeguarding-inclusion-curriculum standard events from the official Ofsted monthly MI CSV… | $0.02 per event |
| [UK Sanctions List Change Monitor (FCDO UKSL)](https://apify.com/plym-actor-factory/uk-sanctions-list-counterparty-portfolio-watch) | Track changes to the UK Sanctions List entries you are exposed to: watch FCDO UKSL Unique IDs and get DELISTED, VARIATION (regime, sanctions, names) and DESIGNATED events from the official UKSL file. | $0.02 per event |
| [UK SRA Firm Portfolio Status Monitor](https://apify.com/plym-actor-factory/uk-sra-firm-portfolio-status-monitor) | Watch a list of SRA firm numbers and emit typed Authorised/Intervention/Closed/licence events from the official SRA Data Share API (user-supplied Azure APIM subscription key). | $0.02 per event |

## European Union & wider Europe

| Actor | Use case | Price |
|---|---|---|
| [Czech ARES IČO Portfolio Status Monitor](https://apify.com/plym-actor-factory/czech-ares-ico-portfolio-monitor) | Watch a list of Czech IČO numbers and emit typed AKTIVNI/ZANIKLY/name/seat/register-status events from free official ARES REST (ares.gov.cz). | $0.02 per event |
| [EU TR Organisation ID Portfolio Status Event Monitor](https://apify.com/plym-actor-factory/eu-tr-org-portfolio-status-monitor) | Watch Transparency Register identificationCodes and emit typed REMOVED / APPEARED / LAST_UPDATE_CHANGED / CATEGORY_CHANGED events from the official EU open-data XML snapshot. | $0.02 per event |
| [Finland PRH Y-tunnus Portfolio Status Monitor](https://apify.com/plym-actor-factory/finland-prh-ytunnus-portfolio-monitor) | Watch a list of Finnish Y-tunnukset and emit typed Business-ID / trade-register / konkurssi / saneeraus / selvitystila / name events from free official PRH YTJ open data (avoindata.prh.fi). | $0.02 per event |
| [France BODACC SIREN Portfolio Event Monitor](https://apify.com/plym-actor-factory/france-bodacc-siren-portfolio-monitor) | Watch a list of French SIRENs and emit typed BODACC gazette events — insolvency, modifications, radiations, cessions — from official DILA open data (Licence Ouverte). | $0.02 per event |
| [Netherlands KvK Open-Data Status Event Monitor](https://apify.com/plym-actor-factory/netherlands-kvk-status-event-monitor) | Watch a list of Dutch KVK numbers and emit typed active/insolvency status events from free official HVDS open data (BV/NV only). | $0.02 per event |
| [Norway Brønnøysundregistret Orgnr Portfolio Status Monitor](https://apify.com/plym-actor-factory/norway-brreg-orgnr-portfolio-monitor) | Watch a list of Norwegian organisasjonsnumre and emit typed konkurs / under avvikling / slettet / name / address events from the free official Brreg Enhetsregisteret API (NLOD). | $0.02 per event |
| [Spain BORME NIF Portfolio Event Monitor](https://apify.com/plym-actor-factory/spain-borme-nif-portfolio-monitor) | Watch a list of Spanish NIFs (with company legal names) and emit typed BORME gazette events — appointments, capital, insolvency, dissolution, address/name changes — from official BOE open data. | $0.02 per event |
| [Switzerland SHAB UID Portfolio Event Monitor](https://apify.com/plym-actor-factory/switzerland-shab-uid-portfolio-monitor) | Watch a list of Swiss CHE UIDs and emit typed SHAB / official gazette events — new registrations, modifications, deletions, bankruptcies — from Amtsblattportal. | $0.02 per event |

## Cross-border KYB & finance

| Actor | Use case | Price |
|---|---|---|
| [DACH Supplier KYB: VIES VAT Check, Impressum & Insolvency](https://apify.com/plym-actor-factory/dach-supplier-kyb-packet) | Supplier verification and vendor onboarding for German, Austrian and Swiss suppliers: from a supplier website, one KYB packet with Impressum identity, a live VIES VAT check and a German… | $0.02 per event |
| [GLEIF LEI Monitor: Lapsed LEI & Entity Change Watch](https://apify.com/plym-actor-factory/gleif-lei-portfolio-watch) | LEI monitoring for regulatory-reporting, treasury and onboarding teams: watch counterparty LEIs and get events when an LEI lapses, is retired or annulled, the entity goes inactive, the legal name or… | $0.02 per event |
| [Poland Supplier Verification: VAT White List & Bank Check](https://apify.com/plym-actor-factory/poland-supplier-kyb-packet) | Supplier verification for AP, treasury and procurement teams paying Polish suppliers: per NIP, one KYB packet with official MF VAT White List status, bank account verification (accountAssigned) with… | $0.02 per event |

## United States – federal

| Actor | Use case | Price |
|---|---|---|
| [CARB LCFS Fuel Pathway Portfolio Status Monitor](https://apify.com/plym-actor-factory/us-carb-lcfs-fuel-pathway-status-monitor) | Watch CARB LCFS fuel pathway IDs and emit typed CERTIFIED/RETIRED/APPEARED/DROPPED/CI events from the official Current Fuel Pathways spreadsheet. | $0.02 per event |
| [College Scorecard Operating Status Portfolio Monitor](https://apify.com/plym-actor-factory/us-college-scorecard-operating-portfolio-monitor) | Watch IPEDS UNITIDs / OPEIDs and emit typed OPERATING_OPEN / OPERATING_CLOSED / OWNERSHIP_CHANGED events from the official US ED College Scorecard API. | $0.02 per event |
| [EPA GHGRP Facility ID Reporting Status Monitor](https://apify.com/plym-actor-factory/us-epa-ghgrp-facility-status-monitor) | Watch GHGRP facility_ids and emit typed STOPPED_REPORTING / RESUMED_REPORTING / YEAR_APPEARED / YEAR_DROPPED / PARENT_CHANGED events from EPA Envirofacts PUB_DIM_FACILITY. | $0.02 per event |
| [EPA PPIS Registration Number Status Monitor](https://apify.com/plym-actor-factory/us-epa-ppis-registration-number-status-monitor) | Watch EPA pesticide Registration Numbers and emit typed ACTIVE/CANCELLED/APPEARED/DROPPED events from the official weekly PPIS XML zip. | $0.02 per event |
| [EPA TSCA Inventory CASRN Activity Status Monitor](https://apify.com/plym-actor-factory/us-epa-tsca-inventory-casrn-status-monitor) | Watch CASRNs and emit typed ACTIVITY_ACTIVE/INACTIVE, FLAG_CHANGED, APPEARED, DROPPED events from the official EPA non-CBI TSCA Inventory CSV zip. | $0.02 per event |
| [FDA AccessGUDID DI Commercial Distribution Status Monitor](https://apify.com/plym-actor-factory/us-fda-accessgudid-di-status-monitor) | Watch Primary Device Identifiers and emit typed DISTRIBUTION_STATUS_CHANGED / RECORD_STATUS_CHANGED / APPEARED / DROPPED events from NLM AccessGUDID. | $0.02 per event |
| [FMCSA Carrier Monitoring: Insurance, Authority & OOS Alerts](https://apify.com/plym-actor-factory/fmcsa-safer-risk-event-monitor) | Carrier monitoring for freight brokers, 3PLs and shippers: watch your USDOT numbers and get events when FMCSA data shows an insurance cancellation, authority revoked or suspended, an out-of-service… | $0.025 per event |
| [H-1B LCA Employer New-Filing Watchlist (honest quarterly lag)](https://apify.com/plym-actor-factory/h1b-lca-employer-filing-watchlist) | Watch a list of employers (names or FEINs) and emit typed LCA_NEW_FILING events when new cases appear in official DOL OFLC public disclosure Excel/open data. | $0.02 per event |
| [MSHA Mine ID Portfolio Status Monitor](https://apify.com/plym-actor-factory/us-msha-mine-id-status-monitor) | Watch MSHA Mine IDs and emit typed ACTIVE/STATUS_CHANGED/ABANDONED_OR_NONPRODUCING/CONTROLLER_CHANGED/OPERATOR_CHANGED/REAPPEARED events from the official MSHA Open Government Data Mines.zip register. | $0.02 per event |
| [TTB Alcohol Permit Portfolio Status Monitor](https://apify.com/plym-actor-factory/us-ttb-alcohol-permit-status-monitor) | Watch TTB Permit_Numbers and emit typed APPEARED/DROPPED/NEW_FLAG/INDUSTRY_CHANGED events from the official TTB FOIA List of Permittees JSON. | $0.02 per event |
| [US CMS Medicare PPEF NPI Portfolio Enrollment Status Monitor](https://apify.com/plym-actor-factory/us-cms-ppef-npi-portfolio-enrollment-monitor) | Watch NPIs and emit typed ENROLLED/DROPPED/PROVIDER_TYPE_CHANGED/ENROLLMENT_ID_CHANGED events from the official CMS data.cms.gov Medicare Fee-For-Service Public Provider Enrollment (PPEF) extract. | $0.02 per event |
| [US ENERGY STAR Unique ID (pd_id) Portfolio Status Monitor](https://apify.com/plym-actor-factory/us-energy-star-pd-id-portfolio-monitor) | Watch ENERGY STAR Unique IDs (pd_id) and emit typed APPEARED/DROPPED/MOST_EFFICIENT events from the official EPA ENERGY STAR Model Index Socrata. | $0.02 per event |
| [US EPA Safer Choice Portfolio Status Monitor](https://apify.com/plym-actor-factory/us-epa-safer-choice-portfolio-monitor) | Watch Safer Choice products/companies (UPC/GTIN, company_name, product_url) and emit typed APPEARED/DROPPED/GOOD_STANDING events from the official EPA Envirofacts Safer Choice table. | $0.02 per event |
| [US EPA SDWIS PWSID Portfolio Activity Status Monitor](https://apify.com/plym-actor-factory/us-epa-sdwis-pwsid-portfolio-status-monitor) | Watch EPA Public Water System IDs (PWSIDs) and emit typed ACTIVE/ACTIVITY_CHANGED/DEACTIVATED/REACTIVATED events from the official EPA Envirofacts WATER_SYSTEM JSON API. | $0.02 per event |
| [US EPA TRI Facility ID Portfolio Status Monitor](https://apify.com/plym-actor-factory/us-epa-tri-facility-portfolio-status-monitor) | Watch TRI Facility IDs and emit typed APPEARED/DROPPED/NAME_CHANGED/PARENT_CHANGED/ADDRESS_CHANGED events from the official EPA Envirofacts tri_facility JSON API. | $0.02 per event |
| [US HRSA Health Center / Look-Alike Site Status Monitor](https://apify.com/plym-actor-factory/us-hrsa-health-center-site-monitor) | Watch Health Center Numbers and/or BPHC site keys and emit typed Active/Inactive/type/location-setting events from the official HRSA data.hrsa.gov Health Center Service Delivery and Look-Alike Sites… | $0.02 per event |
| [US LDA Lobbying Client & Registrant New-Filing Watchlist](https://apify.com/plym-actor-factory/us-lda-lobbying-filing-watchlist) | Watch lobbying client and/or registrant firm names; poll the official Senate LDA REST API (lda.gov); emit typed events only for new filing_uuid values for your book. | $0.02 per event |
| [USDA FSIS MPI Est# Portfolio Status Monitor](https://apify.com/plym-actor-factory/us-fsis-mpi-est-status-monitor) | Watch FSIS establishment numbers and emit typed APPEARED/DROPPED_OR_INACTIVE/ACTIVITIES_CHANGED/SIZE_CHANGED/GRANT_DATE_CHANGED events from the official USDA FSIS MPI Directory JSON API/CSV. | $0.02 per event |
| [USDA SNAP Record_ID Authorization Status Monitor](https://apify.com/plym-actor-factory/us-usda-snap-record-id-authorization-status-monitor) | Watch USDA SNAP retailer Record_IDs and emit typed AUTHORIZED/ENDED/APPEARED/DROPPED events from the official FNS SNAP ArcGIS FeatureServer. | $0.02 per event |

## United States – state

| Actor | Use case | Price |
|---|---|---|
| [California CSLB Contractor License Risk Event Monitor](https://apify.com/plym-actor-factory/us-contractor-license-risk-monitor) | Watch a book of California CSLB contractor license numbers and emit typed risk events (LICENSE_*/BOND_*/WORKERS_COMP_*) from official CSLB Public Data Portal bulk files. | $0.025 per event |
| [Illinois IDFPR License Portfolio Status Monitor](https://apify.com/plym-actor-factory/us-il-idfpr-license-portfolio-monitor) | Watch Illinois IDFPR license_number values and emit typed ACTIVE/status/expiry/discipline/reappeared events from official Illinois Open Data Socrata pzzh-kp68. | $0.02 per event |

## Canada

| Actor | Use case | Price |
|---|---|---|
| [Canada Federal Corporation Status Portfolio Monitor](https://apify.com/plym-actor-factory/canada-federal-corp-status-monitor) | Watch federal corporation numbers / BNs and emit typed status & name change events from the free official ISED Corporations Canada API. | $0.02 per event |
| [Canada PMRA PCP Registration Number Status Monitor](https://apify.com/plym-actor-factory/ca-pmra-registration-number-portfolio-status-monitor) | Watch Canada PMRA PCP Registration Numbers; emit FULL_REGISTRATION/CANCELLED/APPEARED/DROPPED/STATUS_CHANGED/EXPIRY_CHANGED from official product extract CSV. | $0.02 per event |
| [CFIA SFCR Food Licence Portfolio Status Monitor](https://apify.com/plym-actor-factory/ca-cfia-sfcr-licence-portfolio-monitor) | Watch CFIA SFCR Food licence numbers and emit typed APPEARED/DROPPED/ESTABLISHMENTS_CHANGED/DBA_CHANGED events from the official CFIA Food Licence Registry CSV (Open Government Licence — Canada). | $0.02 per event |
| [Health Canada DPD DIN Portfolio Status Event Monitor](https://apify.com/plym-actor-factory/ca-hc-dpd-din-portfolio-status-monitor) | Watch Drug Identification Numbers (DIN) and emit typed Marketed/Cancelled/Dormant/Approved/company events from the official Health Canada Drug Product Database (DPD) API. | $0.02 per event |

## Australia

| Actor | Use case | Price |
|---|---|---|
| [ACMA Radiocomms Licence Portfolio Status Monitor](https://apify.com/plym-actor-factory/au-acma-licence-portfolio-monitor) | Watch ACMA radiocommunications LICENCE_NO values and emit typed Granted/status/expiry/category/client events from the official Spectrum Licensing LicenceSearchJSON API (optional RRL extracts). | $0.02 per event |
| [Australia ABN Status Portfolio Monitor](https://apify.com/plym-actor-factory/australia-abn-status-portfolio-monitor) | Watch a list of Australian Business Numbers and emit typed ABN status / GST / entity name+type change events from free official ABR GUID web services. | $0.02 per event |
| [Australia APVMA Product No Portfolio Status Monitor](https://apify.com/plym-actor-factory/au-apvma-product-number-portfolio-status-monitor) | Watch Australia APVMA Product Numbers (pcode) and emit typed REGISTERED/APPROVED/APPEARED/DROPPED/REGCODE_CHANGED/EXPIRY_CHANGED events from data.gov.au PUBCRIS product.csv. | $0.02 per event |

## Latin America

| Actor | Use case | Price |
|---|---|---|
| [Brazil CNPJ Situação Change Monitor (honest monthly lag)](https://apify.com/plym-actor-factory/brazil-cnpj-situacao-change-monitor) | Watch a list of Brazilian CNPJs and emit typed situação cadastral / material change events from Receita Federal dados abertos (or equivalent open-data mirror). | $0.02 per event |

## Global / security

| Actor | Use case | Price |
|---|---|---|
| [Lookalike Domain CT Brand-Abuse Monitor](https://apify.com/plym-actor-factory/lookalike-ct-brand-abuse-monitor) | Generate lookalikes (dnstwist-class, in-process) for brand apexes, join public CT via crt.sh, and emit LOOKALIKE_CERT_ISSUED events when a lookalike gets a new TLS cert. | $0.02 per event |

---

All Actors: [https://apify.com/plym-actor-factory](https://apify.com/plym-actor-factory). This page is generated automatically from the public Apify Store listing. Data sources are the official public registers named in each Actor's description; this project is not affiliated with those registers.
