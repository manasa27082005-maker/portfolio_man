import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "<!-- Module 1: SEO & Content (Largest) -->"
end_marker = "                </div>\n            </div>\n        </div>\n    </section>"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_section = """<!-- 1. Content Dev (Largest) -->
                    <a href="experience.html" class="expertise-module mod-content mod-xl anim-bubble" style="animation-delay: 0ms;">
                        <svg class="expertise-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"></path></svg>
                        <span class="expertise-label">Content<br>Development</span>
                    </a>
                    
                    <!-- 2. SEO (Second Largest) -->
                    <a href="experience.html" class="expertise-module mod-seo mod-l anim-bubble" style="animation-delay: 100ms;">
                        <svg class="expertise-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                        <span class="expertise-label">SEO & Content<br>Optimization</span>
                    </a>

                    <!-- 3. Social Media Strategy (Medium) -->
                    <a href="experience.html" class="expertise-module mod-social mod-md anim-bubble" style="animation-delay: 200ms;">
                        <svg class="expertise-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><line x1="4" y1="9" x2="20" y2="9"></line><line x1="4" y1="15" x2="20" y2="15"></line><line x1="10" y1="3" x2="8" y2="21"></line><line x1="16" y1="3" x2="14" y2="21"></line></svg>
                        <span class="expertise-label">Social Media<br>Strategy</span>
                    </a>

                    <!-- 4. Video & Reel Conceptualization (Medium) -->
                    <a href="experience.html" class="expertise-module mod-video mod-md anim-bubble" style="animation-delay: 300ms;">
                        <svg class="expertise-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><polygon points="10 8 16 12 10 16 10 8"></polygon></svg>
                        <span class="expertise-label">Video & Reel<br>Conceptualization</span>
                    </a>

                    <!-- 5. PR & Brand Storytelling (Small) -->
                    <a href="experience.html" class="expertise-module mod-pr mod-sm anim-bubble" style="animation-delay: 400ms;">
                        <svg class="expertise-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"></polygon><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"></path></svg>
                        <span class="expertise-label">Public Relations &<br>Brand Storytelling</span>
                    </a>

                    <!-- 6. Script & Narrative Writing (Small) -->
                    <a href="experience.html" class="expertise-module mod-script mod-sm anim-bubble" style="animation-delay: 500ms;">
                        <svg class="expertise-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"><path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"></path><path d="M19 10v2a7 7 0 0 1-14 0v-2"></path><line x1="12" y1="19" x2="12" y2="23"></line><line x1="8" y1="23" x2="16" y2="23"></line></svg>
                        <span class="expertise-label">Script & Narrative<br>Writing</span>
                    </a>
"""
    new_content = content[:start_idx] + new_section + content[end_idx:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Patched index.html successfully.")
else:
    print("Could not find markers.")
