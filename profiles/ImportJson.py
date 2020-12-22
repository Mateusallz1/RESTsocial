import json
from profiles.models import Profile, Post, Comment


def import_json(nome_arquivo='db.json'):
    save_users(nome_arquivo)
    save_posts(nome_arquivo)
    save_comments(nome_arquivo)


def save_users(nome_arquivo):   
    arquivo = open(nome_arquivo)
    data = json.load(arquivo)
    
    profile_list = []

    for i in data['users']:
        profile_list.append(
            Profile(
                id = i['id'],
                name = i['name'],
                email = i['email']
            )
        )
    Profile.objects.bulk_create(profile_list)
        

def save_posts(nome_arquivo):
    arquivo = open(nome_arquivo)
    data = json.load(arquivo)

    posts_list = []

    for i in data['posts']:
        posts_list.append(
            Post(id = i['id'], 
                title = i['title'], 
                body = i['body'],  
                userid = Profile.objects.get(id=i['userId']),   
            )
        )
    Post.objects.bulk_create(posts_list)

def save_comments(nome_arquivo):
    arquivo = open(nome_arquivo)
    data = json.load(arquivo)

    comments_list = []

    for i in data['comments']:
        comments_list.append(
            Comment(postid = Post.objects.get(id = i['postId']),
                    id = i['id'],
                    name = i['name'], 
                    email = i['email'], 
                    body = i['body'], 
            )
        )
    Comment.objects.bulk_create(comments_list)