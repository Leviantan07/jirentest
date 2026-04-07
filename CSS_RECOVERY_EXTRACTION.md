# CSS RECOVERY GUIDE - Exact Rules to Restore

**Use this file for quick copy-paste recovery of missing CSS**

---

## FILE: `components/layout.css`

### SECTION 1: IMAGE & AVATAR SIZING
**Add to end of layout.css before responsive media queries**

```css
/* ============================================================
   Image & Avatar Sizing (RECOVERED FROM MAIN-ORIGINAL-BACKUP)
   ============================================================ */

.helb-user-chip img {
  width: 2.35rem;
  height: 2.35rem;
  border-radius: 999px;
  object-fit: cover;
  box-shadow: var(--helb-shadow-sm);
}

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

.atelier-avatar-group__overflow {
  width: 2.55rem;
  height: 2.55rem;
  margin-left: -0.55rem;
  background: var(--helb-surface-container-high);
  color: var(--helb-on-surface);
  font-size: 0.72rem;
  border: 3px solid var(--helb-surface-container-lowest);
  display: inline-flex;
  align-items: center;
  justify-content: center;
  border-radius: 999px;
  font-weight: 800;
}

.atelier-profile-identity__avatar {
  width: 6.75rem;
  height: 6.75rem;
  margin: 0 auto 1.2rem;
  box-shadow: var(--helb-shadow-md);
  object-fit: cover;
  border-radius: 999px;
}

.atelier-user-inline__avatar {
  width: 2rem;
  height: 2rem;
  box-shadow: var(--helb-shadow-sm);
  object-fit: cover;
  border-radius: 999px;
}

.kanban-card__avatar {
  width: 2rem;
  height: 2rem;
  border-radius: 50%;
  border: 2px solid var(--helb-surface-container-lowest);
  box-shadow: var(--helb-shadow-sm);
  object-fit: cover;
}

.kanban-card__avatar--empty {
  background: var(--helb-surface-container-highest);
  color: var(--helb-outline);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.7rem;
  font-weight: 700;
}
```

---

### SECTION 2: RESPONSIVE TYPOGRAPHY SCALE
**Add after image sizing section**

```css
/* ============================================================
   Responsive Typography Scale (RECOVERED FROM MAIN-ORIGINAL-BACKUP)
   ============================================================ */

.atelier-page-header__title {
  margin: 0.35rem 0 0.45rem;
  font-size: clamp(2.25rem, 4vw, 3.75rem);
  font-weight: 800;
  line-height: 0.98;
  letter-spacing: -0.07em;
  color: var(--helb-on-surface);
}

.atelier-project-card__title {
  font-size: clamp(1.4rem, 2vw, 1.9rem);
  font-weight: 800;
  line-height: 1.08;
  letter-spacing: -0.05em;
  color: var(--helb-primary);
}

.atelier-profile-identity__name {
  margin: 0;
  font-size: clamp(1.85rem, 3vw, 2.35rem);
  font-weight: 800;
  line-height: 1.05;
  letter-spacing: -0.06em;
}

.atelier-stat-card__value {
  display: block;
  margin: 0.55rem 0 0.2rem;
  font-size: clamp(1.9rem, 3vw, 2.55rem);
  font-weight: 800;
  line-height: 1;
  letter-spacing: -0.06em;
}

.atelier-mini-stat__value {
  font-size: 1.4rem;
  font-weight: 800;
  line-height: 1;
  letter-spacing: -0.05em;
}

.atelier-panel__title,
.atelier-form-panel__title {
  display: flex;
  align-items: center;
  gap: 0.55rem;
  margin: 0 0 1.15rem;
  font-size: 1.2rem;
  font-weight: 800;
  letter-spacing: -0.04em;
}

.atelier-empty-state__title {
  margin: 0 0 0.4rem;
  font-size: 1.2rem;
  font-weight: 800;
  letter-spacing: -0.04em;
}

.atelier-form-panel__title {
  margin: 0.25rem 0 0.8rem;
  font-size: clamp(1.9rem, 3vw, 2.4rem);
  line-height: 1.02;
}

.stitch-ticket-title {
  margin: 0;
  font-weight: 800;
  letter-spacing: -0.05em;
  font-size: clamp(2rem, 3vw, 3rem);
  line-height: 1.02;
}

.stitch-epic-card__title {
  display: inline-block;
  font-size: 1.4rem;
  font-weight: 800;
  line-height: 1.08;
  letter-spacing: -0.05em;
  color: var(--helb-primary-container);
}

.stitch-sprint-panel__header h3 {
  margin: 0.35rem 0 0;
  font-size: clamp(1.55rem, 2vw, 2rem);
  font-weight: 800;
  letter-spacing: -0.05em;
  color: var(--helb-primary-container);
}

.stitch-section h2 {
  margin: 0;
  font-weight: 800;
  letter-spacing: -0.05em;
}
```

