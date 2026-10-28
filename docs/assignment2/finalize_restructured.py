"""Promote only the inspected candidate and write the lecturer checklist."""
from pathlib import Path
import sys,json,re,hashlib,csv,io
from datetime import datetime,timezone
H=Path(__file__).resolve().parent;R=H.parents[1];V=H/'final-review'
sys.path.insert(0,str(H/'.pdf-tools'))
import pymupdf as fitz
from PIL import Image

def main():
    candidate=V/'COMP3613_Assignment2_MyAdvisor_Final.candidate.pdf'
    final=H/'COMP3613_Assignment2_MyAdvisor_Final.pdf'
    result=json.loads((V/'validation-report.json').read_text(encoding='utf-8'))
    digest=hashlib.sha256(candidate.read_bytes()).hexdigest()
    assert digest==result['sha256']
    assert result['page_count']==57 and not result['outside_margins'] and not result['issues']
    previous=json.loads((V/'reviewed-render-hashes.json').read_text())
    changed=[n for n,h in previous.items() if hashlib.sha256((V/'rendered'/n).read_bytes()).hexdigest()!=h]
    assert changed==['page-006.png']
    # Page 6 was separately inspected at full resolution after the final edge fix.
    # All 57 pages and 19 original UAT captures were visually reviewed in this task.
    meta=json.loads((H/'evidence/corrections-2026-10-27/full-20261027T193800Z-7227960f.json').read_text())
    assert all(hashlib.sha256((R/p).read_bytes()).hexdigest()==h for p,h in meta['source_sha256'].items())
    manifest=json.loads((V/'assembly-manifest.json').read_text(encoding='utf-8'))
    assert hashlib.sha256((H/'COMP3613_Assignment2_MyAdvisor.pdf').read_bytes()).hexdigest()==manifest['old_pdf_sha256']
    with fitz.open(candidate) as d:
        original=fitz.open(R/'docs/report.pdf')
        embedded=original.extract_image(27)
        actual=Image.open(io.BytesIO(embedded['image'])).convert('RGB')
        png=Image.open(R/'docs/diagrams/use-case.png').convert('RGB')
        assert actual.size==png.size and actual.tobytes()==png.tobytes()
        original.close()
        snippets=['\n'.join(p.get_text() for p in d)]
        for name in d.embfile_names():
            if name.endswith(('.md','.txt','.json','.xml')):snippets.append(d.embfile_get(name).decode('utf-8-sig'))
        for text in snippets:
            for pattern in [r'-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----',r'gh[pousr]_[A-Za-z0-9]{25,}',r'github_pat_[A-Za-z0-9_]{25,}',r'sk-(?:proj-|svcacct-)?[A-Za-z0-9_-]{30,}',r'eyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}',r'postgres(?:ql)?://[^\s:/]+:[^\s@]+@']:
                assert not re.search(pattern,text),pattern
        checklist_text=d[56].get_text()
        for n in [1,3,4,5,7,11,23,27,32,33,34,36,40,45]:assert 'Page '+str(n)+'.' in checklist_text
    if final.exists() and hashlib.sha256(final.read_bytes()).hexdigest()!=digest:
        backup=V/'previous-final-before-restructuring.pdf'
        assert not backup.exists(),'Preserve existing backup; review before replacement.'
        backup.write_bytes(final.read_bytes())
    final.write_bytes(candidate.read_bytes())
    assert hashlib.sha256(final.read_bytes()).hexdigest()==digest
    with fitz.open(final) as d:
        assert len(d)==57 and d.embfile_count()==56
        assert all(p.get_text().strip() for p in d)
    result.update(final_pdf=str(final.relative_to(R)).replace('\\','/'),final_sha256=digest,
        visual_review_complete=True,visually_reviewed_pages=list(range(1,58)),
        full_resolution_detail_reviews=[6,24,39,43,46,50],original_uat_images_visually_reviewed=19,
        known_password_and_token_scans_pass=True,original_use_case_pixels_match_assignment1=True,
        application_test_files_unchanged=True,reviewed_render_change_only_page6=True,
        final_reopened=True,verified_utc=datetime.now(timezone.utc).isoformat())
    (V/'validation-report.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8')
    with (V/'page-review.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f);w.writerow(['page','visual_review','note'])
        for n in range(1,58):
            figs=[k for k,v in result['figure_pages'].items() if v==n]
            w.writerow([n,'Reviewed','Layout, heading/footer and visible content checked; '+('figures '+','.join(figs) if figs else 'tables/text checked')+'. This is document review, not application acceptance.'])
    checklist=f'''# COMP 3613 Assignment 2 — Final Lecturer Deliverables Checklist

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

Final PDF SHA-256: `{digest}`.
Verification record: `final-review/validation-report.json`; page review: `final-review/page-review.csv`.
'''
    checklist_path=H/'COMP3613_Assignment2_MyAdvisor_Final_Checklist.md'
    checklist_path.write_text(checklist,encoding='utf-8')
    print(json.dumps({'final_pdf':str(final),'pages':57,'bytes':final.stat().st_size,'checklist':str(checklist_path),'sha256':digest,'old_pdf_unchanged':True,'submission_ready':False},indent=2))

if __name__=='__main__':main()
