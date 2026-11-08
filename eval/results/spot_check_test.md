# Human spot-check of generated answers

For each answer, mark **Correct** (yes / partial / no) and **Faithful** (yes / no),
then compare with the judge's verdict below it.

## q003 (scenario) A startup wants to build a face recognition database by scraping photos from social media and CCTV. Is that allowed?

**Reference:** Prohibited: untargeted scraping of facial images to create facial recognition databases (Art. 5(1)(e)).

**Answer:** The AI Act expressly prohibits the placing on the market, putting into service, or use of AI systems that create or expand facial‑recognition databases through untargeted scraping of facial images from the internet or CCTV footage [2]. Recital 43 reinforces that such practice should be prohibited because it threatens fundamental rights such as privacy [1]. Therefore, a startup may not build a face‑recognition database by scraping social‑media or CCTV images.

**Sources cited:** [1] AI Act Recital 43, [2] AI Act Article 5(1) - Prohibited AI practices

**Judge:** correct=yes, faithful=True (The answer correctly identifies that the practice is prohibited under Article 5(1)(e) and supported by Recital 43, accurately reflecting the reference note and sources.)

**Your verdict:** Correct = ___ · Faithful = ___

## q004 (plain) Can the police use live facial recognition in public streets?

**Reference:** Prohibited in principle, with narrow exceptions (targeted search for victims, imminent threats, serious crimes) subject to authorisation (Art. 5(1)(h), 5(2)-(3)).

**Answer:** Police (law‑enforcement authorities) may use a real‑time remote biometric identification system – i.e. live facial‑recognition – in publicly accessible spaces only if the use is strictly necessary for one of the limited objectives listed in Article 5(1)(h) (e.g., targeted search for missing persons, prevention of an imminent threat to life or safety, or localisation of a person suspected of a specific offence punishable by at least four years’ imprisonment) [4]. Even then, the deployment must be limited to confirming the identity of the specifically targeted individual, take into account the seriousness, probability and scale of the harm and of the impact on rights and freedoms, and be authorised after a fundamental‑rights impact assessment and registration in the EU database (or, in urgent cases, registration without undue delay) [1][3]. The use must also be notified to the national market‑surveillance and data‑protection authorities as a minimum, without disclosing sensitive operational data [2].

**Sources cited:** [1] AI Act Article 5(2) - Prohibited AI practices, [2] AI Act Article 5(4) - Prohibited AI practices, [3] AI Act Article 5(2) - Prohibited AI practices, [4] AI Act Article 5(1) - Prohibited AI practices

**Judge:** correct=yes, faithful=True (The answer accurately reflects the reference note by stating that live facial recognition is prohibited in principle but allowed under narrow exceptions (targeted search, imminent threats, serious crimes) subject to specific authorizations and safeguards, all of which are supported by the cited sources.)

**Your verdict:** Correct = ___ · Faithful = ___

## q007 (plain) What is the difference between a provider and a deployer of an AI system?

**Reference:** Provider develops or has developed an AI system and places it on the market under its name (Art. 3(3)); deployer uses it under its authority (Art. 3(4)).

**Answer:** A “provider” is the natural or legal person that makes an AI system available – for example by developing, placing it on the market or otherwise supplying it, including general‑purpose systems that generate synthetic content [1][3]. A “deployer” is any natural or legal person, including public authorities, that uses an AI system under its authority (except for personal non‑professional use) and therefore must comply with obligations such as human oversight and registration [2][4][6]. In short, providers supply the system; deployers operate it.

**Sources cited:** [1] AI Act Article 50(2) - Transparency obligations for providers and deployers of certain AI systems, [2] AI Act Recital 13, [3] AI Act Article 50(1) - Transparency obligations for providers and deployers of certain AI systems, [4] AI Act Article 26(2) - Obligations of deployers of high-risk AI systems, [6] AI Act Article 26(1) - Obligations of deployers of high-risk AI systems

**Judge:** correct=partial, faithful=False (The answer correctly defines the deployer but fails to cite the specific definition of a provider (Art. 3(3)) and instead cites sources regarding transparency obligations (Art. 50) which do not define the term, making the provider definition unsupported by the provided sources.)

**Your verdict:** Correct = ___ · Faithful = ___

## q010 (scenario) A university wants an AI system to decide which students get admitted. What does the AI Act say?

**Reference:** High-risk: AI determining access or admission to education (Annex III point 3(a)).

**Answer:** The AI Act classifies an AI system that decides university admissions as a high‑risk AI system because it determines access or admission to an educational institution and can materially influence a person’s future livelihood [1][6]. Such systems are listed in Annex III under the education and vocational‑training category and must comply with the high‑risk obligations (e.g., conformity assessment, transparency, monitoring, and registration in the EU database) imposed on providers and deployers [4][6][7][8]. The university, as the deployer, would therefore have to ensure the system meets those requirements before putting it into service.

