# CSS Visual Regression Analysis & Recovery Plan

**Generated:** April 7, 2026  
**Status:** PRODUCTION BLOCKING - Critical CSS missing from utility and layout files  
**Impact:** Dashboard rendering broken - images, titles, spacing, responsive layout all affected

---

## EXECUTIVE SUMMARY

The deletion of `main-consolidated-pending.css` and trimming of `cards-panels.css` removed **critical display-critical CSS** that was needed for:
- Image sizing (profile pictures now disproportionate)
- Typography scales (project names unreadable)
- Spacing/padding (layout collapsed)
- Responsive breakpoints (mobile layout broken)
- Flex/grid helpers (elements misaligned)

**Finding:** The CSS architecture was fragmented. Essential layout CSS lived in the removed files but should have been in `layout.css` and `utilities-theme.css`.

---

## 1. IMAGE SIZING & PROPORTIONS

### Profile Picture Rules (MISSING) ⚠️ CRITICAL

#### `.helb-user-chip img` — User chip avatar in navbar
```css
.helb-user-chip img {
  width: 2.35rem;
  height: 2.35rem;
  border-radius: 999px;
  object-fit: cover;
  box-shadow: var(--helb-shadow-sm);
}
```
**Location in original:** Line ~750  
**Current status:** NOT in utilities-theme.css or layout.css  
**Impact:** User profile picture in top navbar is stretched/broken  

---

#### `.atelier-avatar-group__avatar` — User avatars in lists/teams
```css
.atelier-avatar-group__avatar,
.atelier-user-cell__avatar {
  width: 2.55rem;
  height: 2.55rem;
  border: 3px solid var(--helb-surface-container-lowest);
  box-shadow: var(--helb-shadow-sm);
  object-fit: cover;
  border-radius: 999px;
}

.atelier-avatar-group__avatar + .atelier-avatar-group__avatar {
  margin-left: -0.85rem;
}
```
**Location in original:** Line ~1030  
**Current status:** NOT in utilities-theme.css or layout.css  
**Impact:** Avatar groups have NO sizing, NO overlap offset  

---

#### `.atelier-profile-identity__avatar` — Dashboard profile picture (LARGEST)
```css
.atelier-profile-identity__avatar {
  width: 6.75rem;
  height: 6.75rem;
  margin: 0 auto 1.2rem;
  box-shadow: var(--helb-shadow-md);
  object-fit: cover;
  border-radius: 999px;
}
```
**Location in original:** Line ~1090  
**Current status:** NOT in utilities-theme.css or layout.css  
**Impact:** Dashboard profile picture is MASSIVE and unproportioned  

---

#### `.atelier-user-inline__avatar` — Inline user references
```css
.atelier-user-inline__avatar {
  width: 2rem;
  height: 2rem;
  box-shadow: var(--helb-shadow-sm);
  object-fit: cover;
  border-radius: 999px;
}
```
**Location in original:** Line ~1230  
**Current status:** NOT in utilities-theme.css or layout.css  

---

#### `.kanban-card__avatar` — Kanban board assignee avatars
```css
.kanban-card__avatar {
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  border: 2px solid var(--helb-surface-container-lowest);
  box-shadow: var(--helb-shadow-sm);
  object-fit: cover;
}
```
**Location in original:** Line ~1515  
**Current status:** NOT in utilities-theme.css or layout.css  

---

### ⚠️ RECOMMENDATION: Image Sizing

**ACTION REQUIRED:** Add ALL image sizing rules to `components/layout.css`
```css
/* Image & Avatar Sizing */
.helb-user-chip img,
.atelier-user-inline__avatar,
.atelier-user-cell__avatar,
.atelier-avatar-group__avatar,
.kanban-card__avatar,
.atelier-profile-identity__avatar {
  object-fit: cover;
  border-radius: 999px;
}

.helb-user-chip img {
  width: 2.35rem;
  height: 2.35rem;
  box-shadow: var(--helb-shadow-sm);
}

/* ... add all other image rules ... */
```

---

## 2. TYPOGRAPHY - PROJECT NAMES & TITLES

### Font-size Scale Rules (MISSING) ⚠️ CRITICAL

The original CSS uses `clamp()` for responsive typography. These are COMPLETELY MISSING:

