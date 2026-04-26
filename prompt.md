# Portfolio Section Prompts — Based on olhauzhykova.com
> Feed each prompt individually to your LLM. Each is fully self-contained.
> Replace [YOUR COLOR PALETTE] and [YOUR CONTENT] with your own.

---

## ▸ PROMPT 0 — GLOBAL SETUP & DESIGN SYSTEM

```
You are an elite front-end developer. Set up the global design system and base styles for a premium, dark-themed personal portfolio website. This is the foundation all other sections will inherit.

OVERALL AESTHETIC:
The site has a refined, editorial, luxury-minimalist feel. It is dark-themed — near-black background (use CSS variable --bg for this). All typography and UI elements are light-colored against the dark canvas. The site feels like a high-end design magazine — generous whitespace, large expressive type, deliberate pacing.

GLOBAL STYLES TO SET UP:

1. CSS CUSTOM PROPERTIES (variables):
   - --bg: [YOUR DARK BACKGROUND COLOR]
   - --text-primary: [YOUR MAIN TEXT COLOR — light/white]
   - --text-secondary: [YOUR SECONDARY/MUTED TEXT COLOR]
   - --accent: [YOUR ACCENT COLOR]
   - --font-display: a serif or high-contrast display typeface (e.g. Playfair Display, Cormorant Garamond, or similar editorial serif)
   - --font-body: a clean, geometric sans-serif (e.g. DM Sans, Neue Haas Grotesk, or similar)
   - --font-mono: a monospace face for labels/tags
   - --section-padding: 120px top and bottom for desktop, 80px for tablet, 60px for mobile
   - --container-width: 1280px max-width, centered with auto margins
   - --gutter: 40px horizontal padding on container

2. RESET & BASE:
   - Full CSS reset (box-sizing border-box, margin 0, padding 0)
   - html: scroll-behavior smooth
   - body: background var(--bg), color var(--text-primary), font-family var(--font-body), overflow-x hidden
   - ::selection: accent background with dark text
   - Scrollbar: styled to be thin and match the dark theme

3. CUSTOM CURSOR:
   Create a custom cursor system with two elements:
   - A small solid circle (8px) that follows the mouse exactly — this is the "dot"
   - A larger hollow circle (40px, 1px border) that follows the mouse with a smooth lag/lerp effect (transition delay ~80ms) — this is the "ring"
   Both are position: fixed, z-index: 9999, pointer-events: none, mix-blend-mode: difference so they invert colors as they pass over elements.
   On hover over any clickable element (a, button), the dot disappears and the ring scales up to 60px and fills with semi-transparent white.

4. PAGE TRANSITIONS:
   On page load, a full-screen overlay (position: fixed, z-index: 9000, background: --bg) slides UP and out of view using a cubic-bezier(0.76, 0, 0.24, 1) easing over 1000ms, revealing the page content beneath. This gives the feel of a curtain lifting.

5. TYPOGRAPHY SCALE:
   - Display/Hero: clamp(80px, 12vw, 160px) — serif display font
   - H1: clamp(48px, 6vw, 80px)
   - H2: clamp(32px, 4vw, 52px)
   - H3: clamp(22px, 2.5vw, 32px)
   - Body large: 18px / line-height 1.7
   - Body: 16px / line-height 1.7
   - Small/label: 12px uppercase, letter-spacing 0.15em

6. ANIMATION UTILITIES:
   Set up a global IntersectionObserver that adds the class .is-visible to any element with the class .reveal when it enters the viewport (threshold: 0.15). Default .reveal state: opacity 0, transform: translateY(40px). When .is-visible is added: opacity 1, transform: translateY(0), transition: opacity 700ms ease, transform 700ms cubic-bezier(0.25, 0.46, 0.45, 0.94). Support .reveal-delay-1 through .reveal-delay-4 adding incremental transition-delays of 150ms each for staggered reveals.

7. LIBRARIES TO INCLUDE (via CDN):
   - GSAP (core + ScrollTrigger plugin)
   - Splitting.js (for character/word split text animations)
   - No jQuery. Vanilla JS only beyond these two.

Output: A single clean HTML file with the <head> (meta, fonts via Google Fonts or similar, CDN links) and a <style> block containing all global CSS variables, reset, base styles, cursor styles, and reveal animation utilities. Include a <script> block with the cursor logic and IntersectionObserver setup. Leave the <body> empty — sections will be added in subsequent prompts.
```

---

