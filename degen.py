'''
This is just a very rough draft for creating a character for 'Degenesis'.
 (Important note:  Character must choose between Primal and Focus)

1. Choose Culture, Concept and Cult
 # Test to check out git uploading
2. Spend Points: 
    -10 Attribute.  Attribute max is 3. 
    -28 skill points. Skill Max is 2.
    -Potential bonuses from CCC give +1 each to the max.

3.  Spend points on background. 6 backgrounds, no trait above 3.

4.  Determine Rank:
    - The character climbs his cult's rank hierarchy until he is unable
    to meet the requirements for the next rank.
    - Collected equipment and bonuses are noted on the character sheet.

5.  Choose Potential:
    -The character gets a cult-specific or common potential at level 1.

6.  Finishing Touches.
'''
'''
cultures = Borca, Franka, Pollen, Balkhan, Hyprispania, Purgare, Africa

concepts = Adventurer, Creator, Mentor, Martyr, Ruler, Seeker, Healer, Traditionalist, Mediator, Hermit, Heretic, Conqueror, Abomination, Destroyer, Chosen, Defiler, Protector, Visionary, Zealot, Disciple, Righteous, Traveler

cults = Spitalians, Chroniclers, Hellvetics, Judges, Clanners, Scrappers, Neoubyans, Scourgers, Anubians, Jehammedans, Apocalyptics, Anabaptists, Palers
'''
class Character(object):
    name = ''
    attributePoints = 10
    skillPoints = 28
    culture = ''
    concept = ''
    cult = ''
    body = 1
    agility = 1
    charisma = 1
    intelligence = 1
    psyche = 1
    instinct = 1
    attributes = ['name','culture', 'concept', 'cult', 'body', 'agility', 'charisma', 'intelligence', 'psyche', 'instinct', 'attributePoints', 'skillPoints']
    
    def __init__(self,name):
        assert self.valid_name(name)
        self.name = name
    def add_points(self):
        accepted = ['body', 'agility', 'char', 'intel', 'psyche', 'instinct']
        accepted_dict = dict(enumerate(accepted, start=1))
        prompt = "\nAvailable Attributes:\n\n\t" + "\n\t".join("%d. %s"%n for n in accepted_dict.items()) + "\n\n Make a selection: "
        attribute = False
        while attribute not in accepted:
            attribute = raw_input(prompt)
            try:
                attribute = accepted_dict[int(attribute)]
            except:
                print "Input was invalid.  Please enter either an attribute or its corresponding number "
        amount = None
        while type(amount) != int and self.attributePoints > 0:
            amount = int(raw_input("Raise to what number? "))
            self.attributePoints -= amount
        self.__setattr__(attribute, self.__getattribute__(attribute) + amount)

    def __str__(self):
        return "\n".join("%*s\t: %s"%(13,n, self.__getattribute__(n)) for n in self.attributes)
    @staticmethod
    def valid_name(name):
        if bool(name) and type(name) == str:
            return True
        else:
            return False

if __name__ == "__main__":
    running = True
    print "Create a character!  You have 10 points to assign to various attributes."
    name = ''
    while not Character.valid_name(name):
        name = raw_input("Please enter your character's name: ")
    CHAR = Character(name)
    OPTIONS_LIST = ["Set Stats", "See current attributes", "Exit"]
    OPTIONS_DICT = dict(enumerate(OPTIONS_LIST, start = 1))
    PROMPT = "\n".join("\t%d. %s"%n for n in OPTIONS_DICT.items())+"\n\nChoice: "
    while running:
        CHOICE = raw_input(PROMPT)
        try:
            CHOICE = int(CHOICE)
        except:
            pass
        if CHOICE in OPTIONS_DICT.keys():
            CHOICE = OPTIONS_DICT[CHOICE]
        if CHOICE == "Set Stats":
            CHAR.add_points()
        elif CHOICE == "See current attributes":
            print CHAR
        elif CHOICE == "Exit":
            running = False
