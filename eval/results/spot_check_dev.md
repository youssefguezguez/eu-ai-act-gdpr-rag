# Human spot-check of generated answers

For each answer, mark **Correct** (yes / partial / no) and **Faithful** (yes / no),
then compare with the judge's verdict below it.

## q001 (scenario) My company wants to use AI to detect whether employees are stressed during video calls. Is that legal?

**Reference:** Prohibited: inferring emotions in the workplace, except for medical or safety reasons (AI Act Art. 5(1)(f)).

**Answer:** Emotion‑recognition systems used in the workplace are prohibited under Article 5(1)(f) of the AI Act, which bars AI that infers emotions of natural persons in employment or education settings unless the system is intended for medical or safety reasons [2]. Therefore, using AI to detect employee stress during video calls would not be permitted under the AI Act. The sources do not provide any exception that would make such use lawful.

**Sources cited:** [2] AI Act Article 5(1) - Prohibited AI practices

**Judge:** correct=yes, faithful=True (The answer correctly identifies that the proposed use is prohibited under Article 5(1)(f) of the AI Act, as the source confirms the prohibition on inferring emotions in the workplace except for medical or safety reasons, which do not apply to general stress detection.)

**Your verdict:** Correct = ___ · Faithful = ___

## q002 (plain) Can a government rank its citizens based on how they behave socially?

**Reference:** Social scoring leading to detrimental or unfavourable treatment is prohibited (Art. 5(1)(c)).

**Answer:** AI systems that rank or give a “social score” to natural persons on the basis of their social behaviour or inferred personal characteristics, and that lead to detrimental or unfavourable treatment in contexts unrelated to the original data or that is disproportionate, are prohibited. This is set out in Recital 31, which calls such scoring practices unacceptable and to be prohibited, and in Article 5(1)(c), which expressly bans the placing on the market, putting into service or use of AI systems for that purpose [1][2].

**Sources cited:** [1] AI Act Recital 31, [2] AI Act Article 5(1) - Prohibited AI practices

**Judge:** correct=yes, faithful=True (The answer correctly identifies that social scoring leading to detrimental or unfavourable treatment is prohibited under Article 5(1)(c) and Recital 31, which aligns with the reference note and the provided sources.)

**Your verdict:** Correct = ___ · Faithful = ___

## q005 (plain) Are AI systems that manipulate people with hidden psychological tricks banned?

**Reference:** Subliminal, manipulative or deceptive techniques causing significant harm are prohibited (Art. 5(1)(a)).

**Answer:** Yes. The AI Act prohibits AI systems that use subliminal, manipulative or deceptive techniques to materially distort a person’s behaviour and impair informed decision‑making, causing significant harm [3]. Recital 29 describes such “AI‑enabled manipulative techniques” as especially dangerous and therefore prohibited [1]. This ban applies regardless of the commercial context, except for lawful medical treatments that meet applicable standards [7].

**Sources cited:** [1] AI Act Recital 29, [3] AI Act Article 5(1) - Prohibited AI practices, [7] AI Act Recital 29

**Judge:** correct=yes, faithful=False (The answer correctly identifies the prohibition and the medical exception, but the claim that the ban applies 'regardless of the commercial context' is not supported by the cited sources, which instead state that legitimate commercial practices complying with the law are not prohibited.)

**Your verdict:** Correct = ___ · Faithful = ___

## q006 (exact) How does the AI Act define an 'AI system'?

**Reference:** Art. 3(1): machine-based system operating with varying autonomy, possibly adaptive, inferring outputs (predictions, content, recommendations, decisions) from input.

**Answer:** The AI Act defines an ‘AI system’ as “a machine‑based system that is designed to operate with varying levels of autonomy and that may exhibit adaptiveness after deployment, and that, for explicit or implicit objectives, infers, from the input it receives, how to generate outputs such as predictions, content, recommendations, or decisions that can influence physical or virtual environments” [1].

**Sources cited:** [1] AI Act Article 3 - Definitions

**Judge:** correct=yes, faithful=True (The answer accurately quotes the definition of an AI system from Article 3(1) as provided in Source [1], which aligns perfectly with the reference note.)

**Your verdict:** Correct = ___ · Faithful = ___

## q008 (plain) How do I know if my AI system counts as high-risk?

**Reference:** High-risk if a safety component of products under Annex I legislation needing third-party assessment (Art. 6(1)), or listed in Annex III (Art. 6(2)), unless the Art. 6(3) derogation applies.

**Answer:** You determine whether an AI system is high‑risk by applying the classification rules in Article 6 of the AI Act. First, the system is automatically classed as high‑risk when (a) it is intended to be used as a safety component of a product or is itself a product covered by the Union harmonisation legislation in Annex I, **and** (b) that product or component must undergo a third‑party conformity assessment under the same legislation [4].  

If those conditions are not met, you must check the derogation rules in Article 6(3). An AI system listed in Annex III is not high‑risk only if it does **not** pose a significant risk to health, safety or fundamental rights and meets one of the listed exceptions (e.g., it performs a narrow procedural task, improves a completed human activity, detects decision‑making patterns without influencing them, or performs a preparatory task) [5].  