## ▸ PROMPT 1 — NAVIGATION / HEADER

```
You are building the navigation header for a premium dark-themed designer portfolio. This component sits at the very top of the page.

LAYOUT:
The navbar is full-width, position: fixed, top: 0, left: 0, z-index: 100. It has NO visible background on load (transparent). As the user scrolls down more than 80px, the navbar gains a subtle backdrop-filter: blur(20px) and a semi-transparent background (rgba of --bg at ~85% opacity) that transitions in smoothly (transition: background 400ms ease). Height: 72px desktop, 60px mobile.

CONTENT & ARRANGEMENT:
The navbar has two sides:
- LEFT: A logo — a minimal custom SVG monogram or wordmark (abstract/geometric style). Roughly 36px tall. On click, scrolls to top.
- RIGHT: Horizontal navigation links — exactly 4 items: "Portfolio", "My Values", "What I Do", "Contact". Each link is in the body sans-serif font, 13px, uppercase, letter-spacing: 0.12em, color: var(--text-primary), font-weight 500. Between the logo and nav links there is flex: 1 space so they sit at opposite ends.

HOVER EFFECT ON NAV LINKS:
Each nav link has a custom underline animation. On hover, a thin 1px line (color: --accent) slides in from left to right beneath the text using a CSS pseudo-element (::after) with width transitioning from 0 to 100% over 300ms ease. On mouse leave, the line slides out from left to right (width goes from 100% to 0 but the origin switches to the right side).

MOBILE HAMBURGER MENU:
On screens below 768px, the four nav links are hidden. A hamburger button appears on the right — it is two horizontal lines (not three), each 24px wide, 1.5px tall, 6px apart, colored --text-primary. On click, a full-screen overlay menu opens:
- The overlay slides in from the RIGHT edge with a transform: translateX(100%) → translateX(0) transition, duration 600ms, cubic-bezier(0.76, 0, 0.24, 1)
- Background: same dark --bg color
- The 4 nav links stack vertically, centered on screen, each in a LARGE serif display font at ~52px, staggered fade-in-up entrance animations with 80ms delay between each
- Social links (LinkedIn, Twitter, Facebook) appear at the bottom as small uppercase labels
- The hamburger transforms into an × close button (the two lines rotate and cross)
- Clicking any link closes the overlay with the reverse slide-out animation

ADDITIONAL DETAIL:
At the very top of the page, above the main navbar, there is a thin secondary row visible only at the very top of the scroll (it disappears as you scroll). It shows the logo again centered, and has the text "Contact" on the far right and a "How can I help you?" label on the left — this functions as a pre-nav identity strip, very minimal.

Output: Full self-contained HTML + CSS + JS for this navbar component. Use CSS variables (--bg, --text-primary, --accent, --font-body, --font-display) so it plugs into the global design system.
```

---

## ▸ PROMPT 2 — HERO SECTION

