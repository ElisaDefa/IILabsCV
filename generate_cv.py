"""
ElevenLabs CV Generator
=======================
Run:  python generate_cv.py
Out:  Eli_Desfassiaux_ElevenLabs_CV.html   (same directory)

To update the CV, only edit the CV_DATA dict below.
The template and styling are handled automatically.
"""

from jinja2 import Environment
from pathlib import Path
from datetime import datetime

# ─────────────────────────────────────────────────────────────────────────────
#  CV DATA  ── edit this section only
# ─────────────────────────────────────────────────────────────────────────────

CV_DATA = {
    "name": {
        "first": "Eli",
        "last":  "Desfassiaux",
    },
    "location": "Mexico City, Mexico",
    "phone":    "+52 999 386 0131",
    "email":    "elisadesfassiaux@gmail.com",
    "linkedin": {
        "url":     "https://www.linkedin.com/in/maelisavelazquez/",
        "display": "linkedin.com/in/maelisavelazquez",
    },
    "tagline": "Lead Solution Engineer  ·  AI Architect  ·  Technical Pre-Sales",
    "target":  "ElevenLabs",

    "voice_intro": {
        "title":    "My Intro by Instant Voice Cloning",
        "subtitle": "by ElevenLabs",
        "url":      "https://soundcloud.com/elisa-desfassiaux-774976349/elevenlabs_eli_intro?si=6efb0a0524cc40928402453337d14691&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing",
        "embed":    "https://w.soundcloud.com/player/?url=https%3A%2F%2Fsoundcloud.com%2Felisa-desfassiaux-774976349%2Felevenlabs_eli_intro&color=%23F97316&auto_play=false&hide_related=true&show_comments=false&show_user=false&show_reposts=false&show_teaser=false",
    },

    "summary": (
        "AI-native Solutions Engineer with <strong>10+ years</strong> designing production-grade "
        "AI systems — including a <strong>patent-pending custom SLM</strong> — writing "
        "<strong>Python API integrations</strong>, and closing enterprise deals across North America "
        "and LATAM. Currently at Salesforce as a Lead SE, where I "
        "<strong>closed $1.9M+ within 6 months against a $1.5M annual quota</strong> by leading 36+ "
        "technical discoveries, custom AI demos, and enterprise workshops. Co-founded an AI startup "
        "where I personally engineered the Python API layer, built a custom "
        "<strong>3B-parameter LLM with HITL fine-tuning</strong>, and launched a B2B AIaaS product — "
        "the same API-first distribution model that defines the modern AI infrastructure market."
    ),

    # ── SKILLS ───────────────────────────────────────────────────────────────
    "skill_groups": [
        {
            "label": "AI & APIs",
            "tags": [
                {"name": "Python",            "accent": True},
                {"name": "LLM Architecture",  "accent": True},
                {"name": "Anthropic API",      "accent": True},
                {"name": "HITL Fine-tuning",   "accent": False},
                {"name": "Custom SLM Dev",     "accent": False},
                {"name": "Generative AI",      "accent": False},
                {"name": "REST APIs",          "accent": False},
            ],
        },
        {
            "label": "Technical Pre-Sales",
            "tags": [
                {"name": "Solutions Engineering", "accent": True},
                {"name": "Demo Building",          "accent": False},
                {"name": "Technical Discovery",    "accent": False},
                {"name": "PoC Development",        "accent": False},
                {"name": "AI Workshops",           "accent": False},
                {"name": "Whiteboarding",          "accent": False},
            ],
        },
        {
            "label": "Architecture",
            "tags": [
                {"name": "System Design",               "accent": False},
                {"name": "B2B API Platforms",           "accent": False},
                {"name": "Supabase / Postgres",         "accent": False},
                {"name": "Cloudflare",                  "accent": False},
                {"name": "Multi-platform Integrations", "accent": False},
            ],
        },
        {
            "label": "Enablement",
            "tags": [
                {"name": "Developer Docs",     "accent": False},
                {"name": "API Onboarding",     "accent": False},
                {"name": "Technical Playbooks","accent": False},
                {"name": "Self-Service Tools", "accent": False},
            ],
        },
        {
            "label": "Languages & Tools",
            "tags": [
                {"name": "JavaScript / TypeScript", "accent": False},
                {"name": "SQL",         "accent": False},
                {"name": "React",       "accent": False},
                {"name": "Salesforce",  "accent": False},
                {"name": "Talend",      "accent": False},
                {"name": "Agile / SAFe","accent": False},
            ],
        },
    ],

    # ── CERTIFICATIONS ────────────────────────────────────────────────────────
    "certifications": [
        "SAFe Certified Product Owner",
        "Salesforce Certified Administrator",
        "Salesforce Platform App Builder",
        "Salesforce Certified CPQ Specialist",
        "Salesforce Certified AI Associate",
        "Salesforce Certified Associate",
        "Business & Benchmark Certificate",
        "Teacher's Course Certification",
    ],

    # ── EDUCATION ─────────────────────────────────────────────────────────────
    "education": [
        {"school": "EBC",                "degree": "Finance and Banking"},
        {"school": "Anahuac University", "degree": "Industrial Engineering"},
    ],

    # ── ACHIEVEMENTS ─────────────────────────────────────────────────────────
    "achievements": [
        {"text": "$1.9M+ closed in ~6 months vs. $1.5M annual quota",       "highlight": True},
        {"text": "Outstanding Value to Clients — Deloitte (5×)",             "highlight": True},
        {"text": "LWC ConFest Award — Sole LATAM rep, 75+ teams",            "highlight": True},
        {"text": "Keynote Speaker, Lesbians Who Tech 10th Summit",           "highlight": True},
        {"text": "VP Kamala Harris Maternal Health Initiative (2021)",        "highlight": False},
    ],

    # ── EXPERIENCE ────────────────────────────────────────────────────────────
    "experience": [
        {
            "company":  "Salesforce",
            "title":    "Lead Solution Engineer",
            "location": "Mexico",
            "start":    "July 2025",
            "end":      "Present",
            "current":  True,
            "bullets": [
                "Closed <strong>$1.9M+ in new business within ~6 months</strong> — exceeding the "
                "$1.5M annual quota by 27% at roughly the halfway mark — by leading full-cycle "
                "technical pre-sales engagements across enterprise accounts, from discovery through "
                "custom demo to close.",

                "Designed and delivered <strong>10+ AI solution workshops</strong> for enterprise "
                "client engineering teams, translating the AI product roadmap into tailored "
                "proof-of-concepts and architecture recommendations that accelerated technical "
                "buy-in and shortened sales cycles.",

                "Led <strong>36+ client technical discovery sessions and custom product demos</strong>, "
                "systematically mapping customer architectures, surfacing integration requirements, "
                "and building technical trust that directly contributed to exceeding quota.",

                "Identified a recurring pattern across client engagements and "
                "<strong>championed an internal new product development initiative</strong>, "
                "bridging field feedback to the product team and establishing a systematic "
                "customer-to-roadmap loop.",
            ],
        },
        {
            "company":  "Humma.ai",
            "title":    "Co-Founder, Co-CEO & CTPO",
            "location": "Los Angeles, CA",
            "start":    "October 2023",
            "end":      "April 2024",
            "current":  False,
            "bullets": [
                "Architected and shipped a <strong>patent-pending, 3B-parameter custom SLM "
                "(Empathetic AI™)</strong> from zero, personally engineering the Python API layer "
                "— async queues, API call scripts — on a Supabase/Postgres backend with HITL "
                "fine-tuning pipeline and Cloudflare CDN.",

                "Launched a <strong>B2B AIaaS distribution model</strong> licensing the model via "
                "API to healthcare orgs and SMBs for customer service, lead generation, and "
                "clinical support — the same API-first enterprise architecture that defines the "
                "modern AI infrastructure market.",

                "Secured <strong>venture capital funding</strong> by translating a complex "
                "multi-layer AI architecture (community data → custom SLM → agentic B2B API) "
                "into clear business value narratives for VC investors.",
            ],
        },
        {
            "company":  "Deloitte",
            "title":    "Manager, Solutions Architect & Delivery Lead",
            "location": "LSHC Practice, Mexico Delivery Center",
            "start":    "May 2023",
            "end":      "July 2025",
            "current":  False,
            "bullets": [
                "Reduced production defects <strong>90%</strong> (40 → 5 in a single release) "
                "across 4 regional workstreams (Canada, US, LATAM) via a systematic regression "
                "testing framework across 300+ user stories.",

                "Accelerated enterprise sales cycles by designing "
                "<strong>high-impact technical demonstrations and solutioning workshops</strong> "
                "for C-level and engineering stakeholders — contributing to a Q4 2024 scope "
                "expansion and two-role team expansion in H1 2025.",

                "Productized a recurring client workflow gap into a "
                "<strong>reusable JS/Jest solution</strong>, converting repeated customer pain "
                "points into a tested, scalable product asset.",

                "Created <strong>comprehensive customer-facing technical documentation</strong> "
                "— developer guides, API onboarding playbooks, training materials — for every "
                "engagement, enabling self-service adoption and reducing onboarding friction.",

                "Built Deloitte's <strong>first LSHC practitioner program</strong> from 0 to "
                "40+ practitioners across 60+ structured learning hours, securing executive "
                "sponsorship and organizing the first-ever LSHC Summit in Querétaro.",
            ],
        },
        {
            "company":  "Deloitte",
            "title":    "Senior Salesforce Consultant",
            "location": "LSHC Practice",
            "start":    "April 2021",
            "end":      "May 2023",
            "current":  False,
            "bullets": [
                "Secured a contract renewal with a <strong>40% team expansion budget</strong>, "
                "earning 3 formal client recognition communications and 2 internal excellence "
                "awards across 2 years.",

                "Architected the <strong>\"Check on Mom\"</strong> patient outreach platform — "
                "selected for inclusion in VP Kamala Harris's Maternal Health Day Initiative "
                "action plan.",

                "Converted repeated customer UI/UX requirements into a "
                "<strong>reusable Lightning Web Components library</strong>, winning the "
                "LWC ConFest Award as the sole LATAM rep among 75+ international teams.",
            ],
        },
        {
            "company":  "The Ksquare Group",
            "title":    "Salesforce Consultant → Junior Developer & Technical PM",
            "location": "",
            "start":    "January 2020",
            "end":      "March 2021",
            "current":  False,
            "bullets": [
                "Delivered a <strong>95% first-pass success rate</strong> on a 14M+ record "
                "Salesforce migration within a 2-month deadline via Talend + Autorabit, with "
                "full dependency analysis and end-to-end UAT.",

                "Improved PMO operational efficiency by <strong>75%+</strong> by establishing "
                "Agile delivery standards and stakeholder frameworks — directly securing multiple "
                "contract renewals.",
            ],
        },
        {
            "company":  "Sirena App",
            "title":    "Customer Success Lead & Technical Team Leader",
            "location": "WhatsApp Integration",
            "start":    "June 2019",
            "end":      "December 2019",
            "current":  False,
            "bullets": [
                "Converted <strong>70+ at-risk accounts to VIP</strong> within 2.5 months "
                "(85% retention) via a SQL-driven account health analytics framework.",

                "Scaled operations from <strong>1 to 9 LATAM professionals</strong> in under "
                "6 months, achieving a 95% BSP migration success rate.",
            ],
        },
    ],
}