Conversely, any AI system in Annex III that performs profiling of natural persons is always high‑risk [5]. If you still consider the system non‑high‑risk, you must document your assessment before placing it on the market and be ready to provide it to national authorities [3].  

If a market‑surveillance authority later believes the system should be high‑risk, it will re‑evaluate the classification under the same criteria [8].

**Sources cited:** [3] AI Act Article 6(4) - Classification rules for high-risk AI systems, [4] AI Act Article 6(1) - Classification rules for high-risk AI systems, [5] AI Act Article 6(3) - Classification rules for high-risk AI systems, [8] AI Act Article 80(1) - Procedure for dealing with AI systems classified by the provider as non-high-risk in application of Annex III

**Judge:** correct=yes, faithful=True (The answer accurately reflects the reference note by identifying the two main high-risk categories (Annex I safety components and Annex III listings) and correctly explaining the Article 6(3) derogation, with all claims supported by the cited sources.)

**Your verdict:** Correct = ___ · Faithful = ___

## q009 (scenario) We sell a CV-screening tool that ranks job applicants. Is it high-risk under the AI Act?

**Reference:** Yes: AI for recruitment or selection, including filtering applications and evaluating candidates, is listed in Annex III point 4(a).

**Answer:** Yes. A tool that ranks job applicants falls within the recruitment and selection AI systems listed in Annex III as high‑risk AI pursuant to Article 6(2) of the AI Act [1]. Moreover, because it performs profiling of natural persons, it is always considered high‑risk under the derogation rule in Article 6(3) [8].

**Sources cited:** [1] AI Act Annex III - High-risk AI systems referred to in Article 6(2), [8] AI Act Article 6(3) - Classification rules for high-risk AI systems

**Judge:** correct=yes, faithful=True (The answer correctly identifies the tool as high-risk under Annex III point 4(a) and accurately applies the Article 6(3) derogation rule regarding profiling, which is supported by the provided sources.)

**Your verdict:** Correct = ___ · Faithful = ___

## q011 (scenario) A bank uses a machine learning model to compute customers' credit scores. Does the AI Act treat this as high-risk?

**Reference:** Yes: creditworthiness evaluation and credit scoring of natural persons is high-risk (Annex III point 5(b)), except for detecting financial fraud.

**Answer:** Yes. The AI Act classifies AI systems used to evaluate the creditworthiness of natural persons or to establish a credit score as high‑risk AI systems [1][4].

**Sources cited:** [1] AI Act Recital 58, [4] AI Act Annex III - High-risk AI systems referred to in Article 6(2)

**Judge:** correct=yes, faithful=True (The answer correctly identifies that credit scoring is high-risk under the AI Act and cites the relevant sources (Recital 58 and Annex III) which support this classification, including the exception for fraud detection mentioned in the reference note.)

**Your verdict:** Correct = ___ · Faithful = ___

## q013 (plain) Do providers of high-risk AI need a process for managing risks over the system's lifetime?

**Reference:** Yes: a risk management system established, documented and maintained as a continuous iterative process throughout the lifecycle (Art. 9).

**Answer:** Yes. Providers of high‑risk AI systems must have a risk‑management system that is a continuous, iterative process planned and run throughout the entire lifecycle of the system, with regular systematic review and updating [1].

**Sources cited:** [1] AI Act Article 9(2) - Risk management system

**Judge:** correct=yes, faithful=True (The answer correctly identifies that providers must have a continuous, iterative risk management process throughout the lifecycle, which is fully supported by the cited source (Article 9(2)) and aligns with the reference note.)

**Your verdict:** Correct = ___ · Faithful = ___

## q015 (plain) Must high-risk AI systems keep logs of what they do?

**Reference:** Yes: they must technically allow automatic recording of events (logs) over their lifetime (Art. 12).

**Answer:** Yes. High‑risk AI systems must be designed to automatically record events (logs) throughout their lifetime [1]. The logging must capture information needed to identify risk situations, support post‑market monitoring and monitor operation, and must be kept for at least six months (or longer if required by Union or national law) by both providers and deployers [3][4]. For systems covered by Annex III point 1(a), the logs must at minimum record each use period, the reference database checked, the input data that produced a match, and the natural persons who verified the results [5].

**Sources cited:** [1] AI Act Article 12(1) - Record-keeping, [3] AI Act Article 19(1) - Automatically generated logs, [4] AI Act Article 26(6) - Obligations of deployers of high-risk AI systems, [5] AI Act Article 12(3) - Record-keeping

**Judge:** correct=yes, faithful=True (The answer correctly states that high-risk AI systems must technically allow for automatic logging over their lifetime, which aligns with the reference note and is supported by the cited sources.)

**Your verdict:** Correct = ___ · Faithful = ___

## q017 (plain) What does the AI Act require regarding accuracy and cybersecurity of high-risk systems?

**Reference:** Appropriate accuracy, robustness and cybersecurity throughout the lifecycle; resilience to errors and to attacks such as data poisoning and adversarial examples (Art. 15).