```
You are building the hero section of a premium dark-themed designer portfolio. This is the first thing the user sees after the page loads and must make an immediate, powerful impression.

LAYOUT & DIMENSIONS:
The hero section is 100vh tall (full viewport height). It has no background image — the dark page background shows through. Content is laid out in a single column, left-aligned, with the container at max-width 1280px, centered with --gutter horizontal padding.

CONTENT STRUCTURE (top to bottom):
1. ROLE LABELS (top area): Three short text labels stacked vertically with a staggered entrance — "Design Director", "Consultant", "Mentor". Each is displayed in a small sans-serif uppercase tag style, 12px, letter-spacing 0.15em. They appear one by one with a fade-in-up animation on page load, each staggered by 150ms.

2. MAIN HEADLINE (center, dominant): The designer's name is split across two massive lines:
   - Line 1: First name — displayed in the serif display font, clamp(80px, 11vw, 150px), font-weight 300 or 400 (light/regular weight for elegance). The text is positioned left of center.
   - Line 2: Last name — same massive size but shifted slightly RIGHT (approx 15-20% indent from left), creating a staircase / offset typographic composition. This asymmetry is critical — the two name lines do NOT align left.
   
   ENTRANCE ANIMATION: Use Splitting.js to split each name into individual characters. On page load, each character animates from opacity: 0, transform: translateY(100%) to its final position, staggered by 30ms per character, with a cubic-bezier(0.25, 0.46, 0.45, 0.94) easing over 800ms. The first name animates first, then the last name starts 200ms after.

3. TAGLINE / SUBTITLE (below name): The text "At the heart of Design" followed by a LINE BREAK and "is an opportunity to problem solve." The word "Design" in "At the heart of Design" has a hand-drawn underline SVG beneath it — an organic, wavy single-stroke underline that feels handwritten, not mechanical. This SVG line animates in using a stroke-dashoffset technique: the path starts fully dashed/invisible and animates to fully drawn over 800ms with an easeInOut timing, triggering 500ms after the name animation completes.
The tagline text is in the body sans-serif, 18-22px, font-weight 300, line-height 1.5, color: --text-primary at ~80% opacity.

4. BIO PARAGRAPH (bottom of hero): Two short sentences of personal introduction text. Sans-serif, 16px, line-height 1.8, max-width: 480px. Appears with a fade-in reveal (opacity 0 → 1, translateY 30px → 0) with a 900ms delay after page load.

DECORATIVE ELEMENT — FLOATING BALL:
A large circular blob/ball element (roughly 200-280px diameter) floats in the hero section. It is positioned to the right side of the screen, vertically centered within the hero. It is NOT a simple circle — it is a morphing blob shape using CSS border-radius animation or SVG path morphing. The blob slowly and continuously morphs its border-radius values cycling through 3-4 different organic shapes, with a duration of ~4s infinite alternate. It has a semi-transparent fill (use --accent color at ~20% opacity) and/or a subtle gradient. It ALSO follows the mouse cursor with a very slow lerp (moves towards cursor position at ~5% of the distance per frame), giving a gentle "magnetic" floating feel.

SCROLL INDICATOR:
At the very bottom center of the hero, a minimal scroll indicator: a small vertical line (1px, ~40px tall, --text-primary at 40% opacity) with a tiny dot that animates downward along the line on a loop (translateY 0 → 40px, opacity 1 → 0, 1.5s infinite). The label "scroll" in 10px uppercase beside it.

OVERALL FEEL:
The hero must feel editorial and spacious. Lots of breathing room. The massive offset typography is the hero's identity — it should feel like a magazine spread, not a typical website header. No images in the hero (other than the optional floating ball).

Output: Full self-contained HTML + CSS + JS for the hero section. Assume GSAP and Splitting.js are already loaded globally.
```

---

## ▸ PROMPT 3 — MARQUEE / TICKER BAND

```
You are building a full-width scrolling marquee text band for a premium dark-themed designer portfolio. This section sits between the hero and the portfolio/work section.

DESIGN:
The band is a horizontal strip, approximately 72-90px tall, that spans 100% of the viewport width with overflow: hidden. It has a distinct background — either a contrasting light color (e.g. a warm off-white or cream) creating a sharp stripe against the dark page, OR a slightly lighter shade of the dark background with a top and bottom 1px border line in the accent color. This color contrast makes it feel like a divider band between sections.

CONTENT:
A single repeated string of text: "AT THE HEART OF DESIGN IS AN OPPORTUNITY TO PROBLEM SOLVE" — this phrase repeats continuously, separated by a decorative bullet or asterisk character (•) with space on each side. The text is uppercase, sans-serif, font-weight 600, font-size clamp(16px, 2vw, 22px), letter-spacing: 0.08em.

ANIMATION:
The text scrolls continuously from right to left in an infinite loop. Implement this using two identical copies of the text side by side inside a flex container, so when the first copy exits left, the second copy seamlessly takes its place (creating an infinite loop with no gap). The scroll speed is approximately 60 seconds per full cycle (slow, cinematic pace — not a fast news ticker). The animation is: transform: translateX(0) → translateX(-50%) over 60s linear infinite.

ON HOVER: When the user hovers over the marquee band, the scroll pauses (animation-play-state: paused). The cursor changes to a grab/pause icon.

DIRECTION VARIANT: The text scrolls LEFT by default. The direction can be reversed (right-to-left → left-to-right) by adding a data-direction="reverse" attribute — implement this in the JS.

Output: Full self-contained HTML + CSS + JS for this marquee component.
```

---

## ▸ PROMPT 4 — PORTFOLIO / WORK SECTION

