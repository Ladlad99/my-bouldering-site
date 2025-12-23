from flask import Flask, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    image_url = url_for('static', filename='hero.jpg')
    
    return f"""
    <html>
        <head>
            <title>Bouldering Library</title>
            <style>
                body {{
                    font-family: 'Segoe UI', Arial, sans-serif;
                    background-color: #2c3e50;
                    color: white;
                    text-align: center;
                    padding: 20px;
                    margin: 0;
                }}
                /* --- Header Section (Buttons and Title) --- */
                .header-container {{
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    padding: 20px;
                    max-width: 1200px;
                    margin: 0 auto;
                }}
                .nav-buttons {{
                    display: flex;
                    flex-direction: column;
                    gap: 10px;
                }}
                
                /* Main Title Styling */
                .main-title {{
                    font-size: 3.5em;
                    color: white;
                    margin: 0 20px;
                    flex-grow: 1;
                    font-weight: bold;
                }}

                /* --- Dropdown Menu (Right) --- */
                .dropdown {{ position: relative; display: inline-block; z-index: 1000; }}
                .dropbtn {{ background-color: #e67e22; color: white; padding: 12px 20px; font-size: 16px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; }}
                .dropdown-content {{ display: none; position: absolute; right: 0; background-color: #34495e; min-width: 200px; border-radius: 5px; }}
                .dropdown-content a {{ color: white; padding: 12px 16px; text-decoration: none; display: block; text-align: right; }}
                .dropdown:hover .dropdown-content {{ display: block; }}

                /* --- QA & Gyms Buttons (Left) --- */
                .qa-btn {{ background-color: #3498db; color: white; padding: 12px 20px; font-size: 16px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; width: 140px; }}
                .gyms-btn {{ background-color: #9b59b6; color: white; padding: 12px 20px; font-size: 16px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; width: 140px; }}

                /* --- Content Styling --- */
                .main-img {{ 
                    width: 100%; 
                    max-width: 750px; 
                    border: 5px solid white; 
                    border-radius: 20px; 
                    margin-top: 10px; /* Moved photo up */
                    margin-bottom: 20px; 
                }}
                .description {{ 
                    font-size: 1.3em; 
                    max-width: 850px; 
                    margin: 0 auto; 
                    line-height: 1.6; 
                    color: #ecf0f1; 
                }}

                /* --- Modal Pop-up Styling --- */
                .modal {{ display: none; position: fixed; z-index: 2000; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.7); }}
                .modal-content {{ background-color: #34495e; margin: 10% auto; padding: 25px; border: 2px solid #e67e22; border-radius: 15px; width: 300px; text-align: left; position: relative; }}
                #answerModal .modal-content {{ margin-top: 15%; width: 250px; border-color: #3498db; }}
                .gyms-modal-content {{ background-color: #2c3e50; margin: 5% auto; padding: 40px; border: 3px solid white; border-radius: 20px; width: 80%; height: 70vh; position: relative; display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: 1fr 1fr; gap: 20px; }}
                .close-btn {{ color: #bdc3c7; position: absolute; top: 10px; right: 20px; font-size: 28px; font-weight: bold; cursor: pointer; z-index: 2001; }}
                .close-btn:hover {{ color: white; }}
                
                .gym-box {{ display: flex; align-items: center; justify-content: center; font-size: 2em; font-weight: bold; text-decoration: none; border-radius: 15px; transition: transform 0.2s; border: 2px dashed rgba(255,255,255,0.2); }}
                .gym-box:hover {{ transform: scale(1.05); }}
                .issac {{ color: #ff69b4; }}
                .block {{ color: #ffff00; }}
                .performance {{ color: #2ecc71; }}
                .viking {{ color: #3498db; }}
                .qa-item {{ cursor: pointer; padding: 10px; border-bottom: 1px solid #2c3e50; transition: 0.3s; }}
                .qa-item:hover {{ color: #e67e22; background-color: #2c3e50; }}
            </style>
        </head>
        <body>
            <div class="header-container">
                <div class="nav-buttons">
                    <button class="qa-btn" onclick="openQA()">QA ❓</button>
                    <button class="gyms-btn" onclick="openGyms()">Gyms In TLV</button>
                </div>

                <div class="main-title">💥 THIS IS BOULDERING 💥</div>

                <div class="dropdown">
                    <button class="dropbtn">MENU ☰</button>
                    <div class="dropdown-content">
                        <a href="https://www.youtube.com/watch?v=9LXySxPDZx0" target="_blank">TOKYO CLIMBING</a>
                        <a href="https://www.youtube.com/watch?v=45KmZUc0CzA" target="_blank">JANJA IN PARIS 🐐</a>
                        <a href="https://www.youtube.com/watch?v=P8lh_Y2OdFk" target="_blank">OUTDOOR BOULDERING</a>
                    </div>
                </div>
            </div>

            <img src="{image_url}" class="main-img" alt="Bouldering Hero">
            
            <p class="description">
                Bouldering is a discipline in sport climbing. This revolutionary sport swept millions around the world with pure adrenaline. 
                It became an Olympic sport with Lead and Speed climbing at the Olympic Games of Tokyo 2020. 
                Come and join this amazing sport!
            </p>

            <div id="qaModal" class="modal">
                <div class="modal-content">
                    <span class="close-btn" onclick="closeQA()">&times;</span>
                    <h3>Common Questions</h3>
                    <div class="qa-item" onclick="openAnswer('Bouldering fits everybody! From a simple ladder to a world-class climb.')">Is Bouldering hard?</div>
                    <div class="qa-item" onclick="openAnswer('In every gym you have rental climbing shoes.')">I heard you need special shoes?</div>
                    <div class="qa-item" onclick="openAnswer('No, typically a climb is between 3-5 meters. You have a good and safe Crash Pad.')">Are you climbing with a rope?</div>
                </div>
            </div>

            <div id="answerModal" class="modal">
                <div class="modal-content">
                    <span class="close-btn" onclick="closeAnswer()">&times;</span>
                    <h3>Explanation</h3>
                    <p id="answerText" style="line-height:1.4;"></p>
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
                function openQA() {{ document.getElementById("qaModal").style.display = "block"; }}
                function closeQA() {{ document.getElementById("qaModal").style.display = "none"; }}
                function openAnswer(text) {{
                    document.getElementById("answerText").innerText = text;
                    document.getElementById("answerModal").style.display = "block";
                }}
                function closeAnswer() {{ document.getElementById("answerModal").style.display = "none"; }}
                function openGyms() {{ document.getElementById("gymsModal").style.display = "block"; }}
                function closeGyms() {{ document.getElementById("gymsModal").style.display = "none"; }}

                window.onclick = function(event) {{
                    if (event.target.className == "modal") {{
                        event.target.style.display = "none";
                    }}
                }}
            </script>
        </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
