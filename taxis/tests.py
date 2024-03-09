from django.test import TestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status


class TestTaxisEndpoints(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_taxis_get(self):
        # Act
        response = self.client.get("/taxis/")

        # Assert
        self.assertEqual(response.status_code, 200)

    def test_create_and_retrieve_taxi(self):
        # Create a new taxi
        response = self.client.post("/taxis/", {"plate": "ABC123"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        taxi_id = response.data["id"]

        # Retrieve the created taxi
        response = self.client.get(reverse("taxi-detail", kwargs={"pk": taxi_id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["id"], taxi_id)
        self.assertEqual(response.data["plate"], "ABC123")

    def test_create_and_retrieve_trayectory(self):
        # Create a new taxi
        taxi_response = self.client.post("/taxis/", {"plate": "XYZ789"})
        taxi_id = taxi_response.data["id"]

        # Create a new trayectory for the created taxi
        response = self.client.post(
            "/trayectories/",
            {
                "date": "2024-03-09",
                "taxi_id": taxi_id,
                "latitude": 123.456,
                "longitude": 789.012,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Retrieve the created trayectory
        response = self.client.get(f"/trayectories/?taxi_id={taxi_id}&date=2024-03-09")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)
        self.assertNotEqual(len(response.data['results']), 0)
