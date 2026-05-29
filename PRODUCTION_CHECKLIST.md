# codecloudworld — Launch Checklist

**Live URL:** https://www.codecloudworld.com
**Last Audited:** 29 May 2026

---

## PHASE 1: Fix Critical Issues (Do First)

### Step 1: Upload Latest theme.xml
Your live site is running an older version. The latest local file has:
- lang="en", BreadcrumbList JSON-LD, og:type=article, rel="noopener" on links, aria improvements, Twitter removed from footer

**How:**
1. Open `theme.xml` from this repo
2. Copy entire contents
3. Go to Blogger Dashboard → Theme → click ⋮ → Edit HTML
4. Select all (Ctrl+A) → Paste → Save Theme

---

### Step 2: Configure robots.txt
Currently **empty** on your live site.

**How:**
1. Blogger Dashboard → Settings
2. Scroll to **Crawlers and indexing**
3. Click **Custom robots.txt** → Enable
4. Paste this:

```
User-agent: *
Allow: /
Disallow: /search
Disallow: /search?
Disallow: /search/label/*?
Disallow: /*?m=1
Disallow: /*?m=0

Sitemap: https://www.codecloudworld.com/sitemap.xml
```

5. Save

**What each line does:**
- `Allow: /` — let Google crawl all pages
- `Disallow: /search` — block search result pages (thin content)
- `Disallow: /search/label/*?` — block label page pagination
- `Disallow: /*?m=1` and `/*?m=0` — block mobile duplicate URLs
- `Sitemap:` — tells Google where your sitemap is

---

### Step 3: Configure Custom Robots Header Tags
Server-level noindex signals (stronger than meta tags).

**How:**
1. Same page: Settings → Crawlers and indexing
2. Click **Custom robots header tags** → Enable
3. Set:

| Page Type | all | noindex | nofollow | noarchive | nosnippet |
|-----------|-----|---------|----------|-----------|-----------|
| **Homepage** | ✅ | | | | |
| **Archive and search pages** | | ✅ | | | |
| **Post and page default** | ✅ | | | | |

4. Save

---

### Step 4: Enable Search Description
**How:**
1. Blogger Dashboard → Settings
2. Scroll to **Meta tags**
3. Enable **Search description**
4. Type: `DevOps, Cloud Computing, MLOps, and AI tutorials. Learn Kubernetes, Docker, CI/CD, Python, and more at codecloudworld.`
5. Save

---

### Step 5: Fix "AI News" Nav Link
Currently broken — URL is `/AI%20nEWS` (space + mixed case).

**How:**
1. Blogger Dashboard → Layout
2. Find **Navigation Menu (LinkList)** widget → Edit
3. Change "AI News" URL to one of:
   - `/search/label/AI` (if you have an "AI" label)
   - `/p/ai-news.html` (if you created a static page)
   - Remove it entirely if not ready
4. Save

---

## PHASE 2: Google Search Console Setup

### Step 6: Add Your Site to Google Search Console
**How:**
1. Go to https://search.google.com/search-console
2. Click **Add property** (top-left dropdown)
3. Choose **URL prefix**
4. Enter: `https://www.codecloudworld.com`
5. Click **Continue**

---

### Step 7: Verify Ownership
Google will show several verification methods. Use **HTML tag**:

1. Google gives you a tag like:
```html
<meta name="google-site-verification" content="abc123xyz..."/>
```
2. Copy the entire tag
3. Give it to me — I'll add it to theme.xml
4. OR add it yourself: Theme → Edit HTML → paste after line 5 (`<meta charset='UTF-8'/>`)
5. Save theme → Go back to Search Console → Click **Verify**

---

### Step 8: Submit Sitemap
After verification:

1. In Search Console → **Sitemaps** (left sidebar)
2. Enter: `sitemap.xml`
3. Click **Submit**
4. It should show `https://www.codecloudworld.com/sitemap.xml` as submitted

---

### Step 9: Request Indexing for Key Pages
1. In Search Console → **URL Inspection** (top search bar)
2. Paste: `https://www.codecloudworld.com/`
3. Click **Request Indexing**
4. Repeat for each post URL:
   - `https://www.codecloudworld.com/2026/05/test-blog.html`
5. Google typically indexes within 2-7 days

---

## PHASE 3: Content (Before Promoting)