# ─────────────────────────────────────────────────────────────────────────────
#  TEMPLATE  ── HTML / CSS / JS — edit only if redesigning
# ─────────────────────────────────────────────────────────────────────────────

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8"/>
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>{{ name.first }} {{ name.last }} — CV for {{ target }}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>
    /* ── TOKENS ── */
    :root {
      color-scheme: dark;
      --bg:         #0A0A0A;
      --bg-2:       #111111;
      --bg-3:       #191919;
      --bg-hover:   #1c1c1c;
      --border:     rgba(255,255,255,0.07);
      --border-2:   rgba(255,255,255,0.12);
      --text-1:     #FAFAFA;
      --text-2:     #A1A1AA;
      --text-3:     #52525B;
      --accent:     #F97316;
      --accent-dim: rgba(249,115,22,0.12);
      --ease:       cubic-bezier(0.4,0,0.2,1);
    }
    * { margin:0; padding:0; box-sizing:border-box; }

    /* ── BASE ── */
    body {
      font-family:'Inter',-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
      background:var(--bg); color:var(--text-1);
      font-size:12.5px; line-height:1.6;
      -webkit-font-smoothing:antialiased;
    }

    /* ── PRINT ── */
    @media print {
      #progress-bar, .exp-toggle-btn, .expand-all-btn { display:none !important; }
      body { background:#fff; color:#111; font-size:11px; }
      :root {
        --bg:#fff; --bg-2:#f5f5f5; --bg-3:#eee; --bg-hover:#eee;
        --border:rgba(0,0,0,0.1); --border-2:rgba(0,0,0,0.18);
        --text-1:#111; --text-2:#444; --text-3:#888;
        --accent:#e05e10; --accent-dim:rgba(224,94,16,0.08);
      }
      .page { max-width:100%; box-shadow:none; border:none; margin:0; border-radius:0; }
      .waveform { display:none; }
      a { color:inherit; text-decoration:none; }
      .exp-body { max-height:none !important; opacity:1 !important; }
      [data-reveal] { opacity:1 !important; transform:none !important; }
    }

    /* ── PROGRESS BAR ── */
    #progress-bar {
      position:fixed; top:0; left:0; width:0%; height:2px;
      background:linear-gradient(90deg, var(--accent), #fb923c);
      z-index:9999; transition:width 0.08s linear;
      box-shadow:0 0 8px rgba(249,115,22,0.5);
    }

    /* ── PAGE ── */
    .page {
      max-width:900px; margin:40px auto 80px;
      border:1px solid var(--border-2); border-radius:14px;
      overflow:hidden;
      box-shadow:0 0 0 1px var(--border), 0 40px 100px rgba(0,0,0,0.7);
      /* entrance */
      opacity:0; transform:translateY(24px);
      transition:opacity 0.6s var(--ease), transform 0.6s var(--ease);
    }
    .page.visible { opacity:1; transform:translateY(0); }

    /* ── HEADER ── */
    .header {
      background:var(--bg-2); padding:36px 40px 30px;
      border-bottom:1px solid var(--border);
      position:relative; overflow:hidden;
    }
    .header-dot-grid {
      position:absolute; inset:0;
      background-image:radial-gradient(circle,rgba(255,255,255,.04) 1px,transparent 1px);
      background-size:20px 20px; pointer-events:none;
    }
    .header-inner {
      position:relative; z-index:1;
      display:flex; align-items:flex-start;
      justify-content:space-between; gap:24px;
    }
    .name {
      font-size:30px; font-weight:700; letter-spacing:-.5px;
      line-height:1.1; margin-bottom:4px;
      /* name slide-in */
      opacity:0; transform:translateX(-16px);
      transition:opacity 0.5s 0.2s var(--ease), transform 0.5s 0.2s var(--ease);
    }
    .name.visible { opacity:1; transform:translateX(0); }
    .name span { color:var(--accent); }

    .role-label {
      font-size:12px; font-weight:500; color:var(--text-2);
      letter-spacing:.04em; margin-bottom:16px;
      opacity:0; transform:translateX(-12px);
      transition:opacity 0.5s 0.35s var(--ease), transform 0.5s 0.35s var(--ease);
    }
    .role-label.visible { opacity:1; transform:translateX(0); }

    .contact-row {
      display:flex; flex-wrap:wrap; gap:6px 16px;
      font-size:11.5px; color:var(--text-2);
      opacity:0;
      transition:opacity 0.5s 0.5s var(--ease);
    }
    .contact-row.visible { opacity:1; }
    .contact-row a { color:var(--text-2); text-decoration:none; transition:color 0.2s; }
    .contact-row a:hover { color:var(--accent); }
    .contact-item { display:flex; align-items:center; gap:5px; }
    .contact-dot { width:3px; height:3px; border-radius:50%; background:var(--text-3); }

    /* ── WAVEFORM ── */
    .waveform { display:flex; align-items:flex-end; gap:3px; height:40px; opacity:.3; }
    .waveform-bar {
      width:3px; border-radius:2px; background:var(--accent);
      animation:wave 1.4s ease-in-out infinite;
      transition:height 0.3s ease;
    }
    .waveform:hover { opacity:.7; }
    .waveform:hover .waveform-bar { animation-duration:0.6s; }
    {{ waveform_css }}
    @keyframes wave { 0%,100%{transform:scaleY(1)} 50%{transform:scaleY(0.3)} }

    /* ── CURRENT BADGE PULSE ── */
    @keyframes pulse-border {
      0%,100% { box-shadow:0 0 0 0 rgba(249,115,22,0.4); }
      50%      { box-shadow:0 0 0 4px rgba(249,115,22,0); }
    }
    .current-badge {
      font-size:9px; font-weight:600; letter-spacing:.06em; text-transform:uppercase;
      color:var(--accent); background:var(--accent-dim);
      border:1px solid rgba(249,115,22,.3); border-radius:3px; padding:1px 6px;
      animation:pulse-border 2.4s ease infinite;
    }

    /* ── BODY GRID ── */
    .body { display:grid; grid-template-columns:250px 1fr; }

    /* ── SIDEBAR ── */
    .sidebar {
      background:var(--bg-2); border-right:1px solid var(--border);
      padding:28px 24px; display:flex; flex-direction:column; gap:28px;
    }

    /* ── MAIN ── */
    .main {
      background:var(--bg); padding:28px 32px;
      display:flex; flex-direction:column; gap:28px;
    }

    /* ── SECTION LABELS ── */
    .section-label {
      font-size:9.5px; font-weight:600; letter-spacing:.12em;
      text-transform:uppercase; color:var(--text-3); margin-bottom:12px;
      display:flex; align-items:center; gap:8px;
    }
    .section-label::after { content:''; flex:1; height:1px; background:var(--border); }

    .section-header-row {
      display:flex; align-items:center; justify-content:space-between;
      margin-bottom:12px;
    }
    .section-header-row .section-label { margin-bottom:0; flex:1; }

    /* ── EXPAND ALL BUTTON ── */
    .expand-all-btn {
      font-size:10px; font-weight:500; letter-spacing:.04em;
      color:var(--text-3); background:transparent;
      border:1px solid var(--border); border-radius:5px;
      padding:3px 10px; cursor:pointer;
      transition:color 0.2s, border-color 0.2s, background 0.2s;
      white-space:nowrap;
    }
    .expand-all-btn:hover { color:var(--accent); border-color:rgba(249,115,22,.3); background:var(--accent-dim); }

    /* ── SKILL TAGS ── */
    .skill-group { margin-bottom:12px; }
    .skill-group-label { font-size:10px; font-weight:600; color:var(--accent); letter-spacing:.05em; margin-bottom:6px; }
    .skill-tags { display:flex; flex-wrap:wrap; gap:4px; }
    .tag {
      font-size:10.5px; color:var(--text-2);
      background:var(--bg-3); border:1px solid var(--border);
      border-radius:4px; padding:2px 7px; line-height:1.6;
      cursor:default;
      transition:color 0.2s, background 0.2s, border-color 0.2s, transform 0.15s;
    }
    .tag:hover {
      color:var(--text-1); background:var(--bg-hover);
      border-color:var(--border-2); transform:translateY(-1px);
    }
    .tag.accent {
      color:var(--accent); background:var(--accent-dim);
      border-color:rgba(249,115,22,.2); font-weight:500;
    }
    .tag.accent:hover {
      background:rgba(249,115,22,0.2); border-color:rgba(249,115,22,.4);
      transform:translateY(-1px);
    }

    /* ── SIDEBAR LISTS ── */
    .sidebar-list { list-style:none; display:flex; flex-direction:column; gap:5px; }
    .sidebar-list li {
      font-size:11px; color:var(--text-2); padding-left:10px;
      position:relative; line-height:1.5;
      transition:color 0.2s;
    }
    .sidebar-list li::before {
      content:''; position:absolute; left:0; top:7px;
      width:4px; height:4px; border-radius:50%; background:var(--text-3);
      transition:background 0.2s, transform 0.2s;
    }
    .sidebar-list li:hover { color:var(--text-1); }
    .sidebar-list li:hover::before { background:var(--accent); transform:scale(1.3); }
    .sidebar-list li.highlight { color:var(--text-1); }
    .sidebar-list li.highlight::before { background:var(--accent); }

    /* ── EDUCATION ── */
    .edu-item { margin-bottom:8px; }
    .edu-school { font-size:11.5px; font-weight:500; }
    .edu-degree { font-size:10.5px; color:var(--text-2); }

    /* ── SUMMARY ── */
    .summary-text {
      font-size:12.5px; color:var(--text-2); line-height:1.75;
      border-left:2px solid var(--accent); padding-left:14px;
      transition:border-color 0.3s;
    }
    .summary-text:hover { border-color:#fb923c; }
    .summary-text strong { color:var(--text-1); font-weight:500; }

    /* ── EXPERIENCE ITEMS ── */
    .exp-item {
      border-radius:8px;
      border:1px solid transparent;
      padding:14px;
      margin:-14px;
      margin-bottom:8px;
      transition:background 0.25s var(--ease), border-color 0.25s var(--ease);
      /* scroll-reveal */
      opacity:0; transform:translateY(14px);
      transition:opacity 0.45s var(--ease), transform 0.45s var(--ease),
                 background 0.25s var(--ease), border-color 0.25s var(--ease);
    }
    .exp-item.revealed { opacity:1; transform:translateY(0); }
    .exp-item:not(:last-child) { border-bottom:1px solid var(--border); padding-bottom:22px; margin-bottom:22px; }
    .exp-item:hover { background:var(--bg-hover); border-color:var(--border); }

    /* ── CLICKABLE JOB HEADER ── */
    .exp-header {
      display:flex; align-items:flex-start;
      justify-content:space-between; gap:12px;
      cursor:pointer; user-select:none;
      padding-bottom:4px;
    }
    .exp-header-left { flex:1; min-width:0; }
    .exp-header-right { display:flex; align-items:center; gap:10px; flex-shrink:0; }

    .exp-company {
      font-size:13.5px; font-weight:600;
      display:flex; align-items:center; gap:7px;
    }
    .exp-dates { font-size:10.5px; color:var(--text-3); white-space:nowrap; padding-top:2px; }

    /* ── CHEVRON ── */
    .chevron {
      color:var(--text-3); flex-shrink:0;
      transition:transform 0.35s var(--ease), color 0.2s;
    }
    .exp-item:hover .chevron { color:var(--text-2); }
    .exp-item.collapsed .chevron { transform:rotate(-90deg); }

    /* ── JOB TITLE ── */
    .exp-title { font-size:11.5px; font-weight:500; color:var(--accent); margin-bottom:10px; }

    /* ── COLLAPSIBLE BODY ── */
    .exp-body {
      overflow:hidden;
      max-height:600px;
      opacity:1;
      transition:max-height 0.45s var(--ease), opacity 0.3s var(--ease);
    }
    .exp-item.collapsed .exp-body { max-height:0; opacity:0; }

    /* ── BULLETS ── */
    .exp-bullets { list-style:none; display:flex; flex-direction:column; gap:6px; }
    .exp-bullets li {
      font-size:11.5px; color:var(--text-2); padding-left:14px;
      position:relative; line-height:1.65;
      opacity:0; transform:translateX(-8px);
      transition:opacity 0.3s var(--ease), transform 0.3s var(--ease),
                 color 0.2s;
    }
    .exp-item.revealed .exp-bullets li { opacity:1; transform:translateX(0); }
    .exp-item.revealed .exp-bullets li:nth-child(1) { transition-delay:0.05s; }
    .exp-item.revealed .exp-bullets li:nth-child(2) { transition-delay:0.1s; }
    .exp-item.revealed .exp-bullets li:nth-child(3) { transition-delay:0.15s; }
    .exp-item.revealed .exp-bullets li:nth-child(4) { transition-delay:0.2s; }
    .exp-bullets li::before {
      content:'—'; position:absolute; left:0;
      color:var(--text-3); font-size:10px; top:1px;
    }
    .exp-bullets li:hover { color:var(--text-1); }
    .exp-bullets li strong { color:var(--text-1); font-weight:500; }

    /* ── VOICE INTRO BAND ── */
    .voice-band {
      background:linear-gradient(90deg, #111111 0%, #0f0f0f 60%, #130d08 100%);
      border-bottom:1px solid var(--border);
      border-top:1px solid var(--border);
      padding:20px 40px;
      position:relative; overflow:hidden;
    }
    .voice-band::before {
      content:'';
      position:absolute; top:0; left:0; right:0; height:1px;
      background:linear-gradient(90deg, transparent, var(--accent), transparent);
      opacity:0.4;
    }
    .voice-band-inner {
      display:flex; align-items:center; gap:24px;
    }
    .voice-info {
      display:flex; align-items:center; gap:14px; flex-shrink:0;
    }
    .voice-icon-wrap {
      width:40px; height:40px; border-radius:8px;
      background:var(--accent-dim);
      border:1px solid rgba(249,115,22,0.25);
      display:flex; align-items:center; justify-content:center;
      flex-shrink:0;
      animation:pulse-border 2.4s ease infinite;
    }
    .voice-icon-wrap svg { color:var(--accent); }
    .voice-title {
      font-size:12px; font-weight:600; color:var(--text-1);
      letter-spacing:-.1px; margin-bottom:2px;
    }
    .voice-meta {
      font-size:10px; color:var(--text-3);
      letter-spacing:.02em; margin-bottom:6px;
    }
    .voice-listen-btn {
      display:inline-flex; align-items:center; gap:5px;
      font-size:10px; font-weight:500; color:var(--accent);
      background:var(--accent-dim);
      border:1px solid rgba(249,115,22,0.25); border-radius:4px;
      padding:3px 9px; text-decoration:none;
      transition:background 0.2s, border-color 0.2s, transform 0.15s;
    }
    .voice-listen-btn:hover {
      background:rgba(249,115,22,0.2); border-color:rgba(249,115,22,0.45);
      transform:translateY(-1px);
    }
    .voice-player {
      flex:1; min-width:0;
      border-radius:6px; overflow:hidden;
      border:1px solid var(--border);
    }
    .voice-player iframe { display:block; border-radius:6px; }
    @media print { .voice-band { display:none; } }

    /* ── FOOTER ── */
    .footer-bar {
      background:var(--bg-2); border-top:1px solid var(--border);
      padding:10px 40px; display:flex; align-items:center;
      justify-content:space-between; font-size:10px; color:var(--text-3);
    }
    .footer-bar a { color:var(--text-3); text-decoration:none; transition:color 0.2s; }
    .footer-bar a:hover { color:var(--accent); }
    .el-wordmark { font-size:10px; font-weight:600; letter-spacing:.08em; text-transform:uppercase; opacity:.4; }
  </style>
</head>
<body>

<!-- Reading progress bar -->
<div id="progress-bar"></div>

<div class="page" id="cv-page">

  <!-- ── HEADER ── -->
  <div class="header">
    <div class="header-dot-grid"></div>
    <div class="header-inner">
      <div>
        <div class="name" id="anim-name">{{ name.first }}&nbsp;<span>{{ name.last }}</span></div>
        <div class="role-label" id="anim-role">{{ tagline }}</div>
        <div class="contact-row" id="anim-contact">
          <span class="contact-item">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></svg>
            {{ location }}
          </span>
          <div class="contact-dot"></div>
          <span class="contact-item">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07A19.5 19.5 0 0 1 4.76 12a19.79 19.79 0 0 1-3.07-8.63A2 2 0 0 1 3.68 1h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L7.91 8.1a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
            {{ phone }}
          </span>
          <div class="contact-dot"></div>
          <span class="contact-item">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
            {{ email }}
          </span>
          <div class="contact-dot"></div>
          <span class="contact-item">
            <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z"/><rect x="2" y="9" width="4" height="12"/><circle cx="4" cy="4" r="2"/></svg>
            <a href="{{ linkedin.url }}" target="_blank">{{ linkedin.display }}</a>
          </span>
        </div>
      </div>
      <div class="waveform" title="ElevenLabs — Voice AI">
        {% for _ in waveform_bars %}<div class="waveform-bar"></div>{% endfor %}
      </div>
    </div>
  </div>

  <!-- ── VOICE INTRO BAND ── -->
  {% if voice_intro %}
  <div class="voice-band">
    <div class="voice-band-inner">
      <div class="voice-info">
        <div class="voice-icon-wrap">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor"
               stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/>
            <path d="M19 10v2a7 7 0 0 1-14 0v-2"/><line x1="12" y1="19" x2="12" y2="23"/>
            <line x1="8" y1="23" x2="16" y2="23"/>
          </svg>
        </div>
        <div>
          <div class="voice-title">{{ voice_intro.title }}</div>
          <div class="voice-meta">{{ voice_intro.subtitle }}</div>
          <a class="voice-listen-btn" href="{{ voice_intro.url }}" target="_blank">
            <svg width="10" height="10" viewBox="0 0 24 24" fill="none" stroke="currentColor"
                 stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
              <polygon points="5 3 19 12 5 21 5 3"/>
            </svg>
            Listen on SoundCloud
          </a>
        </div>
      </div>
      <div class="voice-player">
        <iframe
          width="100%" height="120" scrolling="no" frameborder="no" allow="autoplay"
          src="{{ voice_intro.embed }}">
        </iframe>
      </div>
    </div>
  </div>
  {% endif %}

  <!-- ── BODY ── -->
  <div class="body">

    <!-- ── SIDEBAR ── -->
    <div class="sidebar">

      <div>
        <div class="section-label">Core Competencies</div>
        {% for group in skill_groups %}
        <div class="skill-group">
          <div class="skill-group-label">{{ group.label }}</div>
          <div class="skill-tags">
            {% for tag in group.tags %}
            <span class="tag{% if tag.accent %} accent{% endif %}">{{ tag.name }}</span>
            {% endfor %}
          </div>
        </div>
        {% endfor %}
      </div>

      <div>
        <div class="section-label">Certifications</div>
        <ul class="sidebar-list">
          {% for cert in certifications %}
          <li>{{ cert }}</li>
          {% endfor %}
        </ul>
      </div>

      <div>
        <div class="section-label">Education</div>
        {% for edu in education %}
        <div class="edu-item">
          <div class="edu-school">{{ edu.school }}</div>
          <div class="edu-degree">{{ edu.degree }}</div>
        </div>
        {% endfor %}
      </div>

      <div>
        <div class="section-label">Achievements</div>
        <ul class="sidebar-list">
          {% for ach in achievements %}
          <li{% if ach.highlight %} class="highlight"{% endif %}>{{ ach.text }}</li>
          {% endfor %}
        </ul>
      </div>

    </div>

    <!-- ── MAIN ── -->
    <div class="main">

      <div>
        <div class="section-label">Professional Summary</div>
        <p class="summary-text">{{ summary }}</p>
      </div>

      <div>
        <div class="section-header-row">
          <div class="section-label">Experience</div>
          <button class="expand-all-btn" id="expandAllBtn">Collapse All</button>
        </div>

        {% for job in experience %}
        <div class="exp-item" id="job-{{ loop.index }}">

          <!-- Clickable header -->
          <div class="exp-header" onclick="toggleJob('job-{{ loop.index }}')">
            <div class="exp-header-left">
              <div class="exp-company">
                {{ job.company }}
                {% if job.current %}<span class="current-badge">Current</span>{% endif %}
              </div>
              <div class="exp-title">
                {{ job.title }}{% if job.location %} &nbsp;·&nbsp; {{ job.location }}{% endif %}
              </div>
            </div>
            <div class="exp-header-right">
              <div class="exp-dates">{{ job.start }} — {{ job.end }}</div>
              <svg class="chevron" width="14" height="14" viewBox="0 0 24 24" fill="none"
                   stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="6 9 12 15 18 9"/>
              </svg>
            </div>
          </div>

          <!-- Collapsible body -->
          <div class="exp-body">
            <ul class="exp-bullets">
              {% for bullet in job.bullets %}
              <li>{{ bullet }}</li>
              {% endfor %}
            </ul>
          </div>

        </div>
        {% endfor %}
      </div>

    </div>
  </div>

  <!-- ── FOOTER ── -->
  <div class="footer-bar">
    <span>{{ email }} &nbsp;·&nbsp; <a href="{{ linkedin.url }}">{{ linkedin.display }}</a></span>
    <span class="el-wordmark">Prepared for {{ target }} &nbsp;·&nbsp; Generated {{ generated_at }}</span>
  </div>

</div><!-- /page -->

<script>
  /* ── PAGE ENTRANCE ── */
  requestAnimationFrame(() => {
    document.getElementById('cv-page').classList.add('visible');
    setTimeout(() => document.getElementById('anim-name').classList.add('visible'),    150);
    setTimeout(() => document.getElementById('anim-role').classList.add('visible'),    300);
    setTimeout(() => document.getElementById('anim-contact').classList.add('visible'), 450);
  });

  /* ── READING PROGRESS BAR ── */
  const bar = document.getElementById('progress-bar');
  window.addEventListener('scroll', () => {
    const total = document.documentElement.scrollHeight - window.innerHeight;
    bar.style.width = total > 0 ? (window.scrollY / total * 100) + '%' : '0%';
  }, { passive: true });

  /* ── SCROLL-REVEAL ── */
  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if (e.isIntersecting) {
        e.target.classList.add('revealed');
        revealObserver.unobserve(e.target);
      }
    });
  }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.exp-item').forEach((el, i) => {
    el.style.transitionDelay = (i * 0.07) + 's';
    revealObserver.observe(el);
  });

  /* ── EXPAND / COLLAPSE JOB ── */
  function toggleJob(id) {
    const item = document.getElementById(id);
    item.classList.toggle('collapsed');
    syncExpandAllLabel();
  }

  /* ── EXPAND ALL / COLLAPSE ALL ── */
  const expandBtn = document.getElementById('expandAllBtn');
  function syncExpandAllLabel() {
    const total     = document.querySelectorAll('.exp-item').length;
    const collapsed = document.querySelectorAll('.exp-item.collapsed').length;
    expandBtn.textContent = collapsed > 0 ? 'Expand All' : 'Collapse All';
  }

  expandBtn.addEventListener('click', () => {
    const anyCollapsed = document.querySelectorAll('.exp-item.collapsed').length > 0;
    document.querySelectorAll('.exp-item').forEach(el => {
      if (anyCollapsed) el.classList.remove('collapsed');
      else              el.classList.add('collapsed');
    });
    syncExpandAllLabel();
  });