```
You are building the portfolio/work showcase section for a premium dark-themed designer portfolio.

SECTION HEADER:
At the top left of the section: the label "Portfolio" in a small uppercase sans-serif tag (12px, letter-spacing 0.15em, --accent color). Below it, no large heading — the work speaks for itself. The section flows directly into the grid.

GRID LAYOUT:
6 portfolio items arranged in a 2-column grid on desktop. The columns are NOT equal width — they use an asymmetric alternating pattern:
- Odd rows (row 1, 3): Left card is wider (~58% width), right card is narrower (~38%), with a ~4% gap
- Even rows (row 2): Left card is narrower (~38%), right card is wider (~58%)
This creates a dynamic, offset rhythm rather than a boring equal grid.

EACH PORTFOLIO CARD:
- Aspect ratio: approximately 3:2 (landscape) for wide cards, 4:3 for narrow cards
- Contains: a large background image filling the card (object-fit: cover)
- At the bottom of the card, overlaid on the image: project title (H3, display serif, 24-32px) and a subtitle/role tag (12px uppercase sans-serif) in white text
- The text overlay has a gradient from transparent at top to semi-transparent dark at bottom (linear-gradient(to top, rgba(0,0,0,0.7) 0%, transparent 50%))

HOVER EFFECT (critical — this is the wow factor):
On mouse hover over a card:
1. The background image SCALES UP smoothly: transform: scale(1.06), transition: 500ms cubic-bezier(0.25, 0.46, 0.45, 0.94). The overflow is hidden on the card container so the image scales within bounds.
2. The project title and subtitle SLIDE UP by ~8px: transform: translateY(-8px), same timing.
3. A thin border (1px, --accent color) appears around the card perimeter with a clip-path animation — it draws clockwise starting from the top-left corner.
4. The custom cursor ring (from global setup) enlarges and shows the text "View" inside it, replacing the default cursor ring.

CARD ENTRANCE ANIMATION:
As each card scrolls into the viewport, it reveals with a clip-path animation: clip-path goes from inset(0 0 100% 0) to inset(0 0 0% 0) — a wipe reveal from top to bottom, duration 900ms, cubic-bezier(0.76, 0, 0.24, 1). Each card in a row staggers by 150ms.

NAVIGATION TO PROJECT:
Each card is an <a> tag linking to the project detail page. On click, a page transition overlay (full-screen dark panel) slides in from bottom-to-top BEFORE navigating, taking 400ms, so the transition feels intentional and cinematic.

OUTPUT: Full self-contained HTML + CSS + JS. Include 6 placeholder <div>s with data attributes for image URL, title, and role. Assume GSAP ScrollTrigger is available globally.
```

---

## ▸ PROMPT 5 — KEY PRINCIPLES SECTION

```
You are building the "Key Principles" section for a premium dark-themed designer portfolio. This is a personal values/philosophy section.

LAYOUT:
Two-column layout on desktop (50/50 split), single column on mobile. Left column has the heading and quote. Right column has the four principle cards/items.

LEFT COLUMN — HEADING & QUOTE:
- Small label at top: "Key Principles" — uppercase, 12px, letter-spacing 0.15em, --accent color
- Below: Large heading split into two lines: "Key" on line one and "Principles" on line two, BUT with intentional typographic play — "Principles" is indented ~60px, creating the same staircase offset as the hero name. Font: serif display, ~64px, font-weight 300.
- Subheading text: "I follow and believe in" — italic, sans-serif, 18px
- Block quote below: A multi-sentence personal philosophy quote (2-3 sentences), enclosed in large decorative quotation marks (the opening " is oversized ~80px in --accent color, positioned absolutely to the top-left of the quote block). Quote text is sans-serif, 16px, line-height 1.9, --text-secondary color. The quote has a left border (3px, --accent color) as an additional visual cue.

RIGHT COLUMN — FOUR PRINCIPLES:
Four items listed vertically, each separated by a 1px horizontal rule (--text-primary at 15% opacity).

Each principle item:
- Has a large number on the left (01, 02, 03, 04) in serif display font, ~80px, font-weight 300, opacity 0.12 (very ghosted/watermark-style number behind the text)
- The principle text overlaid on the number: bold sans-serif, 18-20px, e.g. "People are the biggest value"
- On the right edge of each item: a thin right-pointing arrow (→) that slides 8px rightward on hover with transition 300ms ease

SCROLL ANIMATION:
The left column fades in and slides from left (-40px → 0) as it enters the viewport. The right column items stagger in from right (40px → 0) with 100ms between each item.

LEFT-RIGHT STICKY BEHAVIOR (desktop only):
The left column is position: sticky, top: 120px so it stays visible while the user scrolls through the four principles on the right. This creates a natural reading flow where the heading remains anchored while the principles scroll past.

Output: Full self-contained HTML + CSS + JS for this section.
```

