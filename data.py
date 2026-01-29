# data.py

# This dictionary contains all the TechFest & Naadham 2K26 data
kb = {
    # --- MAJOR COMPETITIONS (Tech) ---
    "hackathon": {
        "keywords": ["hackathon", "hack", "ideathon", "coding", "code", "116"],
        "response": """
💻 **Hackathon & Ideathon**
📍 **Venue:** Room 116
- **Ideathon:** 10:30 AM - 12:30 PM
- **Hackathon:** 1:30 PM - 4:00 PM
[cite_start]*Public Allowed: Yes* [cite: 5, 24]
"""
    },
    
    "project": {
        "keywords": ["project", "expo", "exhibition", "model", "118"],
        "response": """
🔬 **Project Expo (School & College)**
📍 **Venue:** Room 118
🕐 **Time:** 9:30 AM - 11:30 AM
[cite_start]*Come see the best innovations!* [cite: 10, 11]
"""
    },

    "bridge": {
        "keywords": ["bridge", "civil", "structure", "design", "117"],
        "response": """
🌉 **Bridge Design Competition**
📍 **Venue:** Room 117
🕐 **Time:** 2:00 PM - 3:30 PM
[cite_start]*Test your engineering skills!* [cite: 24]
"""
    },

    "tech_events": {
        "keywords": ["circuit", "debug", "guess", "output", "component", "identification", "122"],
        "response": """
⚡ **Technical Challenges (Circuit Branch)**
📍 **Venue:** Room 122
- **Component Identification:** 11:30 AM - 12:30 PM
- **Guess the Output:** 2:00 PM - 2:30 PM
- **Circuit Debugging:** 2:30 PM - 3:30 PM
[cite_start][cite: 22, 23, 24]
"""
    },

    "quiz": {
        "keywords": ["quiz", "trivia", "questions", "124"],
        "response": """
🧠 **General Quiz**
📍 **Venue:** Room 124
🕐 **Time:** 11:30 AM - 12:30 PM
[cite_start]*Open to Public* [cite: 15, 19]
"""
    },

    # --- FUN & ENTERTAINMENT ---
    "gaming": {
        "keywords": ["game", "gaming", "esports", "play", "018"],
        "response": """
🎮 **CSE Gaming Arena**
📍 **Venue:** Room 018
*Come play various e-sports titles!*
"""
    },

    "rooms": {
        "keywords": ["snow", "horror", "space", "fun", "room", "019", "022", "115"],
        "response": """
🎉 **Themed Rooms:**
- ❄️ **Snow Room:** Room 019
- 👻 **Horror Room:** Room 022
- 🚀 **Space Room:** Room 115
"""
    },

    "robotics": {
        "keywords": ["robo", "robot", "bot", "003"],
        "response": """
🤖 **Robotics Zone**
📍 **Venue:** Room 003
*Check out the latest bots!*
"""
    },

    "band": {
        "keywords": ["band", "music", "concert", "song", "dj", "performance"],
        "response": """
🎸 **Live Band Performance**
📍 **Venue:** Main Stage
🕐 **Time:** 6:00 PM - 8:30 PM
[cite_start]*Public Allowed: YES* [cite: 42]
"""
    },

    # --- STALLS ---
    "stalls": {
        "keywords": ["stall", "shop", "food", "dept", "department"],
        "response": """
🎪 **Department Stalls:**
- **CSE Stalls:** Room 015 & 016
- **Civil Stall:** Room 023
- **ECE & EEE Stall:** Room 024
- **Mechanical (ME):** Room 013
- **Entrepreneurship:** Room 123
"""
    },

    # --- SCHEDULES ---
    "schedule": {
        "keywords": ["schedule", "time", "when", "list", "plan", "timeline"],
        "response": """
📅 **TechFest 2K26 Schedule**

**Morning:**
- 09:00: Inauguration
- 09:30: Project Expo (Room 118)
- 10:30: Ideathon (Room 116)
- 11:30: Quiz (Room 124) & Comp. ID (Room 122)

**Afternoon:**
- 01:30: Hackathon (Room 116)
- 02:00: Bridge Design (Room 117)
- 02:00: Guess Output (Room 122)
- 02:30: Circuit Debug (Room 122)
- 03:00: Treasure Hunt (Internal)

**Evening:**
- 04:30: Prize Distribution
- 06:00: **Band Performance** 🎸
[cite_start][cite: 7, 11, 16, 19, 23, 24, 42]
"""
    },

    "map": {
        "keywords": ["map", "location", "where", "find", "venue"],
        "response": """
📍 **Quick Location Guide:**
- **Ground Floor:** Robotics (003), ME (013), CSE Stalls (015/16), Gaming (018), Snow (019), Horror (022), Civil/ECE (023/24).
- **First Floor:** Space (115), Hackathon (116), Bridge (117), Expo (118), Tech Events (122), Entrepreneur (123), Quiz (124).
- **Courtyard:** Fun Games
"""
    },
    
    "greetings": {
        "keywords": ["hi", "hello", "hey", "start", "help"],
        "response": "👋 **Hi! Welcome to TechFest 2K26.**\nAsk me about:\n- 📅 Schedule\n- 📍 Where is Gaming?\n- 💻 Hackathon details\n- 🎸 Band Performance"
    }
}