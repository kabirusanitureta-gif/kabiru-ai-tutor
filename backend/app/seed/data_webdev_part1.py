"""
Seed data for the Web Development Fundamentals course — Module 1: HTML Foundations.
Full professional curriculum, Part 1 (Lesson 1).

Each lesson now includes the complete professional structure:
explanation, examples, practice, mini_project, real_world_project,
common_mistakes, best_practices, interview_questions, plus a quiz.
"""

WEBDEV_LESSONS_PART1 = [
    {
        "slug": "webdev-01-intro-web-browsers",
        "title": "1. Introduction to the Web and How Browsers Work",
        "level": "beginner",
        "explanation": (
            "The web works through a client-server model. When you type a URL, your browser (the "
            "client) sends an HTTP request to a server, which sends back an HTTP response containing "
            "HTML, CSS, JavaScript, and other assets. The browser then parses the HTML into a DOM "
            "(Document Object Model) tree, applies CSS to compute how everything should look (the "
            "render tree), and paints pixels to the screen — this pipeline is often called "
            "'Parse -> Style -> Layout -> Paint -> Composite'.\n\n"
            "Every request/response uses HTTP (or encrypted HTTPS). Key HTTP concepts you'll use "
            "constantly as a web developer: methods (GET fetches data, POST sends data), status codes "
            "(200 OK, 404 Not Found, 500 Server Error), and headers (metadata like Content-Type). "
            "Understanding this pipeline explains WHY certain practices matter later — for example, "
            "why placing <script> tags at the end of <body> avoids blocking the initial render, and "
            "why minimizing HTTP requests speeds up page loads."
        ),
        "examples": (
            "Example 1 — A minimal request/response cycle (conceptually):\n"
            "  Browser sends:  GET /index.html HTTP/1.1\n"
            "                  Host: example.com\n"
            "  Server replies: HTTP/1.1 200 OK\n"
            "                  Content-Type: text/html\n"
            "                  <html>...</html>\n"
            "\n"
            "Example 2 — Viewing this in real life using curl (works in Termux/Linux terminal):\n"
            "  curl -I https://example.com\n"
            "  # Shows just the response headers: status code, content type, server info\n"
            "\n"
            "Example 3 — The rendering pipeline in plain terms:\n"
            "  1. Parse HTML -> builds the DOM tree\n"
            "  2. Parse CSS  -> builds the CSSOM (style rules)\n"
            "  3. Combine DOM + CSSOM -> Render Tree (only visible elements)\n"
            "  4. Layout -> calculates exact position/size of every element\n"
            "  5. Paint -> draws pixels\n"
            "  6. Composite -> layers are combined for the final image on screen\n"
        ),
        "practice": (
            "1. Open your browser's DevTools (F12 or long-press > Inspect on mobile Chrome), go to the "
            "Network tab, and reload any website. Identify: the first request made, its status code, "
            "and its Content-Type header.\n"
            "2. Run `curl -I https://example.com` in a terminal (Termux/Linux) and identify the status "
            "code and at least 2 response headers.\n"
            "3. In DevTools, find one request that returned a status code other than 200 (try a "
            "misspelled URL) and note what status code appeared instead.\n"
            "4. Explain in your own words (write 3-4 sentences) why a browser needs BOTH the DOM and "
            "the CSSOM before it can build a Render Tree."
        ),
        "mini_project": (
            "Mini Project: Request/Response Inspector Log\n"
            "Pick any 3 real websites. For each one, use DevTools' Network tab to record: the main "
            "document's status code, its Content-Type, and the total number of requests made to fully "
            "load the page. Write up your findings in a short markdown file comparing the three sites — "
            "which loaded the fewest requests, and can you guess why (e.g. simpler design, fewer "
            "images)?"
        ),
        "real_world_project": (
            "Real-World Project: Page Load Audit for a Local Business\n"
            "Find a real small-business or personal website (with permission, or use your own). Using "
            "DevTools Network and Lighthouse tabs, produce a short audit report covering: total page "
            "weight, number of requests, largest resource loaded, and 3 concrete suggestions to reduce "
            "load time (e.g. 'the hero image is 4MB and should be compressed'). This mirrors real "
            "freelance/agency work — 'website speed audits' are a common paid service in web "
            "development."
        ),
        "common_mistakes": (
            "- Confusing HTTP status code categories: assuming any 4xx or 5xx means 'my code is "
            "broken' — 404 means the resource wasn't found (often just a wrong URL), while 500 means "
            "the SERVER crashed while handling the request; they need different debugging approaches.\n"
            "- Thinking HTTPS is 'optional' or 'just for banks' — browsers now flag plain HTTP sites as "
            "'Not Secure', and many modern browser features (camera, geolocation, service workers) "
            "simply refuse to work over HTTP.\n"
            "- Believing the page is 'done loading' the moment HTML arrives — in reality, CSS, "
            "JavaScript, images, and fonts often load afterward and can still shift layout or run code, "
            "which is why performance work looks at the FULL loading timeline, not just the first "
            "response.\n"
            "- Not realizing that opening a local HTML file directly (file:// URL) behaves differently "
            "from serving it over HTTP (http://localhost) — some browser features (like Fetch to "
            "another origin) are blocked or behave inconsistently under file://."
        ),
        "best_practices": (
            "- Always test your site under HTTPS in production; use a free certificate provider (e.g. "
            "via your host — Render and Vercel provide HTTPS automatically).\n"
            "- Get comfortable with DevTools' Network tab early — it's the single most-used tool for "
            "diagnosing 'why is my site slow / why isn't my API call working' throughout your entire "
            "career as a web developer.\n"
            "- Learn to read status codes at a glance: 2xx = success, 3xx = redirect, 4xx = client "
            "error (you sent something wrong), 5xx = server error (their code crashed).\n"
            "- When debugging 'my page looks broken,' get in the habit of checking the Console tab for "
            "JavaScript errors AND the Network tab for failed requests — most real bugs show up in one "
            "of these two places first."
        ),
        "interview_questions": (
            "1. Explain what happens, step by step, from the moment a user types a URL into the "
            "address bar to when they see the fully rendered page.\n"
            "2. What is the difference between the DOM and the CSSOM, and why does the browser need "
            "both before it can paint anything to the screen?\n"
            "3. What's the difference between a 404 and a 500 status code, and how would your "
            "debugging approach differ for each?\n"
            "4. Why might a browser block a JavaScript fetch() request when a page is opened via a "
            "file:// URL but not when served via http://localhost?\n"
            "5. Name three response headers you'd expect to see on a typical HTML page response, and "
            "explain what each one tells the browser."
        ),
        "assignment": (
            "Assignment: Network Request Report\n"
            "Using your browser's DevTools Network tab, load any 3 different websites of your choice. "
            "For each site, write down: (a) the status code of the main document request, (b) the "
            "total number of requests made, (c) the total page weight in KB/MB, and (d) one request "
            "that surprised you (e.g. an unexpectedly large image, or a request to a third-party "
            "domain like an ad or analytics service). Submit your findings as a short written report "
            "(one paragraph per site)."
        ),
        "challenge": (
            "Challenge: Fastest Page Wins\n"
            "Find or build the SMALLEST possible valid HTML page (correct doctype, head, and body) "
            "that still displays visible text. Measure its total transfer size in DevTools. Then try "
            "to make it even smaller without breaking validity. Compare your smallest page's size "
            "against a popular news website's homepage size — how many times smaller is yours?"
        ),
        "summary": (
            "The web works on a client-server model over HTTP/HTTPS. A browser sends a request, "
            "receives HTML/CSS/JS/assets in response, and renders them through the pipeline: "
            "Parse -> Style -> Layout -> Paint -> Composite. HTTP status codes tell you whether a "
            "request succeeded (2xx), was redirected (3xx), had a client-side problem (4xx), or a "
            "server-side problem (5xx). Understanding this foundational pipeline explains why later "
            "best practices (script placement, HTTPS, minimizing requests) actually matter."
        ),
        "lesson_references": (
            "- MDN Web Docs: 'How the Web Works' (developer.mozilla.org)\n"
            "- MDN Web Docs: 'HTTP overview' (developer.mozilla.org/en-US/docs/Web/HTTP/Overview)\n"
            "- web.dev: 'Critical Rendering Path' (web.dev/critical-rendering-path)\n"
            "- HTTP Status Code reference: httpstatuses.com"
        ),
        "next_lesson_preview": (
            "Next up: HTML Document Structure and Semantic Tags. Now that you understand how a page "
            "gets from a server to your screen, you'll learn how to structure the HTML itself the "
            "right way — using semantic tags that make your pages more accessible, more "
            "SEO-friendly, and easier for other developers to read."
        ),
        "quiz": {
            "title": "Introduction to the Web and Browsers Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does the browser build first after receiving HTML?",
                    "option_a": "The Render Tree",
                    "option_b": "The DOM tree",
                    "option_c": "The final painted pixels",
                    "option_d": "The CSSOM only",
                    "correct_option": "b",
                    "explanation": "The browser parses HTML into the DOM tree first, before combining it with CSS.",
                },
                {
                    "text": "Which HTTP status code range indicates a client-side error (something wrong with the request)?",
                    "option_a": "2xx",
                    "option_b": "3xx",
                    "option_c": "4xx",
                    "option_d": "5xx",
                    "correct_option": "c",
                    "explanation": "4xx codes (like 404) mean the client's request was invalid or the resource wasn't found.",
                },
                {
                    "text": "Which HTTP method is typically used to fetch data without sending a body?",
                    "option_a": "POST",
                    "option_b": "GET",
                    "option_c": "DELETE",
                    "option_d": "PUT",
                    "correct_option": "b",
                    "explanation": "GET requests retrieve data and conventionally carry no request body.",
                },
                {
                    "text": "Why is HTTPS important beyond just 'security'?",
                    "option_a": "It makes pages load HTML faster",
                    "option_b": "Many modern browser APIs (camera, geolocation, service workers) require it",
                    "option_c": "It's only relevant for e-commerce sites",
                    "option_d": "It has no practical effect on functionality",
                    "correct_option": "b",
                    "explanation": "Browsers restrict many powerful APIs to secure (HTTPS) contexts for security reasons.",
                },
            ],
        },
    },
    {
        "slug": "webdev-02-document-structure-semantic",
        "title": "2. HTML Document Structure and Semantic Tags",
        "level": "beginner",
        "explanation": (
            "Every valid HTML page starts with <!DOCTYPE html>, which tells the browser to render in "
            "standards mode (not quirks mode, an old compatibility mode with inconsistent behavior). "
            "The <html> element wraps everything, split into <head> (metadata invisible to "
            "visitors — title, character encoding, linked stylesheets, meta tags) and <body> (the "
            "visible content).\n\n"
            "'Semantic HTML' means choosing tags based on MEANING, not appearance. Instead of wrapping "
            "everything in generic <div> tags, HTML5 gives you meaningful elements: <header>, <nav>, "
            "<main>, <article>, <section>, <aside>, and <footer>. This matters for three real reasons: "
            "(1) screen readers use semantic tags to help blind users navigate a page efficiently, "
            "(2) search engines use them to understand what content matters most for ranking, and "
            "(3) other developers (including future you) can read the structure at a glance instead of "
            "deciphering a wall of unlabeled <div>s."
        ),
        "examples": (
            "Example 1 — A complete, well-structured minimal document:\n"
            "<!DOCTYPE html>\n"
            "<html lang=\"en\">\n"
            "<head>\n"
            "  <meta charset=\"UTF-8\">\n"
            "  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
            "  <title>Kabiru's Portfolio</title>\n"
            "</head>\n"
            "<body>\n"
            "  <header>\n"
            "    <h1>Kabiru Sani</h1>\n"
            "    <nav>\n"
            "      <a href=\"#about\">About</a>\n"
            "      <a href=\"#projects\">Projects</a>\n"
            "    </nav>\n"
            "  </header>\n"
            "  <main>\n"
            "    <section id=\"about\">\n"
            "      <h2>About Me</h2>\n"
            "      <p>Learning full-stack web development.</p>\n"
            "    </section>\n"
            "  </main>\n"
            "  <footer>\n"
            "    <p>&copy; 2026 Kabiru Sani</p>\n"
            "  </footer>\n"
            "</body>\n"
            "</html>\n"
            "\n"
            "Example 2 — Semantic vs non-semantic comparison:\n"
            "<!-- Bad: no meaning, screen readers/SEO get nothing useful -->\n"
            "<div class=\"top\"><div class=\"title\">Blog Post</div></div>\n"
            "\n"
            "<!-- Good: structure carries meaning -->\n"
            "<article>\n"
            "  <h1>Blog Post</h1>\n"
            "</article>\n"
        ),
        "practice": (
            "1. Build a full HTML document skeleton with <head> (including charset and viewport meta "
            "tags) and a <body> containing <header>, <main>, and <footer>.\n"
            "2. Inside <main>, use <section> to divide your page into 'About', 'Skills', and 'Contact' "
            "areas, each with its own heading.\n"
            "3. Add a <nav> inside your <header> with links that jump to each section using # anchors.\n"
            "4. Open your page in a browser, then use DevTools' Accessibility tree (or a screen reader "
            "if available) to see how the semantic structure is exposed."
        ),
        "mini_project": (
            "Mini Project: Semantic Restructuring Exercise\n"
            "Take any existing HTML page you find online (view-source on a simple site), copy its "
            "visible content into a fresh document, and rebuild the SAME content using fully semantic "
            "tags (header/nav/main/section/article/aside/footer) instead of generic divs. Compare "
            "before/after and write 2-3 sentences on what changed."
        ),
        "real_world_project": (
            "Real-World Project: Accessible Landing Page for a Local Organization\n"
            "Design a one-page semantic HTML skeleton (no styling needed yet) for a real or fictional "
            "local organization (a school, mosque, church, small business). Structure it with proper "
            "header/nav/main/sections/footer, correct heading hierarchy (one <h1>, then <h2>s under "
            "it), and appropriate alt text placeholders for images. This exact skeleton-first approach "
            "is standard practice at real agencies before any visual design work begins."
        ),
        "common_mistakes": (
            "- Using multiple <h1> tags per page 'because it looks bold' — a page should generally have "
            "ONE <h1> (the main topic), with <h2>, <h3> etc. nesting logically below it, like an "
            "outline.\n"
            "- Wrapping everything in <div> out of habit, even when a semantic tag exists — this is "
            "sometimes called 'divitis' and hurts both accessibility and SEO.\n"
            "- Forgetting the viewport meta tag — without <meta name=\"viewport\" content=\"width=device-width, "
            "initial-scale=1.0\">, mobile browsers render the page as if it were a desktop page and then "
            "zoom out, making text tiny and layouts broken on phones.\n"
            "- Nesting <section> or <article> purely for CSS styling hooks rather than genuine content "
            "grouping — if you just need a styling wrapper with no semantic meaning, a <div> is "
            "actually the correct, honest choice."
        ),
        "best_practices": (
            "- Always include <!DOCTYPE html>, a charset meta tag, and a viewport meta tag — these "
            "three lines should be in literally every project you ever build.\n"
            "- Think of heading tags (<h1>-<h6>) as an outline, not a font-size tool — never skip "
            "levels (e.g. going from <h2> straight to <h4>) just because you like how it looks; use "
            "CSS to control appearance instead.\n"
            "- Use <main> exactly once per page to mark the primary content, which helps screen reader "
            "users skip repeated navigation and jump straight to the content that matters.\n"
            "- When in doubt about which semantic tag to use, ask: 'if I removed all CSS, would this "
            "structure still make logical sense as an outline of the content?' If yes, you've likely "
            "chosen correctly."
        ),
        "interview_questions": (
            "1. What is the difference between <div> and <section>, and when would you use one over "
            "the other?\n"
            "2. Why does semantic HTML matter for accessibility and SEO, beyond just 'best practice'?\n"
            "3. What does the viewport meta tag do, and what happens visually on mobile if you forget "
            "it?\n"
            "4. Explain why a page should typically have only one <h1> element and how you'd structure "
            "headings for a page with multiple major sections.\n"
            "5. What's the difference between quirks mode and standards mode, and what triggers each?"
        ),
        "assignment": (
            "Assignment: Semantic Audit\n"
            "Pick any 2 real websites. View their page source (or use DevTools' Elements panel). For "
            "each site, count how many <div> tags are used versus semantic tags (header, nav, main, "
            "section, article, aside, footer). Write a short paragraph judging whether each site uses "
            "semantic HTML well or poorly, with specific examples of what you found."
        ),
        "challenge": (
            "Challenge: Zero-CSS Readability\n"
            "Build a complete one-page HTML document (header/nav/main with 3 sections/footer) with "
            "absolutely NO CSS applied. A well-structured semantic page should still be readable and "
            "logically ordered even unstyled. Have someone else read it and tell you, section by "
            "section, what each part of the page is for — if they can't tell, your structure needs work."
        ),
        "summary": (
            "Every HTML document needs <!DOCTYPE html>, a <head> with charset and viewport meta tags, "
            "and a <body>. Semantic tags (header, nav, main, section, article, aside, footer) describe "
            "content by MEANING rather than appearance, which benefits accessibility (screen readers), "
            "SEO (search engines), and code readability (other developers). Heading tags should form a "
            "logical outline — one <h1> per page, with h2-h6 nesting beneath it — never skipped purely "
            "for visual sizing."
        ),
        "lesson_references": (
            "- MDN Web Docs: 'HTML elements reference' (developer.mozilla.org/en-US/docs/Web/HTML/Element)\n"
            "- MDN Web Docs: 'Document and website structure' (developer.mozilla.org)\n"
            "- W3C: 'HTML5 Semantics' specification section\n"
            "- web.dev: 'Learn HTML - Semantic HTML' course"
        ),
        "next_lesson_preview": (
            "Next up: Text Elements and Formatting. You'll go deeper into the tags that shape text "
            "itself — paragraphs, headings in detail, emphasis, quotes, and the many inline elements "
            "HTML provides for expressing meaning within a sentence, not just structuring the page."
        ),
        "quiz": {
            "title": "HTML Document Structure and Semantic Tags Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does <!DOCTYPE html> do?",
                    "option_a": "Links a CSS file",
                    "option_b": "Tells the browser to render in standards mode",
                    "option_c": "Creates a comment",
                    "option_d": "Defines the page title",
                    "correct_option": "b",
                    "explanation": "The doctype declaration ensures consistent, standards-compliant rendering across browsers.",
                },
                {
                    "text": "Which tag should be used to mark the single primary content area of a page?",
                    "option_a": "<section>",
                    "option_b": "<div>",
                    "option_c": "<main>",
                    "option_d": "<article>",
                    "correct_option": "c",
                    "explanation": "<main> identifies the primary content, used once per page, and helps screen reader navigation.",
                },
                {
                    "text": "What problem does the viewport meta tag solve?",
                    "option_a": "It prevents images from loading",
                    "option_b": "It ensures the page renders at the correct scale on mobile devices",
                    "option_c": "It sets the page's character encoding",
                    "option_d": "It adds a favicon",
                    "correct_option": "b",
                    "explanation": "Without it, mobile browsers assume a desktop-width layout and zoom out, breaking the mobile experience.",
                },
                {
                    "text": "Why is using semantic tags instead of only <div> considered best practice?",
                    "option_a": "Semantic tags load faster",
                    "option_b": "They improve accessibility and help search engines understand content structure",
                    "option_c": "<div> is deprecated in HTML5",
                    "option_d": "Browsers render <div> incorrectly",
                    "correct_option": "b",
                    "explanation": "Semantic tags carry meaning that assistive technology and search engines can use, unlike generic divs.",
                },
            ],
        },
    },
    {
        "slug": "webdev-03-text-formatting",
        "title": "3. Text Elements and Formatting",
        "level": "beginner",
        "explanation": (
            "Beyond headings, HTML offers many tags for formatting and giving meaning to text within a "
            "paragraph. <strong> marks text of strong importance (rendered bold), <em> marks stressed "
            "emphasis (rendered italic) — note these are semantic, not just visual: <b> and <i> exist "
            "too, but only for cases with NO extra importance/emphasis meaning (like a book title in "
            "<i>). <blockquote> marks an extended quotation, while inline <q> marks a short one. <br> "
            "forces a line break, <hr> creates a thematic divider, and <pre> preserves whitespace "
            "exactly as typed — essential for displaying code snippets, which is usually paired with "
            "<code> for inline or block code text."
        ),
        "examples": (
            "Example 1 — Semantic emphasis vs plain styling:\n"
            "<p>You <strong>must</strong> save your work before closing the app.</p>\n"
            "<p>The word <em>really</em> changes the meaning of this sentence.</p>\n"
            "<p>The novel <i>Things Fall Apart</i> is a classic. <!-- title, no extra emphasis --></p>\n"
            "\n"
            "Example 2 — Quotes:\n"
            "<blockquote cite=\"https://example.com/source\">\n"
            "  <p>Code is read far more often than it is written.</p>\n"
            "</blockquote>\n"
            "<p>She said <q>let's ship it</q> right before the deploy.</p>\n"
            "\n"
            "Example 3 — Preformatted text and inline code:\n"
            "<p>Use the <code>print()</code> function to display output.</p>\n"
            "<pre><code>def greet(name):\n"
            "    return f\"Hello, {name}!\"\n"
            "</code></pre>\n"
        ),
        "practice": (
            "1. Write a paragraph using <strong> to highlight one important word and <em> to stress "
            "another.\n"
            "2. Add a <blockquote> with a quote you like, including the cite attribute pointing to a "
            "source URL.\n"
            "3. Display a 3-line Python code snippet using <pre><code>...</code></pre>, preserving "
            "indentation exactly.\n"
            "4. Use <hr> to visually separate two unrelated sections of a page."
        ),
        "mini_project": (
            "Mini Project: Formatted Article Page\n"
            "Write a short article (5-6 paragraphs) about any topic you're learning. Use <strong> and "
            "<em> purposefully (not randomly) to guide a reader's attention, include one <blockquote> "
            "citing a source, and one <pre><code> block showing a relevant code example."
        ),
        "real_world_project": (
            "Real-World Project: Documentation Page Recreation\n"
            "Pick a short section from any real technical documentation site (e.g. MDN, Python docs) "
            "and recreate its text formatting in your own HTML file — matching where they use bold, "
            "italic, code blocks, and blockquotes. This trains the exact skill of writing clean "
            "technical documentation, a task nearly every professional developer does regularly."
        ),
        "common_mistakes": (
            "- Using <b> or <i> for emphasis 'because it looks the same as <strong>/<em>' — visually "
            "identical by default, but screen readers announce <strong>/<em> differently, and using "
            "the wrong one misleads assistive technology users.\n"
            "- Using multiple <br> tags in a row to create vertical spacing — this is a CSS job "
            "(margin/padding), not an HTML one; <br> should only be used for genuine line breaks within "
            "content (like a mailing address).\n"
            "- Forgetting to escape special characters in code examples — showing HTML code inside "
            "<pre><code> requires escaping < and > as &lt; and &gt;, or the browser will try to render "
            "them as real tags instead of displaying them as text.\n"
            "- Nesting block-level quotes incorrectly — <blockquote> is a block element and should wrap "
            "block content like <p>, while <q> is inline and used within a sentence."
        ),
        "best_practices": (
            "- Choose tags by meaning first: ask 'is this genuinely important/emphasized, or do I just "
            "want it to look a certain way?' — meaning uses <strong>/<em>, pure look uses CSS.\n"
            "- Always include the cite attribute on <blockquote> when quoting a real source — it's good "
            "practice for both credibility and potential tooling that reads it.\n"
            "- Reserve <pre> for content where whitespace truly matters (code, ASCII art) — never use "
            "it as a shortcut to avoid writing proper paragraph tags.\n"
            "- When displaying code samples on a real project, pair <pre><code> with a syntax "
            "highlighting library (you'll cover this later in the React module) rather than manually "
            "coloring text."
        ),
        "interview_questions": (
            "1. What's the practical (non-visual) difference between <strong> and <b>, or <em> and "
            "<i>?\n"
            "2. When would you use <blockquote> versus <q>?\n"
            "3. Why does <pre><code> matter for displaying code, and what happens if you display code "
            "in a normal <p> tag instead?\n"
            "4. How would you safely display the literal text '<div>' on a web page without the "
            "browser interpreting it as an actual tag?\n"
            "5. Why is using <br><br> for spacing between sections considered bad practice?"
        ),
        "assignment": (
            "Assignment: Bold and Italic Audit\n"
            "Find a real webpage with a mix of bold and italic text (a news article works well). "
            "Inspect each bold/italic instance in DevTools — is it implemented with <strong>/<em>, or "
            "with plain <b>/<i>, or with CSS font-weight/font-style on a <span>? Document at least 5 "
            "examples and judge whether each choice was semantically appropriate."
        ),
        "challenge": (
            "Challenge: Code Snippet Gallery\n"
            "Build a page displaying 5 code snippets in 5 different programming languages (they don't "
            "need to run — just be displayed as text) using proper <pre><code> formatting with "
            "correctly escaped special characters. Add a small caption above each snippet using "
            "semantic text formatting."
        ),
        "summary": (
            "HTML provides semantic text-level tags — <strong> and <em> for meaningful emphasis "
            "(distinct from purely visual <b>/<i>), <blockquote>/<q> for quotations, and <pre>/<code> "
            "for preformatted and code content. Choosing tags by MEANING rather than appearance keeps "
            "content accessible and lets CSS handle pure visual styling separately, which is the "
            "correct separation of concerns in professional HTML."
        ),
        "lesson_references": (
            "- MDN Web Docs: 'Inline text semantics' (developer.mozilla.org/en-US/docs/Web/HTML/Element#inline_text_semantics)\n"
            "- MDN Web Docs: '<blockquote>' and '<q>' element references\n"
            "- MDN Web Docs: '<pre>' and '<code>' element references\n"
            "- W3C: HTML Living Standard, Text-level semantics section"
        ),
        "next_lesson_preview": (
            "Next up: Links, Images, and Media. You'll learn how to connect pages together and embed "
            "images, audio, and video — the elements that turn a page from plain text into a rich, "
            "connected web experience."
        ),
        "quiz": {
            "title": "Text Elements and Formatting Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What is the key difference between <strong> and <b>?",
                    "option_a": "They are visually different by default",
                    "option_b": "<strong> conveys semantic importance, while <b> is purely visual with no extra meaning",
                    "option_c": "<b> is deprecated and should never be used",
                    "option_d": "There is no difference at all",
                    "correct_option": "b",
                    "explanation": "<strong> signals genuine importance to assistive technology; <b> is purely stylistic bolding.",
                },
                {
                    "text": "Which tag preserves whitespace and line breaks exactly as typed?",
                    "option_a": "<code>",
                    "option_b": "<pre>",
                    "option_c": "<blockquote>",
                    "option_d": "<span>",
                    "correct_option": "b",
                    "explanation": "<pre> (preformatted text) preserves exact whitespace and line breaks from the source.",
                },
                {
                    "text": "Which tag is appropriate for a short, inline quotation within a sentence?",
                    "option_a": "<blockquote>",
                    "option_b": "<q>",
                    "option_c": "<pre>",
                    "option_d": "<cite>",
                    "correct_option": "b",
                    "explanation": "<q> is the inline quotation element, used within a sentence, unlike block-level <blockquote>.",
                },
                {
                    "text": "How should you display the literal characters '<div>' as visible text on a page?",
                    "option_a": "Type them directly and it works fine",
                    "option_b": "Escape them as &lt;div&gt;",
                    "option_c": "Wrap them in <strong>",
                    "option_d": "It's not possible in HTML",
                    "correct_option": "b",
                    "explanation": "Angle brackets must be escaped as HTML entities (&lt; and &gt;) to display as literal text instead of being parsed as a tag.",
                },
            ],
        },
    },
    {
        "slug": "webdev-04-links-images-media",
        "title": "4. Links, Images, and Media",
        "level": "beginner",
        "explanation": (
            "Links (<a href=\"...\">) connect pages together and are the foundation of the 'web' in "
            "World Wide Web. Relative paths ('about.html', '../images/logo.png') point within your "
            "own site; absolute URLs ('https://example.com') point elsewhere. Images use <img "
            "src=\"...\" alt=\"...\"> — the alt attribute is NOT optional: it's read aloud by screen "
            "readers and shown if the image fails to load, and search engines use it to understand "
            "image content. For audio and video, HTML5 provides native <audio> and <video> tags with "
            "built-in browser controls, no plugins needed."
        ),
        "examples": (
            "Example 1 — Links (relative vs absolute, plus opening in a new tab):\n"
            "<a href=\"about.html\">About</a>\n"
            "<a href=\"https://developer.mozilla.org\" target=\"_blank\" rel=\"noopener noreferrer\">MDN Docs</a>\n"
            "<a href=\"mailto:kabiru@example.com\">Email me</a>\n"
            "\n"
            "Example 2 — Images with proper alt text:\n"
            "<img src=\"profile.jpg\" alt=\"Kabiru Sani smiling, standing in front of a laptop\" "
            "width=\"300\" height=\"300\">\n"
            "<!-- Decorative-only image: empty alt tells screen readers to skip it -->\n"
            "<img src=\"divider-swirl.png\" alt=\"\">\n"
            "\n"
            "Example 3 — Video and audio with native controls:\n"
            "<video src=\"intro.mp4\" controls width=\"480\">\n"
            "  Your browser does not support the video tag.\n"
            "</video>\n"
            "<audio src=\"podcast-episode1.mp3\" controls></audio>\n"
        ),
        "practice": (
            "1. Create 3 links: one to another page on your own site (relative), one to an external "
            "site (absolute, opening in a new tab safely), and one mailto: link.\n"
            "2. Add 2 images: one meaningful image with descriptive alt text, and one purely decorative "
            "image with empty alt=\"\".\n"
            "3. Embed a video (or audio file) with native browser controls.\n"
            "4. Intentionally break one image's src path and observe what the alt text displays as a "
            "fallback."
        ),
        "mini_project": (
            "Mini Project: Multi-Page Photo Gallery\n"
            "Build 2 linked HTML pages: a gallery.html showing 4 images (each with proper alt text) in "
            "a grid, and a home.html that links to it. Each image should also link to a larger version "
            "of itself (or an external source) opening in a new tab."
        ),
        "real_world_project": (
            "Real-World Project: Accessibility Audit of Image Usage\n"
            "Find a real website with several images (a news site or e-commerce page works well). "
            "Inspect each image in DevTools and record its alt text (or note if it's missing). Identify "
            "at least one image that's missing meaningful alt text, and write what you WOULD have "
            "written for it. This exact type of audit is common paid work for accessibility consultants."
        ),
        "common_mistakes": (
            "- Leaving alt text empty (or omitting it entirely) on meaningful images — this makes "
            "content completely inaccessible to screen reader users and hurts SEO; only truly "
            "decorative images should have alt=\"\".\n"
            "- Writing alt text like 'image123.jpg' or 'picture' — alt text should describe what's "
            "actually depicted and relevant to the content, not just acknowledge an image exists.\n"
            "- Using target=\"_blank\" without rel=\"noopener noreferrer\" — this is a security risk "
            "(the opened page can access window.opener) and should always be paired together.\n"
            "- Not specifying width/height on <img> tags — this causes 'layout shift' as the page "
            "jumps around while images load, which hurts both user experience and Core Web Vitals "
            "scores (covered later in the Performance module)."
        ),
        "best_practices": (
            "- Write alt text as if describing the image to someone on the phone who can't see it — "
            "specific and concise, not generic.\n"
            "- Always pair target=\"_blank\" with rel=\"noopener noreferrer\" for external links.\n"
            "- Use relative paths for links/images within your own site so the whole site still works "
            "if you move it to a different domain.\n"
            "- Always specify width and height attributes on images (even if CSS will resize them) to "
            "prevent layout shift during page load."
        ),
        "interview_questions": (
            "1. Why is the alt attribute on <img> considered mandatory rather than optional, from both "
            "an accessibility and SEO perspective?\n"
            "2. What's the difference between a relative and an absolute URL, and when would you use "
            "each?\n"
            "3. What security risk does target=\"_blank\" introduce without rel=\"noopener noreferrer\", "
            "and how does that attribute fix it?\n"
            "4. Why should you specify width and height on an <img> tag even if you're going to resize "
            "it with CSS?\n"
            "5. When should an image have alt=\"\" instead of descriptive alt text?"
        ),
        "assignment": (
            "Assignment: Broken Link Checker\n"
            "Build a page with 8 links: intentionally make 2 of them point to non-existent pages/files. "
            "Manually click through all 8 and document which ones failed and why (typo, wrong relative "
            "path, wrong extension). Then fix all of them and re-verify."
        ),
        "challenge": (
            "Challenge: Fully Accessible Image Gallery\n"
            "Build an image gallery of at least 6 images where every single image has meaningful, "
            "specific alt text (no generic descriptions allowed), correct width/height attributes to "
            "prevent layout shift, and at least one image correctly marked as decorative with alt=\"\". "
            "Verify your work using a browser's built-in accessibility checker (Lighthouse in DevTools)."
        ),
        "summary": (
            "Links (<a>) connect pages via relative or absolute URLs; always pair target=\"_blank\" "
            "with rel=\"noopener noreferrer\" for security. Images (<img>) require meaningful alt text "
            "for accessibility and SEO — empty alt=\"\" is reserved for purely decorative images. "
            "Native <video> and <audio> tags provide built-in playback controls without needing "
            "external plugins. Always specify image dimensions to prevent layout shift."
        ),
        "lesson_references": (
            "- MDN Web Docs: '<a>: The Anchor element' and '<img>: The Image Embed element'\n"
            "- MDN Web Docs: 'An alt decision tree' (W3C WAI guidance on writing good alt text)\n"
            "- web.dev: 'Optimize Cumulative Layout Shift' (relevant to image dimensions)\n"
            "- MDN Web Docs: '<video>' and '<audio>' element references"
        ),
        "next_lesson_preview": (
            "Next up: Lists and Tables. You'll learn how to properly structure grouped items (ordered "
            "and unordered lists) and tabular data (tables) — two content patterns that appear "
            "constantly across real websites, from navigation menus to pricing comparisons."
        ),
        "quiz": {
            "title": "Links, Images, and Media Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Why is the alt attribute important on <img> tags?",
                    "option_a": "It's purely decorative and optional",
                    "option_b": "It's read by screen readers and shown if the image fails to load",
                    "option_c": "It only affects image file size",
                    "option_d": "It's required only for PNG images",
                    "correct_option": "b",
                    "explanation": "alt text provides accessibility for screen reader users and a fallback when images fail to load.",
                },
                {
                    "text": "What should always accompany target=\"_blank\" on a link?",
                    "option_a": "rel=\"noopener noreferrer\"",
                    "option_b": "download=\"true\"",
                    "option_c": "Nothing else is needed",
                    "option_d": "type=\"external\"",
                    "correct_option": "a",
                    "explanation": "rel=\"noopener noreferrer\" prevents the opened page from accessing window.opener, a security best practice.",
                },
                {
                    "text": "When should an image use alt=\"\" (empty alt text)?",
                    "option_a": "Never, all images need descriptive alt text",
                    "option_b": "When the image is purely decorative and adds no content meaning",
                    "option_c": "Only for background images",
                    "option_d": "When the image is very large",
                    "correct_option": "b",
                    "explanation": "Empty alt text tells screen readers to skip purely decorative images, avoiding unnecessary noise.",
                },
                {
                    "text": "Why should you specify width and height on <img> tags?",
                    "option_a": "It's required by HTML syntax",
                    "option_b": "It prevents layout shift while the image loads",
                    "option_c": "It compresses the image automatically",
                    "option_d": "It has no real effect",
                    "correct_option": "b",
                    "explanation": "Specifying dimensions lets the browser reserve space before the image loads, preventing content from jumping around.",
                },
            ],
        },
    },
    {
        "slug": "webdev-05-lists-tables",
        "title": "5. Lists and Tables",
        "level": "beginner",
        "explanation": (
            "Lists group related items. <ul> (unordered list) is for items with no meaningful order "
            "(navigation links, feature lists) — items are <li>. <ol> (ordered list) is for sequential "
            "items (steps in a recipe, rankings) and numbers automatically. <dl> (description list) "
            "pairs terms with definitions using <dt>/<dd> — less common but perfect for glossaries or "
            "FAQ pages.\n\n"
            "Tables (<table>) display genuinely tabular data — rows and columns of related data points, "
            "like a price comparison or a schedule. A table has <thead> (header row, using <th> cells) "
            "and <tbody> (data rows, using <tr> for each row and <td> for each cell). Tables should "
            "NEVER be used for page layout (that was a common 1990s-2000s hack) — that's what CSS "
            "Flexbox/Grid are for."
        ),
        "examples": (
            "Example 1 — Unordered and ordered lists:\n"
            "<ul>\n"
            "  <li>HTML</li>\n"
            "  <li>CSS</li>\n"
            "  <li>JavaScript</li>\n"
            "</ul>\n"
            "\n"
            "<ol>\n"
            "  <li>Preheat the oven</li>\n"
            "  <li>Mix the ingredients</li>\n"
            "  <li>Bake for 20 minutes</li>\n"
            "</ol>\n"
            "\n"
            "Example 2 — Description list for a glossary:\n"
            "<dl>\n"
            "  <dt>API</dt>\n"
            "  <dd>Application Programming Interface — a way for programs to communicate.</dd>\n"
            "  <dt>DOM</dt>\n"
            "  <dd>Document Object Model — the browser's in-memory representation of a page.</dd>\n"
            "</dl>\n"
            "\n"
            "Example 3 — A properly structured data table:\n"
            "<table>\n"
            "  <thead>\n"
            "    <tr><th>Course</th><th>Lessons</th><th>Level</th></tr>\n"
            "  </thead>\n"
            "  <tbody>\n"
            "    <tr><td>Python</td><td>30</td><td>Beginner-Advanced</td></tr>\n"
            "    <tr><td>SQLite</td><td>10</td><td>Beginner-Advanced</td></tr>\n"
            "  </tbody>\n"
            "</table>\n"
        ),
        "practice": (
            "1. Create an unordered list of 5 of your favorite tools/technologies.\n"
            "2. Create an ordered list explaining the steps to make your favorite meal (at least 4 "
            "steps).\n"
            "3. Build a table with at least 3 columns and 4 rows of real data (e.g. compare 3 "
            "programming languages by year created, use case, and difficulty).\n"
            "4. Add a <dl> glossary with at least 3 terms relevant to something you're currently "
            "learning."
        ),
        "mini_project": (
            "Mini Project: Course Comparison Table\n"
            "Build a page with a table comparing all 7 Kabiru AI Tutor courses (Python, SQLite, "
            "FastAPI, Linux, Git, Web Dev, AI Fundamentals) by number of lessons and difficulty level, "
            "properly using <thead>/<tbody>. Below it, add an ordered list of '5 steps to get started "
            "learning to code' and an unordered list of 'prerequisites' for the platform."
        ),
        "real_world_project": (
            "Real-World Project: Pricing Table Recreation\n"
            "Find a real SaaS product's pricing page (or use a well-known one you know) and recreate "
            "its pricing comparison as a properly structured HTML table — with clear header row, "
            "correctly grouped tbody rows, and appropriate use of <th> for both column AND row headers "
            "where relevant (using the scope attribute). Pricing tables are one of the most common "
            "real-world table use cases in web development."
        ),
        "common_mistakes": (
            "- Using tables for page layout instead of genuine tabular data — this was common decades "
            "ago but breaks on mobile, hurts accessibility, and CSS Grid/Flexbox do layout far better.\n"
            "- Forgetting <thead>/<tbody> and just throwing all <tr> rows together — screen readers and "
            "CSS styling both benefit from this structural separation.\n"
            "- Using <div> styled to look like a list instead of actual <ul>/<ol>/<li> — screen readers "
            "announce 'list with 5 items' for real lists, giving users useful context that divs don't "
            "provide.\n"
            "- Choosing <ul> when order actually matters (like ranked results or recipe steps) — if "
            "removing/reordering items would change the meaning, it should be <ol>, not <ul>."
        ),
        "best_practices": (
            "- Ask 'does the order of these items matter?' — if yes, <ol>; if no, <ul>.\n"
            "- Always structure tables with <thead> and <tbody>, and use <th> (not <td>) for header "
            "cells so screen readers can announce column context for each data cell.\n"
            "- Use the scope attribute (scope=\"col\" or scope=\"row\") on <th> elements in complex "
            "tables to make the header/data relationship unambiguous for assistive technology.\n"
            "- Never reach for a table when you actually need a layout — that's a CSS Grid/Flexbox job "
            "every time in modern web development."
        ),
        "interview_questions": (
            "1. When would you choose <ol> over <ul>, and why does that choice matter beyond visual "
            "numbering?\n"
            "2. Why is using HTML tables for page layout considered an anti-pattern in modern web "
            "development?\n"
            "3. What's the purpose of <thead> and <tbody>, and what would be lost if you just used a "
            "flat list of <tr> rows?\n"
            "4. What does the scope attribute on a <th> element do, and why does it matter for "
            "accessibility?\n"
            "5. When would you use a <dl> (description list) instead of a <ul> or <ol>?"
        ),
        "assignment": (
            "Assignment: List vs Table Judgment Call\n"
            "You're given 5 different real-world data sets (e.g. a shopping list, a class schedule with "
            "days/times/subjects, top-10 movie rankings, a recipe's ingredients, a glossary of 5 terms). "
            "For each one, decide whether it should be a <ul>, <ol>, <table>, or <dl>, and write one "
            "sentence justifying each choice."
        ),
        "challenge": (
            "Challenge: Fully Accessible Data Table\n"
            "Build a table with at least 4 columns and 6 rows of real data. Use <thead>/<tbody> "
            "correctly, apply scope attributes to all header cells, and add a <caption> element "
            "describing the table's purpose. Verify with a browser accessibility checker (Lighthouse) "
            "that the table has no accessibility warnings."
        ),
        "summary": (
            "Lists group related content: <ul> for unordered items, <ol> for sequential/ranked items, "
            "and <dl> for term-definition pairs. Tables (<table>) display genuine tabular data using "
            "<thead>/<tbody> structure with <th> header cells and <td> data cells — never for page "
            "layout, which is CSS Grid/Flexbox's job. Choosing the right structural element (not just "
            "visual appearance) keeps content accessible and meaningful."
        ),
        "lesson_references": (
            "- MDN Web Docs: 'HTML lists' guide (ul, ol, dl)\n"
            "- MDN Web Docs: '<table>: The Table element' and related table element references\n"
            "- W3C WAI: 'Tables Tutorial' (accessible table design guidance)\n"
            "- MDN Web Docs: 'scope attribute' reference for <th>"
        ),
        "next_lesson_preview": (
            "Next up: Forms and Input Elements. You'll learn how to collect user input — text fields, "
            "checkboxes, radio buttons, dropdowns, and more — the foundation of every login page, "
            "search bar, and contact form you'll ever build."
        ),
        "quiz": {
            "title": "Lists and Tables Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "When should you use <ol> instead of <ul>?",
                    "option_a": "When you want numbers instead of bullets, purely visually",
                    "option_b": "When the order of items carries meaning (steps, rankings)",
                    "option_c": "<ol> and <ul> are interchangeable always",
                    "option_d": "Only for navigation menus",
                    "correct_option": "b",
                    "explanation": "<ol> semantically indicates that item order matters, not just a visual numbering preference.",
                },
                {
                    "text": "Why should tables not be used for page layout?",
                    "option_a": "Tables render slower than divs",
                    "option_b": "It breaks accessibility and mobile responsiveness; CSS Grid/Flexbox are the correct tools",
                    "option_c": "Tables cannot contain images",
                    "option_d": "Browsers no longer support the <table> tag",
                    "correct_option": "b",
                    "explanation": "Using tables for layout is an outdated anti-pattern that hurts accessibility and responsive design.",
                },
                {
                    "text": "What is the purpose of <thead> and <tbody>?",
                    "option_a": "They have no functional purpose, purely decorative",
                    "option_b": "They structurally separate header rows from data rows for styling and accessibility",
                    "option_c": "They are required for a table to render at all",
                    "option_d": "They replace the need for <tr> tags",
                    "correct_option": "b",
                    "explanation": "This structural separation aids both CSS styling and screen reader navigation of table content.",
                },
                {
                    "text": "Which element pairs a term with its definition?",
                    "option_a": "<ul>",
                    "option_b": "<ol>",
                    "option_c": "<dl>",
                    "option_d": "<table>",
                    "correct_option": "c",
                    "explanation": "<dl> (description list) with <dt>/<dd> pairs is designed specifically for term-definition content like glossaries.",
                },
            ],
        },
    },
    {
        "slug": "webdev-06-forms-inputs",
        "title": "6. Forms and Input Elements",
        "level": "beginner",
        "explanation": (
            "Forms (<form>) collect user input and are how logins, searches, contact pages, and "
            "checkouts work. Common input types: text, email, password, number, checkbox, radio, and "
            "the versatile <select> dropdown. Every input needs an associated <label> — either "
            "wrapping the input or linked via label's for=\"id\" matching the input's id — this is "
            "critical for accessibility (screen readers announce the label) and usability (clicking "
            "the label focuses the input). The action attribute defines where form data is sent, and "
            "method defines how (GET appends data to the URL, POST sends it in the request body)."
        ),
        "examples": (
            "Example 1 — A labeled login form:\n"
            "<form action=\"/login\" method=\"POST\">\n"
            "  <label for=\"email\">Email</label>\n"
            "  <input type=\"email\" id=\"email\" name=\"email\" required>\n"
            "\n"
            "  <label for=\"password\">Password</label>\n"
            "  <input type=\"password\" id=\"password\" name=\"password\" required minlength=\"6\">\n"
            "\n"
            "  <button type=\"submit\">Log In</button>\n"
            "</form>\n"
            "\n"
            "Example 2 — Checkboxes, radio buttons, and select:\n"
            "<label><input type=\"checkbox\" name=\"subscribe\"> Subscribe to newsletter</label>\n"
            "\n"
            "<p>Preferred language:</p>\n"
            "<label><input type=\"radio\" name=\"lang\" value=\"en\"> English</label>\n"
            "<label><input type=\"radio\" name=\"lang\" value=\"ha\"> Hausa</label>\n"
            "\n"
            "<label for=\"course\">Course</label>\n"
            "<select id=\"course\" name=\"course\">\n"
            "  <option value=\"python\">Python</option>\n"
            "  <option value=\"fastapi\">FastAPI</option>\n"
            "</select>\n"
        ),
        "practice": (
            "1. Build a registration form with fields for name (text), email, password, and age "
            "(number), each with a properly linked <label>.\n"
            "2. Add a checkbox for 'I agree to the terms' marked required.\n"
            "3. Add a <select> dropdown with at least 4 options.\n"
            "4. Test tabbing through your form using only the keyboard (Tab key) and confirm every "
            "field is reachable in a logical order."
        ),
        "mini_project": (
            "Mini Project: Course Feedback Form\n"
            "Build a form collecting: student name (text), email, a rating (radio buttons 1-5), a "
            "dropdown of which course they took, a checkbox for 'recommend to a friend', and a "
            "textarea for comments. Every field must have a properly associated label."
        ),
        "real_world_project": (
            "Real-World Project: Sign-Up Form Recreation\n"
            "Find a real website's sign-up form (any SaaS product, or use Kabiru AI Tutor's own "
            "Register page as reference). Recreate its field structure in plain HTML, matching input "
            "types, required attributes, and validation constraints (minlength, pattern, etc.) as "
            "closely as you can infer from testing the real form's behavior."
        ),
        "common_mistakes": (
            "- Placeholder text used AS a label (no actual <label> element) — placeholder text "
            "disappears once the user starts typing, leaving no accessible label; it should only "
            "supplement a real label, never replace it.\n"
            "- Forgetting the name attribute on inputs — without it, the field's value is not included "
            "when the form is submitted, silently losing data.\n"
            "- Using <div onclick> instead of a real <button> or <input type=\"submit\"> — buttons get "
            "keyboard accessibility (Enter/Space activation) and semantic meaning for free; divs do not.\n"
            "- Not using type=\"email\" or type=\"number\" for appropriate fields — these give free "
            "browser-level validation and better mobile keyboards (numeric keypad for number inputs)."
        ),
        "best_practices": (
            "- Always pair every input with a real <label>, either wrapping it or linked via "
            "for/id.\n"
            "- Use the most specific input type available (email, tel, number, date) rather than "
            "defaulting everything to type=\"text\".\n"
            "- Use the required attribute for mandatory fields, and add helpful constraints (minlength, "
            "pattern) so the browser can catch obvious errors before submission.\n"
            "- Group related radio buttons/checkboxes with <fieldset> and <legend> when there are "
            "multiple related groups on one form, for clearer screen reader announcements."
        ),
        "interview_questions": (
            "1. Why is a real <label> element important even if placeholder text looks similar "
            "visually?\n"
            "2. What's the difference between GET and POST as a form's method, and when would you "
            "choose each?\n"
            "3. Why would you use type=\"email\" instead of type=\"text\" for an email field?\n"
            "4. What happens to a form field's value on submission if it's missing a name attribute?\n"
            "5. What is <fieldset>/<legend> for, and when should you use it?"
        ),
        "assignment": (
            "Assignment: Form Type Selection\n"
            "You're given 6 form field requirements (a phone number, a birthdate, a satisfaction "
            "rating 1-5, a yes/no agreement, a country selection from 190+ options, and a short bio). "
            "For each, choose the most appropriate HTML input type/element and justify your choice in "
            "one sentence."
        ),
        "challenge": (
            "Challenge: Fully Keyboard-Navigable Form\n"
            "Build a 6-field form (mixing text, radio, checkbox, and select) and verify it can be "
            "completely filled out and submitted using ONLY the keyboard — Tab to move between "
            "fields, Space/Enter to activate checkboxes/radios/submit — with a visible focus indicator "
            "on every field."
        ),
        "summary": (
            "Forms collect user input via <input> (with types like text, email, password, checkbox, "
            "radio), <select> dropdowns, and <textarea>. Every field needs an associated <label> for "
            "accessibility and usability. The name attribute is required for a field's value to be "
            "submitted, and choosing specific input types (email, number) provides free browser "
            "validation and better mobile keyboards."
        ),
        "lesson_references": (
            "- MDN Web Docs: 'Your first HTML form' and 'How to structure a web form'\n"
            "- MDN Web Docs: '<input>: The Input element' (full type reference)\n"
            "- web.dev: 'Learn Forms' course\n"
            "- W3C WAI: 'Forms Tutorial' (accessible form design)"
        ),
        "next_lesson_preview": (
            "Next up: HTML5 Semantic Elements and Accessibility Basics. You'll consolidate everything "
            "learned so far into a deeper look at web accessibility (a11y) — ARIA basics, keyboard "
            "navigation, and how to test your pages the way real accessibility audits do."
        ),
        "quiz": {
            "title": "Forms and Input Elements Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Why is a <label> important for form accessibility?",
                    "option_a": "It's purely decorative",
                    "option_b": "Screen readers announce it and clicking it focuses the associated input",
                    "option_c": "It has no functional purpose",
                    "option_d": "It only matters for checkboxes",
                    "correct_option": "b",
                    "explanation": "Labels provide accessible names for inputs and improve click/tap target usability.",
                },
                {
                    "text": "What happens if an input is missing a name attribute?",
                    "option_a": "The form won't render",
                    "option_b": "Its value is not included when the form is submitted",
                    "option_c": "It becomes read-only",
                    "option_d": "Nothing changes",
                    "correct_option": "b",
                    "explanation": "The name attribute is the key used to submit that field's value; without it, the value is lost.",
                },
                {
                    "text": "Why use type=\"email\" instead of type=\"text\" for an email field?",
                    "option_a": "It provides built-in format validation and a better mobile keyboard",
                    "option_b": "It's purely a visual difference",
                    "option_c": "type=\"text\" doesn't work for email addresses",
                    "option_d": "There is no difference",
                    "correct_option": "a",
                    "explanation": "Specific input types give free browser-level validation and optimized on-screen keyboards.",
                },
                {
                    "text": "What does <fieldset>/<legend> help with?",
                    "option_a": "Styling only",
                    "option_b": "Grouping related fields with a clear label for screen readers",
                    "option_c": "Form submission speed",
                    "option_d": "It's deprecated and should not be used",
                    "correct_option": "b",
                    "explanation": "fieldset/legend groups related inputs (like a radio button set) with an announced group label.",
                },
            ],
        },
    },
    {
        "slug": "webdev-07-semantic-accessibility",
        "title": "7. HTML5 Semantic Elements and Accessibility Basics",
        "level": "beginner",
        "explanation": (
            "Accessibility (often abbreviated a11y) means building sites usable by everyone, including "
            "people using screen readers, keyboard-only navigation, or assistive devices. Semantic "
            "HTML (covered in lesson 2) is the FIRST and most important accessibility tool — but "
            "sometimes you need ARIA (Accessible Rich Internet Applications) attributes to add meaning "
            "HTML can't express alone, like aria-label for icon-only buttons or aria-expanded for "
            "collapsible menus. The golden rule: 'No ARIA is better than bad ARIA' — always prefer a "
            "real semantic HTML element over an ARIA-patched generic one."
        ),
        "examples": (
            "Example 1 — Icon-only button needing an accessible name:\n"
            "<button aria-label=\"Close menu\">\n"
            "  <svg>...</svg> <!-- just an X icon, no visible text -->\n"
            "</button>\n"
            "\n"
            "Example 2 — Skip link for keyboard users (a real accessibility best practice):\n"
            "<a href=\"#main-content\" class=\"skip-link\">Skip to main content</a>\n"
            "...\n"
            "<main id=\"main-content\">...</main>\n"
            "\n"
            "Example 3 — Expandable section with ARIA state:\n"
            "<button aria-expanded=\"false\" aria-controls=\"faq-answer-1\">\n"
            "  What is Kabiru AI Tutor?\n"
            "</button>\n"
            "<div id=\"faq-answer-1\" hidden>\n"
            "  An offline-first AI tutoring platform.\n"
            "</div>\n"
        ),
        "practice": (
            "1. Add a 'Skip to main content' link as the very first focusable element on a page.\n"
            "2. Build an icon-only button (can just be a unicode symbol like X) and give it an "
            "accessible name with aria-label.\n"
            "3. Use your browser's built-in screen reader (or DevTools Accessibility panel) to inspect "
            "the accessible name of 3 different elements on a real website.\n"
            "4. Tab through a real website using only the keyboard and note anything that seems "
            "unreachable or confusing."
        ),
        "mini_project": (
            "Mini Project: Accessible FAQ Accordion Structure\n"
            "Build the HTML (no JavaScript needed yet — that comes later) for an FAQ page with 4 "
            "questions, each using a <button> with aria-expanded and aria-controls pointing to its "
            "answer, plus a working skip link at the top of the page."
        ),
        "real_world_project": (
            "Real-World Project: Accessibility Audit Report\n"
            "Run a Lighthouse Accessibility audit (built into Chrome DevTools) on 2 real websites. "
            "Document the score and the top 3 issues flagged for each site. Explain, in your own words, "
            "why each flagged issue matters for a real user with a disability. This is genuine "
            "professional work — accessibility audits are commonly requested client deliverables."
        ),
        "common_mistakes": (
            "- Adding ARIA roles/attributes to elements that already have correct native semantics — "
            "e.g. role=\"button\" on an actual <button> is redundant and can sometimes cause "
            "double-announcements.\n"
            "- Using aria-label on elements that already have clear visible text — this OVERRIDES the "
            "visible text for screen readers, which can create a confusing mismatch between what's "
            "seen and what's heard.\n"
            "- Hiding content with CSS (display: none via a class) but forgetting it's also invisible "
            "to screen readers when you actually wanted it announced but visually hidden — for that "
            "case, use a proper 'visually-hidden' CSS technique instead.\n"
            "- Relying on color alone to convey information (like 'red text means error') — this fails "
            "for colorblind users; always pair color with an icon, text label, or other indicator."
        ),
        "best_practices": (
            "- Prefer real semantic HTML elements over ARIA-patched divs whenever possible — a real "
            "<button> is always better than <div role=\"button\">.\n"
            "- Always test keyboard navigation (Tab, Shift+Tab, Enter, Space) on every interactive "
            "component you build.\n"
            "- Provide a skip link as the first focusable element on every page with a navigation "
            "menu.\n"
            "- Run Lighthouse or axe DevTools accessibility checks regularly during development, not "
            "just as an afterthought before launch."
        ),
        "interview_questions": (
            "1. What does the phrase 'No ARIA is better than bad ARIA' mean in practice?\n"
            "2. What is a skip link, and why does it matter for keyboard users?\n"
            "3. When would you use aria-label versus relying on visible text content?\n"
            "4. Why is relying on color alone to convey meaning considered an accessibility failure?\n"
            "5. What tools would you use to audit a real website's accessibility, and what would you "
            "check first?"
        ),
        "assignment": (
            "Assignment: Keyboard-Only Navigation Test\n"
            "Pick any real website with a navigation menu and at least one form. Unplug your mouse (or "
            "simply don't use it) and navigate the entire page using only Tab, Shift+Tab, Enter, and "
            "Space. Document every point where you got stuck, lost track of focus, or couldn't "
            "complete an action."
        ),
        "challenge": (
            "Challenge: Zero Lighthouse Accessibility Warnings\n"
            "Take your Course Feedback Form mini project from lesson 6 and refine it until it scores "
            "100 on Chrome DevTools' Lighthouse Accessibility audit, with zero warnings. Document what "
            "you had to change to get there."
        ),
        "summary": (
            "Accessibility (a11y) ensures websites work for everyone, including keyboard-only and "
            "screen reader users. Semantic HTML is the foundation; ARIA attributes (aria-label, "
            "aria-expanded, aria-controls) fill gaps HTML can't express alone — but should never "
            "replace real semantic elements when one exists. Skip links, keyboard navigation testing, "
            "and avoiding color-only meaning are practical, testable accessibility practices."
        ),
        "lesson_references": (
            "- MDN Web Docs: 'Accessibility' guide (developer.mozilla.org/en-US/docs/Web/Accessibility)\n"
            "- W3C WAI-ARIA Authoring Practices Guide (APG)\n"
            "- 'The First Rule of ARIA Use' (W3C ARIA specification)\n"
            "- Google web.dev: 'Learn Accessibility' course"
        ),
        "next_lesson_preview": (
            "Next up: HTML Best Practices and SEO Basics — the final lesson of Module 1. You'll learn "
            "how search engines read your pages and the concrete HTML practices that improve "
            "discoverability, wrapping up everything you've learned about structuring a page well."
        ),
        "quiz": {
            "title": "Semantic Elements and Accessibility Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does the golden rule 'No ARIA is better than bad ARIA' mean?",
                    "option_a": "Never use ARIA under any circumstances",
                    "option_b": "Prefer real semantic HTML elements over incorrectly-applied ARIA patches",
                    "option_c": "ARIA should be used on every element",
                    "option_d": "ARIA is only for advanced developers",
                    "correct_option": "b",
                    "explanation": "Incorrect ARIA can actively harm accessibility; a correct native element is always preferred.",
                },
                {
                    "text": "What is the purpose of a 'skip link'?",
                    "option_a": "To skip loading images",
                    "option_b": "To let keyboard users jump directly to the main content, bypassing repeated navigation",
                    "option_c": "To skip form validation",
                    "option_d": "It has no real purpose",
                    "correct_option": "b",
                    "explanation": "Skip links save keyboard/screen reader users from tabbing through the same navigation on every page.",
                },
                {
                    "text": "Why is relying on color alone to convey information problematic?",
                    "option_a": "It's not a real problem",
                    "option_b": "It fails for colorblind users who can't perceive the color difference",
                    "option_c": "Colors are not supported in HTML",
                    "option_d": "It only affects print stylesheets",
                    "correct_option": "b",
                    "explanation": "Color-only cues exclude colorblind users; pairing color with text/icons ensures the information is universally accessible.",
                },
                {
                    "text": "What does aria-expanded communicate on a button?",
                    "option_a": "The button's color",
                    "option_b": "Whether the content it controls is currently expanded or collapsed",
                    "option_c": "The button's font size",
                    "option_d": "Nothing meaningful",
                    "correct_option": "b",
                    "explanation": "aria-expanded tells assistive technology the current open/closed state of a collapsible element.",
                },
            ],
        },
    },
    {
        "slug": "webdev-08-html-best-practices-seo",
        "title": "8. HTML Best Practices and SEO Basics",
        "level": "beginner",
        "explanation": (
            "SEO (Search Engine Optimization) is how search engines find, understand, and rank your "
            "pages. Good HTML structure IS good SEO — semantic tags, proper heading hierarchy, and "
            "descriptive alt text (all covered in previous lessons) directly help search engines "
            "understand your content. Beyond structure, key SEO-relevant tags include: <title> (shown "
            "in search results and browser tabs), <meta name=\"description\"> (the snippet shown under "
            "your title in search results), and canonical URLs (<link rel=\"canonical\">) which tell "
            "search engines the 'official' version of a page when duplicate content might exist."
        ),
        "examples": (
            "Example 1 — SEO-relevant <head> tags:\n"
            "<head>\n"
            "  <title>Kabiru AI Tutor — Learn Python, FastAPI, and More Offline</title>\n"
            "  <meta name=\"description\" content=\"An offline-first AI tutoring platform teaching "
            "Python, SQLite, FastAPI, Linux, and Git from beginner to expert.\">\n"
            "  <link rel=\"canonical\" href=\"https://kabiru-ai-tutor.example.com/\">\n"
            "</head>\n"
            "\n"
            "Example 2 — Open Graph tags for social media previews:\n"
            "<meta property=\"og:title\" content=\"Kabiru AI Tutor\">\n"
            "<meta property=\"og:description\" content=\"Learn to code, fully offline.\">\n"
            "<meta property=\"og:image\" content=\"https://example.com/preview.png\">\n"
            "\n"
            "Example 3 — A well-structured, crawlable heading hierarchy:\n"
            "<h1>Kabiru AI Tutor</h1>\n"
            "  <h2>Courses</h2>\n"
            "    <h3>Python Programming</h3>\n"
            "    <h3>Web Development</h3>\n"
            "  <h2>Features</h2>\n"
        ),
        "practice": (
            "1. Write a unique, descriptive <title> and <meta name=\"description\"> for a page about "
            "yourself.\n"
            "2. Add Open Graph tags so your page would show a nice preview if shared on social media.\n"
            "3. Audit a page you've already built (from an earlier lesson) and fix any heading "
            "hierarchy issues.\n"
            "4. Use Chrome DevTools' Lighthouse to run an SEO audit on any real website and note its "
            "score and top suggestions."
        ),
        "mini_project": (
            "Mini Project: SEO-Optimized Landing Page\n"
            "Take your Personal Bio Page from Lesson 1 and add a complete, professional <head>: unique "
            "title, meta description, Open Graph tags, a canonical link, and a properly nested heading "
            "hierarchy throughout the body. Run it through Lighthouse and aim for a 100 SEO score."
        ),
        "real_world_project": (
            "Real-World Project: Local Business SEO Audit\n"
            "Find a real small local business website. Check its <title>, meta description, heading "
            "structure, and image alt text using View Source or DevTools. Write a short SEO "
            "improvement report identifying 3 specific fixes that would help the business rank better "
            "in local search results — a genuinely billable freelance service."
        ),
        "common_mistakes": (
            "- Using the exact same <title> and meta description on every page of a site — each page "
            "should have unique, specific values describing that page's actual content.\n"
            "- Writing a meta description that's just keyword-stuffed rather than a natural, compelling "
            "summary a human would want to click on — search engines increasingly penalize "
            "keyword-stuffing.\n"
            "- Skipping heading levels (h1 straight to h3) purely for visual sizing — this confuses "
            "both screen readers and search engine crawlers about your content's actual structure.\n"
            "- Forgetting alt text on images (from lesson 4) — this isn't just an accessibility miss, "
            "it's also a missed SEO opportunity since search engines can't 'see' images."
        ),
        "best_practices": (
            "- Write a unique <title> (50-60 characters ideally) and meta description (150-160 "
            "characters) for every page.\n"
            "- Structure headings as a genuine outline (one h1, logical h2/h3 nesting) — this serves "
            "BOTH accessibility and SEO simultaneously, since they rely on the same signal.\n"
            "- Always include a canonical link when the same content might be reachable via multiple "
            "URLs, to avoid 'duplicate content' SEO penalties.\n"
            "- Treat semantic HTML, accessibility, and SEO as the SAME underlying skill — well-"
            "structured, meaningful HTML serves all three goals at once."
        ),
        "interview_questions": (
            "1. Explain the relationship between semantic HTML, accessibility, and SEO — why do good "
            "practices in one area usually help the others?\n"
            "2. What's the difference between <title> and <meta name=\"description\">, and where does "
            "each appear to users?\n"
            "3. What is a canonical URL, and when would you need one?\n"
            "4. Why would keyword-stuffing a meta description actually hurt your SEO rather than help "
            "it?\n"
            "5. How would you audit a page's SEO fundamentals without any paid tools?"
        ),
        "assignment": (
            "Assignment: Title and Description Rewrite\n"
            "Find 3 real pages with poor or missing <title>/meta description tags (view-source on any "
            "site you suspect). Rewrite better versions for each — unique, descriptive, appropriately "
            "sized, and genuinely useful to someone scanning search results."
        ),
        "challenge": (
            "Challenge: Module 1 Capstone — Fully Optimized Multi-Page Site\n"
            "Combine everything from Module 1: build a 3-page site (home, about, contact form) with "
            "full semantic structure, accessible forms, proper images with alt text, complete SEO meta "
            "tags on every page, and zero Lighthouse warnings across Accessibility, SEO, and Best "
            "Practices categories. This capstone proves mastery of HTML Foundations."
        ),
        "summary": (
            "Good SEO starts with good HTML: unique <title> and meta description tags per page, "
            "logical heading hierarchy, descriptive alt text, and canonical URLs when needed. "
            "Semantic HTML, accessibility, and SEO reinforce each other — the same well-structured "
            "markup that helps screen reader users also helps search engines understand and rank your "
            "content. This completes Module 1: HTML Foundations."
        ),
        "lesson_references": (
            "- Google Search Central: 'SEO Starter Guide'\n"
            "- MDN Web Docs: 'What's in the head? Metadata in HTML'\n"
            "- Open Graph Protocol official specification (ogp.me)\n"
            "- web.dev: 'Learn SEO' course"
        ),
        "next_lesson_preview": (
            "You've completed Module 1: HTML Foundations! Next up: Module 2 begins with CSS Syntax, "
            "Selectors, and the Cascade — where you'll go deep into how CSS actually decides which "
            "styles win when multiple rules could apply to the same element."
        ),
        "quiz": {
            "title": "HTML Best Practices and SEO Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does the <meta name=\"description\"> tag control?",
                    "option_a": "The page's main heading",
                    "option_b": "The snippet text shown under the title in search engine results",
                    "option_c": "The page's background color",
                    "option_d": "The browser tab icon",
                    "correct_option": "b",
                    "explanation": "The meta description provides the summary text search engines often display in results.",
                },
                {
                    "text": "Why does good heading hierarchy help SEO as well as accessibility?",
                    "option_a": "It doesn't affect SEO at all",
                    "option_b": "Search engines use heading structure to understand content organization, the same way screen readers do",
                    "option_c": "Headings only affect page load speed",
                    "option_d": "SEO ignores HTML structure entirely",
                    "correct_option": "b",
                    "explanation": "Both search engines and assistive technology rely on the same structural signal: a logical heading outline.",
                },
                {
                    "text": "What problem does a canonical URL solve?",
                    "option_a": "It speeds up page loading",
                    "option_b": "It tells search engines which URL is the 'official' version when duplicate content exists",
                    "option_c": "It encrypts the page",
                    "option_d": "It has no practical purpose",
                    "correct_option": "b",
                    "explanation": "Canonical links prevent duplicate-content SEO penalties when the same content is reachable via multiple URLs.",
                },
                {
                    "text": "Why might keyword-stuffing a meta description hurt rather than help SEO?",
                    "option_a": "It's technically impossible to do",
                    "option_b": "Search engines increasingly penalize unnatural, spammy text over genuine, compelling summaries",
                    "option_c": "Meta descriptions don't affect ranking at all",
                    "option_d": "It always improves ranking regardless",
                    "correct_option": "b",
                    "explanation": "Modern search engines favor natural, useful descriptions over keyword-stuffed spam.",
                },
            ],
        },
    },
    {
        "slug": "webdev-09-css-syntax-selectors-cascade",
        "title": "9. CSS Syntax, Selectors, and the Cascade",
        "level": "beginner",
        "explanation": (
            "CSS rules follow the pattern: selector { property: value; }. Beyond basic tag/class/id "
            "selectors (lesson 2), CSS offers combinators: descendant (space), child (>), adjacent "
            "sibling (+), and attribute selectors ([type=\"text\"]). The 'Cascade' in Cascading Style "
            "Sheets refers to how conflicting rules are resolved when multiple selectors match the "
            "same element, based on three factors in order: (1) importance (!important overrides "
            "everything, use sparingly), (2) specificity (id beats class beats tag), and (3) source "
            "order (later rules win ties). Understanding specificity is the #1 skill for debugging "
            "'why isn\'t my CSS working' situations."
        ),
        "examples": (
            "Example 1 -- Combinators:\n"
            ".card p { color: gray; }         /* any <p> INSIDE .card, any depth */\n"
            ".card > p { color: gray; }       /* only direct <p> children of .card */\n"
            "h2 + p { margin-top: 0; }        /* a <p> immediately after an <h2> */\n"
            "input[type=\"email\"] { border-color: blue; }  /* attribute selector */\n"
            "\n"
            "Example 2 -- Specificity in action:\n"
            "p { color: black; }              /* specificity: 0-0-1 (tag) */\n"
            ".highlight { color: blue; }      /* specificity: 0-1-0 (class) -- wins over tag */\n"
            "#warning { color: red; }         /* specificity: 1-0-0 (id) -- wins over class */\n"
            "\n"
            "Example 3 -- Source order tiebreaker (equal specificity, last one wins):\n"
            ".text { color: green; }\n"
            ".text { color: purple; }         /* this wins -- same specificity, comes later */\n"
        ),
        "practice": (
            "1. Write a descendant selector and a child selector that target different elements, and "
            "explain the difference in your own words.\n"
            "2. Create 3 conflicting rules with different specificity (tag, class, id) targeting the "
            "same element and predict which one wins before testing.\n"
            "3. Use an attribute selector to style all required form inputs differently.\n"
            "4. Deliberately create a specificity conflict, then fix it WITHOUT using !important."
        ),
        "mini_project": (
            "Mini Project: Specificity Debugging Exercise\n"
            "Given a provided HTML snippet and 5 conflicting CSS rules of varying specificity, "
            "determine on paper which rule wins for each element, then verify in the browser using "
            "DevTools' computed styles panel (which shows exactly which rule won and why)."
        ),
        "real_world_project": (
            "Real-World Project: Legacy CSS Cleanup\n"
            "Find a CSS file from any open-source project (or write a deliberately messy one yourself "
            "with 10+ rules and inconsistent specificity/!important usage). Refactor it to remove all "
            "!important flags by fixing the underlying specificity issues instead -- a very real task "
            "in professional CSS maintenance work."
        ),
        "common_mistakes": (
            "- Reaching for !important to 'just make it work' instead of understanding WHY a rule "
            "isn\'t applying -- this creates a cascade of future !important flags fighting each "
            "other.\n"
            "- Over-relying on ID selectors for styling -- IDs have very high specificity, making "
            "future overrides difficult; prefer classes for styling, reserve IDs for JS hooks/anchors.\n"
            "- Not understanding that inline styles (style=\"...\") beat almost all CSS file rules "
            "due to extremely high specificity, causing confusing 'my CSS file isn\'t working' bugs.\n"
            "- Writing overly specific selector chains (.page .content .card .title) that make future "
            "styling fragile and hard to override intentionally."
        ),
        "best_practices": (
            "- Prefer classes over IDs for styling; keep specificity as flat and low as possible "
            "across your whole stylesheet.\n"
            "- Avoid !important except as a last resort (or for legitimate utility classes in a "
            "deliberate system); if you need it often, your specificity architecture needs rethinking.\n"
            "- Use DevTools' computed styles / 'Styles' panel to debug cascade conflicts -- it shows "
            "every matching rule and which one won, with a strikethrough on overridden ones.\n"
            "- Keep selectors as short and flat as reasonably possible for maintainability."
        ),
        "interview_questions": (
            "1. Explain CSS specificity and how it's calculated when multiple selectors match the "
            "same element.\n"
            "2. Why is !important generally considered a last resort in professional CSS?\n"
            "3. What's the difference between a descendant selector and a child selector?\n"
            "4. Why do inline styles typically override external stylesheet rules?\n"
            "5. How would you debug a situation where a CSS rule you wrote 'isn\'t working'?"
        ),
        "assignment": (
            "Assignment: Specificity Calculator\n"
            "Given 8 different CSS selectors of varying complexity (tag, class, id, combinators, "
            "attribute selectors), manually calculate the specificity of each (in id-class-tag "
            "notation) without using any tool, then verify your answers using DevTools."
        ),
        "challenge": (
            "Challenge: Zero !important Stylesheet\n"
            "Take any CSS file you've written so far in this course (or write a new 60+ line one) and "
            "ensure it contains ZERO !important flags while still achieving all intended visual "
            "results, using only correct specificity and source-order management."
        ),
        "summary": (
            "CSS rules are matched to elements by selectors, and conflicts are resolved by the "
            "cascade: importance (!important) first, then specificity (id > class > tag), then "
            "source order as a tiebreaker. Combinators (space, >, +) and attribute selectors ([attr]) "
            "extend basic selection. Mastering specificity is the key skill for debugging CSS "
            "conflicts without resorting to !important."
        ),
        "lesson_references": (
            "- MDN Web Docs: 'CSS selectors' and 'Specificity' guides\n"
            "- MDN Web Docs: 'Cascade, specificity, and inheritance'\n"
            "- CSS-Tricks: 'Specifics on CSS Specificity'\n"
            "- web.dev: 'Learn CSS - The Cascade' module"
        ),
        "next_lesson_preview": (
            "Next up: The Box Model. You'll learn how every single HTML element is really a "
            "rectangular box made of content, padding, border, and margin -- the single most "
            "important mental model for understanding CSS layout and spacing."
        ),
        "quiz": {
            "title": "CSS Syntax, Selectors, and Cascade Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Which selector has higher specificity: a class selector or an id selector?",
                    "option_a": "Class selector",
                    "option_b": "ID selector",
                    "option_c": "They are equal",
                    "option_d": "Depends on source order only",
                    "correct_option": "b",
                    "explanation": "ID selectors have higher specificity than class selectors in the CSS cascade.",
                },
                {
                    "text": "What does the child combinator (>) select?",
                    "option_a": "All descendants at any depth",
                    "option_b": "Only direct children of the specified element",
                    "option_c": "The element immediately following",
                    "option_d": "Elements with a specific attribute",
                    "correct_option": "b",
                    "explanation": "The > combinator matches only direct children, not deeper-nested descendants.",
                },
                {
                    "text": "When two rules have equal specificity, which one applies?",
                    "option_a": "The first one written",
                    "option_b": "The one that appears later in source order",
                    "option_c": "Neither applies",
                    "option_d": "Both apply simultaneously, merged",
                    "correct_option": "b",
                    "explanation": "Source order is the tiebreaker when specificity is equal -- the later rule wins.",
                },
                {
                    "text": "Why is !important generally discouraged in professional CSS?",
                    "option_a": "It's slower to parse",
                    "option_b": "It breaks the normal cascade and makes future overrides difficult",
                    "option_c": "It's not supported in modern browsers",
                    "option_d": "It only works with class selectors",
                    "correct_option": "b",
                    "explanation": "!important overrides normal specificity rules, often leading to a cascade of competing !important flags.",
                },
            ],
        },
    },
    {
        "slug": "webdev-10-box-model",
        "title": "10. The Box Model",
        "level": "beginner",
        "explanation": (
            "Every HTML element is rendered as a rectangular box made of four layers, from inside "
            "out: content (the actual text/image), padding (space inside the border, around the "
            "content), border (a visible or invisible line around the padding), and margin (space "
            "outside the border, separating it from other elements). By default, width/height apply "
            "only to the content box -- padding and border ADD to the element's total rendered size "
            "(content-box model). Setting box-sizing: border-box changes this so width/height include "
            "padding and border, making sizing far more predictable -- most professional stylesheets "
            "apply border-box globally."
        ),
        "examples": (
            "Example 1 -- Default content-box behavior (surprising sizing):\n"
            ".box {\n"
            "  width: 200px;\n"
            "  padding: 20px;\n"
            "  border: 5px solid black;\n"
            "  /* Actual rendered width: 200 + 20+20 (padding) + 5+5 (border) = 250px! */\n"
            "}\n"
            "\n"
            "Example 2 -- border-box fixes this (the professional default):\n"
            "* {\n"
            "  box-sizing: border-box;\n"
            "}\n"
            ".box {\n"
            "  width: 200px;   /* now the TOTAL rendered width is exactly 200px */\n"
            "  padding: 20px;\n"
            "  border: 5px solid black;\n"
            "}\n"
            "\n"
            "Example 3 -- Margin collapsing (a common surprise between vertical margins):\n"
            "p { margin-bottom: 20px; }\n"
            "h2 { margin-top: 30px; }\n"
            "/* Between a <p> and following <h2>, the gap is 30px (the LARGER margin), not 50px */\n"
        ),
        "practice": (
            "1. Build a box with width, padding, and border, then use DevTools' box model diagram to "
            "see the actual computed size.\n"
            "2. Add box-sizing: border-box and observe how the rendered size changes.\n"
            "3. Create two stacked paragraphs with different top/bottom margins and observe margin "
            "collapsing in DevTools.\n"
            "4. Build a card component with distinct content, padding, border, and margin, labeling "
            "each visually with different background colors for content vs padding."
        ),
        "mini_project": (
            "Mini Project: Box Model Visualizer Page\n"
            "Build a page with 4 boxes, each demonstrating one box model concept clearly: (1) default "
            "content-box sizing surprise, (2) border-box fixing it, (3) margin collapsing between two "
            "stacked elements, (4) a box with all 4 layers (content/padding/border/margin) visually "
            "distinguished with different background colors."
        ),
        "real_world_project": (
            "Real-World Project: Global Reset Stylesheet\n"
            "Write a small, professional-grade CSS reset file (5-10 rules) that at minimum sets "
            "box-sizing: border-box globally, removes default margin/padding inconsistencies across "
            "browsers, and sets sensible defaults. This exact pattern (a 'CSS reset' or 'normalize') "
            "is used at the start of nearly every real production stylesheet."
        ),
        "common_mistakes": (
            "- Forgetting that padding/border ADD to width in the default content-box model, causing "
            "layouts to overflow their intended container unexpectedly.\n"
            "- Being surprised by margin collapsing between vertically stacked elements and adding "
            "extra hacky spacing to compensate, instead of understanding and working with the "
            "behavior.\n"
            "- Not setting box-sizing: border-box globally at the start of a project, leading to "
            "constant width-calculation surprises throughout development.\n"
            "- Confusing padding and margin -- padding is INSIDE the border (affects background "
            "color area), margin is OUTSIDE the border (transparent, separates from other elements)."
        ),
        "best_practices": (
            "- Set box-sizing: border-box on * (or html, and inherit on all) at the very start of "
            "every project's stylesheet.\n"
            "- Use DevTools' box model diagram constantly during layout debugging -- it visually shows "
            "content/padding/border/margin sizes for the selected element.\n"
            "- Understand margin collapsing rather than fighting it with excessive padding as a "
            "workaround.\n"
            "- Use padding for space INSIDE a component's visual boundary, and margin for space "
            "BETWEEN components."
        ),
        "interview_questions": (
            "1. Explain the box model: what are the four layers of every HTML element, from inside "
            "out?\n"
            "2. What's the difference between content-box and border-box sizing, and why do most "
            "professionals set border-box globally?\n"
            "3. What is margin collapsing, and when does it occur?\n"
            "4. What's the practical difference between when you'd use padding versus margin?\n"
            "5. If a box has width: 200px, padding: 10px, and border: 2px solid black under the "
            "default box-sizing, what is its actual rendered width?"
        ),
        "assignment": (
            "Assignment: Box Model Math\n"
            "Given 5 different box configurations (varying width, padding, border values) under "
            "default content-box sizing, manually calculate the actual rendered width for each "
            "WITHOUT using DevTools, then verify your answers in the browser."
        ),
        "challenge": (
            "Challenge: Module 2 Foundation -- Consistent Card Grid\n"
            "Build a grid of 6 'cards' with identical dimensions despite having different amounts of "
            "text content in each, using border-box sizing and consistent padding/margin -- a pattern "
            "you'll use constantly in real UI work (product cards, course cards, blog post previews)."
        ),
        "summary": (
            "Every element is a box: content, padding, border, and margin, from inside out. Default "
            "content-box sizing means padding/border ADD to the specified width/height; border-box "
            "sizing (recommended globally) makes width/height represent the TOTAL rendered size "
            "instead, which is far more predictable. Vertical margins between elements can 'collapse' "
            "to the larger of the two values rather than summing."
        ),
        "lesson_references": (
            "- MDN Web Docs: 'The box model' guide\n"
            "- MDN Web Docs: 'box-sizing' property reference\n"
            "- MDN Web Docs: 'Mastering margin collapsing'\n"
            "- CSS-Tricks: 'Box Sizing' almanac entry"
        ),
        "next_lesson_preview": (
            "Next up: Colors, Units, and Typography. You'll learn the different ways to specify "
            "colors and sizes in CSS (px, rem, %, and more), plus the fundamentals of styling text "
            "for readability and visual hierarchy."
        ),
        "quiz": {
            "title": "The Box Model Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What are the four layers of the CSS box model, from inside to outside?",
                    "option_a": "Content, padding, border, margin",
                    "option_b": "Margin, border, padding, content",
                    "option_c": "Content, border, padding, margin",
                    "option_d": "Padding, content, margin, border",
                    "correct_option": "a",
                    "explanation": "From the inside out: content, then padding, then border, then margin.",
                },
                {
                    "text": "Under default content-box sizing, does padding add to an element's specified width?",
                    "option_a": "No, width always represents the total size",
                    "option_b": "Yes, padding and border add to the specified width",
                    "option_c": "Only border adds to width, not padding",
                    "option_d": "Only in older browsers",
                    "correct_option": "b",
                    "explanation": "In content-box (the default), width applies only to content; padding and border add on top of it.",
                },
                {
                    "text": "What does box-sizing: border-box change?",
                    "option_a": "It removes all padding automatically",
                    "option_b": "It makes width/height represent the total size including padding and border",
                    "option_c": "It disables margins",
                    "option_d": "It only affects text elements",
                    "correct_option": "b",
                    "explanation": "border-box makes sizing predictable by including padding and border within the specified width/height.",
                },
                {
                    "text": "What is margin collapsing?",
                    "option_a": "Margins are always summed between elements",
                    "option_b": "Vertical margins between adjacent elements can combine to the larger value instead of summing",
                    "option_c": "Margins disappear when box-sizing is set",
                    "option_d": "It only happens with horizontal margins",
                    "correct_option": "b",
                    "explanation": "Adjacent vertical margins collapse to the larger of the two values rather than adding together.",
                },
            ],
        },
    },
    {
        "slug": "webdev-11-colors-units-typography",
        "title": "11. Colors, Units, and Typography",
        "level": "beginner",
        "explanation": (
            "CSS colors can be written as keywords (red), hex (#ff0000), rgb()/rgba() (rgb(255,0,0)), "
            "or hsl()/hsla() (hue, saturation, lightness — often the most intuitive for adjusting a "
            "color's brightness or vibrancy). CSS units fall into two categories: absolute (px — a "
            "fixed size regardless of context) and relative (%, em, rem, vw, vh — sized based on "
            "something else). rem is relative to the ROOT font-size (usually 16px by default), making "
            "it the preferred unit for consistent, accessible, scalable spacing and font sizing "
            "site-wide — unlike em, which compounds based on each nested parent's font-size, which can "
            "cause unpredictable sizing in deeply nested components. Typography properties (font-family, "
            "font-size, font-weight, line-height, letter-spacing) control text readability and hierarchy."
        ),
        "examples": (
            "Example 1 — Color formats (all represent the same red):\n"
            "color: red;\n"
            "color: #ff0000;\n"
            "color: rgb(255, 0, 0);\n"
            "color: hsl(0, 100%, 50%);\n"
            "\n"
            "Example 2 — rem vs em (why rem is usually safer):\n"
            "html { font-size: 16px; }              /* the root */\n"
            ".card { font-size: 1.25rem; }          /* always 20px, regardless of nesting */\n"
            ".card .nested { font-size: 1.25em; }   /* 1.25x its PARENT's size -- compounds! */\n"
            "\n"
            "Example 3 — Readable typography defaults:\n"
            "body {\n"
            "  font-family: 'Segoe UI', system-ui, sans-serif;\n"
            "  font-size: 1rem;\n"
            "  line-height: 1.6;      /* comfortable reading line height */\n"
            "  color: #1e293b;\n"
            "}\n"
            "h1 { font-size: 2.5rem; font-weight: 700; }\n"
        ),
        "practice": (
            "1. Style the same element's color using all 4 color formats (keyword, hex, rgb, hsl) one "
            "at a time and confirm they render identically.\n"
            "2. Build 3 nested <div> elements, each with font-size: 1.2em, and observe how the text "
            "size compounds/grows at each level — then fix it using rem instead.\n"
            "3. Set a readable line-height (try 1.5-1.6) on a paragraph of text and compare it "
            "visually against line-height: 1.\n"
            "4. Use hsl() to create 3 shades of the same hue by only changing the lightness value."
        ),
        "mini_project": (
            "Mini Project: Typography Style Guide\n"
            "Build a single page demonstrating a complete typographic system: h1-h4 with distinct "
            "sizes/weights (all in rem), body text with comfortable line-height, and a small color "
            "palette (5 colors) defined using hsl() so you can show tints/shades of your brand color "
            "by adjusting only the lightness value."
        ),
        "real_world_project": (
            "Real-World Project: Brand Color Palette Extraction\n"
            "Pick a real company's website (or logo). Use a browser color picker (DevTools has one "
            "built in) to identify their primary and secondary colors, convert them to hex AND hsl "
            "format, and build a small reference page displaying swatches of each with labels — a "
            "genuine first step in real brand/design system work."
        ),
        "common_mistakes": (
            "- Using px for font-size everywhere — this ignores the user's browser font-size "
            "preference (accessibility setting), unlike rem which scales proportionally with it.\n"
            "- Overusing em for font-size in deeply nested components, causing unpredictable "
            "compounding growth that's hard to reason about.\n"
            "- Setting line-height: 1 (or omitting it, relying on the cramped browser default) on body "
            "text, making paragraphs uncomfortable to read.\n"
            "- Choosing colors purely by eye without checking contrast ratios — low-contrast text "
            "(like light gray on white) fails accessibility standards and is hard to read for many "
            "users, not just those with visual impairments."
        ),
        "best_practices": (
            "- Use rem for font-size and most spacing, reserving px for things that should genuinely "
            "never scale (like a 1px border).\n"
            "- Set a comfortable line-height (typically 1.4-1.6) on body text for readability.\n"
            "- Prefer hsl() when building a color system — adjusting lightness/saturation to create "
            "tints and shades is far more intuitive than guessing hex values.\n"
            "- Check color contrast using DevTools' built-in contrast checker (visible when inspecting "
            "text color) to ensure WCAG AA compliance (4.5:1 ratio for normal text)."
        ),
        "interview_questions": (
            "1. What's the difference between rem and em, and why is rem often preferred for "
            "consistent sizing?\n"
            "2. Why might using only px for font sizes be considered an accessibility issue?\n"
            "3. What are the four ways to specify a color in CSS, and which do you personally prefer "
            "for building a design system, and why?\n"
            "4. What does line-height control, and why does it matter for readability?\n"
            "5. What is a color contrast ratio, and why does it matter for accessibility?"
        ),
        "assignment": (
            "Assignment: Unit Conversion Practice\n"
            "Given a root font-size of 16px, convert 6 different px values (12px, 18px, 24px, 32px, "
            "48px, 64px) into their rem equivalents by hand, then verify using DevTools by applying "
            "them and checking computed font-size."
        ),
        "challenge": (
            "Challenge: WCAG AA-Compliant Color Palette\n"
            "Design a 5-color palette (background, text, primary accent, secondary accent, and an "
            "error/warning color) where every text/background pairing you'll realistically use meets "
            "at least a 4.5:1 contrast ratio, verified using DevTools' contrast checker."
        ),
        "summary": (
            "CSS colors can be expressed as keywords, hex, rgb(), or hsl() — hsl() is often most "
            "intuitive for building consistent palettes. Units split into absolute (px) and relative "
            "(rem, em, %, vw/vh); rem (relative to the root font-size) is generally preferred over em "
            "for predictable, accessible sizing. Good typography relies on appropriate font-size "
            "hierarchy, comfortable line-height, and sufficient color contrast for readability."
        ),
        "lesson_references": (
            "- MDN Web Docs: 'CSS values and units' and 'CSS Colors' guides\n"
            "- MDN Web Docs: 'em, ex, ch, rem' unit explanations\n"
            "- WebAIM: 'Contrast Checker' tool and WCAG contrast guidelines\n"
            "- web.dev: 'Learn CSS - Sizing units' module"
        ),
        "next_lesson_preview": (
            "Next up: Backgrounds and Borders. You'll learn how to style element backgrounds "
            "(colors, gradients, images) and borders (including rounded corners and box-shadow) — the "
            "visual polish tools you'll use on nearly every component you build."
        ),
        "quiz": {
            "title": "Colors, Units, and Typography Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "Why is rem generally preferred over em for consistent sizing?",
                    "option_a": "rem is always a smaller value",
                    "option_b": "rem is relative to the root font-size and doesn't compound through nesting like em can",
                    "option_c": "em is not supported in modern browsers",
                    "option_d": "There is no practical difference",
                    "correct_option": "b",
                    "explanation": "rem stays consistent regardless of nesting depth, while em compounds based on each parent's font-size.",
                },
                {
                    "text": "Which CSS color format is often most intuitive for creating tints/shades of the same color?",
                    "option_a": "Hex",
                    "option_b": "Keyword",
                    "option_c": "hsl()",
                    "option_d": "rgb()",
                    "correct_option": "c",
                    "explanation": "hsl() lets you adjust just the lightness value to create tints/shades while keeping the same hue.",
                },
                {
                    "text": "What does line-height control?",
                    "option_a": "The width of text",
                    "option_b": "The vertical spacing between lines of text",
                    "option_c": "The font family",
                    "option_d": "The text color",
                    "correct_option": "b",
                    "explanation": "line-height sets the vertical space each line of text occupies, directly affecting readability.",
                },
                {
                    "text": "Why does color contrast matter for accessibility?",
                    "option_a": "It doesn't affect accessibility",
                    "option_b": "Low contrast text is hard to read for many users, including those with visual impairments",
                    "option_c": "It only matters for print stylesheets",
                    "option_d": "Contrast only affects page load speed",
                    "correct_option": "b",
                    "explanation": "Sufficient contrast (WCAG AA requires 4.5:1 for normal text) ensures text is readable for the widest range of users.",
                },
            ],
        },
    },
    {
        "slug": "webdev-12-backgrounds-borders",
        "title": "12. Backgrounds and Borders",
        "level": "beginner",
        "explanation": (
            "Backgrounds can be a solid color (background-color), an image (background-image: "
            "url(...)), or a gradient (linear-gradient(), radial-gradient()). background-size "
            "(cover/contain) and background-position control how an image fills its container. "
            "Borders (border-width, border-style, border-color, or the shorthand border: 2px solid "
            "black) draw a visible edge; border-radius rounds corners, from subtle (4-8px) to fully "
            "circular (50% on a square element). box-shadow adds depth (offset-x offset-y blur-radius "
            "color), commonly used for cards and elevated UI elements — a small, well-tuned shadow is "
            "one of the highest-impact, lowest-effort visual polish techniques in web design."
        ),
        "examples": (
            "Example 1 — Gradient backgrounds:\n"
            ".hero {\n"
            "  background: linear-gradient(135deg, #16a34a, #0f172a);\n"
            "  color: white;\n"
            "}\n"
            "\n"
            "Example 2 — Background image, properly sized:\n"
            ".banner {\n"
            "  background-image: url('banner.jpg');\n"
            "  background-size: cover;\n"
            "  background-position: center;\n"
            "  height: 300px;\n"
            "}\n"
            "\n"
            "Example 3 — Rounded card with subtle shadow (a near-universal UI pattern):\n"
            ".card {\n"
            "  border: 1px solid #e2e8f0;\n"
            "  border-radius: 12px;\n"
            "  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);\n"
            "  padding: 20px;\n"
            "}\n"
        ),
        "practice": (
            "1. Create 3 boxes with different background types: solid color, linear-gradient, and a "
            "background-image with cover sizing.\n"
            "2. Build a card with border-radius and box-shadow, then experiment with different shadow "
            "blur/offset values to see the visual effect.\n"
            "3. Make a perfect circle using border-radius: 50% on a square element.\n"
            "4. Layer two box-shadows on one element (comma-separated) to create a more complex "
            "elevated effect."
        ),
        "mini_project": (
            "Mini Project: Card Component Library\n"
            "Build 4 visually distinct card variants on one page: a flat card (border only, no "
            "shadow), an elevated card (shadow, no visible border), a gradient-background card, and a "
            "circular avatar-style element using border-radius: 50%."
        ),
        "real_world_project": (
            "Real-World Project: Hero Section Recreation\n"
            "Find a real website's hero/banner section (the large visual area at the top of a "
            "homepage). Recreate its background treatment — whether it's a gradient, image, or solid "
            "color — as closely as you can, including appropriate background-size and "
            "background-position choices."
        ),
        "common_mistakes": (
            "- Using background-size: cover without also setting a fixed height (or min-height) on "
            "the container — cover needs the container to already have dimensions to size against.\n"
            "- Overusing heavy box-shadows (large blur, high opacity) that make a UI look muddy rather "
            "than polished — subtle shadows (low opacity, moderate blur) usually look more "
            "professional.\n"
            "- Forgetting that border adds to an element's size under content-box sizing (tie-back to "
            "lesson 10) — another reason border-box is the professional default.\n"
            "- Using border-radius: 50% on a non-square element expecting a circle — it only produces "
            "a true circle when width equals height; otherwise it creates an ellipse."
        ),
        "best_practices": (
            "- Keep box-shadow subtle by default (small blur, low opacity like rgba(0,0,0,0.1)) and "
            "reserve larger, darker shadows for genuinely elevated/modal elements.\n"
            "- Always pair background-image with background-size and background-position for "
            "predictable results.\n"
            "- Use CSS gradients instead of exporting gradient images from a design tool — they're "
            "resolution-independent, editable, and load faster.\n"
            "- Combine border-radius with overflow: hidden on a parent if you need child content "
            "(like an image) to respect the rounded corners too."
        ),
        "interview_questions": (
            "1. What's the difference between background-size: cover and background-size: contain?\n"
            "2. Why does a background-image sometimes fail to appear even with a correct URL, and "
            "what's the most common cause?\n"
            "3. How would you create a perfect circle using CSS?\n"
            "4. What does the box-shadow property's syntax control (each value in order)?\n"
            "5. Why might you use overflow: hidden alongside border-radius on a parent container?"
        ),
        "assignment": (
            "Assignment: Shadow Elevation System\n"
            "Design 3 levels of box-shadow ('low', 'medium', 'high' elevation) to represent a "
            "consistent depth system, similar to how Material Design or major UI libraries define "
            "elevation levels. Apply each to a sample card and justify your blur/offset/opacity "
            "choices."
        ),
        "challenge": (
            "Challenge: Gradient Hero Banner\n"
            "Build a full-width hero banner section with a multi-color linear-gradient background, "
            "centered white text with adequate contrast against the gradient, and a rounded, "
            "shadowed call-to-action button — a component pattern used on countless real landing "
            "pages."
        ),
        "summary": (
            "Backgrounds can be solid colors, images (with background-size/position controlling "
            "fit), or CSS gradients. Borders draw visible edges and, combined with border-radius, "
            "create rounded corners or circles. box-shadow adds depth and is a high-impact, "
            "low-effort tool for elevated UI elements like cards — subtlety usually looks more "
            "professional than heavy, dark shadows."
        ),
        "lesson_references": (
            "- MDN Web Docs: 'Backgrounds and borders' CSS guide\n"
            "- MDN Web Docs: 'linear-gradient()' and 'radial-gradient()' function references\n"
            "- MDN Web Docs: 'box-shadow' property reference\n"
            "- CSS-Tricks: 'The Shapes of CSS' (border-radius techniques)"
        ),
        "next_lesson_preview": (
            "Next up: Positioning. You'll learn the static/relative/absolute/fixed/sticky positioning "
            "system — how to take elements out of normal document flow and place them exactly where "
            "you need, essential for dropdowns, modals, and sticky navigation bars."
        ),
        "quiz": {
            "title": "Backgrounds and Borders Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does background-size: cover do?",
                    "option_a": "Repeats the image to fill the container",
                    "option_b": "Scales the image to fully cover the container, cropping if necessary",
                    "option_c": "Shrinks the image to fit without cropping",
                    "option_d": "Removes the background image",
                    "correct_option": "b",
                    "explanation": "cover scales the image to completely fill the container, cropping any overflow to maintain aspect ratio.",
                },
                {
                    "text": "How do you create a perfect circle with CSS?",
                    "option_a": "border-radius: 100% on any element",
                    "option_b": "border-radius: 50% on an element with equal width and height",
                    "option_c": "It's not possible without an image",
                    "option_d": "Using border-style: circle",
                    "correct_option": "b",
                    "explanation": "border-radius: 50% only produces a true circle when the element's width and height are equal.",
                },
                {
                    "text": "What does the blur value in box-shadow control?",
                    "option_a": "The shadow's color",
                    "option_b": "How soft/spread out the shadow's edge appears",
                    "option_c": "The shadow's position",
                    "option_d": "Whether the shadow is visible at all",
                    "correct_option": "b",
                    "explanation": "The blur radius controls how soft and spread the shadow's edges appear -- higher values create a softer effect.",
                },
                {
                    "text": "Why might you combine overflow: hidden with border-radius on a parent element?",
                    "option_a": "To improve page load speed",
                    "option_b": "To ensure child content (like an image) respects the parent's rounded corners",
                    "option_c": "overflow: hidden is required for border-radius to work at all",
                    "option_d": "There is no relationship between these properties",
                    "correct_option": "b",
                    "explanation": "Without overflow: hidden, child content can visually spill past the parent's rounded corners.",
                },
            ],
        },
    },
    {
        "slug": "webdev-13-positioning",
        "title": "13. Positioning",
        "level": "intermediate",
        "explanation": (
            "CSS position controls how an element is placed. static is the default — elements flow "
            "normally, top/left/right/bottom have no effect. relative shifts an element FROM its "
            "normal position, without affecting other elements' layout (they still act as if it never "
            "moved) — often used just to establish a positioning context for an absolute child. "
            "absolute removes the element from normal flow entirely and positions it relative to its "
            "nearest ANCESTOR with position other than static (or the page if none exists) — this is "
            "how dropdowns and tooltips are placed precisely. fixed positions relative to the browser "
            "viewport and stays put during scrolling (sticky headers use this, or sticky itself). "
            "sticky behaves like relative until a scroll threshold, then 'sticks' like fixed — the "
            "modern way to build sticky navigation bars without JavaScript."
        ),
        "examples": (
            "Example 1 — relative + absolute: the classic 'positioning context' pattern:\n"
            ".dropdown {\n"
            "  position: relative;    /* establishes context, doesn't move itself */\n"
            "}\n"
            ".dropdown-menu {\n"
            "  position: absolute;\n"
            "  top: 100%;              /* right below the dropdown trigger */\n"
            "  left: 0;\n"
            "}\n"
            "\n"
            "Example 2 — Fixed navigation bar (stays visible while scrolling):\n"
            ".navbar {\n"
            "  position: fixed;\n"
            "  top: 0;\n"
            "  left: 0;\n"
            "  right: 0;\n"
            "  z-index: 100;          /* ensures it stays above other content */\n"
            "}\n"
            "\n"
            "Example 3 — Sticky section headers (sticks after scrolling past it):\n"
            ".section-header {\n"
            "  position: sticky;\n"
            "  top: 0;\n"
            "  background: white;\n"
            "}\n"
        ),
        "practice": (
            "1. Create a parent with position: relative and a child with position: absolute placed in "
            "each corner (top-left, top-right, bottom-left, bottom-right) using top/right/bottom/"
            "left.\n"
            "2. Build a fixed navbar that stays visible while you scroll a long page.\n"
            "3. Build a sticky section header inside a scrollable container.\n"
            "4. Deliberately omit position: relative on a dropdown's parent and observe where the "
            "absolutely positioned child ends up instead (usually the whole page)."
        ),
        "mini_project": (
            "Mini Project: Dropdown Menu Structure\n"
            "Build a navigation bar with one item that reveals a dropdown menu on hover (using CSS "
            ":hover, no JavaScript needed yet), correctly using position: relative on the trigger and "
            "position: absolute on the dropdown panel."
        ),
        "real_world_project": (
            "Real-World Project: Sticky Table of Contents\n"
            "Build a long-form article page (reuse content from an earlier lesson) with a sidebar "
            "table of contents that uses position: sticky to remain visible as the user scrolls "
            "through the article — a very common real pattern on documentation and blog sites."
        ),
        "common_mistakes": (
            "- Using position: absolute without a positioned ancestor (relative/absolute/fixed) — the "
            "element then positions relative to the entire page, often landing in an unexpected "
            "spot.\n"
            "- Forgetting z-index conflicts — two positioned elements can overlap unpredictably "
            "without explicit z-index values establishing which sits on top.\n"
            "- Using position: fixed for elements that should scroll away with content, or vice "
            "versa — a common source of layout bugs.\n"
            "- Expecting position: sticky to work without a defined top/bottom/left/right value, or "
            "inside a parent with overflow: hidden (which breaks sticky behavior)."
        ),
        "best_practices": (
            "- Establish a clear 'positioning context' intentionally (relative on the parent) before "
            "using absolute on a child — never rely on accidental page-level absolute positioning.\n"
            "- Keep a mental z-index scale for your project (e.g. dropdowns: 100, modals: 1000, "
            "toasts: 2000) rather than guessing arbitrary numbers each time.\n"
            "- Prefer position: sticky over JavaScript scroll listeners for simple sticky-header "
            "behavior — it's simpler, more performant, and needs no JS.\n"
            "- Always test positioned elements at different viewport sizes — absolute/fixed "
            "positioning can behave very differently on mobile."
        ),
        "interview_questions": (
            "1. Explain the difference between position: relative and position: absolute.\n"
            "2. What determines the positioning context for an absolutely positioned element?\n"
            "3. What's the difference between position: fixed and position: sticky?\n"
            "4. Why might position: sticky fail to work as expected, even with a top value set?\n"
            "5. How would you build a dropdown menu using only CSS positioning (no JavaScript)?"
        ),
        "assignment": (
            "Assignment: Positioning Diagnosis\n"
            "Given 4 broken positioning examples (each with one intentional bug — missing relative "
            "parent, missing z-index, sticky inside overflow:hidden, wrong top/left values), diagnose "
            "and fix each one, explaining what was wrong in one sentence per example."
        ),
        "challenge": (
            "Challenge: Full Dropdown Navigation System\n"
            "Build a navbar with 3 items, at least one of which has a multi-item dropdown menu "
            "revealed on hover, positioned correctly with relative/absolute, layered correctly with "
            "z-index above the page content, and functional when the page is scrolled."
        ),
        "summary": (
            "position: static is the default (normal flow). relative shifts an element without "
            "affecting others and establishes a positioning context for absolute children. absolute "
            "positions relative to the nearest positioned ancestor, removed from normal flow. fixed "
            "positions relative to the viewport, staying put during scroll. sticky combines relative "
            "and fixed behavior, 'sticking' after a scroll threshold — the modern CSS-only solution "
            "for sticky headers."
        ),
        "lesson_references": (
            "- MDN Web Docs: 'Positioning' CSS layout guide\n"
            "- MDN Web Docs: 'position' property reference (all 5 values)\n"
            "- MDN Web Docs: 'z-index' and stacking context guide\n"
            "- CSS-Tricks: 'position sticky' almanac entry"
        ),
        "next_lesson_preview": (
            "Next up: Flexbox Deep Dive. You briefly used Flexbox for a navbar in an earlier lesson — "
            "now you'll master every Flexbox property (justify-content, align-items, flex-grow/shrink/"
            "basis, flex-wrap) to confidently build any one-dimensional layout."
        ),
        "quiz": {
            "title": "Positioning Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does position: relative do to an element by itself (with no top/left set)?",
                    "option_a": "Nothing visually changes; it just establishes a positioning context for children",
                    "option_b": "It centers the element automatically",
                    "option_c": "It removes the element from the page",
                    "option_d": "It makes the element fixed to the viewport",
                    "correct_option": "a",
                    "explanation": "Without offset values, position: relative has no visual effect except enabling it as a positioning context.",
                },
                {
                    "text": "An absolutely positioned element with no positioned ancestor will position relative to what?",
                    "option_a": "Its immediate parent, always",
                    "option_b": "The entire page (initial containing block)",
                    "option_c": "It will not render at all",
                    "option_d": "The browser will throw an error",
                    "correct_option": "b",
                    "explanation": "Without a positioned ancestor, absolute positioning falls back to the page's initial containing block.",
                },
                {
                    "text": "What's the key difference between position: fixed and position: sticky?",
                    "option_a": "They are functionally identical",
                    "option_b": "fixed is always positioned to the viewport; sticky acts relative until a scroll threshold, then sticks",
                    "option_c": "sticky only works on mobile devices",
                    "option_d": "fixed only works inside a scrollable container",
                    "correct_option": "b",
                    "explanation": "sticky transitions between relative and fixed-like behavior based on scroll position; fixed is always viewport-relative.",
                },
                {
                    "text": "What property resolves overlap conflicts between positioned elements?",
                    "option_a": "opacity",
                    "option_b": "z-index",
                    "option_c": "overflow",
                    "option_d": "display",
                    "correct_option": "b",
                    "explanation": "z-index controls the stacking order of positioned elements when they overlap.",
                },
            ],
        },
    },
    {
        "slug": "webdev-14-flexbox-deep-dive",
        "title": "14. Flexbox Deep Dive",
        "level": "intermediate",
        "explanation": (
            "You used basic Flexbox for a navbar earlier (Lesson 3); now go deeper. On the CONTAINER "
            "(display: flex): flex-direction (row/column) sets the main axis; justify-content aligns "
            "items ALONG the main axis (start/center/space-between/space-around); align-items aligns "
            "items ACROSS the cross axis (start/center/stretch); flex-wrap lets items wrap to new "
            "lines instead of shrinking forever; gap adds spacing between items cleanly (no more "
            "margin hacks). On the CHILDREN: flex-grow (how much an item expands to fill extra "
            "space), flex-shrink (how much it shrinks under pressure), and flex-basis (its starting "
            "size before growing/shrinking) — often combined as the flex shorthand (flex: 1 = grow "
            "and shrink equally, fill available space)."
        ),
        "examples": (
            "Example 1 — Common navbar pattern (justify-content + align-items):\n"
            ".navbar {\n"
            "  display: flex;\n"
            "  justify-content: space-between;   /* logo left, links right */\n"
            "  align-items: center;               /* vertically centered */\n"
            "  gap: 16px;\n"
            "}\n"
            "\n"
            "Example 2 — Equal-width flexible columns:\n"
            ".columns {\n"
            "  display: flex;\n"
            "  gap: 20px;\n"
            "}\n"
            ".columns > div {\n"
            "  flex: 1;    /* each column grows/shrinks equally to fill available space */\n"
            "}\n"
            "\n"
            "Example 3 — Wrapping card grid (falls back gracefully on small screens):\n"
            ".card-row {\n"
            "  display: flex;\n"
            "  flex-wrap: wrap;\n"
            "  gap: 16px;\n"
            "}\n"
            ".card-row > .card {\n"
            "  flex: 1 1 250px;   /* grow, shrink, but prefer 250px as a starting width */\n"
            "}\n"
        ),
        "practice": (
            "1. Build a 3-column layout using flex: 1 on each column so they're always equal width.\n"
            "2. Build a card row using flex-wrap: wrap with flex: 1 1 200px on each card, then resize "
            "your browser to see it reflow.\n"
            "3. Center a single box perfectly both horizontally and vertically inside a full-height "
            "flex container using justify-content and align-items.\n"
            "4. Experiment with flex-direction: column and observe how justify-content and "
            "align-items swap their visual effect (main axis becomes vertical)."
        ),
        "mini_project": (
            "Mini Project: Responsive Feature Row\n"
            "Build a row of 4 'feature' boxes using Flexbox that: are equal width on large screens, "
            "wrap to 2-per-row on medium screens, and stack to 1-per-row on small screens — using "
            "flex-wrap and flex-basis (no media queries needed for this specific effect, though "
            "you'll combine both in the next module)."
        ),
        "real_world_project": (
            "Real-World Project: Pricing Card Layout\n"
            "Build a 3-tier pricing page (Basic/Pro/Enterprise) using Flexbox: cards should be equal "
            "height regardless of content length (a common Flexbox superpower — align-items: stretch "
            "by default), with the middle 'Pro' card slightly larger to draw attention, matching a "
            "pattern used on nearly every real SaaS pricing page."
        ),
        "common_mistakes": (
            "- Forgetting that flex properties on children only work if the PARENT has display: flex "
            "— a very common beginner confusion when flex: 1 'does nothing.'\n"
            "- Using margin: auto hacks for spacing between flex items instead of the simpler gap "
            "property (which has excellent modern browser support).\n"
            "- Confusing justify-content (main axis) with align-items (cross axis) — remember: when "
            "flex-direction is row, justify-content is horizontal and align-items is vertical; this "
            "SWAPS when flex-direction is column.\n"
            "- Not using flex-wrap on a row of items that should reflow on smaller screens, causing "
            "items to shrink painfully small instead of wrapping to a new line."
        ),
        "best_practices": (
            "- Use gap instead of margin for spacing between flex items — cleaner, no need to "
            "special-case the first/last item.\n"
            "- Remember align-items: stretch is the DEFAULT — this is why flex children often become "
            "equal height automatically without you asking for it, a very useful behavior for card "
            "layouts.\n"
            "- Use the flex shorthand (flex: 1, flex: 1 1 200px) rather than setting flex-grow/shrink/"
            "basis separately, for more concise, readable code.\n"
            "- Reach for Flexbox for one-dimensional layouts (a single row or column); reach for Grid "
            "(next lesson) when you need two-dimensional control."
        ),
        "interview_questions": (
            "1. What's the difference between justify-content and align-items, and how does "
            "flex-direction affect which axis each one controls?\n"
            "2. What does flex: 1 actually set (in terms of grow/shrink/basis)?\n"
            "3. Why do flex children often end up the same height without any extra CSS?\n"
            "4. When would you use flex-wrap, and what's the visual difference with and without it?\n"
            "5. Why is gap generally preferred over margin for spacing flex items?"
        ),
        "assignment": (
            "Assignment: Flexbox Property Matrix\n"
            "Build one flex container and, one at a time, apply and screenshot the visual effect of "
            "all 5 justify-content values and all 4 align-items values (using DevTools to toggle "
            "live), documenting what each one visually does with a one-sentence description."
        ),
        "challenge": (
            "Challenge: Sticky Footer Layout\n"
            "Using Flexbox with flex-direction: column on the page's root container and flex: 1 on "
            "the main content area, build a page where the footer always stays at the bottom of the "
            "viewport even when there's very little content — the classic 'sticky footer' problem, "
            "elegantly solved by Flexbox."
        ),
        "summary": (
            "Flexbox arranges items along one axis (row or column). Container properties "
            "(justify-content, align-items, flex-wrap, gap) control alignment and spacing; child "
            "properties (flex-grow, flex-shrink, flex-basis, usually via the flex shorthand) control "
            "how individual items size themselves. align-items: stretch (the default) explains why "
            "flex children often end up equal height automatically — a hugely useful property for "
            "card-based layouts."
        ),
        "lesson_references": (
            "- CSS-Tricks: 'A Complete Guide to Flexbox' (the definitive community reference)\n"
            "- MDN Web Docs: 'Basic concepts of flexbox'\n"
            "- Flexbox Froggy (flexboxfroggy.com) — interactive Flexbox learning game\n"
            "- web.dev: 'Learn CSS - Flexbox' module"
        ),
        "next_lesson_preview": (
            "Next up: CSS Grid Deep Dive. You'll learn two-dimensional layout — rows AND columns "
            "simultaneously — for building complete page layouts, image galleries, and dashboards "
            "that Flexbox alone can't handle as elegantly."
        ),
        "quiz": {
            "title": "Flexbox Deep Dive Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "With the default flex-direction: row, which axis does justify-content control?",
                    "option_a": "The vertical (cross) axis",
                    "option_b": "The horizontal (main) axis",
                    "option_c": "Both axes simultaneously",
                    "option_d": "Neither axis",
                    "correct_option": "b",
                    "explanation": "In row direction, the main axis is horizontal, which is what justify-content aligns along.",
                },
                {
                    "text": "What is the default value of align-items, and what effect does it have?",
                    "option_a": "flex-start; items align to the top",
                    "option_b": "stretch; items stretch to fill the container's cross-axis size",
                    "option_c": "center; items are centered",
                    "option_d": "There is no default value",
                    "correct_option": "b",
                    "explanation": "stretch is the default, which is why flex children often become equal height without extra CSS.",
                },
                {
                    "text": "What does flex: 1 do to a flex item?",
                    "option_a": "Fixes its width to 1px",
                    "option_b": "Allows it to grow and shrink to fill available space equally with siblings set the same way",
                    "option_c": "Removes it from the flex layout",
                    "option_d": "Sets its opacity to 1",
                    "correct_option": "b",
                    "explanation": "flex: 1 is shorthand for flex-grow: 1, flex-shrink: 1, flex-basis: 0%, distributing space equally.",
                },
                {
                    "text": "Which property lets flex items wrap onto multiple lines instead of shrinking indefinitely?",
                    "option_a": "flex-wrap: wrap",
                    "option_b": "flex-direction: column",
                    "option_c": "justify-content: wrap",
                    "option_d": "overflow: wrap",
                    "correct_option": "a",
                    "explanation": "flex-wrap: wrap allows items to move to new lines when they no longer fit on one.",
                },
            ],
        },
    },
    {
        "slug": "webdev-15-css-grid-deep-dive",
        "title": "15. CSS Grid Deep Dive",
        "level": "intermediate",
        "explanation": (
            "CSS Grid controls two dimensions (rows AND columns) simultaneously, making it ideal for "
            "whole-page layouts. On the container (display: grid): grid-template-columns and "
            "grid-template-rows define the track sizes — using px, %, or the flexible fr unit "
            "(fraction of remaining space). repeat() avoids repetition (repeat(3, 1fr) = three equal "
            "columns). auto-fit/auto-fill combined with minmax() create truly responsive grids "
            "WITHOUT media queries — grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)) "
            "automatically fits as many 200px+ columns as will fit, reflowing as the viewport "
            "resizes. gap adds spacing between both rows and columns cleanly. Named grid-template-"
            "areas let you visually 'draw' a layout in your CSS using readable region names."
        ),
        "examples": (
            "Example 1 — Auto-responsive card grid (no media queries needed):\n"
            ".gallery {\n"
            "  display: grid;\n"
            "  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));\n"
            "  gap: 20px;\n"
            "}\n"
            "\n"
            "Example 2 — Classic page layout with named areas:\n"
            ".page {\n"
            "  display: grid;\n"
            "  grid-template-columns: 200px 1fr;\n"
            "  grid-template-rows: auto 1fr auto;\n"
            "  grid-template-areas:\n"
            "    \"sidebar header\"\n"
            "    \"sidebar main\"\n"
            "    \"sidebar footer\";\n"
            "}\n"
            ".sidebar { grid-area: sidebar; }\n"
            ".header  { grid-area: header; }\n"
            ".main    { grid-area: main; }\n"
            "\n"
            "Example 3 — An item spanning multiple columns:\n"
            ".featured-card {\n"
            "  grid-column: span 2;   /* takes up 2 columns' worth of width */\n"
            "}\n"
        ),
        "practice": (
            "1. Build a 3-column grid using grid-template-columns: repeat(3, 1fr) with gap: 16px.\n"
            "2. Convert it to an auto-responsive grid using repeat(auto-fit, minmax(150px, 1fr)) and "
            "resize your browser to see it reflow automatically.\n"
            "3. Build a simple page layout (header, sidebar, main, footer) using named "
            "grid-template-areas.\n"
            "4. Make one grid item span 2 columns using grid-column: span 2."
        ),
        "mini_project": (
            "Mini Project: Auto-Responsive Photo Gallery\n"
            "Build a gallery of 12 images using CSS Grid with auto-fit/minmax so it automatically "
            "reflows from many columns on desktop down to a single column on mobile, with zero media "
            "queries required."
        ),
        "real_world_project": (
            "Real-World Project: Dashboard Layout\n"
            "Build a full admin dashboard skeleton using grid-template-areas: a fixed sidebar, a top "
            "header bar, and a main content area with a nested grid of 4 stat cards inside it — the "
            "exact structural pattern used by real admin panels and SaaS dashboards (including "
            "Kabiru AI Tutor's own Dashboard page)."
        ),
        "common_mistakes": (
            "- Reaching for Grid when Flexbox would be simpler for a genuinely one-dimensional layout "
            "(a single row of nav links doesn't need Grid's two-dimensional power).\n"
            "- Forgetting the fr unit and using percentages instead, which don't account for gap "
            "spacing correctly — fr automatically distributes remaining space after gaps are "
            "subtracted.\n"
            "- Misspelling or mismatching grid-area names between grid-template-areas and individual "
            "items' grid-area declarations — a single typo silently breaks the whole layout.\n"
            "- Using a fixed number of columns (repeat(4, 1fr)) when the content is genuinely dynamic "
            "in count, instead of auto-fit/auto-fill, which handles varying item counts gracefully."
        ),
        "best_practices": (
            "- Reach for Grid for two-dimensional layouts (whole pages, dashboards, galleries); reach "
            "for Flexbox for one-dimensional layouts (navbars, single rows/columns of items).\n"
            "- Use repeat(auto-fit, minmax(...)) for genuinely responsive grids before reaching for "
            "media queries — it often eliminates the need for them entirely for simple reflow cases.\n"
            "- Use named grid-template-areas for complex page layouts — it makes the CSS read almost "
            "like an ASCII diagram of the actual layout, highly maintainable.\n"
            "- Combine Grid (for the overall page) with Flexbox (for aligning content WITHIN a "
            "specific grid cell) — they work together, not in competition."
        ),
        "interview_questions": (
            "1. What's the fundamental difference between when you'd choose Grid over Flexbox?\n"
            "2. Explain what grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)) does and why "
            "it's useful for responsive design.\n"
            "3. What is the fr unit, and how does it differ from using percentages for column "
            "widths?\n"
            "4. How do named grid-template-areas improve the readability of a complex layout's CSS?\n"
            "5. Can Grid and Flexbox be used together in the same project? Give an example of when "
            "you would combine them."
        ),
        "assignment": (
            "Assignment: Grid vs Flexbox Judgment Call\n"
            "You're given 5 different UI patterns (a navbar, a photo gallery, a pricing card row, a "
            "full dashboard layout, a single centered modal). For each, decide whether Grid or "
            "Flexbox is the better tool and justify your choice in one sentence."
        ),
        "challenge": (
            "Challenge: Module 2 Capstone — Magazine-Style Layout\n"
            "Build a magazine/blog homepage layout using CSS Grid with grid-template-areas: a large "
            "featured article spanning 2 columns, 4 smaller article cards in a grid below it, and a "
            "sidebar with a 'popular posts' list — combining Grid for the overall structure with "
            "Flexbox for aligning content within individual cards."
        ),
        "summary": (
            "CSS Grid handles two-dimensional layouts (rows and columns together), complementing "
            "Flexbox's one-dimensional strength. grid-template-columns/rows define tracks (often "
            "using the flexible fr unit), repeat(auto-fit, minmax()) creates responsive grids without "
            "media queries, and named grid-template-areas make complex layouts readable. Grid and "
            "Flexbox are commonly combined: Grid for overall page structure, Flexbox for aligning "
            "content within individual cells."
        ),
        "lesson_references": (
            "- CSS-Tricks: 'A Complete Guide to Grid' (the definitive community reference)\n"
            "- MDN Web Docs: 'Basic concepts of grid layout'\n"
            "- Grid Garden (cssgridgarden.com) — interactive Grid learning game\n"
            "- web.dev: 'Learn CSS - Grid' module"
        ),
        "next_lesson_preview": (
            "Next up: Responsive Design and Media Queries. You'll learn how to adapt layouts across "
            "screen sizes using breakpoints, the mobile-first design approach, and how media queries "
            "complement the auto-responsive Grid/Flexbox techniques you've already learned."
        ),
        "quiz": {
            "title": "CSS Grid Deep Dive Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What is the main advantage of CSS Grid over Flexbox?",
                    "option_a": "Grid is newer and always better",
                    "option_b": "Grid controls two dimensions (rows and columns) simultaneously, unlike Flexbox's single axis",
                    "option_c": "Grid loads faster",
                    "option_d": "There is no real difference",
                    "correct_option": "b",
                    "explanation": "Grid's defining strength is true two-dimensional layout control, which Flexbox doesn't provide.",
                },
                {
                    "text": "What does repeat(auto-fit, minmax(200px, 1fr)) achieve?",
                    "option_a": "Exactly 200 fixed columns",
                    "option_b": "A responsive grid that automatically fits as many 200px+ columns as the space allows",
                    "option_c": "A single column layout only",
                    "option_d": "It disables the grid",
                    "correct_option": "b",
                    "explanation": "This pattern creates a self-adjusting responsive grid without needing separate media query breakpoints.",
                },
                {
                    "text": "What does the fr unit represent in a grid track definition?",
                    "option_a": "A fixed pixel value",
                    "option_b": "A fraction of the remaining available space",
                    "option_c": "A percentage of the viewport",
                    "option_d": "It's not a valid CSS unit",
                    "correct_option": "b",
                    "explanation": "fr distributes available space proportionally, accounting for gaps and fixed-size tracks automatically.",
                },
                {
                    "text": "What is the benefit of named grid-template-areas over numeric grid-column/row placement?",
                    "option_a": "It performs better",
                    "option_b": "It makes complex layouts far more readable, resembling a visual diagram of the layout",
                    "option_c": "It's required for Grid to function",
                    "option_d": "It only works with Flexbox",
                    "correct_option": "b",
                    "explanation": "Named areas let the CSS itself visually communicate the layout's structure, improving maintainability.",
                },
            ],
        },
    },
    {
        "slug": "webdev-16-responsive-media-queries",
        "title": "16. Responsive Design and Media Queries",
        "level": "intermediate",
        "explanation": (
            "Responsive design means a site adapts well to any screen size — phone, tablet, desktop. "
            "Media queries (@media (min-width: 768px) { ... }) apply CSS rules conditionally based on "
            "viewport width (or other features). 'Mobile-first' is the recommended approach: write "
            "your BASE styles for small screens first, then use min-width media queries to progressively "
            "add complexity for larger screens — this tends to produce simpler, more maintainable CSS "
            "than the reverse (desktop-first with max-width overrides). Common breakpoints (though "
            "content should ultimately dictate them, not fixed device sizes): ~640px (small tablets), "
            "~768px (tablets), ~1024px (small desktops), ~1280px (large desktops)."
        ),
        "examples": (
            "Example 1 — Mobile-first media query (base styles = mobile, then enhance):\n"
            ".nav-links {\n"
            "  display: none;         /* hidden by default on mobile */\n"
            "}\n"
            "\n"
            "@media (min-width: 768px) {\n"
            "  .nav-links {\n"
            "    display: flex;       /* shown once the viewport is wide enough */\n"
            "  }\n"
            "}\n"
            "\n"
            "Example 2 — Responsive grid columns via media query (complementing auto-fit techniques):\n"
            ".grid {\n"
            "  display: grid;\n"
            "  grid-template-columns: 1fr;              /* 1 column on mobile */\n"
            "  gap: 16px;\n"
            "}\n"
            "@media (min-width: 768px) {\n"
            "  .grid { grid-template-columns: repeat(2, 1fr); }  /* 2 columns on tablet+ */\n"
            "}\n"
            "@media (min-width: 1024px) {\n"
            "  .grid { grid-template-columns: repeat(4, 1fr); }  /* 4 columns on desktop+ */\n"
            "}\n"
            "\n"
            "Example 3 — Combining with feature queries (dark mode preference):\n"
            "@media (prefers-color-scheme: dark) {\n"
            "  body { background: #0f172a; color: #f1f5f9; }\n"
            "}\n"
        ),
        "practice": (
            "1. Build a navigation bar that shows a simplified layout on mobile (e.g. just a logo) and "
            "reveals full nav links at min-width: 768px.\n"
            "2. Build a grid that goes from 1 column (mobile) to 2 columns (tablet) to 4 columns "
            "(desktop) using min-width media queries.\n"
            "3. Resize your browser window slowly and observe exactly where your layout breaks or "
            "looks awkward — add a breakpoint there instead of at an arbitrary device size.\n"
            "4. Add a prefers-color-scheme: dark media query that swaps your background/text colors."
        ),
        "mini_project": (
            "Mini Project: Fully Responsive Landing Page\n"
            "Take a landing page you've built in a previous lesson and make it genuinely responsive: "
            "mobile-first base styles, at least 2 meaningful breakpoints, a navigation that adapts "
            "(not just shrinks), and test it by resizing from 320px to 1920px width, fixing any "
            "awkward in-between states you find."
        ),
        "real_world_project": (
            "Real-World Project: Cross-Device Audit\n"
            "Take any real website and use Chrome DevTools' device toolbar (responsive design mode) "
            "to test it at 5 different widths (320px, 375px, 768px, 1024px, 1440px). Document any "
            "layout breakage, overlapping text, or unusably small tap targets you find at each size — "
            "genuine QA work performed before every real production launch."
        ),
        "common_mistakes": (
            "- Writing desktop-first CSS with max-width overrides for mobile — this often results in "
            "more complex CSS since you're constantly undoing desktop styles rather than building up "
            "from a simple base.\n"
            "- Choosing breakpoints based on specific device names/sizes (like 'iPhone 12 width') "
            "instead of where YOUR content actually breaks — devices change constantly, but your "
            "content's natural breakpoints are more stable.\n"
            "- Forgetting the viewport meta tag (from Lesson 2) — without it, media queries won't work "
            "as expected since the browser assumes a desktop-width layout by default.\n"
            "- Only testing at a few fixed widths instead of continuously resizing — this misses "
            "awkward 'in-between' states that real users on oddly-sized windows or devices will "
            "encounter."
        ),
        "best_practices": (
            "- Default to mobile-first: write base (no media query) styles for small screens, then "
            "layer on complexity with min-width queries.\n"
            "- Choose breakpoints based on where YOUR content starts looking cramped or awkward, not "
            "arbitrary device widths.\n"
            "- Combine media queries with the auto-fit/minmax responsive Grid techniques from Lesson "
            "15 — media queries for major structural shifts (nav layout, sidebar visibility), "
            "auto-fit for simple item reflow.\n"
            "- Test continuously by dragging the browser window's edge, not just checking a few "
            "device presets."
        ),
        "interview_questions": (
            "1. What does 'mobile-first' mean, and why is it generally preferred over desktop-first "
            "CSS?\n"
            "2. How should you decide where to place a breakpoint, rather than just picking common "
            "device widths?\n"
            "3. Why won't media queries work correctly without the viewport meta tag?\n"
            "4. What's the difference between min-width and max-width media queries, and which "
            "aligns with a mobile-first approach?\n"
            "5. Beyond width, name another media feature you could query for (e.g. color scheme "
            "preference) and describe a use case."
        ),
        "assignment": (
            "Assignment: Breakpoint Discovery\n"
            "Take any multi-column layout you've built in this course. Slowly resize your browser "
            "from full width down to 320px, and document the EXACT pixel width where the layout first "
            "starts to look broken or cramped — that's your natural breakpoint, not a guessed device "
            "size."
        ),
        "challenge": (
            "Challenge: Three-Breakpoint Dashboard\n"
            "Build a dashboard layout (sidebar + main content + stat cards) that meaningfully "
            "restructures at 3 breakpoints: mobile (sidebar becomes a bottom nav or hidden drawer), "
            "tablet (2-column stat cards), and desktop (full sidebar + 4-column stat cards) — using "
            "mobile-first media queries throughout."
        ),
        "summary": (
            "Responsive design adapts layouts across screen sizes using media queries "
            "(@media (min-width: ...)). Mobile-first (base styles for small screens, progressively "
            "enhanced with min-width queries) is the recommended approach over desktop-first. "
            "Breakpoints should be chosen based on where your actual content breaks, not fixed device "
            "sizes. Media queries complement (not replace) the auto-responsive Grid/Flexbox "
            "techniques from earlier lessons."
        ),
        "lesson_references": (
            "- MDN Web Docs: 'Using media queries' and 'Responsive design' guides\n"
            "- MDN Web Docs: '@media' at-rule reference (full feature list)\n"
            "- web.dev: 'Responsive Web Design Basics'\n"
            "- A List Apart: 'Responsive Web Design' (Ethan Marcotte's original 2010 article)"
        ),
        "next_lesson_preview": (
            "Next up: CSS Variables and Custom Properties. You'll learn how to define reusable values "
            "(colors, spacing, fonts) once and reference them everywhere — including dynamically "
            "changing them with JavaScript, essential for building maintainable design systems and "
            "features like dark mode toggles."
        ),
        "quiz": {
            "title": "Responsive Design and Media Queries Quiz",
            "passing_score": 70,
            "questions": [
                {
                    "text": "What does 'mobile-first' CSS mean?",
                    "option_a": "Only building a mobile version of the site",
                    "option_b": "Writing base styles for small screens first, then enhancing for larger screens with min-width queries",
                    "option_c": "Using max-width queries exclusively",
                    "option_d": "Ignoring desktop users entirely",
                    "correct_option": "b",
                    "explanation": "Mobile-first builds up complexity progressively from a simple small-screen base, generally producing simpler CSS.",
                },
                {
                    "text": "How should breakpoints ideally be chosen?",
                    "option_a": "Based on specific popular device widths",
                    "option_b": "Based on where the content itself starts to look broken or cramped",
                    "option_c": "Always at exactly 768px and 1024px",
                    "option_d": "Randomly, it doesn't matter",
                    "correct_option": "b",
                    "explanation": "Content-driven breakpoints are more durable than device-specific ones, since devices and screen sizes constantly change.",
                },
                {
                    "text": "Why is the viewport meta tag required for media queries to work as expected?",
                    "option_a": "It's not actually required",
                    "option_b": "Without it, mobile browsers assume a desktop-width layout, breaking the expected viewport width",
                    "option_c": "It only affects image loading",
                    "option_d": "It controls media query syntax directly",
                    "correct_option": "b",
                    "explanation": "Without the viewport meta tag, mobile browsers render at a fake desktop width, causing media queries to behave unexpectedly.",
                },
                {
                    "text": "Which media query approach aligns with mobile-first design?",
                    "option_a": "max-width queries overriding desktop base styles",
                    "option_b": "min-width queries progressively enhancing mobile base styles",
                    "option_c": "Neither approach relates to mobile-first",
                    "option_d": "Media queries are unrelated to mobile-first design",
                    "correct_option": "b",
                    "explanation": "min-width queries add complexity as the screen grows, matching the mobile-first philosophy of starting simple.",
                },
            ],
        },
    },
]
