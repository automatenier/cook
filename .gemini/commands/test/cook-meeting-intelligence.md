> **Model: Sonnet** -- extracting structured insight from raw conversation

# Workflow: Meeting Intelligence

When user asks to `/meeting-intelligence [filename or ClientName]`:

1. **Locate Transcript**: `02 HMN_A INPUTS/meetings/[filename].md` or ask user to paste.
2. **Extract Structure**:
   - Meeting Type: Discovery / Check-in / Sales call / Internal / RE viewing
   - Date & Participants
   - Key Decisions Made
   - Pain Points Mentioned (direct quotes preferred)
   - Action Items (with owner and deadline)
   - Follow-up Required: Yes/No + what
3. **Route Output**:

   | Meeting Type | Output Location |
   |---|---|
   | JO Consult client | `PDCT_JO_Consult/clients/[ClientName]/meeting_[Date].md` |
   | Sales / discovery | `PDCT_JO_Consult/pipeline/[ProspectName]_[Date].md` |
   | RE prospect | `PDCT_Real_Estate/prospects/[Name]_[Date].md` |
   | RE property tour | `PDCT_Real_Estate/properties/[Property]_notes.md` |
   | Internal | `02 HMN_A INPUTS/ideas/[Date]_meeting_notes.md` |

4. **Update CRM**: Remind user to add action items to the relevant tracker manually.
5. **Archive Transcript**: Move from `02 HMN_A INPUTS/meetings/` to `VLT_Content/ZZ_ARCHIVE/meetings/`.

```bash
/meeting-intelligence Fadli_2026-03-03
/meeting-intelligence Fadli
```
