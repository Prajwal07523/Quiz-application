from django.shortcuts import render
from .models import QuizSession, Question
from django.db.models import Count, Q
import random
import uuid
from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, 'quiz/index.html')


def start_quiz(request):
    session_id = str(uuid.uuid4())  # Create a unique session ID for the user
    questions = Question.objects.all()

    if not questions.exists():
        return JsonResponse({"error": "No questions available in the database"}, status=404)

    # Shuffle questions randomly
    shuffled_questions = random.sample(list(questions), len(questions))

    # Create a QuizSession entry for each question in the shuffled order
    for question in shuffled_questions:
        QuizSession.objects.create(
            session_id=session_id,
            question=question
        )

    # Pick the first question for the user to start with (it will be random)
    first_question = shuffled_questions[0]
    return JsonResponse({
        "session_id": session_id,  # Return the session ID to the user
        "question": first_question.text,
        "options": {
            "A": first_question.option_a,
            "B": first_question.option_b,
            "C": first_question.option_c,
            "D": first_question.option_d,
        }
    })


def get_question(request):
    session_id = request.GET.get("session_id")
    if not session_id:
        return JsonResponse({"error": "Session ID is required."})

    # Find the next unanswered question for the session
    unanswered = QuizSession.objects.filter(session_id=session_id, user_answer__isnull=True)

    if not unanswered.exists():
        return JsonResponse({"error": "No more questions available."})

    # Shuffle the unanswered questions to get a random one
    random_question_session = random.choice(unanswered)
    question = random_question_session.question

    return JsonResponse({
        "id": random_question_session.id,
        "text": question.text,
        "options": {
            "A": question.option_a,
            "B": question.option_b,
            "C": question.option_c,
            "D": question.option_d,
        }
    })


def submit_answer(request):
    session_id = request.GET.get("session_id")
    session_entry_id = request.GET.get("session_entry_id")
    user_answer = request.GET.get("answer")

    try:
        session_entry = QuizSession.objects.get(id=session_entry_id, session_id=session_id)
    except QuizSession.DoesNotExist:
        return JsonResponse({"error": "Invalid session or question."})

    session_entry.user_answer = user_answer
    session_entry.is_correct = session_entry.question.correct_option == user_answer
    session_entry.save()

    return JsonResponse({"is_correct": session_entry.is_correct})


from django.http import JsonResponse
from django.db.models import Count

from django.http import JsonResponse

def quiz_summary(request):
    session_id = request.GET.get("session_id")
    if not session_id:
        return JsonResponse({"error": "Session ID is required."}, status=400)

    # Get all quiz session entries for the given session_id
    sessions = QuizSession.objects.filter(session_id=session_id)

    # Ensure there are sessions to process
    if not sessions.exists():
        return JsonResponse({"error": "No quiz sessions found for the provided Session ID."}, status=404)

    # Process the sessions manually to count correct and incorrect answers
    correct_answers = 0
    incorrect_answers = 0
    details = []

    for session in sessions:
        if session.is_correct:
            correct_answers += 1
        else:
            incorrect_answers += 1

        # Add question details
        question = session.question
        question_details = {
            "question": question.text,
            "user_answer": session.user_answer,
            "is_correct": session.is_correct,
            "options": {
                "A": question.option_a,
                "B": question.option_b,
                "C": question.option_c,
                "D": question.option_d,
            },
            "correct_option": question.correct_option,
        }
        details.append(question_details)

    return JsonResponse({
        "total_questions": sessions.count(),
        "correct_answers": correct_answers,
        "incorrect_answers": incorrect_answers,
        "details": details,
    })