---

## ▸ PROMPT 6 — AWARDS SECTION

```
You are building the Awards highlight block for a premium dark-themed designer portfolio.

DESIGN:
This is NOT a full section — it is a compact horizontal band or card that sits within the "Key Principles" section flow (directly below the principles, before the next major section), OR it acts as a short standalone row between sections.

LAYOUT:
A single full-width row, dark background matching the page. Two content blocks side by side, separated by a vertical rule (1px, --text-primary at 20% opacity):

LEFT BLOCK — AWARDS STAT:
- A very large number: "50+" in serif display font, clamp(64px, 8vw, 100px), font-weight 700
- Below: "design awards including RedDot, Webby, San Francisco Design Week." in body sans-serif, 15px, --text-secondary, max-width 280px

RIGHT BLOCK — TEACHER & SPEAKER LABEL:
- Heading: "Teacher & Speaker" in serif display font, ~36px
- Short description paragraph below: 2 sentences about community involvement and Awwwards Academy. Body sans-serif, 15px, --text-secondary.

NUMBER COUNTER ANIMATION:
The "50+" number uses a count-up animation when it first enters the viewport: it counts from 0 to 50 over 2 seconds with an easeOut timing, then the "+" appends. This is triggered by IntersectionObserver (threshold: 0.5).

Output: Full self-contained HTML + CSS + JS for this component.
```

---

## ▸ PROMPT 7 — TEACHER & SPEAKER SECTION

```
You are building the "Teacher & Speaker" section for a premium dark-themed designer portfolio. This section showcases speaking engagements, courses, and community appearances.

SECTION HEADER:
Left-aligned. Small uppercase label "Speaking & Teaching", then a two-line heading in serif display font (~52px): "Teacher &" / "Speaker" with the same staircase offset (second line indented).

LAYOUT — SPEAKING CARDS:
The speaking engagements are displayed as a horizontal scrollable row on desktop, or a vertical stacked list on mobile.

Each speaking item is a card with:
- A small platform/event logo or icon on the left (circular, ~48px)
- Platform name in uppercase sans-serif label style
- Talk/event title in serif, ~20px, font-weight 400
- A subtle right-arrow link indicator

Cards are separated only by a 1px horizontal rule — no card borders or backgrounds. The feel is like an editorial list, not a grid of boxes.

FEATURED ITEMS (first 2-3 items):
The first 2-3 items are MORE visually prominent — they include a thumbnail image (rectangular, ~160px wide × 100px tall, border-radius: 8px) to the right of the text, showing a photo from the event or a preview of the course. The image has a slight hover scale effect (1.03x).

HOVER BEHAVIOR ON EACH ROW:
When hovering over a row, the entire row gets a very subtle background highlight (--text-primary at 3% opacity) and the right-arrow moves 6px to the right with a smooth transition.

LINK BEHAVIOR:
Each card/row is an <a> tag opening the link in a new tab. The custom cursor shows "↗" (external link indicator) on hover.

SCROLL ANIMATION:
Items stagger in from opacity 0 + translateX(-20px) to their final positions as the section enters the viewport, with 80ms stagger between rows.

Output: Full self-contained HTML + CSS + JS. Include 7 placeholder items with data attributes.
```

---

## ▸ PROMPT 8 — ARTICLES & PUBLICATIONS SECTION

```
You are building the "Articles & Publications" section for a premium dark-themed designer portfolio.

SECTION HEADER:
Left-aligned. Small label "Writing" in uppercase, then large heading "Articles &" / "Publications" in serif display font, two lines, with the staircase indent on the second line.

LAYOUT:
Articles are displayed as a horizontal row of 6 cards. On desktop they all show in one row. On mobile they become a horizontally scrollable carousel (overflow-x: auto, scrollbar hidden, -webkit-overflow-scrolling: touch with momentum).

EACH ARTICLE CARD:
- Fixed width: ~200px, height: ~260px
- Background: slightly lighter than page background (a subtle card surface — same dark family, ~5% lighter)
- Top section: A unique geometric icon/symbol (different for each article — e.g. a star, a checkmark, a droplet, an upward arrow, concentric squares, a plus sign). These are small SVG icons, roughly 40px, in --accent color or white.
- Middle section: Publication source name in uppercase label style (12px, letter-spacing 0.15em) — "MUZLI", "UX PLANET", "DRIBBBLE", "MEDIUM", etc.
- Article title: 2-3 lines, serif font, 17px, font-weight 400, line-height 1.5. This is the dominant text block.
- Bottom: Year label in --text-secondary, small monospace font
- The card has NO border by default. On hover: a 1px border appears in --accent color, and the card lifts slightly with transform: translateY(-6px) and a subtle box-shadow.

STAGGERED ENTRANCE:
Cards reveal from opacity 0 + translateY(30px) as the section scrolls into view, staggered by 100ms per card.

Output: Full self-contained HTML + CSS + JS. 6 placeholder cards.
```

