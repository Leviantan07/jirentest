# CSS ESSENTIALS vs REMOVABLE CLASSIFICATION

**Quick Reference: Which CSS MUST be kept vs which can be safely removed**

---

## DISPLAY-CRITICAL CSS (MUST KEEP)

### 1. IMAGE SIZING 🔴 CRITICAL

| CSS Class | Removal Impact | Status |
|-----------|---|---------|
| `.helb-user-chip img` | Dashboard navbar broken | **RESTORE** |
| `.atelier-avatar-group__avatar` | All avatar groups broken | **RESTORE** |
| `.atelier-profile-identity__avatar` | Profile page broken | **RESTORE** |
| `.atelier-user-inline__avatar` | User references misaligned | **RESTORE** |
| `.kanban-card__avatar` | Kanban display broken | **RESTORE** |

**Why:** Images need explicit sizing to display at correct proportions with `object-fit: cover`

---

### 2. TYPOGRAPHY 🔴 CRITICAL

| CSS Class | Removal Impact | Status |
|-----------|---|---------|
| `.atelier-project-card__title` | Project names unreadable | **RESTORE** |
| `.atelier-page-header__title` | Dashboard title tiny | **RESTORE** |
| `.atelier-stat-card__value` | Stats numbers unreadable | **RESTORE** |
| `.stitch-ticket-title` | Ticket titles invisible | **RESTORE** |
| `.stitch-epic-card__title` | Epic titles tiny | **RESTORE** |
| `.atelier-profile-identity__name` | Profile names tiny | **RESTORE** |

**Why:** These use `clamp()` for responsive sizing. Without them, browser defaults apply (too small)

---

### 3. RESPONSIVE MEDIA QUERIES 🔴 CRITICAL

| Breakpoint | Removal Impact | Status |
|-----------|---|---------|
| `@media (max-width: 1199.98px)` | Tablet layout broken (4-col grids don't collapse) | **RESTORE** |
| `@media (max-width: 991.98px)` | Medium tablet broken (sidebar doesn't collapse) | **RESTORE** |
| `@media (max-width: 768px)` | Mobile completely broken (layouts don't stack) | **RESTORE** |

**Why:** These control grid column changes at breakpoints. Without them, desktop layout applies to mobile.

---

### 4. COMPONENT PADDING 🟡 IMPORTANT

| CSS Class | Removal Impact | Status |
|-----------|---|---------|
| `.atelier-project-card` | Card content touches edges | **RESTORE** |
| `.atelier-stat-card` | Stats cards cramped | **RESTORE** |
| `.atelier-panel` | Panel content no spacing | **RESTORE** |
| `.atelier-mini-stat` | Mini stats cramped | **RESTORE** |
| `.atelier-pill` | Pill buttons too tight | **RESTORE** |

**Why:** Without padding, content is cramped. These define the internal spacing.

---

### 5. LAYOUT GRIDS 🟡 IMPORTANT

| CSS Class | Removal Impact | Status |
|-----------|---|---------|
| `.atelier-stats-grid` | Dashboard KPIs not aligned | **RESTORE** |
| `.atelier-profile-layout` | Profile sidebar wrong layout | **RESTORE** |
| `.atelier-project-card__meta-grid` | Project metadata not gridded | **RESTORE** |
| `.stitch-project-shell` | Project pages misaligned | **RESTORE** |
| `.stitch-ticket-layout` | Ticket pages misaligned | **RESTORE** |

**Why:** These define `display: grid` with specific column counts. Without them, layouts stack incorrectly.

---

### 6. FLEX ROWS 🟡 IMPORTANT

| CSS Class | Removal Impact | Status |
|-----------|---|---------|
| `.atelier-project-card__top` | Project card elements stack wrong | **RESTORE** |
| `.atelier-project-card__content` | Content doesn't expand | **RESTORE** |
| `.atelier-page-header__actions` | Action buttons misaligned | **RESTORE** |
| `.stitch-meta-row` | Metadata rows misaligned | **RESTORE** |

**Why:** These define `display: flex` with alignment. Without them, elements don't align horizontally.

---

## REMOVABLE CSS (CAN SAFELY DELETE)

### ✅ Duplicate styles (safe to remove if elsewhere)
- Button variations (if defined elsewhere)
- Form control styling (if Bootstrap or another file covers)
- Badge styles (if defined in separate badges file)
- Alert variants (if defined in separate alerts file)

### ✅ Decorative/Non-critical (only if space is urgent)
- `.helb-arc-bg` - decorative background gradient
- `.helb-theme-fab` - theme toggle button styling
- Hover states (only remove if absolutely necessary)
- Transition effects (only remove if absolutely necessary)

### ⚠️ CONDITIONAL: Only safe to remove if...
- `.atelier-empty-state` - only if no empty states shown
- `.atelier-identity-dropzone` - only if file upload not used
- `.kanban-card` styles - only if kanban board not visible
- `.stitch-*` styles - only if Sprint board not used

---

## CLASSIFICATION SUMMARY

### 🔴 CRITICAL (Removal = Site Broken)
- All image sizing
- All typography with `clamp()`
- All media queries
- Component padding for cards/panels
- Grid layout definitions

**Status:** 22 CSS rule groups - **ALL MUST BE RESTORED**

---

### 🟡 IMPORTANT (Removal = Poor UX)
- Flex row helpers
- Grid gap definitions
- Component margins
- Additional layout rules

**Status:** 15 CSS rule groups - **ALL SHOULD BE RESTORED**

---

### 🟢 OPTIONAL (Removal = Minor impact)
- Decorative effects
- Some hover states
- Animation transitions
- Unused component styles

**Status:** ~10% of CSS can be removed IF NEEDED for size optimization

---

## CURRENT STATUS

**Missing from current files:** 37+ rule groups (all CRITICAL + IMPORTANT)

**Result of deletion:**
- `main-consolidated-pending.css` deleted → Removed 100+ rules ✗
- `cards-panels.css` trimmed → Removed 316 lines ✗
- **NOT restored to:** `layout.css` or `utilities-theme.css` ✗

---

## RECOMMENDATION FOR FUTURE

### To prevent future regression:

1. **Tag essential rules** in comments:
   ```css
   /* ⚠️ DISPLAY-CRITICAL: Profile image sizing
      Removal breaks dashboard profile pictures */
   .helb-user-chip img {
     width: 2.35rem;
     height: 2.35rem;
   }
   ```

2. **Create `css/ESSENTIAL_RULES.md`** documenting:
   - Which 22 rule groups are critical
   - Which CSS files depend on each rule
   - Impact analysis of removing each rule

3. **Add linting rule**: Block deletion of labeled critical rules

4. **Before deduplication**: Map rule dependencies
   - Use CSS analyzer to find duplicate rules
   - Document which duplicates are in which files
   - Keep ONE copy in correct file, remove others

---

## ONE-LINE SUMMARY

**KEEP:** Image sizing, responsive typography (clamp), media queries, padding, grids, flex rows  
**REMOVE:** Decorative backgrounds, theme FAB, unused components, duplicate styles  
**RESTORE:** All 37+ missing rule groups from main-original-backup.css
