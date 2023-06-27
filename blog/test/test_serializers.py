from django.test import TestCase
from django.contrib.auth.models import User

from ..models import Post, Reaction
from ..serializers import PostSerializer, ReactionSerializer


class PostSerializerTestCase(TestCase):
    def setUp(self):
        self.user1 = User.objects.create(username='Doniyor', password='123')
        self.user2 = User.objects.create(username='Jaloliddin', password='123')
        self.post1 = Post.objects.create(
            title = 'nimadir 1',
            content = 'abs 1',
            author = self.user1
        )
        self.post2 = Post.objects.create(
            title = 'nimadir 2',
            content = 'abs 2',
            author = self.user2
        )

    def test_to_get_a_post(self):
        serializer = PostSerializer(instance=self.post2)

        self.assertEqual(serializer.data['title'], 'nimadir 2')
        self.assertEqual(serializer.data['content'], 'abs 2')
        self.assertEqual(serializer.data['author'], 2)
    
    def test_to_get_all_posts(self):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)

        self.assertEqual(len(serializer.data), 2)
        self.assertEqual(serializer.data[0]['title'], 'nimadir 1')
        self.assertEqual(serializer.data[0]['content'], 'abs 1')
        self.assertEqual(serializer.data[0]['author'], 1)
        self.assertEqual(serializer.data[1]['title'], 'nimadir 2')
        self.assertEqual(serializer.data[1]['content'], 'abs 2')
        self.assertEqual(serializer.data[1]['author'], 2)

    def test_to_create_a_post(self):
        serializer = PostSerializer(
            data = {
                'title': 'nimadir 3',
                'content': 'abs 3', 
                'author': self.user1.pk
            }
        )
        if serializer.is_valid():
            post = serializer.save()
        self.assertEqual(serializer.is_valid(), True, 'Serialzier is not valid')
        self.assertEqual(post.title, 'nimadir 3')
        self.assertEqual(post.content, 'abs 3')
        self.assertEqual(post.author.pk, 1)
        

    def test_to_update_a_post(self):
        serializer = PostSerializer(
            instance = self.post1,
            data = {
                'title': 'new title 1',
                'content': 'new content 1', 
                'author': self.user1.pk
            },
            partial = True
        )
        if serializer.is_valid():
            serializer.save()
        self.assertEqual(serializer.is_valid(), True, 'Serialzier is not valid')
        self.assertEqual(self.post1.id, 1)
        self.assertEqual(self.post1.title, 'new title 1')
        self.assertEqual(self.post1.content, 'new content 1')
        self.assertEqual(self.post1.author.pk, 1)