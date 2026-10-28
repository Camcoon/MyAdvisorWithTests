# COMP 3613 Assignment 2 — Final Lecturer Deliverables Checklist

> **Approved-allocation update ? 27 October 2026:** [Current correction record](reports/degree-requirement-correction.md) supersedes earlier allocation-pending statements and the 735-build attribution for the changed source. Approved fictional category requirements are Core 36, General Education 18, Electives 12, Major 18, Additional 9 (total 93), not official UWI requirements. Historical results/images and synthetic test fixtures below remain preserved. New Postman/manual acceptance remains pending; no old screenshot is relabelled as this build.


Final PDF: [COMP3613_Assignment2_MyAdvisor_Final.pdf](COMP3613_Assignment2_MyAdvisor_Final.pdf)

**57 pages**, reduced from 139. Reviewed 27 October 2026 (America/La_Paz). Original 139-page PDF preserved unchanged. The eight numbered sections follow the requested order; the contents page is unnumbered as a section and appears on physical page 2.

**Submission-ready: NO.** Document assembly and review are complete; the open requirements and findings below remain unresolved. “Included” describes the PDF content, not successful acceptance of the application.

| Lecturer deliverable (exact wording and order) | PDF page(s) | Disposition |
|---|---:|---|
| 1. Name & ID | 1 | Included: Cameron Ramesar, 816044668; verified against the retained statement and Assignment 1 cover. |
| 2. Project Description | 3 | Included: purpose/problem, Student/Advisor, WF1–WF3, technologies and Assignment 2 scope. |
| 3. Use Case Diagram | 4 | Included: actual Assignment 1 diagram; original pixels verified. |
| 4. Entity Relationship Diagram | 5–6 | Included: original ERD plus readable vector keys/relationships from the actual model/source. |
| 5. Application Wireframe | 7–10 | Included: original complete image plus three enlarged workflow panels. |
| 6. Test Plans | 11–31 | Included; plan expectations are separated from execution reports. Google template-specific details remain unverified. |
| User Acceptance Tests Plan | 11–22 | Included: UAT-01–20; objectives/scope, actors/environment, wireframe references, preconditions, steps, data and expected results. |
| Unit Tests | 23–26 | Included: UT-01–23, isolated components, inputs/outputs and positive/negative/boundary strategy. |
| Integration Tests | 27–31 | Included: IT-01–20, real authentication/database/Student–Advisor scenarios and correction supplement. |
| 7. Implementation | 32–35 | Included; publication limitations are explicit. |
| Link to repository | 32 | Clickable intended repository works. Current corrected implementation/evidence publication is incomplete. |
| Unit Tests | 32 | Included: actual pytest files, fixtures/mocks, functions and actual code example. |
| Integration Tests | 33 | Included: TestClient, isolated SQLite/session boundaries, real actor/auth checks and actual workflow excerpt. |
| API Tests (Postman collection exported to JSON in repository) | 34–35 | **INCOMPLETE repository requirement.** Genuine local v2.1 JSON exists, contains 90 requests and is attached to the PDF; intended GitHub export link returns 404. Workspace YAML does not satisfy the exported-JSON requirement. |
| 8. Reports | 36–51 | Included with historical/corrected-build attribution and warning disclosure. |
| Unit Tests Report (screenshot of test results) | 36–39 | Genuine screenshots on 37–39; enlarged 113-pass terminal result on 39. |
| Integration Tests Report (screenshot of test results) | 40–44 | Genuine screenshots on 41–43; enlarged 194-pass terminal result on 43. Supporting full-suite evidence on 44. |
| Postman Collection Run report screenshot | 45–51 | Genuine Runner screenshots on 46–51; 90 requests, 470 assertions passed, 0 observed assertion failures and 0 execution errors. |

## Final verification

