from flask import Flask, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    image_url = url_for('static', filename='hero.jpg')
    qa_bg_url = url_for('static', filename='hero2.jpg')
    hero3_url = url_for('static', filename='hero3.jpg')
    hero5_url = url_for('static', filename='hero5.jpg')
    vid1_url = url_for('static', filename='climb1.mp4')
    vid3_url = url_for('static', filename='climb3.mp4')
    
    return f"""
    <html>
        <head>
            <title>The Bouldering Library</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {{
                    font-family: 'Segoe UI', Roboto, Arial, sans-serif;
                    background: linear-gradient(135deg, #1e2a38 0%, #2c3e50 100%);
                    color: white;
                    text-align: center;
                    padding: 10px;
                    margin: 0;
                    min-height: 100vh;
                }}
                
                .header-container {{
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 20px;
                    max-width: 1200px;
                    margin: 0 auto;
                }}
                .nav-buttons {{ display: flex; flex-direction: column; gap: 8px; }}
                .main-title {{ font-size: 2.2em; color: white; margin: 0 10px; flex-grow: 1; font-weight: 800; }}
                
                .dropbtn {{ background-color: #e67e22; color: white; padding: 12px 20px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; }}
                .qa-btn {{ background-color: #3498db; color: white; padding: 12px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; width: 140px; }}
                .gyms-btn {{ background-color: #9b59b6; color: white; padding: 12px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; width: 140px; }}

                .hero-container {{
                    position: relative;
                    display: inline-block;
                    margin: 30px auto;
                    max-width: 95vw;
                }}

                .click-hint {{
                    position: absolute;
                    left: -170px;
                    top: 50%;
                    transform: translateY(-50%);
                    color: white;
                    font-weight: bold;
                    font-size: 1.1em;
                    white-space: nowrap;
                    animation: floatHint 2s infinite ease-in-out;
                }}

                @keyframes floatHint {{
                    0%, 100% {{ transform: translateY(-50%) translateX(0); }}
                    50% {{ transform: translateY(-50%) translateX(-12px); }}
                }}

                .hero-wrapper {{
                    width: 550px;
                    max-width: 100%;
                    height: 380px;
                    border: 2px solid white;
                    border-radius: 24px;
                    overflow: hidden;
                    cursor: pointer;
                    position: relative;
                    background: #000;
                }}
                
                .main-img {{ 
                    width: 100%; 
                    height: 100%; 
                    object-fit: cover; 
                    object-position: center; /* Fixed for phone center */
                    display: block; 
                }}

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
                    align-items: center;
                    position: relative;
                }}
                
                .slide-content {{
                    background: rgba(0, 0, 0, 0.7);
                    backdrop-filter: blur(5px);
                    padding: 15px 20px;
                    border-radius: 15px;
                    border: 1px solid rgba(255,255,255,0.2);
                    font-size: 1em;
                    line-height: 1.4;
                    margin-bottom: 10px;
                    max-width: 90%;
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
                    cursor: pointer;
                    font-size: 18px;
                    border-radius: 50%;
                    z-index: 10;
                }}
                .prev {{ left: 10px; }}
                .next {{ right: 10px; }}

                .close-slider {{
                    position: absolute;
                    top: 15px;
                    right: 15px;
                    background: rgba(255,255,255,0.3);
                    color: white;
                    border: none;
                    width: 30px;
                    height: 30px;
                    border-radius: 50%;
                    font-weight: bold;
                    cursor: pointer;
                    z-index: 20;
                }}

                .video-container {{ display: flex; justify-content: center; gap: 20px; margin: 30px auto; }}
                .video-item {{ width: 25%; max-height: 200px; object-fit: cover; border-radius: 16px; border: 1px solid white; }}

                .modal {{ display: none; position: fixed; z-index: 2000; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.9); }}
                .modal-content-qa {{ background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('{qa_bg_url}'); background-size: cover; background-position: center; margin: 5% auto; padding: 40px; border: 2px solid #3498db; border-radius: 24px; width: 60%; color: white; position: relative; }}
                .gyms-modal-content {{ background-color: #1e2a38; margin: 5% auto; padding: 50px 20px 20px 20px; border: 2px solid white; border-radius: 24px; width: 85%; height: 75vh; display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 15px; position: relative; }}
                .close-btn {{ color: white; position: absolute; top: 15px; right: 25px; font-size: 35px; cursor: pointer; }}
                .gym-box {{ display: flex; align-items: center; justify-content: center; font-size: 1.5em; font-weight: bold; text-decoration: none; border-radius: 16px; border: 1px dashed rgba(255,255,255,0.4); padding: 5px; text-align: center; }}

                @media (max-width: 768px) {{
                    .header-container {{ flex-direction: column; }}
                    .click-hint {{ 
                        left: -85px; /* Moved to left of pic on mobile */
                        font-size: 0.8em; 
                        white-space: normal; 
                        width: 70px; 
                        text-align: right;
                    }}
                    .hero-wrapper {{ width: 260px; height: 320px; margin-left: 80px; }} /* Shifted wrapper to make room for hint on left */
                    .video-item {{ width: 45%; }}
                    .gyms-modal-content {{ grid-template-columns: 1fr; grid-template-rows: repeat(4, 1fr); height: 85vh; }}
                    .modal-content-qa {{ width: 90%; padding: 20px; }}
                }}
            </style>
        </head>
        <body>
            <div class="header-container">
                <div class="nav-buttons">
                    <button class="qa-btn" onclick="openQA()">QA ❓</button>
                    <button class="gyms-btn" onclick="openGyms()">Gyms In TLV</button>
                </div>
                <div class="main-title">The Bouldering Library</div>
                <div class="dropdown">
                    <button class="dropbtn" onclick="this.nextElementSibling.style.display='block'">MENU ☰</button>
                    <div class="dropdown-content" style="display:none;" onmouseleave="this.style.display='none'">
                        <a href="https://www.youtube.com/watch?v=9LXySxPDZx0" target="_blank">TOKYO CLIMBING</a>
                        <a href="https://www.youtube.com/watch?v=45KmZUc0CzA" target="_blank">JANJA IN PARIS 🐐</a>
                        <a href="https://www.youtube.com/watch?v=P8lh_Y2OdFk" target="_blank">OUTDOOR BOULDERING</a>
                    </div>
                </div>
            </div>

            <div class="hero-container">
                <div class="click-hint">lets get started! &rarr;</div>
                <div class="hero-wrapper" id="heroBox">
                    <img src="{image_url}" id="heroImage" class="main-img" onclick="startSlider()">
                    
                    <div id="slide1" class="slide" style="background-image: url('{hero3_url}');">
                        <button class="close-slider" onclick="stopSlider()">X</button>
                        <button class="nav-arrow prev" onclick="changeSlide(-1)">&#10094;</button>
                        <div class="slide-content">Bouldering is a discipline in sport climbing. This revolutionary sport swept millions around the world with pure adrenaline. It became an Olympic sport at Tokyo 2020.</div>
                        <button class="nav-arrow next" onclick="changeSlide(1)">&#10095;</button>
                    </div>

                    <div id="slide2" class="slide" style="background-image: url('{hero5_url}');">
                        <button class="close-slider" onclick="stopSlider()">X</button>
                        <button class="nav-arrow prev" onclick="changeSlide(-1)">&#10094;</button>
                        <div class="slide-content">It grew from the need of lead outdoor climbers who needed to train in winter. Today, it is a sport in its own right that has swept millions world wide!</div>
                        <button class="nav-arrow next" onclick="changeSlide(1)">&#10095;</button>
                    </div>
                </div>
            </div>
            
            <div class="video-container">
                <video class="video-item" autoplay muted loop playsinline><source src="{vid1_url}" type="video/mp4"></video>
                <video class="video-item" autoplay muted loop playsinline><source src="{vid3_url}" type="video/mp4"></video>
            </div>

            <div id="qaModal" class="modal">
                <div class="modal-content-qa">
                    <span class="close-btn" onclick="closeQA()">&times;</span>
                    <h2>Common Questions</h2>
                    <div class="qa-item" onclick="openAnswer('Bouldering fits everybody! From a simple ladder to a world-class climb.')">Is Bouldering hard?</div>
                    <div class="qa-item" onclick="openAnswer('You can rent climbing shoes at every gym')">I heard you need special shoes?</div>
                    <div class="qa-item" onclick="openAnswer('No, typically a climb is between 3-5 meters. also You have a good and safe mattress.')">Are you climbing with a rope?</div>
                </div>
            </div>

            <div id="answerModal" class="modal"><div class="modal-content-qa" style="border-color: #e67e22; width: 50%;"><span class="close-btn" onclick="closeAnswer()">&times;</span><h2 style="color: #e67e22;">Explanation</h2><p id="answerText"></p></div></div>

            <div id="gymsModal" class="modal">
                <div class="gyms-modal-content">
                    <span class="close-btn" onclick="closeGyms()">&times;</span>
                    <a href="https://www.isaacclimbing.com" target="_blank" class="gym-box" style="color:#ff69b4;">Issac Climbing gym</a>
                    <a href="https://www.thebloc.co.il/tlv" target="_blank" class="gym-box" style="color:#ffff00;">Block Climbing Gym</a>
                    <a href="https://performancerock.co.il/branch/midtown-tlv/" target="_blank" class="gym-box" style="color:#2ecc71;">Performance Climbing Gym</a>
                    <a href="https://vking.co.il/" target="_blank" class="gym-box" style="color:#3498db;">Viking Climbing Gym</a>
                </div>
            </div>

            <script>
                let currentSlide = 0;
                function startSlider() {{
                    document.getElementById("heroImage").style.display = "none";
                    document.querySelector(".click-hint").style.display = "none";
                    currentSlide = 1; showSlide(1);
                }}
                function stopSlider() {{
                    document.getElementById("heroImage").style.display = "block";
                    document.querySelector(".click-hint").style.display = "block";
                    document.getElementById("slide1").style.display = "none";
                    document.getElementById("slide2").style.display = "none";
                }}
                function changeSlide(n) {{ currentSlide += n; if (currentSlide > 2) currentSlide = 1; if (currentSlide < 1) currentSlide = 2; showSlide(currentSlide); }}
                function showSlide(n) {{ document.getElementById("slide1").style.display = (n === 1) ? "flex" : "none"; document.getElementById("slide2").style.display = (n === 2) ? "flex" : "none"; }}
                function openQA() {{ document.getElementById("qaModal").style.display = "block"; }}
                function closeQA() {{ document.getElementById("qaModal").style.display = "none"; }}
                function openGyms() {{ document.getElementById("gymsModal").style.display = "block"; }}
                function closeGyms() {{ document.getElementById("gymsModal").style.display = "none"; }}
                function openAnswer(text) {{ document.getElementById("answerText").innerText = text; document.getElementById("answerModal").style.display = "block"; }}
                function closeAnswer() {{ document.getElementById("answerModal").style.display = "none"; }}
                window.onclick = function(event) {{ if (event.target.className == "modal") {{ event.target.style.display = "none"; }} }}
            </script>
        </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