**Sources cited:** [1] AI Act Recital 56, [4] AI Act Annex III - High-risk AI systems referred to in Article 6(2), [6] AI Act Annex III - High-risk AI systems referred to in Article 6(2), [7] AI Act Article 71(5) - EU database for high-risk AI systems listed in Annex III, [8] AI Act Article 71(3) - EU database for high-risk AI systems listed in Annex III

**Judge:** correct=yes, faithful=True (The answer correctly identifies the system as high-risk under Annex III point 3(a) and accurately cites the relevant sources for the classification and obligations.)

**Your verdict:** Correct = ___ · Faithful = ___

## q012 (plain) Can an AI system listed in Annex III escape the high-risk classification?

**Reference:** Yes, if it does not pose a significant risk, e.g. performs a narrow procedural task, improves a prior human activity, or a preparatory task; never if it profiles natural persons. The provider must document the assessment (Art. 6(3)-(4)).

**Answer:** Yes, an AI system that appears in Annex III can avoid being classified as high‑risk if it does not pose a significant risk to health, safety or fundamental rights and meets one of the listed conditions – e.g., it performs only a narrow procedural task, improves a completed human activity, merely detects decision‑making patterns without replacing human assessment, or carries out a preparatory task for a relevant assessment, provided it does not involve profiling of natural persons [2]. In that case the provider must document the assessment before the system is placed on the market or put into service and remain subject to the registration obligation under Article 49(2) [3].

**Sources cited:** [2] AI Act Article 6(3) - Classification rules for high-risk AI systems, [3] AI Act Article 6(4) - Classification rules for high-risk AI systems

**Judge:** correct=yes, faithful=True (The answer accurately reflects the derogation conditions in Article 6(3) and the documentation/registration requirements in Article 6(4) as cited in the sources, aligning perfectly with the reference note.)

**Your verdict:** Correct = ___ · Faithful = ___

## q014 (plain) What quality rules apply to the training data of high-risk AI systems?

**Reference:** Data governance practices; datasets relevant, sufficiently representative and, to the best extent possible, free of errors and complete (Art. 10(2)-(3)).

**Answer:** High‑risk AI systems that use model‑training techniques must be built on training data sets that meet the quality criteria set out in Article 10 (1) of the AI Act [1]. Those data sets must be relevant, sufficiently representative, as free of errors as possible and complete for the intended purpose, and must have appropriate statistical properties, including respect for the persons or groups the system is meant to serve [2]. In addition, the training data must be governed and managed according to the practices listed in Article 10 (2), which cover design choices, data‑collection origins and original purpose (especially for personal data), preparation operations (annotation, cleaning, etc.), formulation of assumptions, assessment of availability and suitability, bias examination and mitigation, and identification of data gaps [3].

**Sources cited:** [1] AI Act Article 10(1) - Data and data governance, [2] AI Act Article 10(3) - Data and data governance, [3] AI Act Article 10(2) - Data and data governance

**Judge:** correct=yes, faithful=True (The answer accurately cites Article 10(1) for the applicability of quality criteria, Article 10(3) for the specific data quality requirements (relevant, representative, error-free, complete), and Article 10(2) for the data governance practices, all of which are fully supported by the provided sources and align with the reference note.)

**Your verdict:** Correct = ___ · Faithful = ___

## q016 (plain) Does a human need to be able to stop or override a high-risk AI system?

**Reference:** Yes: designed for effective human oversight, including the ability to disregard, override or interrupt the system, e.g. via a stop button (Art. 14(4)).

**Answer:** Yes. Article 14(4)(e) of the AI Act requires that high‑risk AI systems be provided so that natural persons assigned human oversight can intervene in the operation or interrupt the system – for example via a “stop” button or similar procedure that brings the system to a safe state [3]. This is part of the broader human‑oversight obligations for high‑risk AI.

**Sources cited:** [3] AI Act Article 14(4) - Human oversight