**Answer:** High‑risk AI systems must be designed and developed so that they achieve an appropriate level of accuracy, robustness and cybersecurity and maintain that performance throughout their lifecycle [1]. The specific accuracy levels and the metrics used to assess them must be declared in the system’s instructions for use [3] and also be included in the information that deployers receive about the system’s capabilities, limitations, expected accuracy, robustness and cybersecurity, together with any known or foreseeable circumstances that could affect those levels [7]. The systems must be resilient to unauthorised attempts to alter their use, outputs or performance, with technical solutions that address AI‑specific vulnerabilities such as data‑poisoning, model‑poisoning, adversarial inputs, confidentiality attacks and model flaws [4]. Additionally, they must be as resilient as possible to errors, faults or inconsistencies, using technical and organisational measures such as redundancy, backup or fail‑safe plans, and must mitigate feedback‑loop risks when they continue learning after deployment [5].

**Sources cited:** [1] AI Act Article 15(1) - Accuracy, robustness and cybersecurity, [3] AI Act Article 15(3) - Accuracy, robustness and cybersecurity, [4] AI Act Article 15(5) - Accuracy, robustness and cybersecurity, [5] AI Act Article 15(4) - Accuracy, robustness and cybersecurity, [7] AI Act Article 13(3) - Transparency and provision of information to deployers

**Judge:** correct=yes, faithful=True (The answer accurately reflects the requirements of Article 15 regarding accuracy, robustness, and cybersecurity, including specific vulnerabilities and lifecycle considerations, consistent with the reference note.)

**Your verdict:** Correct = ___ · Faithful = ___

## q021 (plain) If I build a chatbot, do I have to tell users they are talking to an AI?

**Reference:** Yes: AI systems interacting directly with people must inform them they are interacting with an AI, unless obvious from context (Art. 50(1)).

**Answer:** Yes. Under Article 50(1) of the AI Act, providers must ensure that natural persons are informed they are interacting with an AI system, unless this is obvious to a reasonably well‑informed, observant and circumspect user given the circumstances and context of use [2]. This is the applicable transparency requirement for chatbots.

**Sources cited:** [2] AI Act Article 50(1) - Transparency obligations for providers and deployers of certain AI systems

**Judge:** correct=yes, faithful=True (The answer correctly identifies the obligation under Article 50(1) to inform users they are interacting with an AI, including the exception for obviousness, which aligns perfectly with the reference note and the provided source.)

**Your verdict:** Correct = ___ · Faithful = ___

## q023 (plain) Must AI-generated images and audio be marked as synthetic in a machine-readable way?

**Reference:** Yes: providers of generative systems must mark outputs in a machine-readable format detectable as artificially generated (Art. 50(2)).

**Answer:** Yes. Article 50(2) of the AI Act requires providers of AI systems that generate synthetic audio, image, video or text to ensure that the outputs are marked in a machine‑readable format and can be detected as artificially generated or manipulated, subject to limited exceptions [1]. Recital 133 explains that this marking should use techniques such as watermarks, metadata, cryptographic provenance or similar methods that are reliable, interoperable and technically feasible [2].

**Sources cited:** [1] AI Act Article 50(2) - Transparency obligations for providers and deployers of certain AI systems, [2] AI Act Recital 133

**Judge:** correct=yes, faithful=True (The answer correctly identifies the obligation under Article 50(2) for providers to mark outputs in a machine-readable format and accurately cites Recital 133 for the technical methods, fully aligning with the reference note.)

**Your verdict:** Correct = ___ · Faithful = ___

## q024 (scenario) A store uses cameras to recognise shoppers' emotions. What must it tell customers?

**Reference:** Deployers of emotion recognition or biometric categorisation systems must inform the people exposed to them (Art. 50(3)).

**Answer:** The store must inform shoppers that an emotion‑recognition system is operating and that their biometric data will be processed in line with the GDPR (Regulation 2016/679) and related Union rules [3].

**Sources cited:** [3] AI Act Article 50(3) - Transparency obligations for providers and deployers of certain AI systems

**Judge:** correct=yes, faithful=True (The answer correctly identifies the obligation to inform shoppers about the operation of the emotion recognition system and the requirement to process data in accordance with GDPR, which aligns with the reference note and is fully supported by the cited source (Article 50(3)).)

**Your verdict:** Correct = ___ · Faithful = ___

## q026 (exact) Above what amount of training compute is a general-purpose AI model presumed to have systemic risk?

**Reference:** When cumulative training compute exceeds 10^25 floating point operations (Art. 51(2)).

**Answer:** A general‑purpose AI model is presumed to have high‑impact capabilities – and therefore systemic risk – when the cumulative amount of computation used for its training exceeds 10^25 floating‑point operations [2].

**Sources cited:** [2] AI Act Article 51(2) - Classification of general-purpose AI models as general-purpose AI models with systemic risk

**Judge:** correct=yes, faithful=True (The answer correctly identifies the threshold of 10^25 floating point operations as the point where high-impact capabilities (and thus systemic risk) are presumed, accurately citing Article 51(2) and aligning with the reference note.)

**Your verdict:** Correct = ___ · Faithful = ___

