📋 PHASE 3 — CONSOLIDATION & ARCHIVE — ROADMAP

Status: READY TO BEGIN
Objective: Consolidate 7 git accordion CSS files + Create _archive.css documentation
Estimated Duration: 2-3 hours
Complexity: Medium (file merging + documentation)

═════════════════════════════════════════════════════════════════════════════

PHASE 3 PART A: GIT ACCORDION CONSOLIDATION

Current State:
  Scattered git_accordion CSS across 7 separate files in blog/static/blog/css/
  
Files to Consolidate:
  1. git_accordion_basics.css
  2. git_accordion_buttons.css  
  3. git_accordion_colors.css
  4. git_accordion_structure.css
  5. git_accordion_responsive.css
  6. git_accordion_animations.css
  7. git_accordion_misc.css (or similar)

Consolidation Strategy:
  1. List all 7 files and their line counts
  2. Read each file:
     - Extract CSS selectors
     - Note any duplicates across files
     - Preserve comments and reasoning
  3. Merge order (semantic):
     - Structure(.git-accordion-board, .git-accordion-card, grid layout)
     - Styling (colors, borders, backgrounds)
     - Buttons (.accordion-btn, states)
     - Animations (@keyframes, transitions)
     - Responsive (@media queries)
     - Miscellaneous (utilities)
  4. Create git_accordion_consolidated.css with:
     - All selectors merged without duplication
     - Section headers marking original file boundaries
     - Comments tracking consolidation
  5. Update index.css:
     - Remove 7 separate @imports
     - Add 1 import for git_accordion_consolidated.css
  6. Keep original files as reference in git history
  7. Optional: Create git_accordion/README.md documenting consolidation

Deliverable:
  ✓ blog/static/blog/css/git_accordion_consolidated.css (~500-800 lines merged)
  ✓ Updated index.css with single git accordion import
  ✓ Phase 3A_CONSOLIDATION_REPORT.md (documenting merge process)

═════════════════════════════════════════════════════════════════════════════

PHASE 3 PART B: ARCHIVE CSS DOCUMENTATION

Current State:
  34+ orphaned CSS classes scattered throughout project
  Not used anywhere, kept for future reference or legacy support
  
Objective:
  Document all orphaned classes in _archive.css with:
  - Original CSS selector and rules
  - Reason for archiving (deprecated, unused, legacy)
  - Potential use cases (in case revival needed)
  - Date archived & originating file

Structure of _archive.css:
  
  /* ============================================================
     ARCHIVED CSS — Legacy & Orphaned Classes
     
     This file documents CSS rules that are no longer actively used
     but are kept for reference. Do not remove without consulting
     the project archive or historical records.
     
     Organization:
     1. Animations & Transitions (retired effects)
     2. ARIA & Accessibility (fallback rules)
     3. Legacy Utilities (deprecated patterns)
     4. Theme Variants (old color schemes)
     5. Responsive Hacks (outdated breakpoints)
     6. Stitch-specific (deprecated board patterns)
     7. Editorial (blog pagination, etc.)
     ============================================================ */

  /* ─────────────────────────────────────────────────────────────
     SECTION 1: ANIMATIONS & TRANSITIONS — ARCHIVED
     ───────────────────────────────────────────────────────────── */
  
  /* Deprecated: Pulse animation (replaced by HELB pulse-fade)
     Original use: loading states in older UI
     Archived: 2025-01-15
     Reason: Superseded by HELB design system animations
  */
  @keyframes pulse-old {
    0% { opacity: 1; }
    50% { opacity: 0.5; }
    100% { opacity: 1; }
  }

  .pulse-old {
    animation: pulse-old 2s infinite;
  }

Discovery Script:
  Use grep/regex to find orphaned classes by searching for:
  - Selectors not referenced in any template (.html files)
  - Selectors not used in any view (.py files)
  - Selectors not referenced in any document
  
  Tools:
  - grep -r "\.class-name" blog/templates/ blog/views.py
  - grep -r "class-name" blog/static/blog/js/
  - Manual code review for documented orphans

Categories Expected:
  ~ 8-12 Animation classes (old effects)
  ~ 5-7 ARIA utilities (accessibility fallbacks)
  ~ 6-8 Legacy grid/layout (float-based old layouts)
  ~ 4-5 Theme variants (deprecated color schemes)
  ~ 3-4 Responsive hacks (old breakpoint code)
  ~ 2-3 Stitch-specific old patterns
  ~ 3-5 Editorial/blog classes
  ──────────────────────────────
  Total: 31-44 orphaned rules (matches 34 estimated)

Deliverable:
  ✓ blog/static/blog/css/_archive.css (~800-1200 lines documented)
  ✓ Comprehensive comments for each orphaned class
  ✓ Categories marked with section headers
  ✓ Phase 3B_ARCHIVE_REPORT.md (audit trail)

═════════════════════════════════════════════════════════════════════════════

PHASE 3 TASKS IN ORDER

[ ] Task 3.1 — Discover git accordion files
    Find all blog/static/blog/css/git_accordion_*.css files
    
[ ] Task 3.2 — Analyze each git accordion file
    - Read each file
    - Count lines and selectors
    - Identify duplicates across files
    - Note any conflicts

[ ] Task 3.3 — Create git_accordion_consolidated.css
    - Merge all 7 files
    - Remove duplicates
    - Add semantic section headers
    - Add merge documentation

[ ] Task 3.4 — Update index.css
    - Replace 7 @imports with 1 consolidated import
    - Update Phase 3 status comment

[ ] Task 3.5 — Create _archive.css
    - Discover orphaned CSS classes
    - Organize by category
    - Add documentation for each
    - Format consistently

[ ] Task 3.6 — Update index.css (again)
    - Verify both consolidated imports are correct
    - Update Phase 3 status to COMPLETE
    - Begin Phase 4 visibility

[ ] Task 3.7 — Create Phase 3 completion report
    - Document consolidation metrics
    - List orphaned classes with categories
    - Provide audit trail
    - Sign off for Phase 4

═════════════════════════════════════════════════════════════════════════════

METRICS TO TRACK

Phase 3A (Git Accordion):
  - Original: 7 separate files
  - Lines before: [TBD after discovery]
  - Lines after: [TBD after consolidation]
  - Duplicates found: [TBD]
  - Duplicates removed: [TBD]
  - Reduction: [TBD] lines

Phase 3B (Archive):
  - Orphaned classes discovered: [TBD, expect ~34]
  - Categories: [7-8 expected]
  - Documentation lines: [estimate 25-30 lines per class]
  - Total archive lines: [estimate 800-1200]

═════════════════════════════════════════════════════════════════════════════

PHASE 4 AWAITS: DEDUPLICATION

After Phase 3 completes:
  • 111+ Type B duplicate CSS rules identified for removal
  • Consolidate identical selectors
  • Reduce CSS payload by ~15% (target: 130 KB from 155 KB)
  • Merge rule implementations
  • Create deduplication report

═════════════════════════════════════════════════════════════════════════════

NEXT COMMAND: Begin Phase 3A (Git Accordion Discovery)

Start with:
  1. List all files in blog/static/blog/css/
  2. Filter for git_accordion_*.css pattern
  3. Read each file to understand structure
  4. Count lines and identify consolidation strategy
