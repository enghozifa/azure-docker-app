from flask import Flask, request, render_template_string
from datetime import datetime

app = Flask(__name__)

students = [
    {"id": 101, "name": "Ahmed Ali", "grade": "Grade 10", "status": "Present"},
    {"id": 102, "name": "Sara Mohamed", "grade": "Grade 9", "status": "Absent"},
    {"id": 103, "name": "Omar Hassan", "grade": "Grade 11", "status": "Present"},
]

announcements = [
    "Parent meeting on Thursday at 10:00 AM",
    "Science fair registration is now open",
    "Mid-term exams start next week"
]

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        student_name = request.form.get("student_name")
        announcement = request.form.get("announcement")

        if student_name:
            students.append({
                "id": len(students) + 101,
                "name": student_name,
                "grade": "New Student",
                "status": "Pending"
            })
            message = f"Student {student_name} added successfully!"

        if announcement:
            announcements.append(announcement)
            message = "Announcement added successfully!"

    current_time = datetime.now().strftime("%A, %d %B %Y - %I:%M %p")

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Smart School Portal</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: #f4f7fb;
            }
            header {
                background: linear-gradient(90deg, #0052cc, #00b8d9);
                color: white;
                padding: 25px;
                text-align: center;
            }
            .container {
                width: 90%;
                margin: 30px auto;
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 25px;
            }
            .card {
                background: white;
                padding: 25px;
                border-radius: 15px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }
            h2 {
                color: #0052cc;
            }
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                padding: 12px;
                border-bottom: 1px solid #ddd;
                text-align: left;
            }
            input, button {
                padding: 12px;
                margin-top: 10px;
                width: 100%;
                border-radius: 8px;
                border: 1px solid #ccc;
            }
            button {
                background: #0052cc;
                color: white;
                border: none;
                cursor: pointer;
            }
            button:hover {
                background: #003d99;
            }
            .message {
                color: green;
                font-weight: bold;
            }
            .full {
                grid-column: span 2;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>🏫 Smart School Portal</h1>
            <p>Running on Azure App Service + Docker + ACR</p>
            <p>{{ current_time }}</p>
        </header>

        <div class="container">
            <div class="card">
                <h2>👨‍🎓 Student List</h2>
                <table>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Grade</th>
                        <th>Status</th>
                    </tr>
                    {% for student in students %}
                    <tr>
                        <td>{{ student.id }}</td>
                        <td>{{ student.name }}</td>
                        <td>{{ student.grade }}</td>
                        <td>{{ student.status }}</td>
                    </tr>
                    {% endfor %}
                </table>
            </div>

            <div class="card">
                <h2>📢 Announcements</h2>
                <ul>
                    {% for item in announcements %}
                    <li>{{ item }}</li>
                    {% endfor %}
                </ul>
            </div>

            <div class="card">
                <h2>➕ Add Student</h2>
                <form method="POST">
                    <input type="text" name="student_name" placeholder="Enter student name" required>
                    <button type="submit">Add Student</button>
                </form>
            </div>

            <div class="card">
                <h2>📝 Add Announcement</h2>
                <form method="POST">
                    <input type="text" name="announcement" placeholder="Enter announcement" required>
                    <button type="submit">Post Announcement</button>
                </form>
            </div>

            <div class="card full">
                <h2>📊 Dashboard Summary</h2>
                <p>Total Students: {{ students|length }}</p>
                <p>Total Announcements: {{ announcements|length }}</p>
                <p class="message">{{ message }}</p>
            </div>
        </div>
    </body>
    </html>
    """, students=students, announcements=announcements, current_time=current_time, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
