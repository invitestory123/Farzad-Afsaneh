import re

with open('poyan_reference.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update Title and Meta
html = re.sub(r'<title>.*?</title>', '<title>Afsaneh &amp; Farzad | محفل شیرینی خوری</title>', html)
html = re.sub(
    r'<meta name="description" content=".*?">',
    '<meta name="description" content="Engagement &amp; Shirinikhori celebration of Afsaneh &amp; Farzad (محفل شیرینی خوری), Monday, December 14, 2026 at 5 PM at Sunrise Event Center &amp; Banquet Hall, Rancho Cordova.">',
    html
)

# 2. Update Hero Section
old_hero_names = re.search(r'<h1 style="margin:0;display:flex;flex-direction:column;align-items:center">.*?</h1>', html, re.DOTALL)
if old_hero_names:
    new_hero_names = '''<h1 style="margin:0;display:flex;flex-direction:column;align-items:center">
          <span class="name foil rv" style="--d:.35s">Afsaneh</span>
          <span class="amp rv" style="--d:.55s" aria-label="and">&amp;</span>
          <span class="name foil rv" style="--d:.75s">Farzad</span>
        </h1>'''
    html = html.replace(old_hero_names.group(0), new_hero_names)

old_lead = re.search(r'<p class="lead rv" style="--d:1.5s">.*?</p>', html, re.DOTALL)
if old_lead:
    new_lead = '''<p class="lead rv" style="--d:1.15s">You are warmly invited to celebrate our<br>Engagement &amp; Shirinikhori Party</p>'''
    html = html.replace(old_lead.group(0), new_lead)

# 3. Update Poem Section to include "محفل شیرینی خوری"
old_poem = re.search(r'<section class="poem".*?</section>', html, re.DOTALL)
if old_poem:
    new_poem = '''<section class="poem" aria-label="Poem" dir="rtl" lang="fa">
        <p class="shirinikhori-title foil rv" style="font-family:'Nastaliq Embedded','Noto Nastaliq Urdu',serif;font-size:clamp(28px,9cqi,46px);line-height:2.2;margin:0 0 .15em;color:var(--gold);letter-spacing:0">محفل شیرینی خوری</p>
        <p class="verse foil rv">رواق منظر چشم من آشیانه توست</p>
        <p class="verse foil rv" style="--d:.15s">کرم نما و فرود آ که خانه خانه توست</p>
        <p class="poet rv" style="--d:.3s">حافظ</p>
      </section>'''
    html = html.replace(old_poem.group(0), new_poem)

# 4. Update Date Section
html = re.sub(r'<p class="month rv">.*?</p>', '<p class="month rv">December</p>', html)
old_dateline = re.search(r'<div class="dateline rv">.*?</div>', html, re.DOTALL)
if old_dateline:
    new_dateline = '''<div class="dateline rv">
          <span class="side">Monday</span>
          <span class="day foil">14</span>
          <span class="side">2026</span>
        </div>'''
    html = html.replace(old_dateline.group(0), new_dateline)

# Update Google Calendar link
old_cal = re.search(r'<a class="calendar rv"[^>]*>.*?</a>', html)
if old_cal:
    cal_url = ("https://calendar.google.com/calendar/render?action=TEMPLATE"
               "&text=Engagement%20of%20Afsaneh%20%26%20Farzad%20(%D9%85%D8%AD%D9%81%D9%84%20%D8%B4%DB%8C%D8%B1%DB%8C%D9%86%DB%8C%20%D8%AE%D9%88%D8%B1%DB%8C)"
               "&dates=20261215T010000Z/20261215T060000Z"
               "&location=Sunrise%20Event%20Center%20%26%20Banquet%20Hall%2C%2011167%20Trade%20Center%20Drive%2C%20Suite%20A1%2C%20Rancho%20Cordova%2C%20CA%2095670"
               "&details=Engagement%20%26%20Shirinikhori%20celebration%20of%20Afsaneh%20%26%20Farzad%20(%D9%85%D8%AD%D9%81%D9%84%20%D8%B4%DB%8C%D8%B1%DB%8C%D9%86%DB%8C%20%D8%AE%D9%88%D8%B1%DB%8C).")
    new_cal = f'<a class="calendar rv" target="_blank" rel="noopener" href="{cal_url}">Add to calendar</a>'
    html = html.replace(old_cal.group(0), new_cal)

# 5. Update Venue Section
html = re.sub(
    r'<p class="venue-name foil rv">.*?</p>',
    '<p class="venue-name foil rv">Sunrise Event Center &amp; Banquet Hall</p><p class="venue-sub rv" style="font-family:var(--f-serif);font-size:clamp(16px,5cqi,22px);margin:2cqi 0 1cqi;color:var(--ink-soft);font-style:italic">11167 Trade Center Drive, Suite A1<br>Rancho Cordova, CA 95670</p>',
    html
)

maps_url = "https://www.google.com/maps/search/?api=1&query=Sunrise+Event+Center+%26+Banquet+Hall+11167+Trade+Center+Dr+Rancho+Cordova+CA+95670"
html = re.sub(r'href="https://maps\.app\.goo\.gl/[^"]*"', f'href="{maps_url}"', html)

# 6. Update Guest Notes (Ladies only -> comment or remove, keep No kids, please)
html = html.replace('<h2 class="foil rv ladies">Ladies only</h2>', '<!-- <h2 class="foil rv ladies">Ladies only</h2> -->')

# 7. Update Footer Monogram Artwork and Caption
old_portrait = re.search(r'<div class="portrait">.*?</div>\s*</footer>', html, re.DOTALL)
if old_portrait:
    new_portrait = '''<div class="portrait">
          <img src="assets/couple.jpg" onerror="this.onerror=null;this.src='assets/couple.svg';" alt="Afsaneh and Farzad" loading="lazy">
          <div class="scrim" aria-hidden="true"></div>
          <div class="ring" aria-hidden="true"></div>
          <div class="caption">
            <p class="mono foil">Afsaneh<em>&amp;</em>Farzad</p>
            <p style="font-family:'Nastaliq Embedded','Noto Nastaliq Urdu',serif;font-size:clamp(18px,5.5cqi,28px);margin:0;color:#f3e6ce;line-height:1.8">محفل شیرینی خوری</p>
            <small>14 · 12 · 2026</small>
          </div>
        </div>
      </footer>'''
    html = html.replace(old_portrait.group(0), new_portrait)

# 8. Update Music / Config in Javascript
old_config = re.search(r'var CONFIG = \{.*?\};', html, re.DOTALL)
if old_config:
    new_config = '''var CONFIG = {
  // Direct link to the trimmed MP3 file (first 13 seconds cut off)
  mp3Url: "./music.mp3",
  youtubeId: "C44KB6qEbYY",
  startSeconds: 13,
  weddingTime: "2026-12-14T17:00:00-08:00",
  // Web3Forms access key for RSVPs. Free key can be pasted here:
  web3formsKey: ""
};'''
    html = html.replace(old_config.group(0), new_config)

# Update RSVP email subject & from_name
html = html.replace('from_name: "Azim Poyan & Brishna Wedding RSVP"', 'from_name: "Afsaneh & Farzad Shirinikhori RSVP"')
html = html.replace('"RSVP: " + name', '"RSVP (محفل شیرینی خوری): " + name')

# Also fix the RSVP handling if web3formsKey is empty: open mailto email instead of showing an error!
old_rsvp_check = '''  if (!CONFIG.web3formsKey || CONFIG.web3formsKey.indexOf("__") === 0 || CONFIG.web3formsKey.indexOf("PASTE") === 0) {
    svcErr.textContent = "RSVP sending isn't set up yet. Please let the couple know, or try again later.";
    svcErr.hidden = false; return;
  }'''

new_rsvp_check = '''  if (!CONFIG.web3formsKey || CONFIG.web3formsKey.indexOf("__") === 0 || CONFIG.web3formsKey.indexOf("PASTE") === 0) {
    // Graceful fallback to mailto so RSVPs always work immediately!
    var mailtoBody = "Dear Afsaneh & Farzad,\\n\\n" +
      "Thank you for the warm invitation to your Engagement & Shirinikhori celebration (محفل شیرینی خوری).\\n\\n" +
      "Guest name: " + name + "\\n" +
      "Attendance: " + attending + "\\n" +
      "Message: " + (message || "(none)") + "\\n\\n" +
      "Warm regards,\\n" + name;
    var mailtoUrl = "mailto:?subject=" + encodeURIComponent("RSVP: " + name + " — " + attending + " (Afsaneh & Farzad Shirinikhori)") + "&body=" + encodeURIComponent(mailtoBody);
    window.location.href = mailtoUrl;
    form.hidden = true; thanks.hidden = false;
    thanksText.textContent = (attending === "Yes" ? "Thank you, " + name + "! Your reply email is ready in your mail app. We look forward to celebrating with you!" : "Thank you for letting us know, " + name + ". You will be dearly missed!");
    return;
  }'''
html = html.replace(old_rsvp_check, new_rsvp_check)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Regenerated index.html! File size:", len(html))