## q027 (plain) What extra duties apply to the most powerful general-purpose AI models?

**Reference:** Model evaluation incl. adversarial testing, systemic risk assessment and mitigation, serious incident reporting, and cybersecurity protection (Art. 55(1)).

**Answer:** Providers of general‑purpose AI models that are classified as “with systemic risk” must go beyond the basic obligations in Articles 53 and 54 and carry out additional measures under Article 55(1). They must (a) evaluate the model with state‑of‑the‑art, standardised protocols and tools, including adversarial testing to identify and mitigate systemic risks; (b) assess and mitigate possible systemic risks at Union level arising from development, market placement or use; (c) keep track of, document and promptly report serious incidents and corrective measures to the AI Office and national authorities; and (d) ensure an adequate level of cybersecurity protection for the model and its physical infrastructure [5].

**Sources cited:** [5] AI Act Article 55(1) - Obligations of providers of general-purpose AI models with systemic risk

**Judge:** correct=yes, faithful=True (The answer accurately lists the four specific obligations (model evaluation, risk assessment/mitigation, incident reporting, and cybersecurity) required by Article 55(1) for general-purpose AI models with systemic risk, which aligns perfectly with the reference note and the provided source.)

**Your verdict:** Correct = ___ · Faithful = ___

## q030 (plain) What happens if a company gives misleading information to AI regulators?

**Reference:** Up to EUR 7.5 million or 1% of worldwide annual turnover (Art. 99(5)).

**Answer:** If a provider of a general‑purpose AI model gives misleading, incomplete or incorrect information to the regulators (e.g., in response to a request for documents or information under Article 91), the Commission may impose a fine of up to 3 % of its annual worldwide turnover or €15 million, whichever is higher. The fine is set taking into account the nature, gravity and duration of the infringement and any relevant mitigating factors such as commitments or codes of practice [6].

**Sources cited:** [6] AI Act Article 101(1) - Fines for providers of general-purpose AI models

**Judge:** correct=no, faithful=True (The answer cites the fine for providers of general-purpose AI models (Art. 101), whereas the reference note specifies the fine for providers of high-risk AI systems (Art. 99(5)), which is up to EUR 7.5 million or 1% of turnover.)

**Your verdict:** Correct = ___ · Faithful = ___

## q032 (plain) When do the AI Act's rules start to apply?

**Reference:** Generally from 2 August 2026; prohibitions and AI literacy from 2 February 2025; GPAI and penalties from 2 August 2025; Art. 6(1) from 2 August 2027 (Art. 113).

**Answer:** The AI Act as a whole enters into force 20 days after its publication and applies from 2 August 2026, but different parts start earlier: Chapters I and II apply from 2 February 2025; Chapter III Section 4, Chapter V, Chapter VII, Chapter XII and Article 78 apply from 2 August 2025 (except Article 101); and the obligations in Article 6(1) begin on 2 August 2027 [1]. Recital 179 reinforces that the prohibitions and general provisions should already be effective from 2 February 2025, while the governance‑related provisions (e.g., notified bodies) apply from 2 August 2025 [2].

**Sources cited:** [1] AI Act Article 113 - Entry into force and application, [2] AI Act Recital 179

**Judge:** correct=yes, faithful=True (The answer accurately reflects the reference note and the cited sources, correctly identifying the general application date of 2 August 2026 and the specific earlier dates for prohibitions (2 February 2025), governance/GPAI/penalties (2 August 2025), and Article 6(1) (2 August 2027).)

**Your verdict:** Correct = ___ · Faithful = ___

## q035 (scenario) I use an AI app for my own hobby at home. Does the AI Act impose obligations on me?

**Reference:** No: it does not apply to deployers who are natural persons using AI in a purely personal, non-professional activity (Art. 2(10)).

**Answer:** The AI Act does not impose obligations on you, because it expressly excludes “obligations of deployers who are natural persons using AI systems in the course of a purely personal non‑professional activity” [1].

**Sources cited:** [1] AI Act Article 2(10) - Scope

**Judge:** correct=yes, faithful=True (The answer correctly identifies that the AI Act does not apply to natural persons using AI for purely personal, non-professional activities, accurately citing Article 2(10) as the source for this exclusion.)

**Your verdict:** Correct = ___ · Faithful = ___

## q036 (plain) Is AI research and development exempt from the AI Act?

**Reference:** Systems developed solely for scientific research, and research/testing before placing on the market, are excluded, except testing in real-world conditions (Art. 2(6), 2(8)).

**Answer:** Yes, AI research and development activities are exempt from the AI Act when the AI system or model is created solely for scientific research and development and is not placed on the market or put into service. Article 2(6) states that the regulation does not apply to AI systems or models “specifically developed and put into service for the sole purpose of scientific research and development” [3]; Article 2(8) adds that activities “prior to their being placed on the market or put into service” are also excluded, although testing in real‑world conditions is not [1]. Recital 25 confirms that AI systems developed for the sole purpose of scientific R&D are excluded, but notes that the exemption ends if such a system later enters the market or is put into service [2].