#### `.atelier-project-card__title` — Project names in dashboard
```css
.atelier-project-card__title {
  font-size: clamp(1.4rem, 2vw, 1.9rem);
  font-weight: 800;
  line-height: 1.08;
  letter-spacing: -0.05em;
  color: var(--helb-primary);
}
```
**Location in original:** Line ~1065  
**Current status:** NOT in utilities-theme.css or layout.css  
**Impact:** Project names rendered at browser default size (too small)  

---

#### `.atelier-page-header__title` — Dashboard page title
```css
.atelier-page-header__title {
  margin: 0.35rem 0 0.45rem;
  font-size: clamp(2.25rem, 4vw, 3.75rem);
  font-weight: 800;
  line-height: 0.98;
  letter-spacing: -0.07em;
  color: var(--helb-on-surface);
}
```
**Location in original:** Line ~975  
**Current status:** NOT in utilities-theme.css or layout.css  

---

#### `.stitch-ticket-title` — Ticket detail page title
```css
.stitch-ticket-title {
  margin: 0;
  font-weight: 800;
  letter-spacing: -0.05em;
  font-size: clamp(2rem, 3vw, 3rem);
  line-height: 1.02;
}
```
**Location in original:** Line ~3570  
**Current status:** NOT in utilities-theme.css or layout.css  

---

#### `.stitch-epic-card__title` — Epic card titles
```css
.stitch-epic-card__title {
  display: inline-block;
  font-size: 1.4rem;
  font-weight: 800;
  line-height: 1.08;
  letter-spacing: -0.05em;
  color: var(--helb-primary-container);
}
```
**Location in original:** Line ~4965  
**Current status:** NOT in utilities-theme.css or layout.css  

---

#### `.stitch-sprint-panel__header h3` — Sprint panel titles
```css
.stitch-sprint-panel__header h3 {
  margin: 0.35rem 0 0;
  font-size: clamp(1.55rem, 2vw, 2rem);
  font-weight: 800;
  letter-spacing: -0.05em;
  color: var(--helb-primary-container);
}
```
**Location in original:** Line ~4935  

---

#### Other typography classes also missing:
- `.atelier-panel__title` — panel section titles
- `.atelier-stat-card__value` — statistics values  
- `.stitch-kpi-tile strong` — KPI values
- `.atelier-profile-identity__name` — profile names

---

### ⚠️ RECOMMENDATION: Typography

**ACTION REQUIRED:** Add all typography sizing rules to `components/layout.css` or new `components/typography.css`

```css
/* Responsive Typography Scale */
.atelier-project-card__title {
  font-size: clamp(1.4rem, 2vw, 1.9rem);
  font-weight: 800;
  line-height: 1.08;
  letter-spacing: -0.05em;
}

.atelier-page-header__title {
  font-size: clamp(2.25rem, 4vw, 3.75rem);
  font-weight: 800;
  line-height: 0.98;
  letter-spacing: -0.07em;
}

/* ... add all other typography ... */
```

---

## 3. SPACING & PADDING UTILITIES

### Card & Container Spacing (MISSING) ⚠️ CRITICAL LAYOUT

The original CSS defines specific padding for each component type. Current CSS has NO padding rules:

#### `.atelier-project-card` — Project cards in dashboard
```css
.atelier-project-card {
  padding: 1.65rem 1.75rem;
  background: color-mix(in srgb, var(--helb-surface-container-lowest) 92%, transparent);
  border-radius: 1.75rem;
  box-shadow: var(--helb-shadow-md);
}
```
**Location in original:** Line ~1050  
**Current status:** Card styling is in cards-panels.css but NOT responsive padding  

---

#### `.atelier-stat-card` — Statistics/KPI cards
```css
.atelier-stat-card {
  padding: 1.2rem 1.25rem;
  background: color-mix(in srgb, var(--helb-surface-container-lowest) 92%, transparent);
  border-radius: 1.75rem;
  box-shadow: var(--helb-shadow-md);
}
```
**Location in original:** Line ~1040  
**Current status:** NOT in utilities-theme.css or layout.css  

---

#### `.atelier-panel` — Generic panel containers
```css
.atelier-panel,
.atelier-role-table-shell {
  padding: 1.5rem 1.65rem;
  background: color-mix(in srgb, var(--helb-surface-container-lowest) 92%, transparent);
  border-radius: 1.75rem;
  box-shadow: var(--helb-shadow-md);
}
```
**Location in original:** Line ~1175  
**Current status:** Partially in cards-panels.css but incomplete  

---

