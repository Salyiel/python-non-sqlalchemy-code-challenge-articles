class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        author._articles.append(self)
        magazine._articles.append(self)

        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str) or not (5 <= len(value) <= 50):
            raise TypeError("Title must be a string between 5 and 50 characters")
        if hasattr(self, '_title'):
            raise AttributeError("Cannot modify title once set")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be an instance of the Author class")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class")
        self._magazine = value


class Author:
    all = []

    def __init__(self, name):
        self.name = name
        self._articles = []
        Author.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError('Name must be a non-empty string')
        if hasattr(self, '_name'):
            raise AttributeError('Cannot modify name once set')
        self._name = value

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set([article.magazine for article in self._articles]))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set([article.magazine.category for article in self._articles]))


class Magazine:
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []
        self._contributors = set()
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (2 <= len(value) <= 16):
            raise TypeError("Name must be a string between 2 and 16 characters")
        if hasattr(self, '_name'):
            raise AttributeError("Cannot modify name once set")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self, author):
        if not isinstance(author, Author):
            raise TypeError('Author must be an instance of the Author class')
        self._contributors.add(author)
        return list(self._contributors)

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        return [author for author in self._contributors if len([article for article in author.articles() if article.magazine == self]) > 2]