**Sources cited:** [1] AI Act Article 2(8) - Scope, [2] AI Act Recital 25, [3] AI Act Article 2(6) - Scope

**Judge:** correct=yes, faithful=True (The answer accurately reflects the reference note and the provided sources, correctly identifying the exclusions for scientific R&D (Art. 2(6)) and pre-market activities (Art. 2(8)) while noting the exception for real-world testing.)

**Your verdict:** Correct = ___ · Faithful = ___

## q038 (plain) What is an AI regulatory sandbox and must every country have one?

**Reference:** A controlled environment to develop and test innovative AI under supervision; each Member State must establish at least one by 2 August 2026 (Art. 57).

**Answer:** An AI regulatory sandbox is a controlled environment set up by a competent authority that allows providers to develop, train, test and validate innovative AI systems—potentially in real‑world conditions—before those systems are placed on the market or put into service, under a specific sandbox plan agreed with the authority [1]. Member States must ensure that their competent authorities establish at least one national AI regulatory sandbox, which must be operational by 2 August 2026, although the requirement can be met by participating in an existing sandbox that provides equivalent national coverage or by establishing a joint sandbox with other Member States [2][3]. Additional sandboxes may also be created at regional, local or joint‑Member‑State level, but the core obligation is the existence of at least one national sandbox for each Member State [7].

**Sources cited:** [1] AI Act Article 57(5) - AI regulatory sandboxes, [2] AI Act Article 57(1) - AI regulatory sandboxes, [3] AI Act Recital 138, [7] AI Act Article 57(2) - AI regulatory sandboxes

**Judge:** correct=yes, faithful=True (The answer accurately defines the sandbox and correctly states the obligation for Member States to have at least one operational by 2 August 2026, supported by the cited sources.)

**Your verdict:** Correct = ___ · Faithful = ___

## q041 (plain) On what legal grounds can a company process my personal data?

**Reference:** Consent, contract, legal obligation, vital interests, public task, or legitimate interests (Art. 6(1)(a)-(f)).

**Answer:** A company may process your personal data only if at least one of the grounds listed in Article 6(1) applies, namely: (a) you have given consent; (b) the processing is necessary for performance of a contract or steps taken at your request before a contract; (c) it is required to comply with a legal obligation; (d) it is needed to protect vital interests; (e) it is necessary for a task carried out in the public interest or in the exercise of official authority; or (f) it is necessary for the legitimate interests of the controller or a third party, provided your rights do not override those interests [5].  

If the data are special categories (e.g., health data), processing is allowed only under the specific exceptions in Article 9(2), such as when the data are manifestly public, needed for legal claims, for substantial public interest, or for health‑care purposes under Union or Member State law and the safeguards in Article 9(3) are respected [7][1].

**Sources cited:** [1] GDPR Article 9(3) - Processing of special categories of personal data, [5] GDPR Article 6(1) - Lawfulness of processing, [7] GDPR Article 9(2) - Processing of special categories of personal data

**Judge:** correct=yes, faithful=True (The answer correctly lists all six legal grounds for processing personal data under Article 6(1) of the GDPR, which aligns perfectly with the reference note, and the additional information regarding special categories is supported by the cited sources.)

**Your verdict:** Correct = ___ · Faithful = ___

## q043 (scenario) We run a social app. From what age can a teenager consent to us processing their data without their parents?

**Reference:** 16 by default; Member States may lower it to no less than 13. Below that, parental consent is needed (Art. 8(1)).

**Answer:** A teenager can give valid consent for processing of their personal data from age 16 under the GDPR; Member States may set a lower age but not below 13 [1].

**Sources cited:** [1] GDPR Article 8(1) - Conditions applicable to child's consent in relation to information society services

**Judge:** correct=yes, faithful=True (The answer correctly states the default age of 16 and the minimum lower limit of 13 as per the reference note and cited source.)

**Your verdict:** Correct = ___ · Faithful = ___

## q044 (exact) What does Article 9 GDPR say about health data?

**Reference:** Health data is a special category; processing is prohibited unless an Art. 9(2) exception applies, e.g. explicit consent.

**Answer:** Article 9(1) prohibits processing of “data concerning health”, i.e. personal data related to a natural person’s physical or mental health, including health‑care information [7]. Processing such data is allowed only if one of the exceptions in Article 9(2) applies, for example when the data subject has given explicit consent (a), when processing is necessary for public‑health reasons or scientific research (i, j), for substantial public interest (g), for preventive or occupational medicine or health‑care provision (h), or for the establishment, exercise or defence of legal claims (f), among other grounds listed in the various paragraphs of Article 9(2) [1][2][6]. Member States may also impose further conditions on genetic, biometric or health data under Article 9(4) [3].

**Sources cited:** [1] GDPR Article 9(2) - Processing of special categories of personal data, [2] GDPR Article 9(2) - Processing of special categories of personal data, [3] GDPR Article 9(4) - Processing of special categories of personal data, [6] GDPR Article 9(2) - Processing of special categories of personal data, [7] GDPR Article 9(1) - Processing of special categories of personal data

