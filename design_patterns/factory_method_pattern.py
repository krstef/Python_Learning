"""
    Creating profiles of different type on social networks - Facebook, LinkedIn..
    And add right sections to the profiles - photos for Facebook, Publications for LinkedIn
"""

import abc


class Section(metaclass=abc.ABCMeta):
    """
        This class acts as Product interface
        Specify methods that all concrete products must implement
    """
    @abc.abstractmethod
    def describe(self):
        """
        Describe should describe each section of the social network
        :return:
        """
        pass


class PersonalSection(Section):
    """
        Common for all social networks
    """
    def describe(self):
        return "Presonal section"


class PhotoSection(Section):
    """
        Photo section of social network
    """
    def describe(self):
        return "Photo section"


class PublicationSection(Section):
    """
        Publication section of social network
    """
    def describe(self):
        return "Publication section"


class Profile(metaclass=abc.ABCMeta):
    """
        This class acts as Creator interface
        Provide factory method for creating profiles
        It should be implemented by concrete profile to actually create profiles with appropriate sections

        It should not know anything about sections that profile has, it should let subclass to decide this
    """
    def __init__(self):
        self.sections = []
        self.create_profile()

    @abc.abstractmethod
    def create_profile(self):
        pass

    def get_sections(self):
        return self.sections

    def add_sections(self, section):
        self.sections.append(section)


class LinkedIn(Profile):

    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(PublicationSection())


class Facebook(Profile):
    def create_profile(self):
        self.add_sections(PersonalSection())
        self.add_sections(PhotoSection())


# Client APP
profile_type = "Linke"
profile = eval(profile_type)()

print(type(profile).__name__)

for a in profile.get_sections():
    print(a.describe())
