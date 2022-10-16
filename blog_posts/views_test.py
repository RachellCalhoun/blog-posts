from django.contrib.auth.models import User
from .models import BlogPost
import os
os.environ.setdefault("DJANGO_ALLOW_ASYNC_UNSAFE", "true")


def test_list(live_server, browser):
    page = browser.new_page(base_url=str(live_server))
    user = User.objects.create_user(username="demo")
    post1 = BlogPost.objects.create(author=user, name="Post 1", text="blahh1")
    post2 = BlogPost.objects.create(author=user, name="Post 2", text="blahh2")
    post3 = BlogPost.objects.create(author=user, name="Post 3", text="blahh3")

    page.goto("/")

    assert page.locator("h2").all_inner_texts() == [post3.name, post2.name, post1.name]