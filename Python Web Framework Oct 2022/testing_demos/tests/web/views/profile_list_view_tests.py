from django.urls import reverse

from testing_demos.web.models import Profile
from tests.common.base_test_case import BaseTestCase


class ProfileListViewTests(BaseTestCase):
    def test_profiles_list_view__when_no_profiles__expect_empty_list_and_count_in_context(self):
        # Act
        # self.client.get() makes HTTP GET request
        response = self.client.get(reverse('list profiles'))

        # print(response)
        # print(response.context)
        # print(response.template_name)

        # Assert
        self.assertCollectionEmpty(response.context['profile_list'])
        self.assertEqual(0, response.context['profiles_count'])

    def test_profiles_list_view__when_profiles__expect_list_of_profiles_and_header_count(self):
        # Arrange
        # The below way of creating profiles doesn't call 'full_clean()' so the validators are skipped
        profiles_count = 10
        profiles = [
            Profile(
                name=f'Test user {i}',
                age=20 + i,
                egn=f'123456789{i}',
            )
            for i in range(1, profiles_count + 1)
        ]

        print([p.egn for p in profiles])

        Profile.objects.bulk_create(profiles)

        # Act
        response = self.client.get(reverse('list profiles'))

        # Assert
        self.assertListEqual(profiles, list(response.context['profile_list']))
        self.assertEqual(profiles_count, response.context['profiles_count'])

    def test_profiles_list_view__when_anonymous_user__expect_username_to_be_anonymous(self):
        # Act
        response = self.client.get(reverse('list profiles'))

        # Assert
        self.assertEqual('Anonymous', response.context['username'])

    def test_profiles_list_view__when_logged_in_user__expect_username_to_be_correct(self):
        # Arrange
        username = 'doncho'
        # User creation can be moved to an 'utils' module
        credentials = {
            'username': username,
            'password': username,
        }

        self.create_and_login_user(**credentials)

        # print(user.pk)

        # Act
        response = self.client.get(reverse('list profiles'))
        print(response.context['user'])

        # Assert
        self.assertEqual(username, response.context['username'])

    def test_profiles_list_view__when_query_is_provided__expect_query_to_be_in_context(self):
        # Act
        response = self.client.get(
            reverse('list profiles'),
            # query params are given with '?' in the url path
            data={
                'query': 'the-query',
            })

        # Assert
        self.assertEqual('the-query', response.context['query'])