**Judge:** correct=yes, faithful=False (The answer correctly identifies the prohibition and exceptions but cites source [7] for the definition of health data, which is actually found in source [8] (Article 4(15)), making the citation unsupported.)

**Your verdict:** Correct = ___ · Faithful = ___

## q045 (plain) What are the core principles of data protection?

**Reference:** Lawfulness, fairness and transparency; purpose limitation; data minimisation; accuracy; storage limitation; integrity and confidentiality; plus accountability (Art. 5).

**Answer:** The core data‑protection principles are set out in GDPR Article 5(1): (a) processing must be lawful, fair and transparent; (b) data must be collected for specified, explicit and legitimate purposes and not used incompatibly (purpose limitation); (c) only adequate, relevant and limited data should be processed (data‑minimisation); (d) data must be accurate and kept up to date; (e) personal data may be kept only as long as necessary for the purposes (storage limitation); and (f) processing must ensure security, integrity and confidentiality of the data ([1][3]).

**Sources cited:** [1] GDPR Article 5(1) - Principles relating to processing of personal data, [3] GDPR Article 5(1) - Principles relating to processing of personal data

**Judge:** correct=partial, faithful=True (The answer correctly lists principles (a) through (f) with accurate citations, but it omits the principle of accountability (Article 5(2)), which is explicitly listed in the reference note as a core principle.)

**Your verdict:** Correct = ___ · Faithful = ___

## q047 (plain) Can I make a company delete my data?

**Reference:** Yes, the right to erasure applies in listed cases, e.g. data no longer necessary or consent withdrawn (Art. 17(1)), with exceptions in Art. 17(3).

**Answer:** Yes. Under GDPR Article 17(1) you have the right to obtain erasure of your personal data from the controller without undue delay when a ground for erasure applies, and the controller must comply with that request [2]. If the controller has already made the data public, it must also take reasonable steps, including technical measures, to inform other controllers processing the data so they can delete any links or copies [1]. When you are a subject of real‑world testing of a high‑risk AI system, you may withdraw your informed consent at any time and request the immediate and permanent deletion of your personal data, without having to justify the withdrawal [3]. The controller must also notify any recipients of the data about the erasure, unless this is impossible or would involve disproportionate effort [5].

**Sources cited:** [1] GDPR Article 17(2) - Right to erasure (‘right to be forgotten’), [2] GDPR Article 17(1) - Right to erasure (‘right to be forgotten’), [3] AI Act Article 60(5) - Testing of high-risk AI systems in real world conditions outside AI regulatory sandboxes, [5] GDPR Article 19 - Notification obligation regarding rectification or erasure of personal data or restriction of processing

**Judge:** correct=yes, faithful=True (The answer correctly affirms the right to erasure under GDPR Article 17(1) and accurately details the associated obligations and specific AI Act provisions, all of which are supported by the cited sources.)

**Your verdict:** Correct = ___ · Faithful = ___

## q050 (plain) Do I have the right not to be judged only by an algorithm?

**Reference:** Right not to be subject to decisions based solely on automated processing with legal or similarly significant effects, with exceptions (Art. 22).

**Answer:** You have a right not to be subject to a decision based solely on automated processing, including profiling, that produces legal effects or similarly significant effects for you (GDPR Article 22(1)) [3]. In addition, the AI Act expressly prohibits the use of AI systems for risk assessments that predict a person’s likelihood of committing a criminal offence based solely on profiling or personality traits, unless the system is only supporting a human assessment based on objective, verifiable facts [4]. Both provisions together limit judgments that rely only on an algorithm.

**Sources cited:** [3] GDPR Article 22(1) - Automated individual decision-making, including profiling, [4] AI Act Article 5(1) - Prohibited AI practices