---

## ▸ PROMPT 9 — MENTORSHIP & JUDGING SECTION

```
You are building the "Mentorship & Judging" section for a premium dark-themed designer portfolio.

SECTION HEADER:
Small label "Recognition", then large heading "Mentorship" / "& Judging" in serif display font (~52px), two lines, staircase indent on line two.

LAYOUT:
A grid of 6 judging/mentorship items. On desktop: 3 columns × 2 rows. On tablet: 2 columns. On mobile: 1 column. Each cell is separated ONLY by thin 1px rules (horizontal and vertical), no card backgrounds or borders — the grid itself is the structure (like a table).

EACH GRID ITEM:
- Organization name: sans-serif, bold, 18px (e.g. "Awwwards", "DEV Challenge", "ADC*E")
- Role label: uppercase, 12px, letter-spacing 0.15em, --accent color (e.g. "Jury Member", "Member and Judge", "Design Mentor")
- Year(s): small, --text-secondary, monospace style
- A small thumbnail photo (square, ~60px, border-radius: 4px) positioned at the bottom-right corner of the cell, showing an image from the event

HOVER STATE:
On hover over a grid cell, the organization name gets an underline in --accent color, and the thumbnail scales up to 1.05x. The cell background shifts to --text-primary at 3% opacity.

SCROLL ANIMATION:
All 6 cells fade in simultaneously when the section enters the viewport (no stagger — they all appear together for a grid "snap" feel).

Output: Full self-contained HTML + CSS + JS.
```

---

## ▸ PROMPT 10 — TESTIMONIALS / "ABOUT WORKING WITH ME" SECTION

```
You are building the testimonials / "About working with me" section for a premium dark-themed designer portfolio. This is one of the most complex sections on the page.

SECTION HEADER:
Large heading: "About working" / "with me" — serif display font, clamp(48px, 6vw, 80px), two lines, staircase indent on second line. Left-aligned.

LAYOUT — HORIZONTAL SLIDER:
This section is a full-width horizontal testimonial slider. It contains 8 testimonial slides. The slider takes up the full viewport width.

EACH SLIDE:
Layout is a two-column structure inside the slide (on desktop):
- LEFT COLUMN (~40% width): Contains a large square photograph of the client/project — approximately 400×400px, object-fit: cover. The photo has a subtle border-radius of 4-8px. No border.
- RIGHT COLUMN (~55% width, with gap): Contains the testimonial text content:
  a. Project name / company: uppercase sans-serif label, 12px, letter-spacing 0.15em, --accent color
  b. Client name + title: bold sans-serif, 16px. Name on one line, title below in --text-secondary
  c. Testimonial text: Long paragraph, serif or body sans-serif, 17px, line-height 1.85. This is the dominant block. It should feel like a genuine recommendation letter.
  d. LinkedIn link: small text link "LinkedIn →" at the bottom in --accent color

SLIDER NAVIGATION:
- A large "Next →" text button in the bottom-right area of the section (NOT typical arrow buttons) — clicking it advances to the next slide. The text is sans-serif, 14px uppercase, with a custom hover effect: the "→" slides 10px to the right on hover.
- Slide progress: A minimal horizontal progress bar at the bottom of the section (full width, 2px tall). The filled portion represents the current slide as a fraction (e.g. slide 3 of 8 = 37.5% filled). It animates smoothly between slides.
- Keyboard support: Left/right arrow keys navigate slides.

SLIDE TRANSITION:
Between slides, the content transitions with a clip-path reveal: the outgoing slide clips from inset(0 0 0 0) to inset(0 100% 0 0) (wipes to the right) while the incoming slide reveals from inset(0 0 0 100%) to inset(0 0 0 0) (wipes in from the right). Duration: 700ms, cubic-bezier(0.76, 0, 0.24, 1). The photo and text animate independently with slight offset timing.

COMPANY LOGOS ROW:
Directly BELOW the slider (same section, after the testimonials), a row of 8 company logos (SVG/PNG) is displayed. These are the logos of the companies that the testimonials are from. They are displayed in a flex row, centered, with equal spacing, each ~80-120px wide, filtered to be white/monochrome (filter: brightness(0) invert(1)) at 40% opacity. On hover over each logo, opacity jumps to 100% with a 200ms transition.

SWIPE SUPPORT:
On mobile/touch, implement touch swipe detection (touchstart + touchend delta calculation) to navigate between slides.

Output: Full self-contained HTML + CSS + JS. Include 8 placeholder slides with data attributes for image, name, company, title, and testimonial text.
```

