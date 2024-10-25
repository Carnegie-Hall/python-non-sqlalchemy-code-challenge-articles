import ipdb

class Article:

    all = ([])

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        # ipdb.set_trace()

    def get_title(self):
    
        return self._title
    
    def set_title(self, title):
        if type(title) != str or hasattr(self, "title"):
            return 
        elif len(title) < 5 and len(title) > 50:
            return 
        
        self._title = title

    title = property(get_title, set_title)
        
class Author:

    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) != str or hasattr(self, "name"):
            return 
        elif len(name) <= 0: 
            return 

        self._name = new_name

    def articles(self):
        return [article for article in Article.all if self == article.author]


    def add_article(self, magazine, title):
        return Article(self, magazine, title)
        # return Article.new_article

    def magazines(self):
        return list(set(article.magazine for article in Article.all if self == article.author))
    
    def topic_areas(self):
        if len(self.articles()) == 0:
            return None
        return list(set([magazine.category for magazine in self.magazines()]))

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        return [article for article in Article.all if self == article.magazine]

    def get_name(self):
    
        return self._name

    def set_name(self, name):
        if type(name) != str:
            return 
        elif len(name) < 2 or len(name) > 16:
            return 
        
        self._name = name

    name = property(get_name, set_name)

    def get_category(self):
    
        return self._category

    def set_category(self, category):
        if type(category) != str:
            return 
        elif len(category) <= 0: 
            return 
        
        self._category = category
    
    category = property(get_category, set_category)

    def contributors(self):
        # if len(self.articles()) == 0:
        authors = list(set([article.author for article in Article.all if self == article.magazine]))
        return authors

    def article_titles(self):
        titles = [article.title for article in Article.all if self == article.magazine]
        if len(titles) == 0:
            return None
        return titles

    def contributing_authors(self):
        auth = []
        non_uq_contr = [article.author for article in Article.all if self == article.magazine]
        for author in self.contributors(): 
            if non_uq_contr.count(author) >= 2: 
                auth.append(author)
        if len(auth) == 0:
            return None
        return auth