#### `.helb-card` & `.helb-card-sm` — HELB utility cards
```css
.helb-card {
  padding: 1.5rem 2rem;
  background: color-mix(in srgb, var(--helb-surface-container-lowest) 92%, transparent);
  border-radius: var(--helb-radius-lg);
  box-shadow: var(--helb-shadow-md);
}

.helb-card-sm {
  padding: 1.25rem 1.5rem;
  background: color-mix(in srgb, var(--helb-surface-container-lowest) 94%, transparent);
  border-radius: var(--helb-radius-md);
  box-shadow: var(--helb-shadow-sm);
}
```
**Location in original:** Line ~1660, 1670  
**Current status:** IN cards-panels.css ✓ BUT responsive padding missing  

---

### Grid Gap & Margin Rules (MISSING) ⚠️ CRITICAL

#### `.atelier-project-card__meta-grid` — Project metadata grid
```css
.atelier-project-card__meta-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
  margin-top: 1.4rem;
  padding-top: 1.2rem;
  border-top: 1px solid rgba(195, 198, 208, 0.16);
}
```
**Location in original:** Line ~1015  
**Current status:** NOT in utilities-theme.css or layout.css  
**Impact:** Project metadata spacing is completely collapsed  

---

#### `.atelier-project-card__footer` — Footer spacing
```css
.atelier-project-card__footer {
  margin-top: 1.25rem;
  padding-top: 1.2rem;
  border-top: 1px solid rgba(195, 198, 208, 0.1);
}
```
**Location in original:** Line ~1020  

---

#### `.atelier-stats-grid` — Dashboard stats grid
```css
.atelier-stats-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1rem;
  margin-bottom: 1.75rem;
}
```
**Location in original:** Line ~1005  
**Current status:** NOT in utilities-theme.css or layout.css  

---

#### `.atelier-mini-stats-grid` — Mini stats
```css
.atelier-mini-stats-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 0.75rem;
  margin-top: 1.4rem;
}
```
**Location in original:** Line ~1105  

---

#### `.stitch-info-grid` — Information tiles
```css
.stitch-info-grid {
  display: grid;
  gap: 1rem;
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.stitch-info-tile {
  display: grid;
  gap: 0.3rem;
  background: var(--helb-surface-container-low);
  border-radius: 1.35rem;
  padding: 1rem 1.05rem;
}
```
**Location in original:** Line ~3530  

---

### ⚠️ RECOMMENDATION: Spacing

**ACTION REQUIRED:** Add spacing rules to `components/layout.css`

```css
/* Card Padding */
.atelier-project-card {
  padding: 1.65rem 1.75rem;
}

.atelier-stat-card {
  padding: 1.2rem 1.25rem;
}

.atelier-panel {
  padding: 1.5rem 1.65rem;
}

/* Grid Gaps */
.atelier-stats-grid {
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1rem;
  margin-bottom: 1.75rem;
}

.atelier-project-card__meta-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
  margin-top: 1.4rem;
  padding-top: 1.2rem;
}

/* ... add all other spacing ... */
```

---

## 4. RESPONSIVE LAYOUT BREAKPOINTS

### Media Query Rules (MISSING ENTIRELY) ⚠️ CRITICAL

#### Breakpoint: 1199.98px (tablet/large)
```css
@media (max-width: 1199.98px) {
  .helb-user-chip__text {
    display: none;
  }
  
  .atelier-stats-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
  
  .atelier-profile-layout,
  .atelier-profile-layout--admin {
    grid-template-columns: 1fr;
  }
}
```
**Location in original:** Line ~2360  
**Current status:** MISSING entirely from utilities-theme.css  
**Impact:** Tablet views have 4-column grids that overflow the screen  

---

#### Breakpoint: 991.98px (tablet/medium)
```css
@media (max-width: 991.98px) {
  .helb-sidebar {
    display: none;
  }

  .helb-topnav--app {
    left: 0;
    width: 100%;
  }

  .helb-main {
    margin-left: 0;
    padding: 1.5rem 1rem 3rem;
  }

  .helb-topnav-search {
    max-width: none;
  }

  .helb-auth-shell--split {
    grid-template-columns: 1fr;
  }

  .helb-auth-card {
    padding: 1.75rem;
  }

  .atelier-project-card__meta-grid {
    grid-template-columns: repeat(2, minmax(0, 1fr));
  }
}
```
**Location in original:** Line ~2379  
**Current status:** MISSING entirely from utilities-theme.css  
**Impact:** Tablets lose sidebar, layout margins collapse incorrectly  

