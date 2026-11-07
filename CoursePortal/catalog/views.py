from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.http import Http404
from django.shortcuts import render

COURSES_DATA = [
    {
        "id": 101,
        "code": "DTI412",
        "title": "Special Topic in Application Development",
        "credits": 3,
        "instructor": "Dr. Sirisuda Buathongkeow",
        "description": "Comprehensive backend application engineering focusing on Django, DRF, RESTful APIs, JWT security, and cloud deployment.",
    },
    {
        "id": 102,
        "code": "DTI201",
        "title": "Database Systems & Data Modeling",
        "credits": 3,
        "instructor": "Department Faculty",
        "description": "Relational database design, ER diagrams, SQL query optimization, normalization, and transaction management.",
    },
    {
        "id": 103,
        "code": "DTI305",
        "title": "Frontend Web Technologies & React",
        "credits": 3,
        "instructor": "Department Faculty",
        "description": "Modern user interface development using JavaScript ES6+, React components, state management, and API integration.",
    },
]


def home_view(request):
    return render(request, "catalog/home.html", {
        "total_courses": len(COURSES_DATA),
        "featured_course": COURSES_DATA[0],
    })


def course_list_view(request):
    query = request.GET.get("q", "").strip()
    search = query.casefold()
    courses = [
        course for course in COURSES_DATA
        if search in course["title"].casefold() or search in course["code"].casefold()
    ]
    return render(request, "catalog/course_list.html", {"courses": courses, "query": query})


def course_detail_view(request, course_id):
    course = next((course for course in COURSES_DATA if course["id"] == course_id), None)
    if course is None:
        raise Http404("Course with specified ID was not found.")
    return render(request, "catalog/course_detail.html", {"course": course})


def inquiry_view(request):
    errors = []
    submitted_data = None
    fields = {}
    if request.method == "POST":
        fields = {
            key: request.POST.get(key, "").strip()
            for key in ("student_name", "email", "message")
        }
        if not fields["student_name"]:
            errors.append("Student Name is required.")
        try:
            validate_email(fields["email"])
        except ValidationError:
            errors.append("A valid Email address is required.")
        if not fields["message"]:
            errors.append("Inquiry message cannot be empty.")
        if not errors:
            submitted_data = fields
            fields = {}
    return render(request, "catalog/inquiry.html", {
        "errors": errors,
        "submitted_data": submitted_data,
        "fields": fields,
    })
