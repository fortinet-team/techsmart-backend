from .models import Question, Choice
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize

import json

@csrf_exempt
def list_question(request):

    if request.method == "GET":
        data = Question.objects.values("id", "question_text", "pub_date")
        # questions = Question.objects.all()
        # data = [{"id" : q.id, "question_text" : q.question_text, "pub_date": q.pub_date} for q in questions]
        return JsonResponse({"status": "OK", "data": list(data)}, status=203, safe=False)

    elif request.method == "POST":
        data = json.loads(request.body)
        question_text = data.get("question_text", "")
        pub_date = data.get("pub_date", "")

        if question_text and pub_date:
            new_question = Question(question_text=question_text, pub_date=pub_date)
            new_question.save()
            return JsonResponse({"message": "Berhasil Menambah Data"})
        else:
            return JsonResponse({"message": "Data tidak valid. Question_text dan pub_date diperlukan."})

    elif request.method == "PUT":
        data = json.loads(request.body)
        question_id = data.get("id", "")
        # question_text = data.get("question_text", "")
        pub_date = data.get("pub_date", "")

        try:
            question = Question.objects.get(pk=question_id)
            if question_text:
                question.question_text = question_text
            if pub_date:
                question.pub_date = pub_date
            question.save()
            return JsonResponse({"message": "Data berhasil diperbarui"})
        except Question.DoesNotExist:
            return JsonResponse({"message": "Pertanyaan tidak ditemukan"}, status=404)

    elif request.method == "DELETE":
        data = json.loads(request.body)
        question_id = data.get("id", "")
        try:
            question = Question.objects.get(pk=question_id)
            question.delete()
            return JsonResponse({"message": "Data berhasil dihapus"})
        except Question.DoesNotExist:
            return JsonResponse({"message": "Pertanyaan tidak ditemukan"}, status=404)

@csrf_exempt
def list_choice(request): 

    if request.method == "GET":
        # choices = Choice.objects.all()
        # print(choices)
        choices = Choice.objects.values("question_id", "question__question_text", "id", "choice_text", "votes")
        return JsonResponse({"status": "OK", "data": list(choices)}, safe=False)
        # return JsonResponse(serialize("json", choices, fields=["question", "choice_text", "votes"]), safe=False)

    elif request.method == "POST":
        data = json.loads(request.body)
        question_id = data.get("question_id", "")
        choice_text = data.get("choice_text", "")
        votes = data.get("votes", 0)

        if question_id and choice_text:
            try:
                question = Question.objects.get(pk=question_id)
                new_choice = Choice(question=question, choice_text=choice_text, votes=votes)
                new_choice.save()
                return JsonResponse({"message": "Berhasil Menambah Data"})
            except Question.DoesNotExist:
                return JsonResponse({"message": "Pertanyaan tidak ditemukan"}, status=404)
        else:
            return JsonResponse({"message": "Data tidak valid. question_id dan choice_text diperlukan."}, status=400)

    elif request.method == "PUT":
        data = json.loads(request.body)
        choice_id = data.get("choice_id", "")
        choice_text = data.get("choice_text", "")
        votes = data.get("votes", 0)
        question_id = data.get("question_id", "")
        question_text = data.get("question_text", "")

        try:
            choice = Choice.objects.get(pk=choice_id)
            if choice_text:
                choice.choice_text = choice_text
            choice.votes = votes
            choice.save()
            
            # Jika ada question_id dan question_text dalam permintaan, perbarui data Question
            if question_id and question_text:
                try:
                    question = Question.objects.get(pk=question_id)
                    question.question_text = question_text
                    question.save()
                except Question.DoesNotExist:
                    return JsonResponse({"message": "Pertanyaan tidak ditemukan"}, status=404)

            return JsonResponse({"message": "Data berhasil diperbarui"})
        except Choice.DoesNotExist:
            return JsonResponse({"message": "Pilihan tidak ditemukan"}, status=404)

    elif request.method == "DELETE":
        data = json.loads(request.body)
        choice_id = data.get("choice_id", "")

        try:
            choice = Choice.objects.get(pk=choice_id)
            choice.delete()
            return JsonResponse({"message": "Data berhasil dihapus"})
        except Choice.DoesNotExist:
            return JsonResponse({"message": "Pilihan tidak ditemukan"}, status=404)

@csrf_exempt
def getquestionByid(request, question_id):
    if request.method == "GET":
        try:
            question = Question.objects.get(pk=question_id)
            data = {
                "question_id": question.id,
                "question_text": question.question_text,
                "pub_date": question.pub_date
            }
            return JsonResponse({"status": "OK", "data": [data]}, safe=False)
        except Question.DoesNotExist:
            return JsonResponse({"message": "Pertanyaan tidak ditemukan"}, status=404)

    return JsonResponse({"message": "Metode HTTP tidak didukung untuk endpoint ini."}, status=405)

@csrf_exempt
def getchoiceByid(request, choice_id):
    if request.method == "GET":
        try:
            choice = Choice.objects.get(pk=choice_id)
            data = {
                "choice_id": choice.id,
                "question_id": choice.question.id,
                "choice_text": choice.choice_text,
                "votes": choice.votes
            }
            return JsonResponse({"status": "OK", "data": [data]}, safe=False)
        except Choice.DoesNotExist:
            return JsonResponse({"message": "Pilihan tidak ditemukan"}, status=404)

    return JsonResponse({"message": "Metode HTTP tidak didukung untuk endpoint ini."}, status=405)