---

## ▸ PROMPT 11 — SERVICES / "WHAT I DO" SECTION

```
You are building the "What I Do" / Services section for a premium dark-themed designer portfolio. This section showcases 5 service offerings in an accordion-style horizontal sliding panel.

SECTION HEADER:
Small label "Services", then large heading "Let's see how" / "I may help you." — serif display font, two lines, staircase indent on second line.

OVERVIEW TAGS ROW:
Before the detail panel, display all 5 service names in a horizontal flex row as pill/tag buttons:
"Mentorship" | "Website Audit" | "Consulting" | "UI/UX Design" | "Design Workshops"
Each tag: border 1px solid --text-primary at 30% opacity, border-radius: 100px (fully rounded pill), padding: 10px 24px, font-size 14px, font-weight 500. The active/selected tag: background --accent (or --text-primary), text --bg (inverted). On hover: background --text-primary at 10% opacity.

MAIN PANEL — HORIZONTAL ACCORDION SLIDER:
Below the tags, a large panel takes up the full width. This panel shows 5 columns, one for each service. On desktop, all 5 columns are visible simultaneously in a compressed state (each showing only the service title vertically). On hover over a column, it EXPANDS to fill ~50% of the panel width, while the other 4 columns compress to share the remaining 50%.

EACH COLUMN (service panel):
- Collapsed state: Shows only the service name rotated 90° (written vertically, bottom-to-top), uppercase, sans-serif 14px
- Expanded state (on hover or when active): Shows full content:
  a. Service title: serif display font, ~40px, horizontal
  b. Brief description: 2-3 sentences, body sans-serif, 16px, --text-secondary
  c. What I can help you with: a short bulleted list (no bullet markers — use thin dashes or dots) of 3-5 items, 15px
  d. How it works: Another short list of process steps, 15px
  e. Pricing info if applicable (e.g. "$250/hour")
  f. A text CTA at the bottom: "Book a session →" or "Drop me a message →"

EXPANSION ANIMATION:
When a column expands: width transitions from ~10% to ~50% using transition: width 500ms cubic-bezier(0.25, 0.46, 0.45, 0.94). The text content inside fades in (opacity 0 → 1, 300ms delay after width transition starts). The vertical title rotates from 90° to 0° (transform: rotate(90deg) → rotate(0deg), same timing).

MOBILE BEHAVIOR:
On mobile, collapse the horizontal accordion entirely. Instead, the 5 services become a vertical accordion: each row shows the service title and a "+" icon. Clicking expands the row to reveal the full content below, with a smooth max-height transition.

Output: Full self-contained HTML + CSS + JS for this section. Include all 5 services as placeholder data.
```

---

## ▸ PROMPT 12 — CONTACT & FOOTER SECTION

