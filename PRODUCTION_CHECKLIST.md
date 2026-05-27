# Production Readiness Checklist — codecloudworld

## Status: Theme Code Complete | Pending: Dashboard Actions

---

## DONE (in theme code)

- [x] SEO title (dynamic per page type)
- [x] Meta description (dynamic for posts, static for homepage)
- [x] Canonical URL on every page
- [x] Robots `noindex, follow` on archive/search/label pages
- [x] Open Graph meta tags (title, url, site_name, image, description)
- [x] Twitter Card meta tags (summary_large_image)
- [x] JSON-LD structured data — WebSite (homepage) + BlogPosting (posts)
- [x] Favicon (inline SVG cloud icon)
- [x] Preconnect hints (fonts.googleapis.com, fonts.gstatic.com, cdn.jsdelivr.net, cdnjs.cloudflare.com)
- [x] Google Fonts combined into single request with `display=swap`
- [x] Theme-color meta (#0f172a)
- [x] Prism JS/CSS lazy-loaded only on single post pages
- [x] `loading="lazy"` on post thumbnail images
- [x] `aria-label` on search icon link
- [x] Mobile `?m=1` → `?m=0` redirect (forces responsive theme)
- [x] Mobile responsive layout (clean list style, edge-to-edge)
- [x] Off-canvas mobile menu with overlay
- [x] 404 error page
- [x] Dead CSS removed (hero, .pro-btn, dropdown, .email-capture-form, modal)
- [x] Label widget link color fixed for dark theme
- [x] Nav widget background forced transparent via `<b:skin>`
- [x] HTML bugs fixed: self-closing `<div>`/`<script>` tags, `data:post.dateHeader` → `data:post.date`, footer `©` encoding, quote consistency

---

## ACTION ITEMS (manual steps required)

### ~~1. Upload Theme to Blogger~~ ✅
- ~~Go to **Blogger Dashboard → Theme → Edit HTML**~~
- ~~Select all → Paste contents of `theme.xml` → Save~~

### ~~2. Disable Mobile Theme~~ ✅
- ~~**Blogger Dashboard → Theme → click ⋮ (three dots) → Mobile Settings → Select "Desktop"**~~
- ~~This prevents Blogger from serving its default mobile template~~

### 3. Enable Search Description
- **Blogger Dashboard → Settings → Search preferences → Meta tags → Enable**
- Write a blog-level description (e.g., "DevOps, Cloud Computing, MLOps tutorials and guides")
- For each post: **Post settings → Search description** — write a unique 150-160 char description

### 4. Set Up Email Subscriptions (follow.it — recommended)
- Go to https://follow.it and sign up (free)
- Enter blog URL: `testtheme731.blogspot.com`
- It auto-detects your RSS feed
- Copy the form action URL it provides
- Update `theme.xml` line ~364: replace `action='#'` with the follow.it URL
- **Result:** Subscribers automatically get emailed when you publish a new post

### 5. Update Footer Links
In `theme.xml` (lines ~442-466), replace all `href='#'` with real URLs:

**Resources section:**
- Tutorials → `/search/label/Tutorials` (or your label URL)
- Roadmaps → your roadmaps page URL
- Certification Guides → your guides URL
- Newsletter → link to follow.it public page or `/p/newsletter.html`

**Company section:**
- About Us → `/p/about.html` (create a Blogger static page)
- Contact → `/p/contact.html`
- Advertise → `/p/advertise.html`
- Privacy Policy → `/p/privacy-policy.html`

**Follow Us section:**
- Twitter → `https://twitter.com/YOUR_HANDLE`
- LinkedIn → `https://linkedin.com/in/YOUR_PROFILE`
- GitHub → `https://github.com/helloamitkr`
- YouTube → `https://youtube.com/@YOUR_CHANNEL`

### 6. Submit Sitemap to Google
- Go to https://search.google.com/search-console
- Add your blog as a property
- Go to **Sitemaps** → Submit: `https://testtheme731.blogspot.com/sitemap.xml`

### 7. Set Up Google Analytics (optional)
- Create a GA4 property at https://analytics.google.com
- Get your Measurement ID (G-XXXXXXXXXX)
- Add to `theme.xml` just before `</head>`:
```xml
<script async='async' src='https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX'/>
<script>
  //<![CDATA[
  window.dataLayer=window.dataLayer||[];
  function gtag(){dataLayer.push(arguments);}
  gtag('js',new Date());gtag('config','G-XXXXXXXXXX');
  //]]>
</script>
```

### 8. Custom Domain (optional)
- **Blogger Dashboard → Settings → Publishing → Custom domain**
- Point your domain's CNAME to `ghs.google.com`
- Enables HTTPS automatically

---

## File Structure
```
theme-codecloudworld/
├── theme.xml              # Main Blogger template (upload to Blogger)
├── css/
│   └── theme.css          # External CSS (served via jsDelivr CDN)
├── PRODUCTION_CHECKLIST.md # This file
└── README.md              # (create if needed)
```

## CDN URL
```
https://cdn.jsdelivr.net/gh/helloamitkr/theme-codecloudworld@main/css/theme.css
```

## Purge CDN Cache (after CSS changes)
```
https://purge.jsdelivr.net/gh/helloamitkr/theme-codecloudworld@main/css/theme.css
```
