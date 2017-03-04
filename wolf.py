"""Some nice classes about wolves."""

class AbstractAnimal(object):
    """An AbstractAnimal class for living mammals that are cute."""

    def __init__(self, name):
        self.name = name

    def speak(self):
        print "%s, I'm %s the %s" % (
            self.greet, self.name, self.species)

class Wolf(AbstractAnimal):
    """A furry dog-like wild animal."""
    species = "wolf"
    greet = "Howwwwwwwl"
    is_pup = True

    def __init__(self, name, furr_pattern, howl_volume, habitat):
        super(Wolf, self).__init__(name)

        self.furr_pattern = furr_pattern
        self.howl_volume = howl_volume
        self.habitat = habitat

    def adapt(self):
        print "adapting to %s" % self.habitat  
        self.speak()

    def adopt(self, new_home):
        """Wolf gets adopted by a loving family."""

        self.habitat = new_home
        self.adapt()

    def __repr__(self):
        return "<Wolf %s>" % self.name 

class WolfPack(object):
    """A pack of wolf objects."""

    def __init__(self, name):
        self.members = []
        self.name = name

    def set_motto(self, motto):
        self.motto = motto

    def add(self, new_member):
        """Add a wolf to the wolf pack."""

        self.members.append(new_member)

    def cheer(self):
        try:
            a = self.motto
        except AttributeError:
            raise AttributeError("Yo, what's the motto with you????")

        cheer = ""
        for wolf in self.members:
            cheer = cheer + ("Gooooooo %s \n" % wolf.name)
        cheer = cheer + self.motto + "\n"
        print "**** **** ****"
        print cheer
        print "**** **** ****"

    def adapt_all_members(self):
        for wolf in self.members:
            wolf.adapt()

    def __repr__(self):
        return str(self.members)




larry = Wolf("Larry", "spotted", 60, "the woods")

pink_ladies = WolfPack('Pink Ladies')

susan = Wolf("Susan", "white", 75, "the woods")
tracy = Wolf("Tracy", "white", 73, "the woods")
sharon = Wolf("Sharon", "black", 60, "the woods")
pink_ladies.add(tracy)
pink_ladies.add(susan)
pink_ladies.add(sharon)
pink_ladies.set_motto("Change the Ratio")
pink_ladies.add(Wolf("Judy", "pink", 20, "the woods"))
