from app import api, db
from models import Post, MenuItem, User
from flask import request, Response
from flask_restful import Resource



class UserResource(Resource):
    def get(self, user_id):
        user =  User.query.filter(User.id == user_id).first()
        return user.serialize
    


class ArticleResource(Resource):
    def get(self):
        articles = Post.query.all()
        articles_list = []
        for article in articles:
            articles_list.append(article.serialize)
        return articles_list

    def post(self):
        data = request.json
        article = Post(title=data.get("post_header"), body=data.get("post_text"))
        db.session.add(article)
        db.session.commit()
        return article.serialize


class ArticleSingleResource(Resource):
    def get(self, post_id):
        article = Post.query.get(post_id)
        return article.serialize

    def put(self, post_id):
        data = request.json
        article = Post.query.get(post_id)
        article.title = data.get("post_header")
        article.body = data.get("post_text")
        db.session.add(article)
        db.session.commit()
        return article.serialize

    def delete(self, post_id):
        article = Post.query.get(post_id)
        db.session.delete(article)
        db.session.commit()
        return Response("", status=204)


class MenuItemResource(Resource):
    def get(self):
        menu_items = MenuItem.query.all()
        menu_items_list = []
        for menu_item in menu_items:
            menu_items_list.append(menu_item.serialize)
        return menu_items_list

    def post(self):
        data = request.json
        menu_item = MenuItem(name=data.get("name"), link=data.get("link"))
        db.session.add(menu_item)
        db.session.commit()
        return menu_item.serialize


api.add_resource(ArticleResource, "/api/articles")
api.add_resource(ArticleSingleResource, "/api/articles/<int:post_id>")
api.add_resource(MenuItemResource, "/api/menu-items")
api.add_resource(UserResource, "/api/post-author/<int:user_id>")