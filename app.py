from flask import Flask, url_for
import os

app = Flask(__name__)

@app.route('/')
def home():
    image_url = url_for('static', filename='hero.jpg')
    # Link your 3 MP4 files here
    vid1_url = url_for('static', filename='climb1.mp4')
    vid2_url = url_for('static', filename='climb2.mp4')
    vid3_url = url_for('static', filename='climb3.mp4')
    
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
                /* --- Header Section --- */
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
                .main-title {{
                    font-size: 3.5em;
                    color: white;
                    margin: 0 20px;
                    flex-grow: 1;
                    font-weight: bold;
                }}

                /* --- Buttons & Dropdown --- */
                .dropdown {{ position: relative; display: inline-block; z-index: 1000; }}
                .dropbtn {{ background-color: #e67e22; color: white; padding: 12px 20px; font-size: 16px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; }}
                .dropdown-content {{ display: none; position: absolute; right: 0; background-color: #34495e; min-width: 200px; border-radius: 5px; }}
                .dropdown-content a {{ color: white; padding: 12px 16px; text-decoration: none; display: block; text-align: right; }}
                .dropdown:hover .dropdown-content {{ display: block; }}
                .qa-btn {{ background-color: #3498db; color: white; padding: 12px 20px; font-size: 16px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; width: 140px; }}
                .gyms-btn {{ background-color: #9b59b6; color: white; padding: 12px 20px; font-size: 16px; border: none; border-radius: 5px; cursor: pointer; font-weight: bold; width: 140px; }}

                /* --- Main Hero Image (Sized Down) --- */
                .main-img {{ 
                    width: 100%; 
                    max-width: 600px; /* Sized down from 750px */
                    border: 5px solid white; 
                    border-radius: 20px; 
                    margin-top: 10px;
                    margin-bottom: 20px; 
                }}

                /* --- Video Gallery (Perfect Line) --- */
                .video-container {{
                    display: flex;
                    justify-content: center;
                    gap: 15px;
                    max-width: 1000px;
                    margin: 0 auto 30px auto;
                }}
                .video-item {{
                    width: 30%; /* Ensures they stay in one line */
                    aspect-ratio: 16/9;
                    object-fit: cover;
                    border: 3px solid #e67e22;
                    border-radius: 10px;
                    background-color: black;
                }}

                /* --- Description at bottom --- */
                .description {{ 
                    font-size: 1.3em; 
                    max-width: 850px; 
                    margin: 0 auto 50px auto; 
                    line-height: 1.6; 
                    color: #ecf0f1; 
                }}

                /* --- Modals --- */
                .modal {{ display: none; position: fixed; z-index: 2000; left: 0; top: 0; width: 100%; height: 100%; background-color: rgba(0,0,0,0.7); }}
                .modal-content {{ background-color: #34495e; margin: 10% auto; padding: 25px; border: 2px solid #e67e22; border-radius: 15px; width: 300px; text-align: left; position: relative; }}
                #answerModal .modal-content {{ margin-top: 1
