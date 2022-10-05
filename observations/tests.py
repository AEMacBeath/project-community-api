from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Observation


class ObservationListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='alice', password='pass')

    def test_can_list_observations(self):
        alice = User.objects.get(username='alice')
        Observation.objects.create(owner=alice, title='a title')
        response = self.client.get('/observations/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data, len(response.data))

    def test_logged_in_user_can_create_observation(self):
        self.client.login(username='alice', password='pass')
        response = self.client.post('/observations/', {'title': 'a title'})
        count = Observation.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_user_not_logged_in_cant_create_observation(self):
        response = self.client.post('/observations/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class ObservationDetailViewTests(APITestCase):
    def setUp(self):
        alice = User.objects.create_user(username='alice', password='pass')
        zoe = User.objects.create_user(username='zoe', password='pass')
        Observation.objects.create(
            owner=alice, title='a title', content='alices content'
        )
        Observation.objects.create(
            owner=zoe, title='another title', content='zoes content'
        )

    def test_can_retrieve_observation_using_valid_id(self):
        response = self.client.get('/observations/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_observation_using_invalid_id(self):
        response = self.client.get('/observations/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_observation(self):
        self.client.login(username='alice', password='pass')
        response = self.client.put('/observations/1/', {'title': 'a new title'})
        observation = Observation.objects.filter(pk=1).first()
        self.assertEqual(observation.title, 'a new title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_observation(self):
        self.client.login(username='alice', password='pass')
        response = self.client.put('/observations/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
