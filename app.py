from flask import Flask, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    image_url = url_for('static', filename='hero.jpg')
    qa_bg_url = url_for('static', filename='hero2.jpg')
    hero3_url = url_for('static', filename='hero3.jpg') # Background for the text swap
    vid1_url = url_for('static', filename='climb1.mp4')
    vid3_url = url_for('static', filename='climb3.mp4')
    
    return f"""
    <html>
        <head>
            <title>Bouldering Library</title>
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <style>
                body {{
                    font-family: 'Segoe UI', Arial, sans-serif;
                    background-color: #2c3e50;
                    color: white;
                    text-align: center;
                    padding: 10px;
                    margin: 0;
                }}
                /* --- Header --- */
                .header-container {{
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 10px 20px;
                    max-width: 1200px;
                    margin: 0 auto;
                }}
                .nav-buttons {{ display: flex; flex-direction: column; gap: 5px; }}
                .main-title {{ font-size: 2.5em; color: white; margin: 0 20px; flex-grow: 1; font-weight: bold; }}
                
                .dropdown {{ position: relative; display: inline-block; z-index: 1000; }}
                .dropbtn {{ background-color: #e67e22; color: white; padding: 10px 15px; font-size: 16px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; }}
                .dropdown-content {{ display: none; position: absolute; right: 0; background-color: #34495e; min-width: 200px; border-radius: 5px; }}
                .dropdown-content a {{ color: white; padding: 12px 16px; text-decoration: none; display: block; text-align: right; }}
                .dropdown:hover .dropdown-content {{ display: block; }}
                
                .qa-btn {{ background-color: #3498db; color: white; padding: 10px; font-size: 14px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; width: 130px; }}
                .gyms-btn {{ background-color: #9b59b6; color: white; padding: 10px; font-size: 14px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; width: 130px; }}

                /* --- Sized Down Hero Section --- */
                .hero-wrapper {{
                    width: 100%;
                    max-width: 500px; /* Reduced size to fit screen without scroll */
                    height: 350px;
                    margin: 0 auto 20px auto;
                    border: 5px solid white;
                    border-radius: 20px;
                    overflow: hidden;
                    cursor: pointer;
                    position: relative;
                }}
                
                .main-img {{ 
                    width: 100%; 
                    height: 100%;
                    object-fit: cover;
                }}

                .description-overlay {{
                    display: none;
                    width: 100%;
                    height: 100%;
                    background-image: linear-gradient(rgba(0,0,0,0.7), rgba(0,0,0,0.7)), url('{hero3_url}');
                    background-size: cover;
                    background-position: center;
                    padding: 20px;
                    box-sizing: border-box;
                    justify-content: center;
                    align-items: center;
                    font-size: 1.1em;
                    line-height: 1.4;
                }}

                /* --- Videos --- */
                .video-container {{
                    display: flex;
                    justify-content: center;
                    gap: 20px;
                    max-width: 1100px;
                    margin: 0 auto 20px auto;
                }}
                .video-item {{
                    width: 20%; 
                    max-height: 180px; 
                    object-fit: contain; 
                    border: 2px solid white; 
                    border-radius: 12px;
                }}

                /* --- Modals --- */
                .modal {{ display: none; position: fixed; z-index: 2000; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.85); }}
                
                .modal-content-qa {{ 
                    background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('{qa_bg_url}');
                    background-size: cover;
                    margin: 5% auto; 
                    padding: 40px; 
                    border: 3px solid #3498db; 
                    border-radius: 20px; 
                    width: 60%;
                    color: white; 
                }}

                .gyms-modal-content {{ background-color: #2c3e50; margin: 5% auto; padding: 40px; border: 3px solid white; border-radius: 20px; width: 80%; height: 70vh; display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 20px; }}
                
                .close-btn {{ color: #ffffff; position: absolute; top: 15px; right: 25px; font-size: 35px; font-weight: bold; cursor: pointer; }}
                
                .qa-item {{ cursor: pointer; padding: 15px; font-size: 1.3em; border-bottom: 1px solid rgba(255,255,255,0.3); background: rgba(0,0,0,0.2); margin-bottom: 10px; border-radius: 5px; text-align: left; }}

                .gym-box {{ display: flex; align-items: center; justify-content: center; font-size: 1.8em; font-weight: bold; text-decoration: none; border-radius: 15px; border: 2px dashed rgba(255,255,255,0.2); }}
                .issac {{ color: #ff69b4; }} .block {{ color: #ffff00; }} .performance {{ color: #2ecc71; }} .viking {{ color: #3498db; }}

                /* Mobile Responsiveness */
                @media (max-width: 768px) {{
                    .header-container {{ flex-direction: column; }}
                    .video-container {{ flex-direction: row; gap: 10px; }}
                    .video-item {{ width: 45%; }}
                    .gyms-modal-content {{ grid-template-columns: 1fr; overflow-y: auto; }}
                }}
            </style>
        </head>
        <body>
            <div class="header-container">
                <div class="nav-buttons">
                    <button class="qa-btn" onclick="openQA()">QA ❓</button>
                    <button class="gyms-btn" onclick="openGyms()">Gyms In TLV</button>
                </div>

                <div class="main-title">The Boulder Coach</div>

                <div class="dropdown">
                    <button class="dropbtn">MENU ☰</button>
                    <div class="dropdown-content">
                        <a href="https://www.youtube.com/watch?v=9LXySxPDZx0" target="_blank">TOKYO CLIMBING</a>
                        <a href="https://www.youtube.com/watch?v=45KmZUc0CzA" target="_blank">JANJA IN PARIS 🐐</a>
                        <a href="https://www.youtube.com/watch?v=P8lh_Y2OdFk" target="_blank">OUTDOOR BOULDERING</a>
                    </div>
                </div>
            </div>

            <div class="hero-wrapper" onclick="toggleDescription()">
                <img src="{image_url}" id="heroImage" class="main-img" alt="Bouldering Hero">
                <div id="heroDescription" class="description-overlay">
                    Bouldering is a discipline in sport climbing. This revolutionary sport swept millions around the world with pure adrenaline. 
                    It became an Olympic sport with Lead and Speed climbing at the Olympic Games of Tokyo 2020. 
                    Come and join this amazing sport!
                </div>
            </div>
            
            <div class="video-container">
                <video class="video-item" autoplay muted loop playsinline>
                    <source src="{vid1_url}" type="video/mp4">
                </video>
                <video class="video-item" autoplay muted loop playsinline>
                    <source src="{vid3_url}" type="video/mp4">
                </video>
            </div>

            <div id="qaModal" class="modal">
                <div class="modal-content-qa">
                    <span class="close-btn" onclick="closeQA()">&times;</span>
                    <h2 style="font-size: 2.5em; margin-bottom: 20px;">Common Questions</h2>
                    <div class="qa-item" onclick="openAnswer('Bouldering fits everybody! From a simple ladder to a world-class climb.')">Is Bouldering hard?</div>
                    <div class="qa-item" onclick="openAnswer('You can rent climbing shoes at every gym')">I heard you need special shoes?</div>
                    <div class="qa-item" onclick="openAnswer('No, typically a climb is between 3-5 meters. also You have a good and safe mattress.')">Are you climbing with a rope?</div>
                </div>
            </div>

            <div id="answerModal" class="modal">
                <div class="modal-content-qa" style="border-color: #e67e22; width: 50%;">
                    <span class="close-btn" onclick="closeAnswer()">&times;</span>
                    <h2 style="font-size: 2em; color: #e67e22;">Explanation</h2>
                    <p id="answerText" style="font-size: 1.8em; line-height: 1.4;"></p>
                </div>
            </div>

            <div id="gymsModal" class="modal">
                <div class="gyms-modal-content">
                    <span class="close-btn" onclick="closeGyms()">&times;</span>
                    <a href="https://www.isaacclimbing.com" target="_blank" class="gym-box issac">Issac Climbing gym</a>
                    <a href="https://www.thebloc.co.il/tlv" target="_blank" class="gym-box block">Block Climbing Gym</a>
                    <a href="https://performancerock.co.il/branch/midtown-tlv/" target="_blank" class="gym-box performance">Performance Climbing Gym</a>
                    <a href="https://vking.co.il/" target="_blank" class="gym-box viking">Viking Climbing Gym</a>
                </div>
            </div>

            <script>
                function toggleDescription() {{
                    var img = document.getElementById("heroImage");
                    var desc = document.getElementById("heroDescription");
                    if (img.style.display === "none") {{
                        img.style.display = "block";
                        desc.style.display = "none";
                    }} else {{
                        img.style.display = "none";
                        desc.style.display = "flex";
                    }}
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
    app.run(host='0.0.0.0', port=port, debug=False)