**Judge:** correct=yes, faithful=True (The answer correctly identifies that Article 14(4)(e) requires the ability to intervene or interrupt the system (e.g., via a stop button), which aligns with the reference note's requirement for effective human oversight including the ability to stop or override.)

**Your verdict:** Correct = ___ · Faithful = ___

## q018 (plain) What are the obligations of a company that uses, but did not build, a high-risk AI system?

**Reference:** Deployers must follow the instructions for use, assign competent human oversight, monitor operation, keep logs and inform affected persons (Art. 26).

**Answer:** A company that deploys a high‑risk AI system must check that the system is registered in the EU database referred to in Article 71; if it is not, the company must refrain from using the system and must inform the provider or the distributor of the non‑registration [5]. The AI Act does not contain further obligations for deployers that are not public authorities, so other duties (e.g., conformity‑assessment or CE‑marking) are not addressed for such users in the provided texts.

**Sources cited:** [5] AI Act Article 26(8) - Obligations of deployers of high-risk AI systems

**Judge:** correct=no, faithful=False (The answer incorrectly claims that non-public authority deployers have no further obligations and that duties like conformity assessment are not addressed, whereas the reference note explicitly lists obligations for deployers (such as following instructions, human oversight, and monitoring) under Article 26, and the provided sources (specifically Art 25) indicate that deployers can assume provider obligations (including conformity assessment) under certain conditions.)

**Your verdict:** Correct = ___ · Faithful = ___

## q019 (scenario) Before rolling out a high-risk AI tool to monitor staff performance, do we have to tell our employees?

**Reference:** Yes: employers must inform workers' representatives and affected workers before using a high-risk AI system at the workplace (Art. 26(7)).

**Answer:** Yes. Under Article 26(7) of the AI Act, deployers who are employers must inform workers’ representatives and the affected workers that they will be subject to the use of a high‑risk AI system before it is put into service or used at the workplace [1].

**Sources cited:** [1] AI Act Article 26(7) - Obligations of deployers of high-risk AI systems

**Judge:** correct=yes, faithful=True (The answer correctly identifies the obligation to inform workers' representatives and affected workers under Article 26(7) of the AI Act, which is fully supported by the provided source.)

**Your verdict:** Correct = ___ · Faithful = ___

## q020 (exact) Who has to carry out a fundamental rights impact assessment under the AI Act?

**Reference:** Deployers that are public bodies or private entities providing public services, and deployers of credit scoring or life/health insurance pricing systems, before deploying Annex III high-risk systems (Art. 27(1)).

**Answer:** Deployers must carry out the assessment. Specifically, the AI Act requires that “deployers that are bodies governed by public law, or are private entities providing public services, and deployers of high‑risk AI systems referred to in points 5 (b) and (c) of Annex III” perform a fundamental‑rights impact assessment before putting the system into use [5]. Recital 96 reinforces this by stating that “deployers of high‑risk AI systems that are bodies governed by public law, or private entities providing public services… should carry out a fundamental rights impact assessment prior to putting it into use” [3].

**Sources cited:** [3] AI Act Recital 96, [5] AI Act Article 27(1) - Fundamental rights impact assessment for high-risk AI systems

**Judge:** correct=yes, faithful=True (The answer correctly identifies the specific deployers (public bodies, private entities providing public services, and deployers of Annex III 5(b)/(c) systems) required to perform the assessment, accurately reflecting the reference note and supported by the cited sources.)

**Your verdict:** Correct = ___ · Faithful = ___

## q022 (plain) Do deepfakes have to be labelled?

**Reference:** Yes: deployers must disclose that deep fake content has been artificially generated or manipulated, with lighter rules for artistic or satirical works (Art. 50(4)).

**Answer:** Yes. Deployers of AI systems that generate or manipulate image, audio or video content creating a deep‑fake must disclose that the content has been artificially generated or manipulated, unless the use is authorised by law for criminal‑law purposes or the content is part of an artistic, satirical or similar work where only a limited disclosure is required [1].

**Sources cited:** [1] AI Act Article 50(4) - Transparency obligations for providers and deployers of certain AI systems

**Judge:** correct=yes, faithful=True (The answer correctly identifies the disclosure obligation for deepfakes under Article 50(4) and accurately describes the exceptions for criminal law purposes and artistic/satirical works, fully supported by the cited source.)

**Your verdict:** Correct = ___ · Faithful = ___

## q025 (plain) What do companies releasing large foundation models have to do under the AI Act?

**Reference:** GPAI providers: technical documentation, information for downstream providers, a copyright compliance policy, and a public summary of training content (Art. 53(1)).

**Answer:** Companies that release large foundation (general‑purpose) models must first check whether the model is classified as a high‑risk AI system or falls under Article 5 or 50; otherwise the AI Act does not apply to open‑source releases [1]. If the model is considered high‑risk, the provider is subject to the full set of provider obligations (e.g., conformity assessment, documentation and post‑market monitoring) and must ensure that any third‑party components are covered by written agreements specifying the information and assistance needed for compliance [7][6]. The Commission will maintain a public list of general‑purpose AI models that pose systemic risk, which the provider must monitor for inclusion [2]. Where the model conforms to harmonised standards published in the Official Journal, it is presumed to meet the relevant requirements [5]. Finally, providers may be invited to participate in AI regulatory sandboxes, with priority access for SMEs and start‑ups, to help achieve compliance and foster innovation [3][4].

**Sources cited:** [1] AI Act Article 2(12) - Scope, [2] AI Act Article 52(6) - Procedure, [3] AI Act Article 57(9) - AI regulatory sandboxes, [4] AI Act Article 62(1) - Measures for providers and deployers, in particular SMEs, including start-ups, [5] AI Act Article 40(1) - Harmonised standards and standardisation deliverables, [6] AI Act Article 25(4) - Responsibilities along the AI value chain, [7] AI Act Article 25(1) - Responsibilities along the AI value chain

**Judge:** correct=no, faithful=False (The answer fails to mention the specific mandatory obligations for GPAI providers (technical documentation, information for downstream providers, copyright policy, and training data summary) required by the reference note, and instead provides irrelevant or conditional information about high-risk systems and open-source exemptions.)

**Your verdict:** Correct = ___ · Faithful = ___

## q028 (exact) What is the maximum fine for using a prohibited AI practice?

**Reference:** Up to EUR 35 million or 7% of total worldwide annual turnover, whichever is higher (Art. 99(3)).

**Answer:** The AI Act provides that non‑compliance with the prohibition of AI practices set out in Article 5 is punishable by an administrative fine of up to €35 million, or, for an undertaking, up to 7 % of its total worldwide annual turnover for the preceding financial year, whichever is higher (Article 99(3)) [1]. For Union institutions, bodies, offices and agencies the ceiling is lower – up to €1.5 million (Article 100(2)) [5]. The higher fine applies to private undertakings.

**Sources cited:** [1] AI Act Article 99(3) - Penalties, [5] AI Act Article 100(2) - Administrative fines on Union institutions, bodies, offices and agencies

**Judge:** correct=yes, faithful=True (The answer correctly states the maximum fine of EUR 35 million or 7% of worldwide turnover as per the reference note and accurately cites the relevant sources for both private undertakings and Union institutions.)

**Your verdict:** Correct = ___ · Faithful = ___

## q029 (plain) How much can a company be fined for breaking the high-risk AI rules?

**Reference:** Up to EUR 15 million or 3% of worldwide annual turnover, whichever is higher (Art. 99(4)).

**Answer:** A company that breaches the high‑risk AI rules can be fined up to €35 million or, if it is an undertaking, up to 7 % of its total worldwide annual turnover for the preceding financial year, whichever is higher [2]. For other obligations related to operators, providers, importers, distributors or notified bodies (but not the prohibitions in Article 5), the maximum fine is €15 million or, for an undertaking, up to 3 % of its worldwide turnover, whichever is higher [6].

**Sources cited:** [2] AI Act Article 99(3) - Penalties, [6] AI Act Article 99(4) - Penalties

**Judge:** correct=yes, faithful=True (The answer correctly identifies the maximum fine for high-risk AI rules (€15 million or 3% of turnover) as per Article 99(4) and accurately distinguishes it from the higher fines for prohibited practices in Article 99(3), with all claims supported by the cited sources.)

**Your verdict:** Correct = ___ · Faithful = ___

## q031 (plain) Are fines lower for startups and small companies under the AI Act?

**Reference:** For SMEs including start-ups, each fine is capped at the lower of the percentage or amount (Art. 99(6)).

**Answer:** Yes. Article 99(6) of the AI Act requires that for SMEs, including start‑ups, any fine must be limited to the lower of the amounts or percentages set out in paragraphs 3, 4 and 5, so their penalties are capped at a lower level than for larger undertakings [1].

**Sources cited:** [1] AI Act Article 99(6) - Penalties

**Judge:** correct=yes, faithful=True (The answer correctly identifies that Article 99(6) caps fines for SMEs and start-ups at the lower of the specified amounts or percentages, which aligns with the reference note and the provided source.)

**Your verdict:** Correct = ___ · Faithful = ___

## q033 (plain) Do companies have to train their staff on AI?

**Reference:** Providers and deployers must ensure a sufficient level of AI literacy of their staff (Art. 4).

**Answer:** Yes. Article 4 of the AI Act requires providers and deployers of AI systems to take measures, as far as possible, to ensure a sufficient level of AI literacy for their staff and anyone else involved in operating or using the systems, taking into account their knowledge, experience, education and the context of use [1].

**Sources cited:** [1] AI Act Article 4 - AI literacy

**Judge:** correct=yes, faithful=True (The answer correctly identifies Article 4 as the basis for the obligation to ensure AI literacy for staff, which aligns with the reference note and is fully supported by the cited source.)

**Your verdict:** Correct = ___ · Faithful = ___

## q034 (scenario) Does the AI Act apply to AI systems developed only for military purposes?

**Reference:** No: systems used exclusively for military, defence or national security purposes are excluded (Art. 2(3)).

**Answer:** The AI Act does not apply to AI systems that are placed on the market, put into service or used exclusively for military, defence or national security purposes, regardless of the type of entity carrying out those activities[4]. This exclusion also covers systems that are not placed on the market or put into service in the Union but whose output is used in the Union solely for those purposes[4].

**Sources cited:** [4] AI Act Article 2(3) - Scope

**Judge:** correct=yes, faithful=True (The answer correctly states that the AI Act does not apply to AI systems used exclusively for military, defence, or national security purposes, accurately reflecting the exclusion in Article 2(3) cited in the source.)

**Your verdict:** Correct = ___ · Faithful = ___

## q037 (plain) Are open-source AI models covered by the AI Act?

**Reference:** Free and open-source AI systems are excluded unless placed on the market as high-risk, prohibited, or Art. 50 systems (Art. 2(12)).

**Answer:** Open‑source AI models are generally outside the scope of the AI Act, but they become covered if they are placed on the market or put into service as high‑risk systems or as an AI system that falls under Article 5 or 50, or if they present systemic risks [3]. The exemption also does not apply to providers of general‑purpose models released under a free and open‑source licence when those models have systemic risks [2][4].

**Sources cited:** [2] AI Act Article 54(6) - Authorised representatives of providers of general-purpose AI models, [3] AI Act Article 2(12) - Scope, [4] AI Act Article 53(2) - Obligations for providers of general-purpose AI models

**Judge:** correct=yes, faithful=True (The answer accurately reflects the exclusion in Article 2(12) for open-source AI systems and correctly identifies the specific exceptions for high-risk, prohibited, or Article 50 systems, as well as the additional obligations for general-purpose models with systemic risks found in Articles 53 and 54.)

**Your verdict:** Correct = ___ · Faithful = ___

## q039 (plain) If a high-risk AI system causes a serious incident, how quickly must the provider report it?

**Reference:** Immediately after establishing a causal link, and no later than 15 days; 2 days for widespread infringements; 10 days in case of death (Art. 73).

**Answer:** The provider must report a serious incident as soon as it has established a causal link (or a reasonable likelihood of such a link) with the high‑risk AI system, and in any case no later than 15 days after it becomes aware of the incident [3]. If the incident involves a death, the report must be sent immediately after the causal relationship is established, but not later than 10 days after awareness [1]. For a widespread infringement or a serious incident defined in Article 3(49)(b), the report must be provided immediately and at most two days after awareness [7]. The other provisions (e.g., for safety‑component devices) limit the scope of reporting but do not change these time limits.

**Sources cited:** [1] AI Act Article 73(4) - Reporting of serious incidents, [3] AI Act Article 73(2) - Reporting of serious incidents, [7] AI Act Article 73(3) - Reporting of serious incidents

**Judge:** correct=yes, faithful=True (The answer accurately reflects the reporting deadlines specified in Article 73 of the AI Act, including the general 15-day limit, the 10-day limit for deaths, and the 2-day limit for widespread infringements, all supported by the provided sources.)

**Your verdict:** Correct = ___ · Faithful = ___

## q040 (scenario) An AI system was used to reject my loan application. Can I ask for an explanation?

**Reference:** Yes: right to a clear and meaningful explanation of the AI system's role in decisions based on Annex III high-risk systems (AI Act Art. 86); GDPR Art. 22 also gives safeguards for solely automated decisions.

**Answer:** Yes, you can request an explanation of the individual decision made by the AI system, because the AI Act provides a right to an explanation of AI‑driven decisions (Article 86(1)) [5]. However, that right does not apply if Union or national law provides an exception or restriction that is compatible with Union law [5]. The sources do not specify whether loan‑scoring systems fall under such an exception, so you may be able to obtain an explanation unless a specific legal exemption applies.

**Sources cited:** [5] AI Act Article 86(2) - Right to explanation of individual decision-making

**Judge:** correct=partial, faithful=False (The answer cites Article 86(1) for the right to explanation, but the provided source [5] only contains Article 86(2) (the exception clause), not the substantive right in paragraph 1; furthermore, it fails to mention the GDPR Art. 22 safeguards and the specific applicability to Annex III high-risk systems (creditworthiness) as required by the reference note.)

**Your verdict:** Correct = ___ · Faithful = ___

## q042 (plain) What makes consent valid under the GDPR, and can I withdraw it?

**Reference:** Freely given, specific, informed and unambiguous (Art. 4(11)); controller must demonstrate it; it can be withdrawn at any time as easily as given (Art. 7).

**Answer:** Consent is valid when the controller can demonstrate that the data subject has freely given it, that it is presented in a clearly distinguishable, intelligible and plain‑language form separate from other matters, and that the subject’s freedom to consent is not conditioned on a contract unless the processing is necessary for that contract [4][2][3]. The controller must also give the data subject all required information, including the right to withdraw consent at any time without affecting the lawfulness of prior processing [1][6]. The data subject may withdraw consent whenever they wish, and the withdrawal must be as easy as giving consent [1].

**Sources cited:** [1] GDPR Article 7(3) - Conditions for consent, [2] GDPR Article 7(4) - Conditions for consent, [3] GDPR Article 7(2) - Conditions for consent, [4] GDPR Article 7(1) - Conditions for consent, [6] GDPR Article 14(2) - Information to be provided where personal data have not been obtained from the data subject

**Judge:** correct=partial, faithful=True (The answer correctly cites the sources for the conditions of consent and withdrawal, but it omits the explicit definition of consent as 'specific' and 'unambiguous' found in Article 4(11) (which is not in the provided sources), whereas the reference note explicitly includes these key elements.)

**Your verdict:** Correct = ___ · Faithful = ___

## q046 (plain) Can I ask a company what data it holds about me and get a copy?

**Reference:** Yes: right of access, including a copy of the personal data (Art. 15).

**Answer:** Yes. Under Article 15(1) of the GDPR you have the right to obtain from the controller confirmation of whether personal data concerning you are being processed and, if so, to access those data together with information such as the purposes, categories and recipients of the data [6]. The controller must also provide you with a copy of the personal data undergoing processing, and may charge a reasonable fee for additional copies, especially when the request is made electronically [1]. The right to obtain a copy must not adversely affect the rights and freedoms of others [2].

**Sources cited:** [1] GDPR Article 15(3) - Right of access by the data subject, [2] GDPR Article 15(4) - Right of access by the data subject, [6] GDPR Article 15(1) - Right of access by the data subject

**Judge:** correct=yes, faithful=True (The answer correctly identifies the right of access under Article 15 of the GDPR, including the right to a copy, and all factual claims are accurately supported by the cited sources.)

**Your verdict:** Correct = ___ · Faithful = ___

## q048 (scenario) I'm switching banks. Can I take my data with me in a usable format?

**Reference:** Right to data portability: receive data in a structured, commonly used, machine-readable format and transmit it to another controller (Art. 20).

**Answer:** Yes. Under Article 20(2) of the GDPR you have the right to have your personal data transmitted directly from your current bank to the new one, where this is technically feasible [7]. If the transfer involves a third country or international organisation, the bank must also inform you of the safeguards it relies on for that transfer [6]. This is information, not legal advice.

**Sources cited:** [6] GDPR Article 15(2) - Right of access by the data subject, [7] GDPR Article 20(2) - Right to data portability

**Judge:** correct=partial, faithful=True (The answer correctly cites the right to direct transmission (Art. 20(2)) but fails to mention the core requirement of the right to data portability: receiving data in a structured, commonly used, and machine-readable format, which is the primary mechanism for taking data to a new bank.)

**Your verdict:** Correct = ___ · Faithful = ___

## q049 (plain) Can I stop a company from using my data for direct marketing?

**Reference:** Yes: right to object to direct marketing at any time; the data must then no longer be processed for that purpose (Art. 21(2)-(3)).

**Answer:** Yes. Under the GDPR you have a right to object at any time to the processing of your personal data for direct‑marketing purposes, including any related profiling, and the data must then stop being used for those purposes[1][2]. The right must be presented to you clearly, separately and free of charge[3]. The AI Act does not affect this right.

**Sources cited:** [1] GDPR Article 21(2) - Right to object, [2] GDPR Article 21(3) - Right to object, [3] GDPR Recital 70

**Judge:** correct=yes, faithful=True (The answer correctly identifies the right to object to direct marketing under GDPR Article 21(2)-(3) and accurately cites the sources for the right, the cessation of processing, and the requirement for clear presentation, while the statement regarding the AI Act is a non-contradictory clarification not supported by the provided sources but not factually incorrect in this context.)

**Your verdict:** Correct = ___ · Faithful = ___

## q051 (plain) How long does a company have to answer my data access request?

**Reference:** Without undue delay and within one month, extendable by two further months where necessary (Art. 12(3)).

**Answer:** A company must reply to a data‑access request without undue delay and, at the latest, within one month of receiving the request; it may extend this deadline by up to two additional months when the request is complex or numerous, and must inform you of any extension within the original month together with the reasons for the delay [1].

**Sources cited:** [1] GDPR Article 12(3) - Transparent information, communication and modalities for the exercise of the rights of the data subject

**Judge:** correct=yes, faithful=True (The answer accurately reflects the one-month deadline and the two-month extension provision found in the cited source (GDPR Article 12(3)) and the reference note.)

**Your verdict:** Correct = ___ · Faithful = ___

## q052 (exact) How quickly must a personal data breach be reported to the supervisory authority?

**Reference:** Without undue delay and, where feasible, within 72 hours of becoming aware of it (Art. 33(1)).

**Answer:** A controller must notify the supervisory authority of a personal data breach without undue delay and, where feasible, no later than 72 hours after becoming aware of it, unless the breach is unlikely to risk the rights and freedoms of individuals [1].

**Sources cited:** [1] GDPR Article 33(1) - Notification of a personal data breach to the supervisory authority

**Judge:** correct=yes, faithful=True (The answer accurately states the 72-hour deadline and the 'without undue delay' requirement, and correctly includes the exception for breaches unlikely to result in a risk, all of which are supported by the cited source.)

**Your verdict:** Correct = ___ · Faithful = ___

## q055 (plain) Which organisations must appoint a data protection officer?

**Reference:** Public authorities; organisations whose core activities involve large-scale regular and systematic monitoring or large-scale special category data (Art. 37(1)).

**Answer:** A controller or processor must designate a data protection officer when (a) the processing is carried out by a public authority or body (except courts acting in their judicial capacity), (b) its core activities consist of regular and systematic monitoring of data subjects on a large scale, or (c) its core activities consist of large‑scale processing of special categories of data under Article 9 or of data concerning criminal convictions and offences under Article 10 [6]. A group of undertakings may also appoint a single DPO, provided the officer is easily accessible from each establishment [1]. The DPO may be a staff member or work under a service contract [2].

**Sources cited:** [1] GDPR Article 37(2) - Designation of the data protection officer, [2] GDPR Article 37(6) - Designation of the data protection officer, [6] GDPR Article 37(1) - Designation of the data protection officer

**Judge:** correct=yes, faithful=True (The answer accurately identifies the three categories of organisations required to appoint a DPO under Article 37(1) as cited in source [6], which aligns perfectly with the reference note.)

**Your verdict:** Correct = ___ · Faithful = ___

## q056 (scenario) We're a 40-person company. Do we need to keep a record of our processing activities?

**Reference:** The exemption for organisations under 250 employees does not apply if processing is risky, not occasional, or includes special category data, so usually yes (Art. 30(5)).

**Answer:** You are exempt from the general duty to keep a record of processing activities because you have fewer than 250 employees, unless the processing you carry out is likely to pose a risk to data‑subjects’ rights and freedoms, is not occasional, or involves special‑category data or criminal‑offence data [1]. If any of those conditions apply, you would still need to maintain the record as set out in Articles 30(1)‑(3) and make it available to the supervisory authority on request [2][3][4][5].

**Sources cited:** [1] GDPR Article 30(5) - Records of processing activities, [2] GDPR Article 30(1) - Records of processing activities, [3] GDPR Article 30(2) - Records of processing activities, [4] GDPR Article 30(4) - Records of processing activities, [5] GDPR Article 30(3) - Records of processing activities

**Judge:** correct=yes, faithful=True (The answer correctly identifies the exemption for companies under 250 employees and accurately lists the specific conditions (risk, non-occasional, special category/criminal data) under which the exemption does not apply, aligning with the reference note and cited sources.)

**Your verdict:** Correct = ___ · Faithful = ___

## q058 (plain) What does privacy by design and by default mean?

**Reference:** Implement data protection principles in the design of processing, and by default process only data necessary for each purpose (Art. 25).

**Answer:** Privacy by design and by default requires controllers to implement appropriate technical and organisational measures that, taking into account the state of the art, costs, nature, scope, context and purposes of processing and the risks to individuals’ rights and freedoms, embed data‑protection principles such as data minimisation into processing from the outset and throughout its lifecycle, for example by using pseudonymisation [2]. By default, these measures must ensure that only the personal data strictly necessary for each specific purpose are processed, limiting the amount collected, the extent of processing, storage periods and accessibility, so that data are not made accessible to an indefinite number of persons without the individual’s intervention [1].

**Sources cited:** [1] GDPR Article 25(2) - Data protection by design and by default, [2] GDPR Article 25(1) - Data protection by design and by default

**Judge:** correct=yes, faithful=True (The answer accurately reflects the requirements of GDPR Article 25(1) and 25(2) regarding privacy by design and by default, matching the key points in the reference note.)

**Your verdict:** Correct = ___ · Faithful = ___

## q061 (plain) Can personal data be sent to servers outside the EU?

**Reference:** Only under Chapter V: adequacy decision (Art. 45) or appropriate safeguards such as standard contractual clauses (Art. 46).

**Answer:** Yes, personal data may be transferred to servers outside the EU, but only if the transfer complies with the GDPR’s rules on international transfers. A transfer is allowed when the European Commission has adopted an adequacy decision for the third country or sector (Article 45(1)) [8], or when the controller provides appropriate safeguards such as binding corporate rules (Article 46(1)) [4]. If neither an adequacy decision nor safeguards exist, a transfer may still occur under one of the specific derogations listed in Article 49(1) (e.g., explicit consent, performance of a contract, vital interests, public interest, legal claims, etc.) [5]. All transfers must respect the overall requirement that the level of protection ensured in the Union is not undermined [3].

**Sources cited:** [3] GDPR Recital 101, [4] GDPR Article 46(1) - Transfers subject to appropriate safeguards, [5] GDPR Article 49(1) - Derogations for specific situations, [8] GDPR Article 45(1) - Transfers on the basis of an adequacy decision

**Judge:** correct=yes, faithful=True (The answer correctly identifies that transfers are permitted under Chapter V mechanisms (adequacy, safeguards, derogations) and accurately cites the provided sources for each claim.)

**Your verdict:** Correct = ___ · Faithful = ___

## q063 (scenario) A company leaked my data and I suffered as a result. Can I claim compensation?

**Reference:** Yes: right to compensation for material or non-material damage from the controller or processor (Art. 82).

**Answer:** Yes, you have a right to compensation for the material or non‑material damage you suffered because the company’s processing infringed the GDPR (Article 82(1) GDPR) [2]. The controller (or processor) that caused the breach is liable for that damage (Article 82(2) GDPR) [3], and if several controllers or processors are involved they can each be held liable for the whole damage to ensure effective compensation (Article 82(4) GDPR) [4]. If the responsible party has already paid full compensation, it may seek contribution from any other controllers or processors involved (Article 82(5) GDPR) [1]. If you need assistance, you may also mandate a not‑for‑profit body to lodge a complaint and pursue compensation on your behalf (Article 80(1) GDPR) [6].

**Sources cited:** [1] GDPR Article 82(5) - Right to compensation and liability, [2] GDPR Article 82(1) - Right to compensation and liability, [3] GDPR Article 82(2) - Right to compensation and liability, [4] GDPR Article 82(4) - Right to compensation and liability, [6] GDPR Article 80(1) - Representation of data subjects

**Judge:** correct=yes, faithful=True (The answer correctly identifies the right to compensation under Article 82 GDPR for material or non-material damage, which aligns with the reference note, and all specific claims are supported by the cited sources.)

**Your verdict:** Correct = ___ · Faithful = ___

## q065 (exact) What counts as personal data under the GDPR, and is pseudonymised data still personal data?

**Reference:** Any information relating to an identified or identifiable person (Art. 4(1)); pseudonymised data remains personal data, anonymous data does not (Recital 26).

**Answer:** Personal data is “any information relating to an identified or identifiable natural person (‘data subject’)”, where identification can be direct or indirect by means such as a name, identification number, location data, online identifier or other characteristic of the person [2]. Pseudonymisation is defined as processing personal data so that it can no longer be attributed to a specific data subject without additional information that is kept separately and protected by technical and organisational measures [1]. Because the additional information that would allow re‑identification is retained, pseudonymised data remain personal data under the GDPR, and the recitals stress that pseudonymisation is meant to reduce risk but does not remove the data from the scope of the Regulation [3][4].

**Sources cited:** [1] GDPR Article 4 - Definitions, [2] GDPR Article 4 - Definitions, [3] GDPR Recital 29, [4] GDPR Recital 28

**Judge:** correct=yes, faithful=False (The answer correctly identifies the definition of personal data and that pseudonymised data remains personal data, but it cites Recitals 28 and 29 for the claim that pseudonymisation does not remove data from the GDPR's scope, whereas these recitals only discuss risk reduction and incentives, not the explicit exclusion of scope (which is typically found in Recital 26, not provided in the sources).)

**Your verdict:** Correct = ___ · Faithful = ___

## q067 (cross) Can we use sensitive data like ethnicity to detect and fix bias in our AI model?

**Reference:** Exceptionally, for bias detection and correction in high-risk systems, under strict safeguards (AI Act Art. 10(5)), as a derogation from the GDPR Art. 9 prohibition.

**Answer:** Yes. Article 10(5) of the AI Act permits providers of high‑risk AI systems to process special categories of personal data – such as ethnicity – but only when it is strictly necessary to detect and correct bias and only under the safeguards set out in the regulation (e.g., the data cannot be replaced by other data, technical limits, pseudonymisation, strict access controls and documentation) [2]. The same provision also requires that the processing be justified as strictly necessary, that the data be deleted once bias is corrected or the retention period ends, and that the reasons for the processing be recorded in the GDPR‑style processing‑activities log [1]. Recital 70 reinforces that such processing may be allowed as a matter of substantial public interest for bias detection and correction [8].

**Sources cited:** [1] AI Act Article 10(5) - Data and data governance, [2] AI Act Article 10(5) - Data and data governance, [8] AI Act Recital 70

**Judge:** correct=yes, faithful=True (The answer correctly identifies that Article 10(5) of the AI Act allows for the processing of special categories of data for bias detection in high-risk systems under strict safeguards, which aligns with the reference note's description of an exceptional derogation from GDPR Article 9.)

**Your verdict:** Correct = ___ · Faithful = ___

## q069 (cross) Our AI automatically rejects job applicants. Which EU rules apply?

**Reference:** AI Act: high-risk (Annex III point 4); GDPR: right not to be subject to solely automated decisions with significant effects (Art. 22).

**Answer:** The AI Act does not list recruitment or automatic selection of job applicants among the high‑risk AI systems in Annex III [6]; therefore the specific obligations for high‑risk AI (e.g., registration under Article 49 or authorisation for biometric identification) are not triggered by the sources provided. Consequently, the AI Act texts I have do not answer this question.

**Sources cited:** [6] AI Act Annex III - High-risk AI systems referred to in Article 6(2)

**Judge:** correct=no, faithful=False (The answer incorrectly claims that recruitment AI is not listed in Annex III based on a source that only covers migration, and it completely fails to mention the GDPR Article 22 right not to be subject to solely automated decisions, which is a key part of the reference note.)

**Your verdict:** Correct = ___ · Faithful = ___

## q072 (unanswerable) What penalties does China's AI law impose on deepfakes?

**Reference:** Outside the corpus (non-EU law): should decline.

**Answer:** The AI Act and GDPR texts I have do not answer this question.

**Sources cited:** none

**Judge:** correct=None, faithful=None ()

**Your verdict:** Correct = ___ · Faithful = ___

## q074 (unanswerable) Which AI chatbot is the most accurate on the market today?

**Reference:** Not a legal question covered by the texts: should decline.

**Answer:** The AI Act and GDPR texts I have do not answer this question.

**Sources cited:** none

**Judge:** correct=None, faithful=None ()

**Your verdict:** Correct = ___ · Faithful = ___

## q076 (unanswerable) Has the European Commission fined OpenAI under the AI Act?

**Reference:** Enforcement news is not in the legal texts: should decline rather than guess.

**Answer:** The AI Act and GDPR texts I have do not answer this question.

**Sources cited:** none

**Judge:** correct=None, faithful=None ()

**Your verdict:** Correct = ___ · Faithful = ___
