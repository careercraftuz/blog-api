from django.test import TestCase
from django.contrib.auth.models import User
from ..models import Post, Reaction


# Create your tests here.
class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(username='Doniyor', password='123')
        User.objects.create(username='Jaloliddin', password='123')
    
    def test_users(self):
        users = User.objects.all()
        self.assertEqual(len(users), 2)
        self.assertEqual(users[0].username, 'Doniyor')
        self.assertEqual(users[1].username, 'Jaloliddin')

    def test_user1(self):
        user = User.objects.get(id=1)

        self.assertEqual('Doniyor', user.username)
        self.assertEqual('123', user.password)

    def test_user2(self):
        user = User.objects.get(id=2)

        self.assertEqual('Jaloliddin', user.username)
        self.assertEqual('123', user.password)


class PostModelTestCase(TestCase):
    def setUp(self):
        user1 = User.objects.create(username='Doniyor', password='123')
        user2 = User.objects.create(username='Jaloliddin', password='123')
        Post.objects.create(
            title = 'nimadir 1',
            content = 'abs 1',
            author = user1
        )
        Post.objects.create(
            title = 'nimadir 2',
            content = 'abs 2',
            author = user2
        )

    def test_posts(self):
        posts = Post.objects.all()

        self.assertEqual(len(posts), 2)
        self.assertEqual(posts[0].title, 'nimadir 1')
        self.assertEqual(posts[1].title, 'nimadir 2')

    def test_post1(self):
        post = Post.objects.get(id=1)
        
        self.assertEqual('nimadir 1', post.title)
        self.assertEqual('abs 1', post.content)
        self.assertEqual(1, post.author.id)
    
    def test_post2(self):
        post = Post.objects.get(id=2)
        
        self.assertEqual('nimadir 2', post.title)
        self.assertEqual('abs 2', post.content)
        self.assertEqual(2, post.author.id)


class ReactionTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(username="Jaloliddin", password='123')
        self.post1 = Post.objects.create(title='title', content='content', author=self.user)
        self.post2 = Post.objects.create(title='title 2', content='content 2', author=self.user)
        Reaction.objects.create(like=True, user=self.user, post=self.post1)
        Reaction.objects.create(like=False, user=self.user, post=self.post2)

    def test_reactions(self):
        reactions = Reaction.objects.all()

        self.assertEqual(len(reactions), 2)
        self.assertEqual(reactions[0].like, True)
        self.assertEqual(reactions[1].like, False)

    def test_reaction1(self):
        reaction = Reaction.objects.get(id=1)

        self.assertEqual(reaction.like, True)
        
        self.assertEqual(reaction.user, self.user)
        self.assertEqual(reaction.user.username, 'Jaloliddin')
        
        self.assertEqual(reaction.post, self.post1)
        self.assertEqual(reaction.post.title, 'title')

    def test_reaction2(self):
        reaction = Reaction.objects.get(id=2)

        self.assertEqual(reaction.like, False)
        
        self.assertEqual(reaction.user, self.user)
        self.assertEqual(reaction.user.username, 'Jaloliddin')
        
        self.assertEqual(reaction.post, self.post2)
        self.assertEqual(reaction.post.title, 'title 2')