```
You are building the combined Contact + Footer section for a premium dark-themed designer portfolio. This is the last section on the page.

CONTACT AREA — TOP PART:
A full-width section with generous vertical padding (150px top).

LEFT SIDE (~50%):
- Large email address as a clickable mailto link: body sans-serif or display serif, clamp(20px, 3vw, 36px), color --text-primary, no underline by default. On hover: underline slides in from left, and the text color shifts to --accent.

RIGHT SIDE (~45%):
- A compact contact form. NOT a standard form — styled to match the dark luxury aesthetic:
  - Input fields: NO box/border visible by default. Only a bottom border (1px, --text-primary at 30% opacity). Background: transparent. Text: --text-primary. Font: body sans-serif, 16px. On focus: the bottom border animates to full --accent color.
  - The form has two inputs side-by-side: name and email (each ~48% width with 4% gap).
  - Below: A row of service tags (same pill style as the What I Do section) acting as a multi-select for "type of inquiry": "Consulting", "Design", "Mentorship", "Design Workshops", "Website Audit". The user can click multiple tags to select them. Selected tags: filled with --accent. This replaces a dropdown.
  - A single "Submit" or "Send" button: minimal, just text with a right arrow "→", no box. On hover the arrow animates right by 8px.
  - On successful submit: The form fades out and a full-width thank you message fades in: "Thank you for your message. I'll get back to you soon." — serif italic, ~28px, centered.

FOOTER BOTTOM BAR:
A thin bar at the very bottom separated by a 1px rule from the contact area:
- LEFT: The logo (same as navbar)
- CENTER: "Made by [Studio Name]" in small --text-secondary
- RIGHT: Social links — "LinkedIn", "Twitter", "Facebook" — in small uppercase sans-serif, each with hover underline effect matching the navbar

FOOTER FEEL:
The footer should feel like the final page of a coffee table book — refined, spacious, confident. No clutter.

SCROLL-TO-TOP:
A small circular button in the bottom-right corner (fixed position): contains an upward arrow "↑", 44×44px, border: 1px solid --text-primary at 40% opacity, border-radius: 50%. On hover: background fills to --accent, arrow animates upward slightly. Only visible after the user scrolls past 400px (fades in/out based on scroll position). On click: smooth scroll to top with 800ms duration.

Output: Full self-contained HTML + CSS + JS for the contact + footer section.
```

---

## ▸ PROMPT 13 — FINAL ASSEMBLY & PAGE-WIDE SCROLL ANIMATIONS

```
You are assembling all sections of a premium dark-themed designer portfolio into a single cohesive page and adding the final layer of page-wide scroll animations using GSAP ScrollTrigger.

ASSEMBLY ORDER (top to bottom):
1. Global styles + custom cursor
2. Navigation / Header
3. Hero Section
4. Marquee / Ticker Band
5. Portfolio / Work Grid Section
6. Key Principles Section
7. Awards Band
8. Teacher & Speaker Section
9. Articles & Publications Section
10. Mentorship & Judging Section
11. Testimonials / About Working With Me Section
12. Services / What I Do Section
13. Contact & Footer Section

PAGE-WIDE SCROLL BEHAVIORS TO ADD (GSAP ScrollTrigger):

1. SECTION NUMBERS:
   Each major section (except hero) has a fixed-position section counter that updates as you scroll: "02 / 09", "03 / 09" etc. This appears in the bottom-left corner, small monospace text, --text-primary at 40% opacity. It transitions between numbers with a clip-path reveal (current number exits up, next enters from below).

2. HORIZONTAL SCROLL SECTION (optional but premium):
   The Portfolio section can optionally be transformed into a horizontal scroll section using GSAP ScrollTrigger's horizontal pinning: the section pins to the viewport while the cards scroll HORIZONTALLY as the user scrolls vertically. This is a hallmark of premium portfolio sites. The section requires enough scroll distance (height: 300vh) to allow all cards to pass. After all cards have passed, the section unpins and normal vertical scroll resumes.

3. PARALLAX ON SECTION HEADINGS:
   All major section headings (serif display text) have a subtle parallax effect: as the section scrolls through the viewport, the heading moves at 80% of scroll speed (scrub: true in GSAP ScrollTrigger), creating a gentle depth illusion.

4. BACKGROUND COLOR SHIFT:
   A subtle background color progression as the user scrolls. The page background stays dark throughout, but the exact shade very subtly shifts between sections — e.g. pure #0a0a0a in the hero to a slightly warmer dark in the middle sections and back to cool dark at the footer. This is done with GSAP ScrollTrigger and backgroundColor tweening, barely perceptible but adds depth.

5. PROGRESS BAR:
   A 2px horizontal progress bar at the very top of the viewport (above the navbar, position: fixed, z-index: 200, width: 100%, top: 0). It fills from left to right in --accent color as the user scrolls from top to bottom of the page.

PERFORMANCE CONSIDERATIONS:
- All animations that are not in the viewport should NOT be running (use IntersectionObserver / ScrollTrigger to pause/start)
- Images should be lazy-loaded (loading="lazy" on all <img> tags)
- The page should achieve a Lighthouse performance score of 90+ on desktop

Output: The complete assembled HTML file with all sections integrated, global GSAP scroll animation setup, and all performance optimizations applied. Use all CSS variables consistently. Ensure smooth, flicker-free scroll performance.
```

---

*These 13 prompts cover every section and interaction on the reference portfolio. Feed them one at a time to your LLM, assemble the outputs, and slot in your own content + color palette.*