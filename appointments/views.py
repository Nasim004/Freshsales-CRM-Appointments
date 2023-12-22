import json
import requests
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

headers = {
    "content-type": "application/json",
    "Authorization": "Token token=aRMe4bU6IzRjwGTiefaf5Q",
}


@csrf_exempt
def create_appointment(request):
    title = request.GET.get("title")
    from_date = request.GET.get("from_date")
    end_date = request.GET.get("end_date")

    data = {
        "appointment": {"title": title, "from_date": from_date, "end_date": end_date}
    }
    url = "https://tempoai.myfreshworks.com/crm/sales/api/appointments"
    response = requests.post(url, data=json.dumps(data), headers=headers)
    if response.status_code == 201:
        return JsonResponse({"Message": "Appointment created successfully"})
    else:
        error_message = (
            response.json().get("errors", {}).get("message", "Unknown error")
        )
        return JsonResponse({"error": error_message}, status=response.status_code)


def view_appointment(request):
    id = request.GET.get("id")
    url = f"https://tempoai.myfreshworks.com/crm/sales/api/appointments/{id}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data)
    else:
        error_message = (
            response.json().get("errors", {}).get("message", "Unknown error")
        )
        return JsonResponse({"error": error_message}, status=response.status_code)


def list_all_appointments(request):
    filter = request.GET.get("filter")
    url = "https://tempoai.myfreshworks.com/crm/sales/api/appointments"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        appointments = data.get("appointments", [])
        return JsonResponse({"appointments": appointments})
    else:
        error_message = (
            response.json().get("errors", {}).get("message", "Unknown error")
        )
        return JsonResponse({"error": error_message}, status=response.status_code)


@csrf_exempt
def update_appointments(request, id):
    title = request.GET.get("title")
    from_date = request.GET.get("from_date")
    end_date = request.GET.get("end_date")

    existing_data_url = (
        f"https://tempoai.myfreshworks.com/crm/sales/api/appointments/{id}"
    )
    existing_data_response = requests.get(existing_data_url, headers=headers)
    existing_data = existing_data_response.json()

    if title:
        existing_data["appointment"]["title"] = title
    if from_date:
        existing_data["appointment"]["from_date"] = from_date
    if end_date:
        existing_data["appointment"]["end_date"] = end_date

    update_url = f"https://tempoai.myfreshworks.com/crm/sales/api/appointments/{id}"
    response = requests.put(update_url, data=json.dumps(existing_data), headers=headers)
    print(response.status_code)
    return HttpResponse(response)

@csrf_exempt
def delete_appointment(request, id):
    url = f"https://tempoai.myfreshworks.com/crm/sales/api/appointments/{id}"
    response = requests.delete(url, headers=headers)
    if response.status_code == 200:
        return JsonResponse({"200": "Appointment Deleted Sucessfully"})
    else:
        error_message = (
            response.json().get("errors", {}).get("message", "Unknown error")
        )
        return JsonResponse({"error": error_message}, status=response.status_code)