---

### SECTION 3: COMPONENT PADDING & SPACING
**Add after typography section**

```css
/* ============================================================
   Component Padding & Spacing (RECOVERED FROM MAIN-ORIGINAL-BACKUP)
   ============================================================ */

.atelier-stat-card {
  padding: 1.2rem 1.25rem;
  background: color-mix(in srgb, var(--helb-surface-container-lowest) 92%, transparent);
  border-radius: 1.75rem;
  box-shadow: var(--helb-shadow-md);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
}

.atelier-project-card {
  padding: 1.65rem 1.75rem;
  background: color-mix(in srgb, var(--helb-surface-container-lowest) 92%, transparent);
  border-radius: 1.75rem;
  box-shadow: var(--helb-shadow-md);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
}

.atelier-project-card--dashboard {
  padding: 1.75rem 1.9rem;
}

.atelier-panel {
  padding: 1.5rem 1.65rem;
  background: color-mix(in srgb, var(--helb-surface-container-lowest) 92%, transparent);
  border-radius: 1.75rem;
  box-shadow: var(--helb-shadow-md);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
}

.atelier-role-table-shell {
  padding: 1.5rem 1.65rem;
  background: color-mix(in srgb, var(--helb-surface-container-lowest) 92%, transparent);
  border-radius: 1.75rem;
  box-shadow: var(--helb-shadow-md);
  backdrop-filter: blur(18px);
  -webkit-backdrop-filter: blur(18px);
}

.atelier-mini-stat {
  background: var(--helb-surface-container-low);
  border-radius: 1rem;
  padding: 0.85rem 0.7rem;
  display: grid;
  gap: 0.2rem;
}

.atelier-empty-state {
  padding: 2.5rem 1.25rem;
  text-align: center;
}

.atelier-empty-state--table {
  padding: 2.75rem 1rem;
}

.atelier-empty-state--dashboard {
  display: grid;
  justify-items: center;
  gap: 0.9rem;
  padding: 3.5rem 1.5rem;
  background: color-mix(in srgb, var(--helb-surface-container-lowest) 92%, transparent);
  border-radius: 2rem;
  box-shadow: var(--helb-shadow-md);
}

.atelier-ticket-stack__item {
  background: var(--helb-surface-container-low);
  border-radius: 1.25rem;
  padding: 1rem 1.1rem;
}

.atelier-pill {
  padding: 0.78rem 1rem;
  background: var(--helb-surface-container-low);
  color: var(--helb-on-surface);
  text-decoration: none;
  gap: 0.55rem;
  font-size: 0.88rem;
  font-weight: 700;
}
```

---

### SECTION 4: GRID LAYOUTS & FLEX ROWS
**Add after spacing section**

