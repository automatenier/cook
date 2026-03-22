## Implementation Status (UPDATED 2026-03-22)

### 1. Unified Brand Configuration
Created `AI_Tools/brands.json` to store IDs for all brands.
- **HTS Agency:** Configured.
- **Toyota:** Configured.
- **Real Estate:** Facebook Page ID (`61585032227421`) configured. **IG User ID pending.**

### 2. Tool Updates
Updated `AI_Tools/content_fb_ig_post.py` and `AI_Tools/content_post_all.py` to support the `--brand` flag.
- Usage: `py -3 AI_Tools/content_post_all.py --file "video.mp4" --title "Title" --description "Desc" --brand realestate`

### 3. Simplified Commands
**For Real Estate:**
```powershell
py -3 AI_Tools/content_post_all.py --file "[PATH]" --title "[TITLE]" --description "[CAPTION]" --brand realestate
```

---

## Original Plan (Reference)
L1- # Implementation Plan: Multi-Brand Content Scheduling (HTS Agency vs. Real Estate)

This plan outlines the setup for distinct content scheduling workflows for **HTS Agency** and your **Real Estate personal brand**. This ensures that assets, captions, and Meta credentials (FB Page ID / IG User ID) are correctly mapped to each brand.

## Objective
To enable seamless, independent posting for two distinct brands using the existing `content_fb_ig_post.py` tool by formalizing their credentials and target platforms.

## Key Files & Context
- **Tool:** `AI_Tools/content_fb_ig_post.py` (handles the API logic).
- **Credentials:** Found in `.pass` (currently retrieved manually; should be formalized in `.env`).
- **Brand 1: HTS Agency**
  - **Focus:** AI Agency / Personal Brand.
  - **Meta Page ID:** `498449366690089` (HTS Agency).
  - **IG User ID:** `17841401286528474`.
- **Brand 2: Real Estate**
  - **Focus:** 9-5 Personal Brand / Properties.
  - **Meta Page ID:** `61585032227421` (savasainhouse_jordan).
  - **IG User ID:** [UPDATE NEEDED: @savasainhouse_jordan ID]

## Implementation Steps

### 1. Formalize Credentials in `.env`
Update the `.env` file to store credentials for both brands using prefixes to avoid confusion.
- `HTS_META_PAGE_ID`
- `HTS_IG_USER_ID`
- `RE_META_PAGE_ID`
- `RE_IG_USER_ID`
- `META_PAGE_ACCESS_TOKEN` (Shared, as they are under the same Business Portfolio/System User).

### 2. Update Tool to Support Brand-Specific Environments (Optional but Recommended)
Modify `AI_Tools/content_fb_ig_post.py` to accept a `--brand` flag that automatically loads the correct IDs, or use a wrapper script.

### 3. Create Simplified Commands/Aliases
Provide ready-to-use commands for each brand.

**For HTS Agency:**
```powershell
$env:META_FB_PAGE_ID="498449366690089"; $env:META_IG_USER_ID="17841401286528474"; py -3 AI_Tools/content_fb_ig_post.py --file "[PATH]" --caption "[TEXT]" --platform both
```

**For Real Estate:**
```powershell
# Update IDs first
$env:META_FB_PAGE_ID="[SAVASA_PAGE_ID]"; $env:META_IG_USER_ID="[SAVASA_IG_ID]"; py -3 AI_Tools/content_fb_ig_post.py --file "[PATH]" --caption "[TEXT]" --platform both
```

## Verification & Testing
1. **Verification:** Identify the correct Meta Page ID and Instagram User ID for the @savasainhouse_jordan account.
2. **Test Post:** Run a test with a placeholder image to the Real Estate brand to verify the connection.
3. **Cross-Check:** Ensure HTS Agency posts continue to land on the correct HTS Agency profiles.

## Migration & Rollback
- The logic in `content_fb_ig_post.py` remains unchanged, maintaining backward compatibility.
- New brand-specific environment variables in `.env` will not interfere with existing tool behavior.
