from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.test import TestCase, Client
from peteslist.forms import ForSaleForm
from peteslist.models import Post, Favorite, Location


class TestPost(TestCase):
    def setUp(self):
        joe = User.objects.create_user(username='joe', email='joe@joe.com',
                                 password='password')
        post = Post.objects.create(user=joe, title='Test title 1',
                                   description='The best description ever.')
        Favorite.objects.create(user=joe, post=post)
        self.assertEqual(post.favorite_count, 1)


class TestLocationList(TestCase):
    def setUp(self):
        self.client = Client()

    def test_session_redirect(self):
        session = self.client.session
        session['location'] = 'boston'
        session.save()
        response = self.client.get(reverse('list_locations'))
        self.assertEqual(response.status_code, 302)
        # self.assertRedirects(response, reverse('temp_only', kwargs={'city': 'boston'}))
        # self.assertEqual(response.status_code, 200)


class Testloc(TestCase):
    def setUp(self):
        self.client = Client()

    def test_bad_city(self):
        response = self.client.get(reverse('temp_only', kwargs={'city': 'neverneverland'}))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('locs_list'))

    def test_good_city(self):
        response = self.client.get(reverse('temp_only', kwargs={'city': 'boston'}))
        self.assertEqual(response.status_code, 302)

class TestForSalePost(TestCase):
    def setUp(self):
        self.joe = User.objects.create_user(username='joe', email='joe@joe.com',
                                 password='password')
        self.client = Client()

    def test_get(self):
        response = self.client.get(reverse('post'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/login/?next=/posts/create/')

    def test_get_login(self):
        self.client.post('/login/', {'username': 'joe', 'password': 'password'})
        response = self.client.get(reverse('post'))
        self.assertEqual(response.status_code, 200)

    def test_bad_form(self):
        self.client.post('/login/', {'username': 'joe', 'password': 'password'})
        response = self.client.post(reverse('post'), {'title':'Test title',
                                           'description': 'Test description'})
        self.assertEqual(response.status_code, 200)

# class ForSaleFormTest(TestCase):
#
#     def test_for_sale_form(self):
#         joe = User.objects.create_user(username='joe', email='joe@joe.com',
#                                  password='password')
#         location = Location.objects.create(city='boston', state='MA')
#         form_data = {'title': 'Test title', 'description': 'Test description',
#                      'by_phone': False, 'by_text': True, 'user': joe}
#         form = ForSaleForm(data=form_data)
#         self.assertTrue(form.is_valid())

class TestListPosts(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='joe', email='joe@joe.com',
                                 password='password')
        self.client = Client()

    # def test_list_posts(self):
    #     location = Location.objects.create(city='boston', state='MA')
    #     post = Post.objects.create(user=self.user, title='Test title 1',
    #                                description='The best description ever.',
    #                                location=location)
    #     response = self.client.get(reverse('list_posts'))
    #     self.assertEqual(response.status_code, 200)
    #     response_post = response.context_data['post_list'][0]
    #     self.assertEqual(response_post.id, post.id)