---

#### Breakpoint: 768px (mobile)
```css
@media (max-width: 768px) {
  .helb-topnav {
    padding: 0 1rem;
  }

  .helb-topnav-right {
    gap: 0.5rem;
  }

  .helb-topnav-search {
    display: none;
  }

  .helb-theme-fab {
    right: 1rem;
    bottom: 1rem;
  }

  .helb-auth-body {
    padding: 1rem;
  }

  .helb-auth-card,
  .helb-auth-card--compact {
    padding: 1.5rem;
  }

  .atelier-page-header {
    align-items: flex-start;
  }

  .atelier-stats-grid {
    grid-template-columns: 1fr;
  }

  .atelier-project-card,
  .atelier-panel,
  .atelier-role-table-shell {
    padding: 1.25rem;
  }

  .atelier-project-card__top,
  .atelier-project-card__footer,
  .atelier-panel__split-header,
  .atelier-ticket-stack__item {
    flex-direction: column;
  }

  .atelier-project-card__meta-grid,
  .atelier-mini-stats-grid {
    grid-template-columns: 1fr;
  }

  .atelier-ticket-stack__status {
    align-items: flex-start;
  }

  .atelier-table thead th,
  .atelier-table tbody td {
    padding-left: 0.95rem;
    padding-right: 0.95rem;
  }

  .atelier-inline-code {
    max-width: 100%;
  }
}
```
**Location in original:** Line ~2413  
**Current status:** MISSING entirely from utilities-theme.css  
**Impact:** Mobile views are COMPLETELY broken  

---

### ⚠️ RECOMMENDATION: Responsive Breakpoints

**ACTION REQUIRED:** Add ALL media queries to `components/utilities-theme.css`

Create a dedicated responsive section with all three breakpoints.

---

## 5. FLEX & GRID LAYOUT HELPERS

### Display Helpers (MISSING) ⚠️ CRITICAL

#### `.atelier-project-card__top` — Header flex row
```css
.atelier-project-card__top,
.atelier-project-card__footer,
.atelier-panel__split-header,
.atelier-ticket-stack__item,
.atelier-user-inline,
.atelier-user-cell,
.atelier-project-ref {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
}
```
**Location in original:** Line ~1050  
**Current status:** NOT in utilities-theme.css or layout.css  
**Impact:** Project card elements are NOT aligned side-by-side  

---

#### `.atelier-project-card__content` — Content flex container
```css
.atelier-project-card__content {
  flex: 1;
  min-width: 0;
}
```
**Location in original:** Line ~1055  
**Current status:** NOT in utilities-theme.css or layout.css  
**Impact:** Content doesn't expand to fill available space  

---

#### `.atelier-stats-grid` — Dashboard KPI grid
```css
.atelier-stats-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1rem;
  margin-bottom: 1.75rem;
}
```
**Location in original:** Line ~1005  
**Current status:** NOT in layout.css  

---

#### `.atelier-profile-layout` — Profile page grid
```css
.atelier-profile-layout {
  display: grid;
  grid-template-columns: minmax(18rem, 23rem) minmax(0, 1fr);
  gap: 1.5rem;
  align-items: start;
}

.atelier-profile-layout--admin {
  grid-template-columns: minmax(21rem, 28rem) minmax(0, 1fr);
}
```
**Location in original:** Line ~1080  
**Current status:** NOT in utilities-theme.css or layout.css  
**Impact:** Profile page has NO 2-column layout  

---

#### `.stitch-project-shell` — Project page layout
```css
.stitch-project-shell {
  display: grid;
  gap: 1.5rem;
  align-items: start;
  grid-template-columns: minmax(0, 1.65fr) minmax(20rem, 0.9fr);
}
```
**Location in original:** Line ~3515  
**Current status:** NOT in layout.css  

---

#### `.stitch-ticket-layout` — Ticket detail layout
```css
.stitch-ticket-layout {
  display: grid;
  gap: 1.5rem;
  align-items: start;
  grid-template-columns: minmax(0, 1.7fr) minmax(19.5rem, 0.95fr);
}
```
**Location in original:** Line ~3520  

---

