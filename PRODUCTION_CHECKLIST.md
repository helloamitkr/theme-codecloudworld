# Production Readiness Checklist — codecloudworld

---

## SEO — Implemented in Theme Code

### On-Page SEO
- [x] `lang="en"` on `<html>` tag
- [x] Dynamic `<title>` — `PostName | BlogTitle` for posts, `pageTitle` for homepage
- [x] Meta description — dynamic from post meta, fallback auto-generated
- [x] Canonical URL (`<link rel="canonical">`) on every page
- [x] Robots meta — `noindex, follow` on archive/search/label pages, full `index, follow` on posts/homepage

### Open Graph (Facebook/LinkedIn)
- [x] `og:type` — `article` on posts, `website` on homepage
- [x] `og:title`, `og:url`, `og:site_name`, `og:image`, `og:description`

### Twitter Cards
- [x] `summary_large_image` card type
- [x] `twitter:title`, `twitter:description`, `twitter:image`

### JSON-LD Structured Data (Google Rich Results)
- [x] `WebSite` schema on homepage with `SearchAction`
- [x] `BlogPosting` schema on posts with `headline`, `datePublished`, `author`, `publisher`, `logo`, `mainEntityOfPage`
- [x] `BreadcrumbList` schema on posts (Home → Post Title)

### Accessibility & Semantic HTML
- [x] `aria-label` on logo link, search icon, nav element
- [x] `aria-hidden="true"` on decorative SVGs
- [x] `alt` text on post images via `expr:alt='data:post.title'`
- [x] `rel="noopener noreferrer"` + `target="_blank"` on external links
- [x] Semantic `<header>`, `<main>`, `<aside>`, `<footer>`, `<article>`, `<nav>`

### Performance
- [x] Fonts combined into 1 request with `display=swap` (no FOIT)
- [x] Preconnect hints (4 domains)
- [x] Prism JS/CSS lazy-loaded only on single post pages
- [x] `loading="lazy"` on post thumbnail images
- [x] Dead CSS removed (~250 lines total)
- [x] External CSS via jsDelivr CDN

### Other
- [x] Favicon (inline SVG)
- [x] Theme-color meta `#0f172a`
- [x] Mobile `?m=1` → `?m=0` redirect
- [x] Responsive mobile layout
- [x] 404 error page
- [x] Newsletter subscribe form (Google Forms via fetch no-cors)

---

## robots.txt — Blogger Dashboard Setup

Blogger auto-generates a `robots.txt` at `https://testtheme731.blogspot.com/robots.txt`.
To customize it:

1. Go to **Blogger Dashboard → Settings → Crawlers and indexing**
2. Enable **Custom robots.txt**
3. Paste this:

```
User-agent: *
Allow: /
Disallow: /search
Disallow: /search?
Disallow: /search/label/*?
Disallow: /*?m=1
Disallow: /*?m=0

Sitemap: https://testtheme731.blogspot.com/sitemap.xml
```

**What this does:**
- **Allows** all crawlers to index posts, pages, homepage
- **Blocks** search results pages, label pagination, and mobile parameter URLs (prevents duplicate content)
- **Points** Google to your sitemap

### Custom robots header tags (same page in Settings)
Set these in **Blogger → Settings → Crawlers and indexing → Custom robots header tags**:

| Page Type | Setting |
|-----------|---------|
| Homepage | `index, follow` |
| Archive pages | `noindex, follow` |
| Search pages | `noindex, follow` |
| Post pages | `index, follow` |

---

## Remaining Action Items

### 1. Configure robots.txt (see above)
- Blogger Dashboard → Settings → Crawlers and indexing → Custom robots.txt

### 2. Configure custom robots header tags (see above)
- Same settings page — enables server-level noindex signals

### 3. Submit Sitemap to Google Search Console
- Go to https://search.google.com/search-console
- Add property: `https://testtheme731.blogspot.com`
- Sitemaps → Submit: `https://testtheme731.blogspot.com/sitemap.xml`

### 4. Write Post Search Descriptions
- For **every post**: Post editor → Post settings → Search description
- Write unique 150-160 char descriptions (Google uses these in search results)

### 5. Upload Latest theme.xml
- Blogger Dashboard → Theme → Edit HTML → paste → Save

### 6. Update Remaining Footer Links
- LinkedIn → replace `href='#'` with your real URL
- YouTube → replace `href='#'` with your real URL

### 7. Google Analytics (optional)
Add before `</head>` in theme.xml:
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

---

## File Structure
```
theme-codecloudworld/
├── theme.xml                # Main Blogger template (upload to Blogger)
├── css/
│   └── theme.css            # External CSS (served via jsDelivr CDN)
├── PRODUCTION_CHECKLIST.md  # This file
├── blogger-pages/           # Static page HTML for Blogger
└── preview/                 # Local preview versions
```

## CDN URL
```
https://cdn.jsdelivr.net/gh/helloamitkr/theme-codecloudworld@main/css/theme.css
```

## Purge CDN Cache (after CSS changes)
```
https://purge.jsdelivr.net/gh/helloamitkr/theme-codecloudworld@main/css/theme.css
```
