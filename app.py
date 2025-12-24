from flask import Flask, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    image_url = url_for('static', filename='hero.jpg')
    qa_bg_url = url_for('static', filename='hero2.jpg')
    hero3_url = url_for('static', filename='hero3.jpg')
    hero6_url = url_for('static', filename='hero6.jpg') # Updated to hero6
    vid1_url = url_for('static', filename='climb1.mp4')
    vid3_url = url_for('static', filename='climb3.mp4')
    
    return f"""
    <html>
        <head>
            <title>The Bouldering Library</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
            <style>
                :root {{
                    --glass: rgba(255, 255, 255, 0.1);
                    --glass-dark: rgba(0, 0, 0, 0.7);
                    --border: 1px solid rgba(255, 255, 255, 0.2);
                }}

                body {{
                    font-family: 'Segoe UI', Roboto, sans-serif;
                    background: linear-gradient(135deg, #1e2a38 0%, #2c3e50 100%);
                    color: white;
                    text-align: center;
                    padding: 0;
                    margin: 0;
                    min-height: 100vh;
                    overflow-x: hidden;
                }}

                /* --- Header --- */
                .header-container {{
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 20px;
                    max-width: 1200px;
                    margin: 0 auto;
                }}
                .nav-buttons {{ display: flex; flex-direction: column; gap: 10px; }}
                .main-title {{ font-size: 2.2em; font-weight: 800; letter-spacing: -1px; }}

                .qa-btn {{ background: #3498db; color: white; padding: 12px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; width: 140px; }}
                .gyms-btn {{ background: #9b59b6; color: white; padding: 12px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; width: 140px; }}
                .dropbtn {{ background: #e67e22; color: white; padding: 12px 20px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; }}

                /* --- Hero Section --- */
                .hero-container {{
                    position: relative;
                    margin: 20px auto;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    gap: 15px;
                }}

                .click-hint {{
                    color: white;
                    font-weight: bold;
                    font-size: 0.9em;
                    animation: floatHint 2s infinite ease-in-out;
                    white-space: nowrap;
                }}

                @keyframes floatHint {{
                    0%, 100% {{ transform: translateX(0); }}
                    50% {{ transform: translateX(-10px); }}
                }}

                .hero-wrapper {{
                    width: 550px;
                    max-width: 85vw;
                    height: 380px;
                    border: 2px solid white;
                    border-radius: 24px;
                    overflow: hidden;
                    cursor: pointer;
                    position: relative;
                    background: #000;
                    box-shadow: 0 15px 35px rgba(0,0,0,0.4);
                }}

                .main-img {{ width: 100%; height: 100%; object-fit: cover; object-position: center; }}

                .slide {{
                    display: none;
                    width: 100%;
                    height: 100%;
                    background-size: cover;
                    background-position: center;
                    padding: 20px;
                    box-sizing: border-box;
                    flex-direction: column;
                    justify-content: flex-end;
                    position: relative;
                }}

                .slide-content {{
                    background: var(--glass-dark);
                    backdrop-filter: blur(8px);
                    padding: 15px;
                    border-radius: 15px;
                    border: var(--border);
                    font-size: 0.95em;
                    line-height: 1.4;
                    margin-bottom: 10px;
                }}

                .nav-arrow {{
                    position: absolute;
                    top: 50%;
                    transform: translateY(-50%);
                    background: rgba(255,255,255,0.2);
                    color: white;
                    border: 1px solid white;
                    width: 40px;
                    height: 40px;
                    border-radius: 50%;
                    z-index: 10;
                }}

                /* --- Video Cards --- */
                .video-container {{
                    display: flex;
                    justify-content: center;
                    gap: 15px;
                    padding: 20px;
                }}
                .video-item {{ width: 25%; max-height: 180px; object-fit: cover; border-radius: 16px; border: 1px solid white; }}

                /* --- QA Accordion Slide-down --- */
                .qa-section {{
                    max-height: 0;
                    overflow: hidden;
                    transition: max-height 0.5s ease-out;
                    background: var(--glass-dark);
                    width: 90%;
                    margin: 0 auto;
                    border-radius: 20px;
                }}
                .qa-section.open {{ max-height: 1000px; padding: 20px; margin-bottom: 20px; border: var(--border); }}

                .qa-row {{ margin-bottom: 10px; text-align: left; }}
                .qa-question {{
                    padding: 15px;
                    background: rgba(255,255,255,0.1);
                    border-radius: 10px;
                    cursor: pointer;
                    font-weight: bold;
                    display: flex;
                    justify-content: space-between;
                }}
                .qa-answer {{
                    max-height: 0;
                    overflow: hidden;
                    transition: all 0.3s ease;
                    padding: 0 15px;
                    color: #3498db;
                    font-style: italic;
                }}
                .qa-answer.show {{ max-height: 100px; padding: 10px 15px; }}

                /* --- Gym Modal --- */
                .modal {{ display: none; position: fixed; z-index: 2000; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.9); }}
                .gyms-modal-content {{ 
                    background: #1e2a38; margin: 10% auto; padding: 50px 20px 20px; 
                    border: 1px solid white; border-radius: 24px; width: 85%; height: 60vh;
                    display: grid; grid-template-columns: 1fr 1fr; gap: 15px; position: relative;
                }}
                .close-btn {{ position: absolute; top: 15px; right: 20px; font-size: 30px; cursor: pointer; }}
                .gym-box {{ display: flex; align-items: center; justify-content: center; font-size: 1.1em; font-weight: bold; text-decoration: none; border-radius: 12px; border: 1px dashed rgba(255,255,255,0.5); padding: 10px; }}

                /* --- Mobile Fixes --- */
                @media (max-width: 768px) {{
                    .header-container {{ flex-direction: column; gap: 15px; }}
                    .hero-container {{ flex-direction: row; gap: 8px; padding: 0 10px; }}
                    .click-hint {{ font-size: 0.75em; width: 60px; text-align: right; }}
                    .hero-wrapper {{ height: 320px; }}
                    .video-item {{ width: 45%; }}
                    .gyms-modal-content {{ grid-template-columns: 1fr; height: 80vh; }}
                }}
            </style>
        </head>
        <body>
            <div class="header-container">
                <div class="nav-buttons">
                    <button class="qa-btn" onclick="toggleQASection()">QA ❓</button>
                    <button class="gyms-btn" onclick="openGyms()">Gyms In TLV</button>
                </div>
                <div class="main-title">The Bouldering Library</div>
                <div class="dropdown">
                    <button class="dropbtn">MENU ☰</button>
                </div>
            </div>

            <div id="qaSection" class="qa-section">
                <h2 style="color:#3498db">Common Questions</h2>
                <div class="qa-row">
                    <div class="qa-question" onclick="toggleAnswer(this)">Is Bouldering hard? <span>+</span></div>
                    <div class="qa-answer">Bouldering fits everybody! From a simple ladder to a world-class climb.</div>
                </div>
                <div class="qa-row">
                    <div class="qa-question" onclick="toggleAnswer(this)">I heard you need special shoes? <span>+</span></div>
                    <div class="qa-answer">You can rent climbing shoes at every gym.</div>
                </div>
                <div class="qa-row">
                    <div class="qa-question" onclick="toggleAnswer(this)">Are you climbing with a rope? <span>+</span></div>
                    <div class="qa-answer">No, typically a climb is 3-5 meters. also You have a good and safe mattress.</div>
                </div>
            </div>

            <div class="hero-container">
                <div class="click-hint" id="hintText">lets get started! &rarr;</div>
                <div class="hero-wrapper">
                    <img src="{image_url}" id="heroImage" class="main-img" onclick="startSlider()">
                    
                    <div id="slide1" class="slide" style="background-image: url('{hero3_url}');" onclick="stopSlider()">
                        <button class="nav-arrow prev" onclick="event.stopPropagation(); changeSlide(-1)">&#10094;</button>
                        <div class="slide-content">Bouldering is a discipline in sport climbing. This revolutionary sport swept millions around the world with pure adrenaline.</div>
                        <button class="nav-arrow next" onclick="event.stopPropagation(); changeSlide(1)">&#10095;</button>
                    </div>

                    <div id="slide2" class="slide" style="background-image: url('{hero6_url}');" onclick="stopSlider()">
                        <button class="nav-arrow prev" onclick="event.stopPropagation(); changeSlide(-1)">&#10094;</button>
                        <div class="slide-content">It grew from lead outdoor climbers who needed to train in winter. Today, it is a sport in its own right!</div>
                        <button class="nav-arrow next" onclick="event.stopPropagation(); changeSlide(1)">&#10095;</button>
                    </div>
                </div>
            </div>
            
            <div class="video-container">
                <video class="video-item" autoplay muted loop playsinline><source src="{vid1_url}" type="video/mp4"></video>
                <video class="video-item" autoplay muted loop playsinline><source src="{vid3_url}" type="video/mp4"></video>
            </div>

            <div id="gymsModal" class="modal">
                <div class="gyms-modal-content">
                    <span class="close-btn" onclick="closeGyms()">&times;</span>
                    <a href="https://www.isaacclimbing.com" target="_blank" class="gym-box" style="color:#ff69b4;">Issac gym</a>
                    <a href="https://www.thebloc.co.il/tlv" target="_blank" class="gym-box" style="color:#ffff00;">Block gym</a>
                    <a href="https://performancerock.co.il/branch/midtown-tlv/" target="_blank" class="gym-box" style="color:#2ecc71;">Performance</a>
                    <a href="https://vking.co.il/" target="_blank" class="gym-box" style="color:#3498db;">Viking gym</a>
                </div>
            </div>

            <script>
                let currentSlide = 0;

                function startSlider() {{
                    document.getElementById("heroImage").style.display = "none";
                    document.getElementById("hintText").style.visibility = "hidden";
                    currentSlide = 1; showSlide(1);
                }}

                function stopSlider() {{
                    document.getElementById("heroImage").style.display = "block";
                    document.getElementById("hintText").style.visibility = "visible";
                    document.getElementById("slide1").style.display = "none";
                    document.getElementById("slide2").style.display = "none";
                }}

                function changeSlide(n) {{
                    currentSlide += n;
                    if (currentSlide > 2) currentSlide = 1;
                    if (currentSlide < 1) currentSlide = 2;
                    showSlide(currentSlide);
                }}

                function showSlide(n) {{
                    document.getElementById("slide1").style.display = (n === 1) ? "flex" : "none";
                    document.getElementById("slide2").style.display = (n === 2) ? "flex" : "none";
                }}

                function toggleQASection() {{
                    const sec = document.getElementById("qaSection");
                    sec.classList.toggle("open");
                    if(sec.classList.contains("open")) {{
                        sec.scrollIntoView({{ behavior: 'smooth' }});
                    }}
                }}

                function toggleAnswer(el) {{
                    const ans = el.nextElementSibling;
                    ans.classList.toggle("show");
                    el.querySelector("span").innerText = ans.classList.contains("show") ? "-" : "+";
                }}

                function openGyms() {{ document.getElementById("gymsModal").style.display = "block"; }}
                function closeGyms() {{ document.getElementById("gymsModal").style.display = "none"; }}

                window.onclick = function(event) {{
                    if (event.target.className == "modal") {{ closeGyms(); }}
                }}
            </script>
        </body>
    </html>
    """