| Requested check | Result |
|---|---|
| Generate the new PDF | Complete; final file reopens successfully, 57 pages. |
| Open and visually inspect every page | Complete: all 57 rendered pages reviewed; full-size detail checks on ERD, table and mandatory results; per-page log in final-review/page-review.csv. |
| Check all required deliverables against lecturer list | Complete review; included items and incomplete repository export requirement are distinguished above. |
| Three mandatory testing report screenshots present/readable | Yes: unit page 39, integration page 43 and Postman pages 46–51. Genuine originals retained; no synthetic screenshots. |
| All diagrams included | Yes: use case page 4, original/keyed ERD pages 5–6, original/enlarged wireframe pages 7–10. |
| Exported Postman JSON available in repository | **No.** Live GitHub contents lookup returned 404 twice; complete, untruncated 430-entry remote tree confirms absence. |
| Contents, headings and page numbers | Verified against bookmarks, printed contents entries and numbered page footers. No out-of-margin words or empty pages detected. |
| Evidence and counts accurate | Historical marked runs 113/194; historical full run 715; corrected full run 735 and targeted run 284, reported separately without adding overlapping runs. Retained XML/text checked. |
| Correspondence to final corrected implementation | All 70 app/test source hashes match retained 735-pass run. Historical marked, Runner and UAT screenshots cannot be attributed retroactively to this build; fresh marked/Runner/manual evidence remains outstanding as described. |
| No secrets/passwords/authentication-token values | Scoped PDF and attachment text scans pass; displayed and attached screenshots visually reviewed. Password constants are redacted in attached text copies; exact sanitized collection bytes are preserved. No deployment/private DB credentials copied. |
| Unresolved requirements/findings disclosed | Yes: Appendix B, page 55; full audit/correction records attached. Submission readiness remains NO. |
| Existing PDF preserved until verification | Yes: original 139-page COMP3613_Assignment2_MyAdvisor.pdf hash unchanged. Verified candidate copied to the separate requested Final filename. |

## Repository and template verification

- Repository: https://github.com/Camcoon/MyAdvisorWithTests — public main inspected at `864386fe10fa5e61869e07500d84e51ff7e46b9b`.
- Required exported collection link: https://github.com/Camcoon/MyAdvisorWithTests/blob/main/docs/assignment2/postman/MyAdvisor-Assignment2.postman_collection.json — **does not work (404)**. Local path: `docs/assignment2/postman/MyAdvisor-Assignment2.postman_collection.json`.
- Collection SHA-256: `409cffa7540cd73880d74139f77346cdb47d06a18d9ae8e1b11cf70ef2c44b6d`; exact JSON is embedded in the single PDF. This preserves evidence without claiming remote compliance.
- Main contains A2 API/tests and six pytest PNGs; corrected app/CSS files, correction tests/browser harness, Runner/UAT images and current evidence are unpublished. The local origin names Camcoon/MyAdvisor, a different repository. No publication or remote changes were made.
- Lecturer Google Docs edit/text-export requests were inaccessible. Exact template headings, extra fields, sign-offs and formatting are unverified. Existing plans and explicitly supplied fields were used; no template content was invented.

## Unresolved requirements and audit findings

- **F02/F03:** publish the correct corrected source, sanitized JSON and current evidence to the intended repository and verify retrieval/import. This task stops at the PDF/checklist and does not publish.
- **F04:** latest confirmed UAT remains **1 Pass / 0 Fail / 19 Not Run** (18 partial, UAT-05 unverified); corrected-build manual acceptance and complete Postman retest/supplemental HTML/registration checks are pending.
- **F05 / DATA-01:** fictional demo degree total 93 conflicts with category total 120; owner allocation approval/implementation remains pending. No authoritative UWI curriculum is claimed.
- **F09/F15:** CSRF/trusted-origin design and production signing-key disposition remain open; no deployed security certification or live exploit claim.
- **F10/F13:** historical build attribution remains incomplete; Postman percentage/discovery assertions need stronger independent oracles and a new retained run.
- **F01/F07/F08:** fixes are regression-tested locally but unpublished and still require the documented new browser/API evidence. **F06:** computed contrast passes locally; human readability acceptance remains pending.
- **F12/F14/F16:** remote documentation is older; duplicate-tree cleanup is suggested; one disclosed Starlette/httpx deprecation remains.
- External template-specific requirements are unverified. These limitations prevent a submission-ready declaration.

Supporting UAT summary: pages 52–54. Findings: page 55. Traceability: page 56. Lecturer checklist inside PDF: page 57. All 19 original UAT images, six pytest screenshots, six Runner screenshots and full supporting records are preserved among 56 embedded attachments.

Final PDF SHA-256: `e26ab1fe95ab668a2bbf46871493ce82821bccd41e58aa22440dcd26d7d37acd`.
Verification record: `final-review/validation-report.json`; page review: `final-review/page-review.csv`.