#### `.atelier-avatar-group` — Avatar group flex container
```css
.atelier-page-header__actions,
.atelier-tag-filter,
.atelier-form-actions,
.atelier-ticket-stack__badges,
.atelier-pill-list,
.atelier-avatar-group {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
}
```
**Location in original:** Line ~1000  
**Current status:** NOT in utilities-theme.css or layout.css  

---

### ⚠️ RECOMMENDATION: Layout Helpers

**ACTION REQUIRED:** Add flex/grid helper classes to `components/layout.css`

```css
/* Flex Row Helpers */
.atelier-project-card__top,
.atelier-project-card__footer,
.atelier-panel__split-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
}

/* Grid Layouts */
.atelier-stats-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1rem;
}

.atelier-profile-layout {
  display: grid;
  grid-template-columns: minmax(18rem, 23rem) minmax(0, 1fr);
  gap: 1.5rem;
  align-items: start;
}

/* ... add all other layout helpers ... */
```

---

## SUMMARY: WHAT'S MISSING VS WHAT EXISTS

### ✅ EXISTS (in cards-panels.css):
- `.helb-card` and `.helb-card-sm` basic styling
- `.card` and `.card-body` overrides
- `.content-section` styling

### ❌ MISSING (should be in layout.css):
1. **Image sizing** (all `.atelier-*__avatar` classes)
2. **Typography scales** (all `font-size: clamp()` rules)
3. **Component padding** (`.atelier-stat-card`, `.atelier-panel`, etc.)
4. **Grid definitions** (`.atelier-stats-grid`, `.atelier-profile-layout`, etc.)
5. **Flex rows** (`.atelier-project-card__top`, etc.)
6. **ALL responsive media queries** (1199px, 991px, 768px breakpoints)

### ✅ EXISTS (in utilities-theme.css):
- Color theme variables
- Basic utility classes (`.text-muted`, `.bg-light`, `.shadow-sm`)
- Dark theme definitions
- Form control styling
- Scrollbar styling

### ❌ MISSING (should be in utilities-theme.css):
- **ALL media query breakpoints** (entire responsive section)

---

## CRITICAL RECOMMENDATIONS

### 🚨 PRIORITY 1 - RECOVER IMMEDIATELY:
1. **Restore image sizing CSS** → Add all `.atelier-*__avatar` and `.helb-user-chip img` rules to `layout.css`
2. **Restore typography scale** → Add all `clamp()` font-size rules to `layout.css`
3. **Restore component padding** → Add `.atelier-stat-card`, `.atelier-panel`, `.atelier-project-card` padding

### 🚨 PRIORITY 2 - FIX LAYOUT:
4. **Restore grid layouts** → Add `.atelier-stats-grid`, `.atelier-profile-layout`, `.stitch-project-shell` to `layout.css`
5. **Restore flex rows** → Add all `.atelier-*-top/footer` flex helpers to `layout.css`

### 🚨 PRIORITY 3 - FIX RESPONSIVENESS:
6. **Restore media queries** → Add ALL breakpoints (1199px, 991px, 768px) to `utilities-theme.css`

### LONG-TERM (After production recovery):
- Reorganize CSS: Create dedicated `typography.css`, `responsive.css`, `spacing.css`
- Add CSS linting to prevent future deduplication accidents
- Document which classes are "essential" vs "optional"

---

## FILES TO MODIFY

| File | Action | Section |
|------|--------|---------|
| `components/layout.css` | ADD | Image sizing, typography, padding, grids, flex helpers |
| `components/utilities-theme.css` | ADD | Media query breakpoints (all 3) |
| `components/cards-panels.css` | NO CHANGE | Keep as-is |
| `components/main-original-backup.css` | REFERENCE | Source of truth |

---

## EXTRACTION CHECKLIST

### For `components/layout.css` - ADD these sections:
- [ ] Image & Avatar sizing (6 rule groups)
- [ ] Typography scale (8+ font-size rules)
- [ ] Component padding (8+ padding rules)
- [ ] Grid layouts (6+ grid definitions)
- [ ] Flex rows (3+ flex helpers)

### For `components/utilities-theme.css` - ADD these sections:
- [ ] @media (max-width: 1199.98px)
- [ ] @media (max-width: 991.98px)
- [ ] @media (max-width: 768px)

---

**End of Analysis**  
**Generated from:** blog/static/blog/main-original-backup.css (5450 lines)  
**Analysis by:** Visual regression detection  
**Recovery effort:** ~2-3 hours to restore all rules