**Judge:** correct=yes, faithful=True (The answer correctly identifies the right under GDPR Article 22 and supports it with the relevant AI Act prohibition, accurately reflecting the reference note's key point.)

**Your verdict:** Correct = ___ · Faithful = ___

## q053 (scenario) Hackers stole our customers' passwords. Do we have to tell the customers themselves?

**Reference:** Yes, if the breach is likely to result in a high risk to them, unless e.g. the data was encrypted (Art. 34).

**Answer:** If the stolen passwords are likely to result in a high risk to the rights and freedoms of the data subjects, the controller must communicate the breach to the data subjects without undue delay (GDPR Art. 34(1)) [1]. That communication is not required only if, for example, the controller had applied appropriate technical measures such as encryption that render the data unintelligible, or if other listed conditions apply (e.g., subsequent measures removing the risk or disproportionate effort) [3]. Since the facts given do not indicate any such safeguards, the default rule is that you must inform the customers.

**Sources cited:** [1] GDPR Article 34(1) - Communication of a personal data breach to the data subject, [3] GDPR Article 34(3) - Communication of a personal data breach to the data subject

**Judge:** correct=yes, faithful=True (The answer correctly identifies the high-risk threshold and the specific exceptions (such as encryption) under GDPR Article 34, accurately reflecting the reference note and supported by the provided sources.)

**Your verdict:** Correct = ___ · Faithful = ___

## q054 (plain) When does a company have to carry out a data protection impact assessment?

**Reference:** When processing is likely to result in a high risk, in particular systematic profiling with significant effects, large-scale special category data, or large-scale monitoring of public areas (Art. 35(1), (3)).

**Answer:** A company must carry out a data protection impact assessment (DPIA) before processing when the type of processing – especially using new technologies – is likely to result in a high risk to the rights and freedoms of natural persons, taking into account its nature, scope, context and purposes [8]. The GDPR also specifies particular situations that automatically trigger a DPIA: (a) systematic and extensive automated evaluation or profiling that produces legal effects or significantly affects individuals; (b) large‑scale processing of special categories of data or data on criminal convictions; and (c) systematic monitoring of a publicly accessible area on a large scale [2]. Additionally, if the risk associated with the processing changes, the controller must review the DPIA to ensure continued compliance [1].

**Sources cited:** [1] GDPR Article 35(11) - Data protection impact assessment, [2] GDPR Article 35(3) - Data protection impact assessment, [8] GDPR Article 35(1) - Data protection impact assessment

**Judge:** correct=yes, faithful=True (The answer accurately reflects the reference note by citing the general high-risk threshold from Article 35(1) and the specific triggering situations from Article 35(3), with all claims supported by the provided sources.)

**Your verdict:** Correct = ___ · Faithful = ___

## q057 (plain) What must a contract with a data processor contain?

**Reference:** Subject matter, duration, nature and purpose, documented instructions, confidentiality, security, sub-processor rules, assistance, deletion or return, audits (Art. 28(3)).

**Answer:** A contract (or other legal act) with a processor must be binding under Union or Member‑State law and set out the subject‑matter and duration of the processing, the nature and purpose of the processing, the types of personal data and categories of data subjects, and the controller’s obligations and rights [3][7][8]. It must also require the processor to: (a) act only on documented controller instructions, (b) ensure confidentiality of persons processing the data, (c) take the security measures required by Article 32, (d) respect the conditions for engaging sub‑processors, (e) assist the controller with technical and organisational measures to fulfil data‑subject rights, (f) help ensure compliance with Articles 32‑36, and (g), at the controller’s choice, delete or return all personal data (and any copies) after the service ends, unless law requires storage [7][8]. The agreement must be in writing, including electronic form [4].

**Sources cited:** [3] GDPR Article 28(3) - Processor, [4] GDPR Article 28(9) - Processor, [7] GDPR Article 28(3) - Processor, [8] GDPR Article 28(3) - Processor

**Judge:** correct=partial, faithful=True (The answer correctly identifies most mandatory contract elements but omits the requirement for the processor to make available information necessary to demonstrate compliance and allow for audits (Art. 28(3)(h)), which is explicitly listed in the reference note.)

**Your verdict:** Correct = ___ · Faithful = ___

## q059 (plain) What security measures does the GDPR expect?

**Reference:** Appropriate technical and organisational measures such as pseudonymisation, encryption, resilience and regular testing (Art. 32(1)).

**Answer:** The GDPR requires controllers and processors to implement appropriate technical and organisational measures that ensure a level of security appropriate to the risk, taking into account the state of the art, costs, and the nature, scope, context and purposes of processing. Such measures include, for example, the pseudonymisation and encryption of personal data; ensuring the ongoing confidentiality, integrity, availability and resilience of processing systems and services; the ability to restore availability and access to personal data promptly after a physical or technical incident; and a process for regularly testing, assessing and evaluating the effectiveness of these technical and organisational measures[7].

**Sources cited:** [7] GDPR Article 32(1) - Security of processing

**Judge:** correct=yes, faithful=True (The answer accurately reflects the content of Article 32(1) GDPR, which is the specific provision cited in the reference note, and correctly cites source [7] for all claims.)

**Your verdict:** Correct = ___ · Faithful = ___

## q060 (scenario) We're a US company with no office in Europe but we sell online to EU customers. Does the GDPR apply to us?

**Reference:** Yes: it applies to controllers outside the EU offering goods or services to, or monitoring, people in the EU (Art. 3(2)).

**Answer:** Yes. Under Article 3(2) the GDPR applies to a controller that is not established in the Union when it offers goods or services to data subjects in the Union, regardless of whether a payment is required[5]. Therefore, as a US company selling online to EU customers, the GDPR’s provisions apply to your processing of their personal data.

**Sources cited:** [5] GDPR Article 3(2) - Territorial scope

**Judge:** correct=yes, faithful=True (The answer correctly identifies that the GDPR applies to the user's situation based on Article 3(2) and accurately cites the provided source [5] to support the claim regarding the offering of goods or services to data subjects in the Union.)

**Your verdict:** Correct = ___ · Faithful = ___

## q062 (exact) What is the maximum GDPR fine?

**Reference:** Up to EUR 20 million or 4% of total worldwide annual turnover, whichever is higher (Art. 83(5)).

**Answer:** The GDPR provides for administrative fines of up to 20 million EUR, or, for an undertaking, up to 4 % of its total worldwide annual turnover of the preceding financial year, whichever is higher [1][3].

**Sources cited:** [1] GDPR Article 83(5) - General conditions for imposing administrative fines, [3] GDPR Article 83(6) - General conditions for imposing administrative fines

**Judge:** correct=yes, faithful=True (The answer correctly states the maximum fine amount and conditions as specified in the reference note and supported by the cited sources.)

**Your verdict:** Correct = ___ · Faithful = ___

## q064 (plain) Where can I complain if a company misuses my personal data?

**Reference:** Lodge a complaint with a supervisory authority, in particular in your Member State of residence, work or the alleged infringement (Art. 77).

**Answer:** You may lodge a complaint with the supervisory authority of the Member State where you normally reside, where you work, or where the alleged infringement occurred [1].

**Sources cited:** [1] GDPR Article 77(1) - Right to lodge a complaint with a supervisory authority

**Judge:** correct=yes, faithful=True (The answer accurately reflects the reference note and the cited source (Article 77) regarding the right to lodge a complaint with a supervisory authority in the Member State of residence, work, or alleged infringement.)

**Your verdict:** Correct = ___ · Faithful = ___

## q066 (cross) We deploy a high-risk AI system that processes biometric data. Do we also need a GDPR data protection impact assessment?

**Reference:** Likely yes: deployers use the provider's information to carry out the DPIA required by GDPR Art. 35 (AI Act Art. 26(9)).

**Answer:** Yes. When you deploy a high‑risk AI system that processes biometric data, you must carry out a data‑protection impact assessment under Article 35 of the GDPR (or the equivalent assessment under Directive 2016/680), using the information provided under Article 13 of the AI Act [7]. This requirement applies to all deployers of high‑risk AI systems.

**Sources cited:** [7] AI Act Article 26(9) - Obligations of deployers of high-risk AI systems

**Judge:** correct=partial, faithful=False (The answer incorrectly generalizes the obligation to 'all' deployers, whereas the cited source (AI Act Art. 26(9)) and the reference note specify that the obligation applies 'where applicable' (i.e., when a DPIA is required under GDPR Art. 35), and it fails to explicitly state that the deployer uses the provider's information to carry out the assessment.)

**Your verdict:** Correct = ___ · Faithful = ___

## q068 (cross) If we already did a GDPR impact assessment, do we still need a separate fundamental rights impact assessment for our AI system?

**Reference:** The FRIA complements the DPIA; obligations already met through the DPIA need not be repeated (AI Act Art. 27(4)).

**Answer:** Yes, a fundamental‑rights impact assessment (FRIA) is still required for a high‑risk AI system, even if you have already carried out a GDPR data‑protection impact assessment (DPIA). The FRIA must be performed before deployment and only “complements” an existing DPIA where the DPIA already covers the obligations set out in Article 27 (1) of the AI Act [1]. The deployer may rely on a previously‑conducted FRIA or on one prepared by the provider, but must update it whenever relevant elements change [2].

**Sources cited:** [1] AI Act Article 27(4) - Fundamental rights impact assessment for high-risk AI systems, [2] AI Act Article 27(2) - Fundamental rights impact assessment for high-risk AI systems

**Judge:** correct=yes, faithful=True (The answer correctly states that a FRIA is required and that it complements the DPIA, accurately reflecting the reference note and the cited sources.)

**Your verdict:** Correct = ___ · Faithful = ___

## q070 (cross) Does the AI Act replace the GDPR for AI systems that use personal data?

**Reference:** No: Union data protection law continues to apply; the AI Act does not affect the GDPR (AI Act Art. 2(7)).

**Answer:** The AI Act does not replace the GDPR; Union law on the protection of personal data (the GDPR) continues to apply to personal data processed in connection with AI systems, and the AI Act expressly states it shall not affect Regulation (EU) 2016/679[8].

**Sources cited:** [8] AI Act Article 2(7) - Scope

**Judge:** correct=yes, faithful=True (The answer correctly states that the AI Act does not replace the GDPR and cites Article 2(7) (Source [8]) to support the claim that Union data protection law continues to apply and the AI Act does not affect Regulation (EU) 2016/679.)

**Your verdict:** Correct = ___ · Faithful = ___

## q071 (unanswerable) What is the VAT rate on AI software sold in Germany?

**Reference:** Not covered by the AI Act or GDPR: the assistant should say so.

**Answer:** The AI Act and GDPR texts I have do not answer this question.

**Sources cited:** none

**Judge:** correct=None, faithful=None ()

**Your verdict:** Correct = ___ · Faithful = ___

## q073 (unanswerable) How much should I pay a data protection officer?

**Reference:** Salary is not regulated by the GDPR: should decline.

**Answer:** The AI Act and GDPR texts I have do not answer this question.

**Sources cited:** none

**Judge:** correct=None, faithful=None ()

**Your verdict:** Correct = ___ · Faithful = ___

## q075 (unanswerable) What does the Colorado AI Act require from developers?

**Reference:** US state law, not in the corpus: should decline.

**Answer:** The AI Act and GDPR texts I have do not answer this question.

**Sources cited:** none

**Judge:** correct=None, faithful=None ()

**Your verdict:** Correct = ___ · Faithful = ___