```css
/* ============================================================
   Grid Layouts & Grid Gaps (RECOVERED FROM MAIN-ORIGINAL-BACKUP)
   ============================================================ */

.atelier-stats-grid {
  display: grid;
  grid-template-columns: repeat(4, minmax(0, 1fr));
  gap: 1rem;
  margin-bottom: 1.75rem;
}

.atelier-stats-grid--compact {
  margin-bottom: 1.5rem;
}

.atelier-project-list,
.atelier-ticket-stack,
.atelier-form-stack,
.atelier-profile-sidebar,
.atelier-profile-main,
.atelier-stack-section {
  display: grid;
  gap: 1rem;
}

.atelier-project-card__meta-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1rem;
  margin-top: 1.4rem;
  padding-top: 1.2rem;
  border-top: 1px solid rgba(195, 198, 208, 0.16);
}

.atelier-project-card__meta-grid--dashboard {
  grid-template-columns: repeat(2, minmax(0, 1fr));
  margin-top: 1rem;
  padding-top: 0;
  border-top: 0;
}

.atelier-project-card__meta-item {
  display: grid;
  gap: 0.35rem;
}

.atelier-mini-stats-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 0.75rem;
  margin-top: 1.4rem;
}

.atelier-profile-layout {
  display: grid;
  grid-template-columns: minmax(18rem, 23rem) minmax(0, 1fr);
  gap: 1.5rem;
  align-items: start;
}

.atelier-profile-layout--admin {
  grid-template-columns: minmax(21rem, 28rem) minmax(0, 1fr);
}

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

.atelier-project-card__top {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
}

.atelier-project-card__content {
  flex: 1;
  min-width: 0;
}

.atelier-project-card__title-row {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.atelier-project-card__footer {
  margin-top: 1.25rem;
  padding-top: 1.2rem;
  border-top: 1px solid rgba(195, 198, 208, 0.1);
}

.atelier-panel__split-header {
  margin-bottom: 1.25rem;
}

.atelier-panel__split-header--table {
  padding-bottom: 1rem;
}

.atelier-ticket-stack__status {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.45rem;
}

/* Stitch/Project specific grids */
.stitch-project-shell,
.stitch-ticket-layout,
.stitch-sprint-admin-layout {
  display: grid;
  gap: 1.5rem;
  align-items: start;
}

.stitch-project-shell {
  grid-template-columns: minmax(0, 1.65fr) minmax(20rem, 0.9fr);
}

.stitch-ticket-layout {
  grid-template-columns: minmax(0, 1.7fr) minmax(19.5rem, 0.95fr);
}

.stitch-sprint-admin-layout {
  grid-template-columns: minmax(0, 1.45fr) minmax(21rem, 0.92fr);
}

.stitch-project-main,
.stitch-project-side,
.stitch-ticket-main,
.stitch-ticket-sidebar,
.stitch-sprint-stack,
.stitch-sprint-sidebar {
  display: grid;
  gap: 1rem;
}

.stitch-info-grid,
.stitch-kpi-grid,
.stitch-sprint-card__meta-grid,
.stitch-linked-grid,
.stitch-attachments-grid {
  display: grid;
  gap: 1rem;
}

.stitch-info-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.stitch-kpi-grid {
  grid-template-columns: repeat(4, minmax(0, 1fr));
}

.stitch-info-tile,
.stitch-kpi-tile {
  display: grid;
  gap: 0.3rem;
  background: var(--helb-surface-container-low);
  border-radius: 1.35rem;
  padding: 1rem 1.05rem;
}

.stitch-linked-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.stitch-attachments-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
}

.stitch-epic-grid {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 1.5rem;
}

.stitch-sprint-ticket-list,
.stitch-backlog-list {
  display: grid;
  gap: 0.85rem;
}

.stitch-sprint-ticket-list {
  padding: 0 1rem 1rem;
}

.stitch-ticket-list,
.stitch-related-grid {
  display: grid;
  gap: 0.85rem;
}

.stitch-meta-row,
.stitch-chip-row,
.stitch-panel-head,
.stitch-project-actions,
.stitch-quick-panel__actions,
.stitch-toolbar-form,
.stitch-sprint-card__status-form,
.stitch-inline-form,
.stitch-ticket-kicker,
.stitch-ticket-assignee-card__content,
.stitch-action-stack,
.stitch-member-list {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  flex-wrap: wrap;
}

.stitch-project-header,
.stitch-section__header,
.stitch-sprint-card__header,
.stitch-ticket-meta-row,
.stitch-link-row,
.stitch-ticket-row,
.stitch-panel-head {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
}

.stitch-project-main {
  display: grid;
  gap: 1rem;
}

.stitch-project-side {
  display: grid;
  gap: 1rem;
}
```

---

### SECTION 5: ADDITIONAL CRITICAL LAYOUT RULES
**Add after grid section**

