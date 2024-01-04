from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pymongo import MongoClient
from rest_framework.decorators import api_view

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import random

import requests
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.conf import settings
from django.utils import timezone
from datetime import datetime, timedelta, time as dt_time
import pytz
import hashlib
import json
from urllib.parse import unquote

from django.core.mail import send_mail

from dateutil import parser

import sys
import os
import pandas as pd

# MongoDB initialization
client = MongoClient('mongodb://localhost:27017/')
db = client.server_db
sensor_data_collection = db.klaen_arduinoSensor
buildthing_data_collection = db.klaen_buildthing

# Create your views here.
def indoorBuildthing(request):
    try:
        num_documents = buildthing_data_collection.count_documents({})

        # Fetch a limited number of documents (e.g., 100) from the collection
        # You can adjust the limit as needed for better response time
        documents = list(buildthing_data_collection.find(
            projection={"_id": 0}
        ).sort("Time", -1).limit(10))

        # Close the MongoDB connection
        client.close()
        
        collection_stats = db.command('collStats','klaen_buildthing')
        size_in_mb = collection_stats['size'] / (1024 * 1024)

        # Create a response dictionary with data and count
        response_data = {
            'total_rows': num_documents,
            'size_in_mb':size_in_mb,
            'data': documents,
        }

        # Pass the response_data to JsonResponse
        return JsonResponse(response_data, safe=False)
    except Exception as e:
        # Handle any exceptions that may occur
        return JsonResponse({'error': str(e)}, status=500)
