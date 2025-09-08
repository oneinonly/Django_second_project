from django.shortcuts import render
def home(req):
     
    return render(req, 'Home.html' )

def about(req):
    return render(req, 'About.html')

def index_view(request):
    return render(request, "index.html")


def contact(req):
    context = {
        'name': "netligent",
        'profile': "SOFTWARE DEVELOPER",
        'Salary': 364364,
        'department': "information technology",
        'att': ['A', 'P', 'A', 'A', 'P'],
        'desc': "Hello I am working as a Software developer"
    }
    return render(req, 'contact.html', context)

def candidate_view(request):
    # Backend data (jo aap template ko bhejna chahte ho)
    context = {
        'name': 'Arun Kumar',
        'age': 25,
        'skills': ['Python', 'Django', 'JavaScript']
    }
    return render(request, 'candidate.html', context)

def marksheet_view(request):
    data = {
        "roll_no": "1100853",
        "school": "GOVT SR SEC SCH, SRINAGAR ROAD, AJMER",
        "year": 2024,
        "name": "Ganesh",
        "mother": "Parvati",
        "father": "Shiv",
        "gender": 'Male',
        "dob": '01-01-2000',
        "medium": 'English',
        "subjects": [
            {"name": "HINDI", "th": 68, "ss": 20, "pr": 0},
            {"name": "ENGLISH", "th": 58, "ss": 20, "pr": 0},
            {"name": "SCIENCE", "th": 63, "ss": 20, "pr": 0},
            {"name": "SOC.SCIENCE", "th": 66, "ss": 20, "pr": 0},
            {"name": "MATHEMATICS", "th": 62, "ss": 20, "pr": 0},
            {"name": "SANSKRIT", "th": 62, "ss": 20, "pr": 0},
        ],
        "total": 499,
        "percentage": 83.17,
        "result": "First Division",
    }
    return render(request, "marksheet.html", data)
def admitcard_view(request):
    data = {
        "roll_no": "631005633",
        "name": "ARUN AHIRWAR",
        "father": "RAMESH AHIRWAR",
        "cnic": "61101-0134843-2",
        "paper_type": "FULLSTACK DEVELOPMENT",
        "test_date": "Sunday 1st September, 2025",
        "report_time": "08:00 AM",
        "center": "MAULANA AZAD,  BHOPAL",
        "photo": "/static/images/photo.jpg",  # apni image static folder me rakhna
    }
    return render(request, "admitcard_view.html", data)