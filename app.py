from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return f"""
    <html>
        <head>
            <title>Bouldering Library</title>
            <style>
                body {{ font-family: 'Segoe UI', Arial, sans-serif; background-color: #2c3e50; color: white; text-align: center; padding: 50px; margin: 0; }}
                .dropdown {{ position: fixed; top: 20px; right: 20px; display: inline-block; z-index: 1000; }}
                .dropbtn {{ background-color: #e67e22; color: white; padding: 12px 20px; font-size: 16px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; }}
                .dropdown-content {{ display: none; position: absolute; right: 0; background-color: #34495e; min-width: 200px; border-radius: 5px; }}
                .dropdown-content a {{ color: white; padding: 12px 16px; text-decoration: none; display: block; text-align: right; }}
                .dropdown:hover .dropdown-content {{ display: block; }}
                h1 {{ font-size: 3.5em; margin-bottom: 30px; margin-top: 60px; }}
                .main-img {{ width: 100%; max-width: 750px; border: 5px solid white; border-radius: 20px; margin-bottom: 30px; }}
                .sub-title {{ font-size: 2.5em; margin-bottom: 20px; color: #e67e22; font-weight: bold; }}
                .description {{ font-size: 1.3em; max-width: 850px; margin: 0 auto; line-height: 1.6; color: #ecf0f1; }}
            </style>
        </head>
        <body>
            <div class="dropdown">
                <button class="dropbtn">MENU ☰</button>
                <div class="dropdown-content">
                    <a href="https://www.youtube.com/watch?v=9LXySxPDZx0" target="_blank">TOKYO CLIMBING</a>
                    <a href="https://www.youtube.com/watch?v=45KmZUc0CzA" target="_blank">JANJA IN PARIS 🐐</a>
                    <a href="https://www.youtube.com/watch?v=P8lh_Y2OdFk" target="_blank">OUTDOOR BOULDERING</a>
                </div>
            </div>
            <h1>Welcome To The Bouldering Library</h1>
            <img src="/static/hero.jpg" class="main-img">
            <div class="sub-title">💥 THIS IS BOULDERING 💥</div>
            <p class="description">
                Bouldering is a discipline in sport climbing. This revolutionary sport swept millions around the world with pure adrenaline. 
                It became an Olympic sport with Lead and Speed climbing at the Olympic Games of Tokyo 2020. 
                Come and join this amazing sport!
            </p>
        </body>
    </html>
    """

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
