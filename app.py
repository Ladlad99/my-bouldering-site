<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>האתר שלי - סטייל אסתטי</title>
    <style>
        /* הגדרות כלליות - הכל נשאר אותו דבר במבנה */
        body {
            margin: 0;
            padding: 0;
            display: flex;
            flex-direction: column;
            align-items: center;
            font-family: 'Segoe UI', Arial, sans-serif;
            
            /* שינוי צבעים: רקע שחור בהיר נקי */
            background-color: #1a1a1a; 
            color: #ffffff; /* טקסט לבן נשאר לבן */
        }

        /* עיצוב התמונה שלך */
        .profile-img {
            width: 180px;
            height: 180px;
            border-radius: 50%;
            margin-top: 40px;
            object-fit: cover;
            /* מסגרת חום אסתטי במקום כתום */
            border: 4px solid #8b5a2b; 
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        }

        h1 {
            margin: 20px 0 10px 0;
            font-size: 2.5rem;
        }

        /* כתוביות שהיו בכתום - עכשיו בחום */
        .highlight {
            color: #8b5a2b;
            font-weight: bold;
        }

        .description {
            font-size: 1.1rem;
            max-width: 600px;
            text-align: center;
            margin-bottom: 40px;
            color: #e0e0e0;
        }

        /* אזור הסרטונים מיוטיוב */
        .video-section {
            display: flex;
            flex-direction: column;
            gap: 20px;
            width: 100%;
            align-items: center;
            padding-bottom: 50px;
        }

        iframe {
            width: 90%;
            max-width: 560px;
            aspect-ratio: 16 / 9;
            border-radius: 12px;
            /* מסגרת עדינה לסרטון בשחור עוד יותר כהה */
            border: 2px solid #2c2c2c;
        }

        /* כפתורי קישור אם יש */
        .btn {
            background-color: #8b5a2b;
            color: white;
            padding: 12px 25px;
            text-decoration: none;
            border-radius: 8px;
            margin-top: 20px;
            transition: 0.3s;
        }

        .btn:hover {
            background-color: #a67c52;
        }
    </style>
</head>
<body>

    <img src="https://images.unsplash.com/photo-1506794778202-cad84cf45f1d?q=80&w=1000" alt="Profile" class="profile-img">

    <h1>ברוכים הבאים ל<span class="highlight">ערוץ שלי</span></h1>
    <p class="description">
        כאן תוכלו למצוא את כל הסרטונים והתכנים שלי בסטייל <span class="highlight">נקי ואסתטי</span>. 
        הלבן נשאר לבן, הרקע הפך לשחור והדגשים עברו לחום יוקרתי.
    </p>

    <div class="video-section">
        <h2 class="highlight">סרטונים נבחרים</h2>
        
        <iframe src="https://www.youtube.com/watch?v=nJNyylYDp0Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
        
        <iframe src="https://www.youtube.com/watch?v=rQq_8YeP3Y4" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
    </div>

    <a href="https://www.youtube.com/watch?v=P8lh_Y2OdFk" class="btn">לערוץ היוטיוב המלא</a>

</body>
</html>

