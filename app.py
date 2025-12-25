from flask import Flask, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    image_url = url_for('static', filename='hero.jpg')
    qa_bg_url = url_for('static', filename='hero2.jpg')
    hero3_url = url_for('static', filename='hero3.jpg')
    hero6_url = url_for('static', filename='hero6.jpg')
    hero4_url = url_for('static', filename='hero4.jpg')
    vid1_url = url_for('static', filename='climb1.mp4')
    vid3_url = url_for('static', filename='climb3.mp4')
    
    return f"""
    <html>
        <head>
            <title>The Bouldering Library</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {{
                    font-family: 'Segoe UI', Roboto, sans-serif;
                    background: linear-gradient(135deg, #1e2a38 0%, #2c3e50 100%);
                    color: white;
                    text-align: center;
                    padding: 0;
                    margin: 0;
                    min-height: 100vh;
                    scroll-behavior: smooth;
                }}

                /* --- Header --- */
                .header-container {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    padding: 45px 20px 20px 20px; /* Moves title and content down */
                    max-width: 1200px;
                    margin: 0 auto;
                    position: relative;
                }}
                .nav-buttons {{ 
                    position: absolute; 
                    left: 20px; 
                    display: flex; 
                    flex-direction: column; 
                    gap: 12px; 
                    top: 55px; /* Moves buttons slightly down */
                }}
                .main-title {{ 
                    font-size: 2.5em; 
                    font-weight: 800; 
                    text-shadow: 0 4px 10px rgba(0,0,0,0.3);
                    text-transform: uppercase;
                }}

                .qa-btn {{ background: #3498db; color: white; padding: 12px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; width: 140px; }}
                .gyms-btn {{ background: #9b59b6; color: white; padding: 12px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; width: 140px; }}

                /* --- Hero Section Symmetry Fix --- */
                .hero-container {{
                    position: relative;
                    margin: 20px auto;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    gap: 20px;
                    /* Shifted to compensate for the hint text on the left */
                    transform: translateX(-35px); 
                }}

                .click-hint {{
                    color: white;
                    font-weight: bold;
                    font-size: 1em;
                    animation: floatHint 2s infinite ease-in-out;
                }}

                @keyframes floatHint {{
                    0%, 100% {{ transform: translateX(0); }}
                    50% {{ transform: translateX(-10px); }}
                }}

                .hero-wrapper {{
                    width: 550px;
                    max-width: 80vw;
                    height: 380px;
                    border: 2px solid white;
                    border-radius: 24px;
                    overflow: hidden;
                    cursor: pointer;
                    position: relative;
                    box-shadow: 0 20px 40px rgba(0,0,0,0.4);
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
                    background: rgba(0, 0, 0, 0.7);
                    backdrop-filter: blur(8px);
                    padding: 20px;
                    border-radius: 15px;
                    border: 1px solid rgba(255,255,255,0.2);
                    font-size: 1.1em;
                    line-height: 1.5;
                    margin-bottom: 10px;
                }}

                .nav-arrow {{
                    position: absolute;
                    top: 50%;
                    transform: translateY(-50%);
                    background: rgba(255,255,255,0.2);
                    color: white;
                    border: 1px solid white;
                    width: 45px;
                    height: 45px;
                    border-radius: 50%;
                    z-index: 10;
                    cursor: pointer;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    font-size: 20px;
                }}
                .prev {{ left: 15px; }}
                .next {{ right: 15px; }}

                /* --- Sleek Black Back to Top --- */
                .back-to-top {{
                    position: fixed;
                    bottom: 30px;
                    right: 30px;
                    background-color: #000000;
                    color: white;
                    width: 50px;
                    height: 50px;
                    border-radius: 50%;
                    display: none; 
                    justify-content: center;
                    align-items: center;
                    cursor: pointer;
                    z-index: 1000;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.5);
                    font-size: 24px;
                    border: 1px solid rgba(255,255,255,0.2);
                }}

                /* --- Video Container --- */
                .video-container {{
                    display: flex;
                    justify-content: center;
                    gap: 30px;
                    padding: 40px 20px;
                    transform: translateX(0); /* Reset centering */
                }}
                .video-item {{ width: 25%; max-height: 200px; object-fit: cover; border-radius: 16px; border: 1px solid white; }}

                /* --- QA Section (Bottom) --- */
                .qa-section {{
                    background-image: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), url('{qa_bg_url}');
                    background-size: cover;
                    background-position: center;
                    background-attachment: fixed;
                    padding: 60px 20px;
                    margin-top: 50px;
                    border-top: 2px solid #3498db;
                }}
                .qa-content {{ max-width: 800px; margin: 0 auto; }}
                .qa-row {{ margin-bottom: 15px; text-align: left; }}
                .qa-question {{
                    padding: 20px;
                    background: rgba(255,255,255,0.1);
                    backdrop-filter: blur(5px);
                    border-radius: 12px;
                    cursor: pointer;
                    font-weight: bold;
                    display: flex;
                    justify-content: space-between;
                    border: 1px solid rgba(255,255,255,0.1);
                    font-size: 1.2em;
                }}
                .qa-answer {{
                    max-height: 0;
                    overflow: hidden;
                    transition: all 0.4s ease;
                    padding: 0 20px;
                    color: #3498db;
                    font-size: 1.1em;
                    background: rgba(0,0,0,0.3);
                    border-radius: 0 0 12px 12px;
                }}
                .qa-answer.show {{ max-height: 200px; padding: 15px 20px; border: 1px solid rgba(52, 152, 219, 0.3); border-top: none; }}

                /* --- Gym Modal --- */
                .modal {{ display: none; position: fixed; z-index: 2000; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.9); }}
                .gyms-modal-content {{ 
                    background: #1e2a38; margin: 10vh auto; padding: 60px 20px 20px; 
                    border: 2px solid white; border-radius: 24px; width: 80%; height: 70vh;
                    display: grid; grid-template-columns: 1fr 1fr; gap: 20px; position: relative;
                }}
                .close-btn {{ position: absolute; top: 15px; right: 25px; font-size: 35px; cursor: pointer; }}
                .gym-box {{ display: flex; align-items: center; justify-content: center; font-size: 1.6em; font-weight: bold; text-decoration: none; border-radius: 16px; border: 2px dashed rgba(255,255,255,0.4); padding: 15px; text-align: center; }}

                /* --- Mobile --- */
                @media (max-width: 768px) {{
                    .header-container {{ padding-top: 110px; }}
                    .nav-buttons {{ position: absolute; top: 20px; left: 50%; transform: translateX(-50%); flex-direction: row; }}
                    .hero-container {{ gap: 5px; margin-top: 40px; transform: translateX(0); }}
                    .click-hint {{ font-size: 0.7em; width: 50px; text-align: right; }}
                    .hero-wrapper {{ height: 320px; width: 260px; }}
                }}
            </style>
        </head>
        <body>
            <div id="top"></div>
            <div class="header-container">
                <div class="nav-buttons">
                    <button class="qa-btn" onclick="scrollToQA()">QA ❓</button>
                    <button class="gyms-btn" onclick="openGyms()">Gyms In TLV</button>
                </div>
                <div class="main-title">The Bouldering Library</div>
            </div>

            <div class="hero-container">
                <div class="click-hint" id="hintText">lets get started! &rarr;</div>
                <div class="hero-wrapper">
                    <img src="{image_url}" id="heroImage" class="main-img" onclick="startSlider()">
                    
                    <div id="slide1" class="slide" style="background-image: url('{hero3_url}');" onclick="stopSlider()">
                        <div class="nav-arrow prev" onclick="event.stopPropagation(); changeSlide(-1)">&#10094;</div>
                        <div class="slide-content">Bouldering is a discipline in sport climbing. This revolutionary sport swept millions around the world with pure adrenaline.</div>
                        <div class="nav-arrow next" onclick="event.stopPropagation(); changeSlide(1)">&#10095;</div>
                    </div>

                    <div id="slide2" class="slide" style="background-image: url('{hero6_url}');" onclick="stopSlider()">
                        <div class="nav-arrow prev" onclick="event.stopPropagation(); changeSlide(-1)">&#10094;</div>
                        <div class="slide-content">It grew from lead outdoor climbers who needed to train in winter. Today, it is a sport in its own right!</div>
                        <div class="nav-arrow next" onclick="event.stopPropagation(); changeSlide(1)">&#10095;</div>
                    </div>

                    <div id="slide3" class="slide" style="background-image: url('{hero4_url}');" onclick="stopSlider()">
                        <div class="nav-arrow prev" onclick="event.stopPropagation(); changeSlide(-1)">&#10094;</div>
                        <div class="slide-content">Today bouldering starts from a simple ladder, all the way to the Olympics!</div>
                        <div class="nav-arrow next" onclick="event.stopPropagation(); changeSlide(1)">&#10095;</div>
                    </div>
                </div>
            </div>
            
            <div class="video-container">
                <video class="video-item" autoplay muted loop playsinline><source src="{vid1_url}" type="video/mp4"></video>
                <video class="video-item" autoplay muted loop playsinline><source src="{vid3_url}" type="video/mp4"></video>
            </div>

            <div id="qaSection" class="qa-section">
                <div class="qa-content">
                    <h2 style="font-size: 2.5em; margin-bottom: 40px; color: #3498db;">Common Questions</h2>
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
                        <div class="qa-answer">No, typically a climb is between 3-5 meters. also You have a good and safe mattress.</div>
                    </div>
                </div>
            </div>

            <div id="backToTop" class="back-to-top" onclick="scrollToTop()">&#8593;</div>

            <div id="gymsModal" class="modal">
                <div class="gyms-modal-content">
                    <span class="close-btn" onclick="closeGyms()">&times;</span>
                    <a href="https://www.isaacclimbing.com" target="_blank" class="gym-box" style="color:#ff69b4;">Issac Climbing Gym</a>
                    <a href="https://www.thebloc.co.il/tlv" target="_blank" class="gym-box" style="color:#ffff00;">Block Climbing Gym</a>
                    <a href="https://performancerock.co.il/branch/midtown-tlv/" target="_blank" class="gym-box" style="color:#2ecc71;">Performance Climbing Gym</a>
                    <a href="https://vking.co.il/" target="_blank" class="gym-box" style="color:#3498db;">Viking Climbing Gym</a>
                </div>
            </div>

            <script>
                let currentSlide = 0;
                const totalSlides = 3;

                function startSlider() {{
                    document.getElementById("heroImage").style.display = "none";
                    document.getElementById("hintText").style.visibility = "hidden";
                    currentSlide = 1; showSlide(1);
                }}

                function stopSlider() {{
                    document.getElementById("heroImage").style.display = "block";
                    document.getElementById("hintText").style.visibility = "visible";
                    document.querySelectorAll(".slide").forEach(s => s.style.display = "none");
                }}

                function changeSlide(n) {{
                    currentSlide += n;
                    if (currentSlide > totalSlides) currentSlide = 1;
                    if (currentSlide < 1) currentSlide = totalSlides;
                    showSlide(currentSlide);
                }}

                function showSlide(n) {{
                    document.querySelectorAll(".slide").forEach((s, idx) => {{
                        s.style.display = (idx + 1 === n) ? "flex" : "none";
                    }});
                }}

                function scrollToQA() {{
                    document.getElementById("qaSection").scrollIntoView({{ behavior: 'smooth' }});
                }}

                function scrollToTop() {{
                    window.scrollTo({{ top: 0, behavior: 'smooth' }});
                }}

                function toggleAnswer(el) {{
                    const ans = el.nextElementSibling;
                    ans.classList.toggle("show");
                    el.querySelector("span").innerText = ans.classList.contains("show") ? "-" : "+";
                }}

                function openGyms() {{ document.getElementById("gymsModal").style.display = "block"; }}
                function closeGyms() {{ document.getElementById("gymsModal").style.display = "none"; }}

                window.onscroll = function() {{
                    let btn = document.getElementById("backToTop");
                    if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {{
                        btn.style.display = "flex";
                    }} else {{
                        btn.style.display = "none";
                    }}
                }};

                window.onclick = function(event) {{
                    if (event.target.className == "modal") {{ closeGyms(); }}
                }}
            </script>
        </body>
    </html>
    """
