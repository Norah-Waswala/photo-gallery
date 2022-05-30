from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Image,Location,Category
import datetime as dt
# Create your tests here.

class LocationTestClass(TestCase):
    # Set up method
    def setUp(self):
        self.school=Location('school')

    # Testing  instance
    def test_instance(self):
#         self.assertTrue(isinstance(self.school,Location)) 

#     # Testing Save Method
#     def test_save_method(self):
#         self.school.save_editor()
#         location =Location.objects.all()
#         self.assertTrue(len(location) > 0) 

# class CategoryTestClass(TestCase):
#     # Set up method
#     def setUp(self):
#         self.leisure=Category(name='leisure')

#     # Testing  instance
#     def test_instance(self):
#         self.assertTrue(isinstance(self.leisure,Category)) 

#     def test_save_method(self):
#         '''
#          test_save_category to test if we can add a category from our category list
#         '''
#         self.leisure.save_category()
#         category = Category.objects.all()
#         self.assertTrue(len(category) > 0) 

#     # def test_delete_credentials(self):
#     #     '''
#     #      test_delete_category to test if we can remove a category from our category list
#     #     '''
#     #     self.new_credentials.save_credentials()
#     #     test_credentials =credentials("instagram","insta-norah","$!dg68r6hd") # new credentials object
#     #     self.new_credentials.delete_credentials()# Deleting a credentials object
#     #     self.assertEqual(len(credentials.credentials_list),0)


# class ArticleTestClass(TestCase):

#     def setUp(self):
#         # Creating a new editor and saving it
#         self.james= Location(first_name = 'James', last_name ='Muriuki', email ='james@moringaschool.com')
#         self.james.save_editor()

#         # Creating a new tag and saving it
#         self.new_tag = Tags(name = 'student')
#         self.new_tag.save()

#         self.new_article= Article(title = 'Test Article',post = 'This is a random test Post',editor = self.james)
#         self.new_article.save()

#         self.new_article.tags.add(self.new_tag)

#     def tearDown(self):
#         Editor.objects.all().delete()
#         Tags.objects.all().delete()
#         Article.objects.all().delete()

# def test_get_news_today(self):
#         today_news = Article.todays_news()
#         self.assertTrue(len(today_news)>0)

# def test_get_news_by_date(self):
#         test_date = '2017-03-17'
#         date = dt.datetime.strptime(test_date, '%Y-%m-%d').date()
#         news_by_date = Article.days_news(date)
#         self.assertTrue(len(news_by_date) == 0)