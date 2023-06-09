import pytest

from news.models import Comment, News


@pytest.fixture
def author(django_user_model):
    return django_user_model.objects.create(username='Автор')


@pytest.fixture
def author_client(author, client):
    client.force_login(author)
    return client


@pytest.fixture
def news():
    news = News.objects.create(
        title='Заголовок',
        text='Текст',
    )
    return news


@pytest.fixture
def news_id(news):
    return news.id,


@pytest.fixture
def comment(author, news):
    comment = Comment.objects.create(
            news=news,
            author=author,
            text='Текст комментария'
    )
    return comment


@pytest.fixture
def comment_id(comment):
    return comment.id,


