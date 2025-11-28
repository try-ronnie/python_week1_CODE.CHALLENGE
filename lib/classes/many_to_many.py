
class Article:
    all = []
    #first we need to define a class level list 
    def __init__(self, author, magazine, title):
        #this relies on the objects of the magazine and author
        #inorder to get the authors articles we need a list of all the articles written


        if isinstance(author , Author):
            self._author = author
        else:
            raise ValueError('needs to be an instance of Author to pass')
        
        if isinstance(magazine , Magazine):
            self._magazine = magazine
        else:
            raise ValueError('needs tp be an instance of magazine to pass ')
        if isinstance(title , str) and 5<= len(title) <= 50:
            self._title = title
        else:
            raise ValueError('this is either not a string or does not meet the requirementof the character legth')
        Article.all.append(self)

        #in article.all(the list we created)note that this is at instance level ... so we choose the

#then since article property title is not allowed to change we write a setter
#property title is not allowed to change hence requires only a getter
    
    @property
    def title (self):
        return self._title
#author property is required to change after initialization
    @property
    def author (self):
        return self._author

    @author.setter
    def author (self , value):
        self._author = value


#magazine property is required to change after setter
    @property
    def magazine(self):
        return self._magazine
    @magazine.setter
    def magazine (self , value):
        self._magazine = value


class Author:
    # this is our blueprint for author
    #validation should occur where initialization occur
    # this is to ensure that a valid name is passed initializes
    # but then i realised that hasattr is practicaly useless since we wount reinitialize the object
    def __init__(self, name):
            if not isinstance(name , str) or len(name) == 0:
                raise ValueError
            else:
                self._name = name
            
    @property
    def name(self):
        return self._name
# this means that name will only be read only and cannot be set

    def articles(self):
        return [article for article in Article.all if article.author == self]
    # since we are in the author cass ... running this will open the list of articles .... and access the values of author(author.)
    #since we are calling it upon a saved instance of Author 
    #we it then checks the list of articles as it checks whether the article is from the instance of our author 

    
            

    def magazines(self):
        return list({article.magazine  for article in self.articles()})
        #since there is no list of the magazines created we access the value of article.magazine that returns all the magazine for that specific article
        #we put this logic in a set to remove duplicates
        #then we convert it to a list since we need to return a list of magazines
        # the article.magazine means the magazine for thi instance?>>>

    def topic_areas(self):
        return list({mag.category for mag in self.magazines()})
    def add_article(self, magazine, title):
        Article(self ,magazine , title)
        # this is just a method that helps us come up with an article instance


class Magazine:
    all = []
    def __init__(self, name, category):
        if not isinstance(name, str) or 2 <= len(name) <= 16:
            raise ValueError('name ,ust be a string of 2-16 characters')
        self._name = name
        if not isinstance(category , str) or len(category) > 0: 
            raise ValueError('category has to be a str and of atleast 0 + characters')
        self._category = category 
# we use isinstance over type since it allows us to identify if the value given is a string and instance of the given category
#note that when we use user.name = "kamau" we are modifying the attribute on that instance not on the class  ......... hence it is automatically an instance .... 
#type wouldnt allow us to check the child of a given parent... in this sense ..... it only matches  if the object is that exact type .... 

    @property
    def name (self):
        return self._name
    @property
    def category (self):
        return self._category 
    @name.setter
    def name (self, value):
        if isinstance(value , str) or 2 <= len(value) <= 16:
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
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list({article.author for article in self.articles()})

    def article_titles(self):
        return [article.title for article in self.articles()]

    def contributing_authors(self):
        authors_count = {}
        for article in self.articles():
            authors_count[article.author] = authors_count.get(article.author, 0) + 1
        return [author for author, count in authors_count.items() if count > 2]
        



# (line 26) the setter btw allows for us to change the value of the author attribute being passed when the property is run ..... article1.author (this runs the property that returns the value of the author given at initialization ) 
#so when you do article1.author = "" we run the setter function istead of the getter since we pass in a value so the setter is the one that expects a passed value for it to run 
#one thing to note is that in this progra, ..... article need the instances of author magazine to work .... meaning that 
#article() expects the instance object from author and maagazine in is initialization according to how the code is written