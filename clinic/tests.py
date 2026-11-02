from rest_framework.test import APITestCase


class DoctorListCreateViewTests(APITestCase):
    def test_post_creates_doctor(self):
        response = self.client.post(
            "/api/doctors/",
            {
                "doctor_name": "Gokul",
                "specialization": "cardiology",
                "experience": 5,
                "hospital": "Lakeshore",
                "consultation_fee": 500,
            },
            format="json",
        )

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["doctor_name"], "Gokul")
        self.assertEqual(response.data["available"], True)