</script>
</body>
</html>"""


# ─────────────────────────────────────────────────────────────────────────────
#  GENERATOR  ── no editing needed below this line
# ─────────────────────────────────────────────────────────────────────────────

def generate(data: dict, output_path: str = None) -> Path:
    env = Environment(autoescape=False)
    template = env.from_string(TEMPLATE)

    # Pre-compute waveform CSS so the template needs no range() calls
    _heights = [12, 28, 20, 36, 16, 32, 22, 38, 14, 26, 18, 30, 10]
    waveform_css = "\n    ".join(
        f".waveform-bar:nth-child({i+1}) {{ height:{h}px; animation-delay:{i*0.1:.1f}s; }}"
        for i, h in enumerate(_heights)
    )

    data = {
        **data,
        "generated_at":  datetime.now().strftime("%B %d, %Y"),
        "waveform_css":  waveform_css,
        "waveform_bars": list(range(13)),   # plain list — fully iterable in Jinja2
    }

    html = template.render(**data)

    if output_path is None:
        first = data["name"]["first"]
        last  = data["name"]["last"]
        target = data["target"].replace(" ", "_")
        output_path = Path(__file__).parent / f"{first}_{last}_{target}_CV.html"

    out = Path(output_path)
    out.write_text(html, encoding="utf-8")
    print(f"✓  CV written → {out.resolve()}")
    return out


if __name__ == "__main__":
    generate(CV_DATA)
