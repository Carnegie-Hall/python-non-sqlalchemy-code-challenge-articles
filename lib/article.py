# import ipdb

# class Article:

#     all = []
    
#     def __init__(self, author, magazine, title):
#         self.author = author
#         self.magazine = magazine
#         self.title = title 
#         # ipdb.set_trace()
#         print("Hello")

#     def get_title(self):
    
#         return self._title
    
#     def set_title(self, title):
#         if type(title) != str or hasattr(self, "title"):
#             return 
#         elif len(title) < 5 and len(title) > 50:
#             return 
        
#         self._title = title

# title = property(get_title, set_title)