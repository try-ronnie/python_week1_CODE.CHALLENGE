class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    # this is our blueprint for author
    #validation should occur where initialization occur
    # this is to ensure that a valid name is passed o initializes
    def __init__(self, name):
        if not isinstance(name , str) or len(name) == 0:
            raise AssertionError
        else:
            self._name = name
    @property
    def name(self):
        return self._name
# this means that name will only be read only and cannot be set

    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass