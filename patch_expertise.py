import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_marker = "<!-- QUICK SNAPSHOT SECTION -->"
end_marker = "<!-- PROJECTS -->"

start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    new_section = """<!-- AREAS OF EXPERTISE -->
    <section class="expertise-section highlights-section" id="expertise" style="padding-top: 100px;">
        <div class="two-col fade-in">
            <div>
                <p class="two-col-label">01 — Areas of Expertise</p>
            </div>
            <div class="two-col-content">
                <h2 style="font-family: 'Cormorant Garamond', serif; font-size: clamp(36px, 5vw, 48px); font-weight: 400; color: var(--terracotta); margin-bottom: 16px;">Quick Highlights</h2>
                <p style="font-size: 14px; color: var(--muted); line-height: 1.8; max-width: 480px;">A snapshot of my core experience, skills, and areas of focus in marketing, digital communication, and strategic content development.</p>
            </div>
        </div>

        <div class="projects-grid" style="margin-top: 60px;">
            <!-- Card 1 -->
            <div class="project-card fade-in" style="transition-delay:0.05s">
                <div class="project-info">
                    <p class="project-category">Core Focus</p>
                    <h3 class="project-title">Professional<br>Experience</h3>
                    <p class="project-desc">Hands-on experience in marketing, PR, and communications through internships with nonprofit and youth-focused organizations.</p>
                </div>
            </div>

            <!-- Card 2 -->
            <div class="project-card fade-in" style="transition-delay:0.1s">
                <div class="project-info">
                    <p class="project-category">Core Focus</p>
                    <h3 class="project-title">Marketing Strategy<br>Projects</h3>
                    <p class="project-desc">Academic projects focused on campaign planning, consumer research, and brand positioning.</p>
                </div>
            </div>

            <!-- Card 3 -->
            <div class="project-card fade-in" style="transition-delay:0.15s">
                <div class="project-info">
                    <p class="project-category">Core Focus</p>
                    <h3 class="project-title">Digital Marketing<br>Skills</h3>
                    <p class="project-desc">Foundational knowledge in SEO, email marketing, social media strategy, and digital analytics.</p>
                </div>
            </div>

            <!-- Card 4 -->
            <div class="project-card fade-in" style="transition-delay:0.2s">
                <div class="project-info">
                    <p class="project-category">Core Focus</p>
                    <h3 class="project-title">Content & PR<br>Strategy</h3>
                    <p class="project-desc">Experience developing storytelling frameworks, communication narratives, and digital content strategies.</p>
                </div>
            </div>
        </div>
    </section>

    """
    
    new_content = content[:start_idx] + new_section + content[end_idx:]
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Patched index.html successfully.")
else:
    print("Could not find markers.")
