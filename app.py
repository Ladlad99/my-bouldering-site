from flask import Flask, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Asset URLs
    image_url = url_for('static', filename='hero.jpg')
    qa_bg_url = url_for('static', filename='hero2.jpg')
    hero3_url = url_for('static', filename='hero3.jpg')
    hero6_url = url_for('static', filename='hero6.jpg')
    hero4_url = url_for('static', filename='hero4.jpg')
    hero5_url = url_for('static', filename='hero5.jpg')
    vid1_url = url_for('static', filename='climb1.mp4')
    vid3_url = url_for('static', filename='climb3.mp4')
    
    return f"""
    <html>
        <head>
            <title>The Bouldering Library</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://fonts.googleapis.com/css2?family=Architects+Daughter&display=swap" rel="stylesheet">
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
                    overflow-x: hidden;
                }}

                /* --- Header --- */
                .header-container {{
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    padding: 45px 20px 20px 20px;
                    max-width: 1200px;
                    margin: 0 auto;
                    position: relative;
                }}
                
                /* Left Buttons (Only QA remains) */
                .nav-buttons {{ 
                    position: absolute; 
                    left: 20px; 
                    display: flex; 
                    flex-direction: column; 
                    gap: 20px; 
                    top: 55px;
                    align-items: flex-start;
                }}

                .main-title {{ 
                    font-size: 2.5em; 
                    font-weight: 800; 
                    text-shadow: 0 4px 10px rgba(0,0,0,0.3);
                    text-transform: uppercase;
                }}

                /* --- Top Right Menu (Chalkboard Style - No Slant) --- */
                .menu-container {{
                    position: absolute;
                    right: 30px;
                    top: 50px;
                    z-index: 100;
                    text-align: right;
                }}

                .menu-label {{
                    font-family: 'Architects Daughter', cursive;
                    font-size: 1.8em;
                    color: #fdfdfd;
                    /* transform: rotate(5deg); REMOVED SLANT */
                    cursor: pointer;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
                    transition: 0.3s;
                    display: inline-block;
                    padding-bottom: 10px;
                }}
                
                .menu-label:hover {{
                    color: #3498db;
                    transform: scale(1.1); /* Simple scale instead of rotate */
                }}

                /* The Fade-in List */
                .menu-dropdown {{
                    visibility: hidden;
                    opacity: 0;
                    position: absolute;
                    right: 0;
                    top: 50px;
                    background: rgba(0, 0, 0, 0.8);
                    border: 1px solid rgba(255,255,255,0.2);
                    border-radius: 12px;
                    padding: 15px;
                    width: 220px;
                    display: flex;
                    flex-direction: column;
                    gap: 10px;
                    transition: opacity 0.4s ease, visibility 0.4s ease;
                    backdrop-filter: blur(5px);
                }}

                .menu-container:hover .menu-dropdown {{
                    visibility: visible;
                    opacity: 1;
                }}

                .menu-item {{
                    color: white;
                    text-decoration: none;
                    font-weight: bold;
                    font-size: 1.1em;
                    padding: 8px 12px;
                    border-radius: 6px;
                    transition: 0.3s;
                    cursor: pointer;
                    text-align: center;
                }}
                
                .menu-item:hover {{
                    background: rgba(255, 255, 255, 0.2);
                    color: #3498db;
                }}

                /* --- Text Only Buttons --- */
                .btn-text-only {{
                    background: none;
                    border: none;
                    color: white;
                    padding: 5px 0;
                    cursor: pointer;
                    font-weight: 700;
                    font-size: 1.1em;
                    letter-spacing: 1px;
                    text-transform: uppercase;
                    transition: all 0.3s ease;
                    text-shadow: 0 2px 4px rgba(0,0,0,0.5);
                    position: relative;
                }}
                .btn-text-only::after {{
                    content: ''; position: absolute; width: 0; height: 2px; bottom: 0; left: 0; background-color: white; transition: width 0.3s ease;
                }}
                .btn-text-only:hover::after {{ width: 100%; }}

                /* --- Hero Section --- */
                .hero-container {{
                    position: relative;
                    margin: 40px auto;
                    width: 550px;
                    max-width: 80vw;
                }}

                .click-hint {{
                    position: absolute;
                    left: -180px;
                    top: 50%;
                    transform: translateY(-50%);
                    color: white;
                    font-weight: bold;
                    font-size: 1em;
                    animation: floatHint 2s infinite ease-in-out;
                    white-space: nowrap;
                }}

                .shop-hint-chalk {{
                    position: absolute;
                    top: -40px;
                    right: -100px;
                    font-family: 'Architects Daughter', cursive;
                    font-size: 1.8em;
                    color: #fdfdfd;
                    transform: rotate(-8deg); /* Shop hint stays slanted per previous design */
                    cursor: pointer;
                    text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
                    transition: 0.3s;
                    white-space: nowrap;
                }}
                .shop-hint-chalk:hover {{ transform: rotate(-5deg) scale(1.1); color: #3498db; }}

                @keyframes floatHint {{ 
                    0%, 100% {{ transform: translateY(-50%) translateX(0); }} 
                    50% {{ transform: translateY(-50%) translateX(-10px); }} 
                }}

                .hero-wrapper {{
                    width: 100%;
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
                    display: none; width: 100%; height: 100%; background-size: cover; background-position: center;
                    padding: 20px; box-sizing: border-box; flex-direction: column; justify-content: flex-end; position: relative;
                }}

                .slide-content {{
                    background: rgba(0, 0, 0, 0.7); backdrop-filter: blur(8px); padding: 20px;
                    border-radius: 15px; border: 1px solid rgba(255,255,255,0.2); font-size: 1.1em; line-height: 1.5; margin-bottom: 10px;
                }}

                .nav-arrow {{
                    position: absolute; top: 50%; transform: translateY(-50%); background: rgba(255,255,255,0.2); color: white;
                    border: 1px solid white; width: 45px; height: 45px; border-radius: 50%; z-index: 10; cursor: pointer;
                    display: flex; align-items: center; justify-content: center; font-size: 20px;
                }}
                .prev {{ left: 15px; }}
                .next {{ right: 15px; }}

                /* --- Shop Tab Modal --- */
                .shop-modal-content {{
                    background-image: linear-gradient(rgba(0,0,0,0.1), rgba(0,0,0,0.1)), url('{hero5_url}');
                    background-size: cover;
                    background-position: center;
                    margin: 15vh auto;
                    padding: 40px 20px 80px 20px; 
                    border: 1px solid rgba(255,255,255,0.4);
                    border-radius: 20px;
                    width: 500px;
                    max-width: 90%;
                    min-height: 400px;
                    position: relative;
                    box-shadow: 0 0 40px rgba(0,0,0,0.5);
                    text-align: center;
                    display: flex;
                    flex-direction: column;
                    justify-content: flex-end;
                    cursor: pointer;
                    animation: modalPopUp 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275);
                }}

                @keyframes modalPopUp {{
                    0% {{ transform: scale(0.5); opacity: 0; }}
                    80% {{ transform: scale(1.05); opacity: 1; }}
                    100% {{ transform: scale(1); opacity: 1; }}
                }}

                .shop-grid {{
                    display: flex;
                    justify-content: center;
                    gap: 20px;
                    flex-wrap: wrap;
                    margin-bottom: 20px;
                }}
                
                .shop-item {{
                    background: none; border: none; padding: 10px;
                    transition: transform 0.3s ease; cursor: pointer;
                    display: flex; flex-direction: column; align-items: center;
                }}
                .shop-item:hover {{ transform: scale(1.1); }}

                .emoji-icon {{
                    font-size: 4em; margin-bottom: 10px; display: block;
                    filter: drop-shadow(0 4px 8px rgba(0,0,0,0.6));
                }}
                .shop-item span {{ 
                    font-weight: 700; font-size: 1.1em; text-transform: capitalize; color: #fff; text-shadow: 0 2px 5px rgba(0,0,0,0.8);
                }}

                .contact-container {{
                    position: absolute; bottom: 20px; left: 20px; text-align: left; cursor: default;
                }}
                .contact-btn {{
                    font-size: 0.9em; font-weight: bold; color: white; cursor: pointer; text-decoration: underline; opacity: 0.9; transition: 0.3s; text-shadow: 0 2px 4px rgba(0,0,0,0.8);
                }}
                .contact-btn:hover {{ opacity: 1; color: #3498db; }}

                .contact-form {{ display: none; margin-top: 5px; background: rgba(0,0,0,0.6); padding: 10px; border-radius: 8px; width: 200px; }}
                .contact-input {{ width: 100%; padding: 5px; margin-bottom: 5px; border-radius: 4px; border: none; font-family: inherit; font-size: 0.8em; }}
                .send-btn-link {{ display: inline-block; background-color: #3498db; color: white; padding: 4px 10px; border-radius: 4px; text-decoration: none; font-size: 0.8em; font-weight: bold; }}

                .video-container {{ display: flex; justify-content: center; gap: 30px; padding: 40px 20px; }}
                .video-item {{ width: 25%; max-height: 200px; object-fit: cover; border-radius: 16px; border: 1px solid white; }}

                /* --- QA Section --- */
                .qa-section {{
                    background-image: linear-gradient(rgba(0,0,0,0.8), rgba(0,0,0,0.8)), url('{qa_bg_url}');
                    background-size: cover; background-position: center; background-attachment: fixed;
                    padding: 60px 20px; margin-top: 50px; border-top: 1px solid rgba(255,255,255,0.2);
                }}
                .qa-content {{ max-width: 800px; margin: 0 auto; }}
                .qa-row {{ margin-bottom: 15px; text-align: left; }}
                .qa-question {{
                    padding: 20px; background: rgba(255,255,255,0.1); backdrop-filter: blur(5px);
                    border-radius: 12px; cursor: pointer; font-weight: bold; display: flex;
                    justify-content: space-between; border: 1px solid rgba(255,255,255,0.1); font-size: 1.2em;
                }}
                .qa-answer {{
                    max-height: 0; overflow: hidden; transition: all 0.4s ease; padding: 0 20px;
                    color: #3498db; font-size: 1.1em; background: rgba(0,0,0,0.3); border-radius: 0 0 12px 12px;
                }}
                .qa-answer.show {{ max-height: 200px; padding: 15px 20px; border: 1px solid rgba(52, 152, 219, 0.3); border-top: none; }}

                /* --- Generic Modal --- */
                .modal {{ display: none; position: fixed; z-index: 2000; left: 0; top: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.8); }}
                .modal-content-gym {{ 
                    background: #1e2a38; margin: 10vh auto; padding: 60px 20px 20px; 
                    border: 2px solid white; border-radius: 24px; width: 80%; height: 70vh;
                    position: relative; overflow-y: auto;
                }}
                .close-btn {{ position: absolute; top: 15px; right: 15px; font-size: 30px; cursor: pointer; color: white; z-index: 10; text-shadow: 0 2px 5px rgba(0,0,0,0.5); }}
                .gym-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 20px; height: 100%; }}
                .gym-box {{ display: flex; align-items: center; justify-content: center; font-size: 1.6em; font-weight: bold; text-decoration: none; border-radius: 16px; border: 2px dashed rgba(255,255,255,0.4); padding: 15px; text-align: center; }}

                .back-to-top {{
                    position: fixed; bottom: 30px; right: 30px; background-color: #000000; color: white; width: 50px; height: 50px;
                    border-radius: 50%; display: none; justify-content: center; align-items: center; cursor: pointer; z-index: 1000;
                    box-shadow: 0 4px 15px rgba(0,0,0,0.5); font-size: 24px; border: 1px solid rgba(255,255,255,0.2);
                }}

                @media (max-width: 768px) {{
                    .header-container {{ padding-top: 110px; }}
                    .nav-buttons {{ position: absolute; top: 20px; left: 50%; transform: translateX(-50%); flex-direction: row; align-items: center; }}
                    .menu-container {{ right: 50%; transform: translateX(50%); top: 70px; }}
                    .menu-dropdown {{ right: auto; left: 50%; transform: translateX(-50%); }}
                    .hero-container {{ width: 100%; margin-top: 50px; flex-direction: column; }}
                    .click-hint {{ position: relative; left: auto; top: auto; transform: none; margin-bottom: 10px; animation: none; }}
                    .shop-hint-chalk {{ position: relative; top: auto; right: auto; margin-top: 10px; transform: rotate(-3deg); }}
                    .hero-wrapper {{ height: 320px; width: 90vw; }}
                    .shop-modal-content {{ width: 85%; padding: 40px 10px 80px 10px; }}
                    .shop-grid {{ gap: 15px; }}
                    .gym-grid {{ grid-template-columns: 1fr; }}
                }}
            </style>
        </head>
        <body>
            <div id="top"></div>
            <div class="header-container">
                <div class="nav-buttons">
                    <button class="btn-text-only" onclick="scrollToQA()">QA ❓</button>
                    </div>

                <div class="main-title">The Bouldering Library</div>

                <div class="menu-container">
                    <span class="menu-label">Menu</span>
                    <div class="menu-dropdown">
                        <div class="menu-item">Strength For Climbers</div>
                        <div class="menu-item">Techniques</div>
                        <div class="menu-item" onclick="openGyms()">Gyms In TLV</div>
                        <div class="menu-item">About</div>
                    </div>
                </div>
            </div>

            <div class="hero-container">
                <div class="click-hint">lets get started! &rarr;</div>
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
                <div class="shop-hint-chalk" onclick="openShop()">Our Shop!</div>
            </div>
            
            <div class="video-container">
                <video class="video-item" autoplay muted loop playsinline><source src="{vid1_url}" type="video/mp4"></video>
                <video class="video-item" autoplay muted loop playsinline><source src="{vid3_url}" type="video/mp4"></video>
            </div>

            <div id="shopModal" class="modal">
                <div class="shop-modal-content" onclick="closeShop()">
                    <div class="shop-grid" onclick="event.stopPropagation()">
                        <div class="shop-item">
                            <span class="emoji-icon">📝</span>
                            <span>Training Plan</span>
                        </div>
                        <div class="shop-item">
                            <span class="emoji-icon">💻</span>
                            <span>Online Coaching</span>
                        </div>
                        <div class="shop-item">
                            <span class="emoji-icon">🤜🤛</span>
                            <span>1 on 1 Session</span>
                        </div>
                    </div>

                    <div class="contact-container" onclick="event.stopPropagation()">
                        <div class="contact-btn" onclick="toggleContact()">Contact Us</div>
                        <div id="contactForm" class="contact-form">
                            <input type="text" id="contactMsg" class="contact-input" placeholder="Your phrase..." onkeyup="updateMailLink()">
                            <a id="mailLink" href="mailto:Elad@mulitime.com" class="send-btn-link">Send</a>
                        </div>
                    </div>
                </div>
            </div>

            <div id="gymsModal" class="modal">
                <div class="modal-content-gym">
                    <span class="close-btn" onclick="closeGyms()">&times;</span>
                    <div class="gym-grid">
                        <a href="https://www.isaacclimbing.com" target="_blank" class="gym-box" style="color:#ff69b4;">Issac Climbing Gym</a>
                        <a href="https://www.thebloc.co.il/tlv" target="_blank" class="gym-box" style="color:#ffff00;">Block Climbing Gym</a>
                        <a href="https://performancerock.co.il/branch/midtown-tlv/" target="_blank" class="gym-box" style="color:#2ecc71;">Performance Climbing Gym</a>
                        <a href="https://vking.co.il/" target="_blank" class="gym-box" style="color:#3498db;">Viking Climbing Gym</a>
                    </div>
                </div>
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

            <script>
                let currentSlide = 0;
                const totalSlides = 3;

                function startSlider() {{
                    document.getElementById("heroImage").style.display = "none";
                    currentSlide = 1; showSlide(1);
                }}
                function stopSlider() {{
                    document.getElementById("heroImage").style.display = "block";
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
                function scrollToQA() {{ document.getElementById("qaSection").scrollIntoView({{ behavior: 'smooth' }}); }}
                function scrollToTop() {{ window.scrollTo({{ top: 0, behavior: 'smooth' }}); }}
                function toggleAnswer(el) {{
                    const ans = el.nextElementSibling;
                    ans.classList.toggle("show");
                    el.querySelector("span").innerText = ans.classList.contains("show") ? "-" : "+";
                }}
                
                function openShop() {{ document.getElementById("shopModal").style.display = "block"; }}
                function closeShop() {{ document.getElementById("shopModal").style.display = "none"; }}
                function openGyms() {{ document.getElementById("gymsModal").style.display = "block"; }}
                function closeGyms() {{ document.getElementById("gymsModal").style.display = "none"; }}

                function toggleContact() {{
                    var form = document.getElementById("contactForm");
                    form.style.display = (form.style.display === "block") ? "none" : "block";
                }}

                function updateMailLink() {{
                    var msg = document.getElementById("contactMsg").value;
                    var link = document.getElementById("mailLink");
                    link.href = "mailto:Elad@mulitime.com?body=" + encodeURIComponent(msg);
                }}

                window.onscroll = function() {{
                    let btn = document.getElementById("backToTop");
                    if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {{ btn.style.display = "flex"; }}
                    else {{ btn.style.display = "none"; }}
                }};

                window.onclick = function(event) {{
                    if (event.target.className == "modal") {{ 
                        if (event.target.id === "gymsModal") closeGyms();
                        if (event.target.id === "shopModal") closeShop();
                    }}
                }}
            </script>
        </body>
    </html>
    """
