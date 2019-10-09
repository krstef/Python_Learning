"""
    Demo example: News agency - Subscribers on news receives notification when news are published

    Pattern contains:
     Subject: Object which is changeable -> news publisher
     Observer: Interested in changes of the Subject -> subscriber to the news (mail, newspaper etc)

    Goal: Easy add new subscriber
    Note -
"""

import abc


class NewsPublisher:
    """ This class represents a Subject
        Provides attach() and detach() methods to enable Observer interface to register/deregister
        subscribers() method returns list of subscribers
        notify() sends notifications to all subscribers
        add_news() used for creating news
        get_news() used for getting latest news
    """

    def __init__(self):
        self._subscribers = []
        self.latest_news = None

    def attach(self, subscriber):
        self._subscribers.append(subscriber)

    def detach(self):
        return self._subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self._subscribers]

    def notify(self):
        for subscriber in self._subscribers:
            subscriber.update()

    def add_news(self, news):
        self.latest_news = news

    def get_news(self):
        return "Today news:", self.latest_news


class ObserverInterface(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def update(self):
        pass


class EmailObserver(ObserverInterface):

    def __init__(self, publisher):
        self.publisher = publisher
        # register itself for new updates
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__)
        print(self.publisher.get_news())


class SmsObserver(ObserverInterface):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__)
        print(self.publisher.get_news())


class AnyObserver(ObserverInterface):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__)
        print(self.publisher.get_news())


def main():
    news_publisher = NewsPublisher()
    for Subscribers in [SmsObserver, AnyObserver, EmailObserver]:
        Subscribers(news_publisher)
    # all subscribers subscribed to the news publisher
    print("\Subscribers:", news_publisher.subscribers)
    # add news and notify all subscribers
    news_publisher.add_news("Hello, this are my first news")
    news_publisher.notify()
    # detach last subscriber
    print("\nDetached:", type(news_publisher.detach()).__name__)

    # repeat story
    news_publisher.add_news("Hello, this are my SECOND news, but unfortunately, we don't "
                            "have email subscribers anymore")
    news_publisher.notify()

if __name__ == '__main__':
    main()
