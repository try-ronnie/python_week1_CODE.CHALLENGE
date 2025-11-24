class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        if isinstance(title , str) and 5< len(title) < 50:
            self._title = title
        else:
            raise ValueError('the title has to be a string that contains a minimum of 5 characrers and a maximum of 50')

    @property
    def title (self):
        return self._title
    
        
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
        self._name = name
        self._category = category
# we use isinstance over type since it allows us to identify if the value given is a string and instance of the given category
#note that when we use user.name = "kamau" we are modifying the attribute on thtat instance not on the class  ......... hence it is automatically an instance .... 
#type wouldnt allow us to check the child of a given parent... in this sense ..... it only matches  if the object is that exact type .... 

    @property
    def name (self):
        return self._name
    @property
    def category (self):
        return self._category 
    @name.setter
    def name (self, value):
        if isinstance(value , str) and 2 < len(value) < 16:
            self._name = value
        else:
            raise AssertionError('name must be a string between 3 and 15 characters')
    @category.setter
    def category (self , value):
            if isinstance(value , str) and len(value) > 0:
                self._category = value
            else:
                raise AssertionError("category must be have a number of characters above zero")
    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass

mag = Magazine('Techtimes ' , 'tecknolojia')
print(mag.name)