### Step 10: Publish 5-10 Quality Posts
Google won't rank a site with 1 test post. Before promoting:

- [ ] Write **5-10 real posts** (1500+ words each)
- [ ] Each post should have:
  - Descriptive title with target keyword
  - Featured image (add to post, minimum 1200x630px)
  - Search description (Post settings → Search description, 150-160 chars)
  - Labels/tags (Post settings → Labels)
  - Internal links to other posts
  - Code examples, images, step-by-step instructions
- [ ] Suggested topics for your niche:
  - "Kubernetes for Beginners: Complete Guide"
  - "Docker vs Podman: Which Should You Use?"
  - "CI/CD Pipeline with GitHub Actions — Step by Step"
  - "Top 10 DevOps Tools in 2026"
  - "How to Deploy on AWS with Terraform"

---

### Step 11: Write Search Descriptions for Every Post
For each existing and future post:

1. Edit the post in Blogger
2. Right sidebar → **Post settings → Search description**
3. Write 150-160 characters including your primary keyword
4. Example: "Learn how to deploy applications on Kubernetes using Helm charts. Step-by-step guide with examples, rolling updates, and monitoring setup."

---

### Step 12: Add Labels to Every Post
1. Edit each post → Right sidebar → **Labels**
2. Add 2-3 relevant labels per post
3. Be consistent: `Kubernetes`, `Docker`, `DevOps`, `CI/CD`, `Python`, `AI`
4. These create category pages like `/search/label/Kubernetes`

---

## PHASE 4: Social & Analytics

### Step 13: Update Footer Social Links
In theme.xml, replace `href='#'` with real URLs:

| Link | Current | Action |
|------|---------|--------|
| LinkedIn | `#` | Add your LinkedIn URL |
| YouTube | `#` | Add your YouTube URL or remove |
| GitHub | ✅ Done | `https://github.com/helloamitkr` |

---

### Step 14: Google Analytics (Optional)
1. Go to https://analytics.google.com
2. Create a GA4 property for `www.codecloudworld.com`
3. Get your Measurement ID (e.g., `G-XXXXXXXXXX`)
4. Give it to me — I'll add it to theme.xml

---

### Step 15: Test Everything
Run these tests after all steps:

| Test | URL |
|------|-----|
| **Rich Results** | https://search.google.com/test/rich-results?url=https://www.codecloudworld.com |
| **PageSpeed** | https://pagespeed.web.dev/analysis?url=https://www.codecloudworld.com |
| **Mobile-Friendly** | https://search.google.com/test/mobile-friendly?url=https://www.codecloudworld.com |
| **robots.txt** | https://www.codecloudworld.com/robots.txt (should show your config) |
| **Sitemap** | https://www.codecloudworld.com/sitemap.xml (should list your posts) |
| **OG Tags** | https://developers.facebook.com/tools/debug/?q=https://www.codecloudworld.com |

---

## Already Done in Theme Code ✅

- [x] Dynamic `<title>` per page type
- [x] Meta description (dynamic + fallback)
- [x] Canonical URL on every page
- [x] Robots meta (noindex on archive/search/label)
- [x] Open Graph tags (og:type=article on posts)
- [x] Twitter Card tags
- [x] JSON-LD: WebSite + BlogPosting + BreadcrumbList
- [x] `lang="en"` on html
- [x] Favicon (inline SVG)
- [x] Preconnect hints (4 domains)
- [x] Fonts combined + display=swap
- [x] Theme-color meta
- [x] Prism JS/CSS lazy-loaded on post pages only
- [x] `loading="lazy"` on images
- [x] `aria-label` on all icon links + nav
- [x] `aria-hidden` on decorative SVGs
- [x] `rel="noopener noreferrer"` on external links
- [x] Mobile ?m=1 redirect
- [x] Responsive mobile layout
- [x] 404 error page
- [x] Newsletter form (Google Forms fetch no-cors)
- [x] Dead CSS removed

---

## Quick Reference

**CDN URL:**
```
https://cdn.jsdelivr.net/gh/helloamitkr/theme-codecloudworld@main/css/theme.css
```

**Purge CDN Cache:**
```
https://purge.jsdelivr.net/gh/helloamitkr/theme-codecloudworld@main/css/theme.css
```

**Sitemap:**
```
https://www.codecloudworld.com/sitemap.xml
```
