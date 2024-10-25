# class Author:
    
#     def __init__(self, name):
#         self.name
#         pass

#     def get_name(self):
#         if len(self.name) < 1:
#             raise Exception("Name must be > 1 character")
#         return self._name

#     def set_name(self, name):
#         if len(name) < 1:
#             raise Exception("Name must be > 1 character")
#         self._name = name 

#     name = property(get_name, set_name)





# def articles(self):
#         return self._articles 

#     def magazines(self):
#         unique_magazines = set(article.magazine for article in self.articles())
#         return list(unique_magazines)

#     def add_article(self, magazine, title):
#         article = Article(self, magazine, title)
#         self._articles.append(article)
#         return article

#     def topic_areas(self):
#         unique_topics = set(article.magazine.category for article in self.articles())
#         return list(unique_topics)

