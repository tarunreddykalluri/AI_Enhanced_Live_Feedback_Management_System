from google import genai
import json
import os
from dotenv import load_dotenv
from django.shortcuts import render
from django.http import JsonResponse
from .forms import feedbackform
from .models import Feedback

load_dotenv()

client = genai.Client(api_key=os.environ.get("GEMINI_API_KEY"))

def feedbackview(request):
    print("Entered feedbackview")
    f = feedbackform()

    if request.method == 'POST':
        print("POST detected", request.POST)

        if 'submit' in request.POST:
            print("Submit clicked")
            f = feedbackform(request.POST)

            if f.is_valid():
                feedback_instance = f.save()
                print("Feedback saved successfully")

                d = {
                    'id': feedback_instance.id,
                    'name': feedback_instance.name,
                    'age': feedback_instance.age,
                    'movie': feedback_instance.movie,
                    'email': feedback_instance.email,
                    'feed': feedback_instance.feed
                }

                return render(request, 'myapp/response.html', d)

        elif 'view' in request.POST:
            print("View clicked")

            d = {
                'name': request.POST.get('name', ''),
                'age': request.POST.get('age', ''),
                'movie': request.POST.get('movie', ''),
                'email': request.POST.get('email', ''),
                'feed': request.POST.get('feed', '')
            }

            return render(request, 'myapp/output.html', d)

    return render(request, 'myapp/input.html', {'form': f})


def analyze_ai(request, feedback_id):
    if request.method == "POST":
        try:
            feedback = Feedback.objects.get(id=feedback_id)

            prompt = f"""
            Analyze this movie review and return the result ONLY as a JSON object.

            Movie: {feedback.movie}
            Review: {feedback.feed}

            Format:
            {{
                "sentiment": "Positive/Negative/Neutral",
                "summary": "One short sentence",
                "suggestions": "One tip for the director"
            }}
            """

            response = client.models.generate_content(
                model="gemini-3-flash-preview",
                contents=prompt
            )

            raw_text = response.text.strip()
            raw_text = raw_text.replace('```json', '').replace('```', '')
            ai_data = json.loads(raw_text)

            feedback.sentiment = ai_data.get('sentiment')
            feedback.summary = ai_data.get('summary')
            feedback.suggestions = ai_data.get('suggestions')
            feedback.is_analyzed = True
            feedback.save()

            return JsonResponse({
                "status": "success",
                "data": ai_data
            })

        except Exception as e:
            print(f"AI Error: {str(e)}")

            return JsonResponse({
                "status": "error",
                "message": str(e)
            }, status=500)

    return JsonResponse({
        "status": "error",
        "message": "POST request required"
    }, status=405)