```css
/* ============================================================
   Additional Layout Rules (RECOVERED FROM MAIN-ORIGINAL-BACKUP)
   ============================================================ */

.atelier-profile-identity {
  text-align: center;
}

.atelier-profile-identity__email {
  margin: 0.45rem 0 0.85rem;
  color: var(--helb-secondary);
  font-weight: 600;
}

.atelier-profile-identity__note {
  margin: 0.95rem 0 0;
  font-size: 0.84rem;
  color: var(--helb-on-surface-variant);
}

.atelier-ticket-title {
  display: inline-block;
  margin-top: 0.5rem;
  font-size: 0.98rem;
  font-weight: 700;
  color: var(--helb-on-surface);
}

.atelier-ticket-meta {
  display: flex;
  flex-wrap: wrap;
  gap: 0.7rem;
  margin-top: 0.45rem;
}

.atelier-user-inline {
  align-items: center;
}

.atelier-user-inline strong,
.atelier-user-cell__name,
.atelier-project-ref strong {
  display: block;
  font-size: 0.9rem;
  font-weight: 700;
  color: var(--helb-on-surface);
}

.atelier-project-ref {
  flex-direction: column;
  gap: 0.2rem;
}

.atelier-user-cell {
  align-items: center;
}

.stitch-ticket-row {
  position: relative;
  gap: 1rem;
  padding: 1rem 1rem 1rem 1.2rem;
  border-radius: 1.35rem;
  background: var(--helb-surface-container-low);
}

.stitch-ticket-row::before {
  content: "";
  position: absolute;
  inset: 0 auto 0 0;
  width: 0.28rem;
  border-radius: 1.35rem 0 0 1.35rem;
  background: var(--ticket-accent, var(--helb-primary));
}

.stitch-ticket-row__title {
  display: inline-block;
  margin: 0.45rem 0 0.35rem;
  font-size: 1rem;
  font-weight: 800;
  color: var(--helb-on-surface);
}

.stitch-sprint-ticket {
  padding: 1rem 1.15rem;
  border-radius: 1.35rem;
  background: var(--helb-surface-container-lowest);
  box-shadow: var(--helb-shadow-sm);
}

.stitch-backlog-item {
  display: grid;
  grid-template-columns: auto minmax(0, 1fr) auto;
  align-items: center;
  padding: 1rem 1.1rem;
  border-radius: 1.55rem;
  background: color-mix(in srgb, var(--helb-surface-container-lowest) 90%, transparent);
  box-shadow: var(--helb-shadow-sm);
}

.stitch-backlog-item__rank {
  width: 2.8rem;
  align-self: stretch;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 1.1rem;
  background: var(--helb-surface-container-low);
  color: var(--helb-primary-container);
  font-size: 0.9rem;
  font-weight: 800;
  box-shadow: inset 0 0 0 1px rgba(195, 198, 208, 0.12);
}

.stitch-backlog-item__body {
  min-width: 0;
}

.stitch-epic-card {
  min-height: 14.5rem;
  display: grid;
  gap: 0.95rem;
  padding: 1.5rem;
  border-radius: 1.65rem;
  background: var(--helb-surface-container-lowest);
  box-shadow: var(--helb-shadow-sm);
}

.stitch-sprint-panel {
  padding: 0.55rem;
  border-radius: 1.85rem;
  background: color-mix(in srgb, var(--helb-surface-container-lowest) 84%, var(--helb-surface-container-low) 16%);
  box-shadow: var(--helb-shadow-md);
}

.stitch-sprint-panel__header {
  align-items: flex-start;
  padding: 1rem 1.1rem 0.8rem;
}

.stitch-sprint-card__meta-grid {
  grid-template-columns: repeat(3, minmax(0, 1fr));
  margin-bottom: 1rem;
}

.stitch-info-tile strong {
  color: var(--helb-on-surface);
}

.stitch-kpi-tile strong {
  color: var(--helb-on-surface);
}

.stitch-ticket-row__aside {
  min-width: 9rem;
  display: grid;
  gap: 0.2rem;
  justify-items: end;
  text-align: right;
  font-size: 0.78rem;
}
```

---

## FILE: `components/utilities-theme.css`

### SECTION 1: ADD RESPONSIVE MEDIA QUERIES
**Add at end of utilities-theme.css file**

```css
/* ============================================================
   Responsive Media Queries (RECOVERED FROM MAIN-ORIGINAL-BACKUP)
   
   These breakpoints are CRITICAL for responsive layout:
   - 1199.98px: Tablet/Large (3-col grids)
   - 991.98px: Tablet/Medium (sidebar collapse)
   - 768px: Mobile (1-col layout)
   ============================================================ */

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

  .stitch-epic-grid,
  .atelier-project-card__meta-grid--dashboard {
    grid-template-columns: 1fr;
  }
}

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

  .stitch-project-shell,
  .stitch-ticket-layout,
  .stitch-sprint-admin-layout {
    grid-template-columns: 1fr;
  }
}

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

  .stitch-ledger-footer,
  .atelier-role-section__header,
  .stitch-sprint-panel__header,
  .stitch-sprint-ticket,
  .stitch-archive-callout {
    flex-direction: column;
    align-items: flex-start;
  }

  .stitch-backlog-item {
    grid-template-columns: 1fr;
  }

  .stitch-backlog-item__rank {
    width: 100%;
    min-height: 2.25rem;
  }

  .helb-auth-social {
    grid-template-columns: 1fr;
  }

  .stitch-info-grid,
  .stitch-kpi-grid,
  .stitch-epic-grid,
  .stitch-linked-grid,
  .stitch-attachments-grid {
    grid-template-columns: 1fr;
  }
}
```

---

## IMPLEMENTATION STEPS

1. **Open** `components/layout.css`
2. **Add** SECTION 1-5 from above (Image sizing, Typography, Padding, Grids, Additional rules)
3. **Save** and verify in browser

4. **Open** `components/utilities-theme.css`
5. **Scroll** to end of file
6. **Add** SECTION 1 (Media Queries)
7. **Save** and verify in browser

8. **Test** dashboard, profile, project pages
9. **Test** mobile responsiveness (768px, 991px, 1199px breakpoints)

---

## VERIFICATION CHECKLIST

After adding CSS:

- [ ] Profile pictures display correctly (proper sizing)
- [ ] Project names are larger and readable
- [ ] Cards have proper padding and spacing
- [ ] Dashboard grids display correctly
- [ ] Mobile view (< 768px) stacks vertically
- [ ] Tablet view (< 1199px) uses 2-column layout
- [ ] Navbar and sidebar responsive

---

**Status:** This file contains ALL necessary CSS to recover from the regression.  
**Time to implement:** ~10 minutes copy-paste + testing
