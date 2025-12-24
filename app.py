from flask import Flask, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Asset URLs
    image_url = url_for('static', filename='hero.jpg')
    qa_bg_url = url_for('static', filename='hero2.jpg')
    hero3_url = url_for('static', filename='hero3.jpg')
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
                    font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
                    background: linear-gradient(135deg, #1e2a38 0%, #2c3e50 100%);
                    color: white;
                    text-align: center;
                    padding: 10px;
                    margin: 0;
                    min-height: 100vh;
                }}
                
                /* --- Header Concept --- */
                .header-container {{
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 20px;
                    max-width: 1200px;
                    margin: 0 auto;
                }}
                .nav-buttons {{ display: flex; flex-direction: column; gap: 8px; }}
                .main-title {{ 
                    font-size: 2.8em; 
                    color: white; 
                    margin: 0 20px; 
                    flex-grow: 1; 
                    font-weight: 800;
                    letter-spacing: -1px;
                    text-shadow: 0 4px 10px rgba(0,0,0,0.3);
                }}
                
                /* Keep original button styles */
                .dropdown {{ position: relative; display: inline-block; z-index: 1000; }}
                .dropbtn {{ background-color: #e67e22; color: white; padding: 12px 20px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; box-shadow: 0 4px 15px rgba(230, 126, 34, 0.3); }}
                .dropdown-content {{ display: none; position: absolute; right: 0; background-color: #34495e; min-width: 200px; border-radius: 8px; overflow: hidden; }}
                .dropdown-content a {{ color: white; padding: 12px 16px; text-decoration: none; display: block; text-align: right; }}
                .dropdown-content a:hover {{ background: #2c3e50; }}
                .dropdown:hover .dropdown-content {{ display: block; }}
                
                .qa-btn {{ background-color: #3498db; color: white; padding: 12px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; width: 140px; box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3); }}
                .gyms-btn {{ background-color: #9b59b6; color: white; padding: 12px; border: none; border-radius: 8px; cursor: pointer; font-weight: bold; width: 140px; box-shadow: 0 4px 15px rgba(155, 89, 182, 0.3); }}

                /* --- Hero Container --- */
                .hero-container {{
                    position: relative;
                    display: inline-block;
                    margin: 40px auto;
                    max-width: 95vw;
                }}

                .click-hint {{
                    position: absolute;
                    left: -180px;
                    top: 50%;
                    transform: translateY(-50%);
                    color: rgba(255,255,255,0.8);
                    font-weight: 500;
                    font-size: 1.1em;
                    letter-spacing: 1px;
                    animation: floatHint 2.5s infinite ease-in-out;
                }}

                @keyframes floatHint {{
                    0%, 100% {{ transform: translateY(-50%) translateX(0); }}
                    50% {{ transform: translateY(-50%) translateX(-15px); }}
                }}

                .hero-wrapper {{
                    width: 550px;
                    max-width: 100%;
                    height: 380px;
                    border: 1px solid rgba(255,255,255,0.2);
                    border-radius: 24px;
                    overflow: hidden;
                    cursor: pointer;
                    position: relative;
                    background: rgba(255, 255, 255, 0.05);
                    backdrop-filter: blur(10px);
                    box-shadow: 0 25px 50px rgba(0,0,0,0.4);
                    transition: transform 0.3s ease;
                }}
                .hero-wrapper:hover {{ transform: scale(1.02); }}
                
                .main-img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}

                /* Slides with Concept Style */
                .slide {{
                    display: none;
                    width: 100%;
                    height: 100%;
                    background-size: cover;
                    background-position: center;
                    padding: 40px;
                    box-sizing: border-box;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    position: relative;
                }}
                
                .slide-content {{
                    background: rgba(15, 23, 42, 0.8);
                    backdrop-filter: blur(8px);
                    padding: 25px;
                    border-radius: 16px;
                    border: 1px solid rgba(255,255,255,0.1);
                    font-size: 1.15em;
                    line-height: 1.6;
                    box-shadow: 0 10px 30px rgba(0,0,0,0.5);
                }}

                /* Elegant Navigation Arrows */
                .nav-arrow {{
                    position: absolute;
                    top: 50%;
                    transform: translateY(-50%);
                    background: rgba(255,255,255,0.1);
                    color: white;
                    border: 1px solid rgba(255,255,255,0.3);
                    width: 45px;
                    height: 45px;
                    cursor: pointer;
                    font-size: 18px;
                    border-radius: 50%;
                    z-index: 10;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    transition: 0.3s;
                }}
                .nav-arrow:hover {{ background: white; color: #1e2a38; }}
                .prev {{ left: 15px; }}
                .next {{ right: 15px; }}

                /* --- Video Cards --- */
                .video-container {{
                    display: flex;
                    justify-content: center;
                    gap: 25px;
                    margin: 40px auto;
                    max-width: 1000px;
                }}
                .video-item {{ 
                    width: 25%; 
                    max-height: 200px; 
                    object-fit: cover; 
                    border-radius: 16px;
                    border: 1px solid rgba(255,255,255,0.1);
                    box-shadow: 0 10px 20px rgba(0,0,0,0.2);
                }}

                /* --- Modal Concept --- */
                .modal-content-qa {{ 
                    background-image: linear-gradient(rgba(15, 23, 42, 0.85), rgba(15, 23, 42, 0.85)), url('{qa_bg_url}');
                    background-size: cover; background-position: center;
                    margin: 5vh auto; padding: 40px; border: 1px solid rgba(255,255,255,0.2); 
                    border-radius: 24px; width: 65%; color: white; position: relative;
                    backdrop-filter: blur(15px);
                }}
                
                .gym-box {{ 
                    display: flex; align-items: center; justify-content: center; font-size: 1.6em; font-weight: bold; 
                    text-decoration: none; border-radius: 16px; background: rgba(255,255,255,0.03);
                    border: 1px solid rgba(255,255,255,0.1); transition: 0.3s;
                }}
                .gym-box:hover {{ background: rgba(255,255,255,0.1); transform: translateY(-5px); }}
                
                /* Mobile Elegance */
                @media (max-width: 768px) {{
                    .header-container {{ flex-direction: column; padding: 10px; }}
                    .main-title {{ font-size: 2em; margin: 15px 0; }}
                    .click-hint {{ 
                        position: relative; left: 0; top: 0; transform: none; 
                        display: block; margin-bottom: 20px; text-align: left; padding-left: 10px;
                    }}
                    @keyframes floatHint {{ 0%, 100% {{ transform: translateX(0); }} 50% {{ transform: translateX(10px); }} }}
                    .hero-wrapper {{ width: 100%; height: 320px; border-radius: 20px; }}
                    .video-item {{ width: 45%; }}
                    .gyms-modal-content {{ grid-template-columns: 1fr; height: 85vh; gap: 10px; padding: 60px 20px 20px; }}
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
                    <button class="dropbtn">MENU ☰</button>
                    <div class="dropdown-content">
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
                        <button class="nav-arrow prev" onclick="changeSlide(-1)">&#10094;</button>
                        <div class="slide-content">
                            Bouldering is a discipline in sport climbing. This revolutionary sport swept millions around the world with pure adrenaline. It became an Olympic sport with Lead and Speed climbing at the Olympic Games of Tokyo 2020.
                        </div>
                        <button class="nav-arrow next" onclick="changeSlide(1)">&#10095;</button>
                    </div>

                    <div id="slide2" class="slide" style="background-image: url('{hero4_url}');">
                        <button class="nav-arrow prev" onclick="changeSlide(-1)">&#10094;</button>
                        <div class="slide-content">
                            It grew from the need of lead outdoor climbers who needed a good way to train during the winter season. Today, it has become a sport in its own right that has swept millions around the world!
                        </div>
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
                    <h2 style="font-size: 2.4em; margin-bottom: 30px;">Common Questions</h2>
                    <div class="qa-item" style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 20px; margin-bottom: 15px; cursor: pointer;" onclick="openAnswer('Bouldering fits everybody! From a simple ladder to a world-class climb.')">Is Bouldering hard?</div>
                    <div class="qa-item" style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 20px; margin-bottom: 15px; cursor: pointer;" onclick="openAnswer('You can rent climbing shoes at every gym')">I heard you need special shoes?</div>
                    <div class="qa-item" style="background: rgba(255,255,255,0.05); border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 20px; margin-bottom: 15px; cursor: pointer;" onclick="openAnswer('No, typically a climb is between 3-5 meters. also You have a good and safe mattress.')">Are you climbing with a rope?</div>
                </div>
            </div>

            <div id="answerModal" class="modal" style="z-index: 3000;">
                <div class="modal-content-qa" style="border-color: #e67e22; width: 50%; min-height: 200px;">
                    <span class="close-btn" onclick="closeAnswer()">&times;</span>
                    <h2 style="color: #e67e22; font-size: 2em;">Explanation</h2>
                    <p id="answerText" style="font-size: 1.6em; line-height: 1.5;"></p>
                </div>
            </div>

            <div id="gymsModal" class="modal">
                <div class="gyms-modal-content" style="background: #1e2a38; display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 20px; width: 80%; margin: 5vh auto; padding: 50px; border-radius: 24px; border: 1px solid rgba(255,255,255,0.2); position: relative;">
                    <span class="close-btn" onclick="closeGyms()">&times;</span>
                    <a href="https://www.isaacclimbing.com" target="_blank" class="gym-box" style="color:#ff69b4;">Issac Climbing gym</a>
                    <a href="https://www.thebloc.co.il/tlv" target="_blank" class="gym-box" style="color:#ffff00;">Block Climbing Gym</a>
                    <a href="https://performancerock.co.il/branch/midtown-tlv/" target="_blank" class="gym-box" style="color:#2ecc71;">Performance Climbing Gym</a>
                    <a href="https://vking.co.il/" target="_blank" class="gym-box" style="color:#3498db;">Viking Climbing Gym</a>
                </div>
            </div>

            <script>
                let currentSlide = 0;
                const totalSlides = 2;

                function startSlider() {{
                    document.getElementById("heroImage").style.display = "none";
                    document.querySelector(".click-hint").style.display = "none";
                    currentSlide = 1;
                    showSlide(currentSlide);
                }}

                function changeSlide(n) {{
                    currentSlide += n;
                    if (currentSlide > totalSlides) currentSlide = 1;
                    if (currentSlide < 1) currentSlide = totalSlides;
                    showSlide(currentSlide);
                }}

                function showSlide(n) {{
                    document.getElementById("slide1").style.display = (n === 1) ? "flex" : "none";
                    document.getElementById("slide2").style.display = (n === 2) ? "flex" : "none";
                }}

                function openQA() {{ document.getElementById("qaModal").style.display = "block"; }}
                function closeQA() {{ document.getElementById("qaModal").style.display = "none"; }}
                function openGyms() {{ document.getElementById("gymsModal").style.display = "block"; }}
                function closeGyms() {{ document.getElementById("gymsModal").style.display = "none"; }}
                function openAnswer(text) {{
                    document.getElementById("answerText").innerText = text;
                    document.getElementById("answerModal").style.display = "block";
                }}
                function closeAnswer() {{ document.getElementById("answerModal").style.display = "none"; }}

                window.onclick = function(event) {{
                    if (event.target.className == "modal") {{ event.target.style.display = "none"; }}
                }}
            </script>
        </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
