from django.db import models
PARTY_CHOICES = [("D","D"),("R","R"),("I","I")]
MAIL_IN_CHOICES = [("Yes","Yes"),("No","No"),("Yes, with exceptions","Yes, with exceptions")]
#Model to represent a state.
class State(models.Model):
    name = models.CharField(max_length=100)
    initials = models.CharField(max_length=2)
    important_chars = models.TextField(blank=True)
    capital = models.CharField(max_length=200,default="not specified")
    other_areas = models.TextField(default="not specified")
    cost_voting = models.CharField(max_length=20,default="not specified")

    congressional_makeup=models.TextField(blank=True) #Raw JSON

    important_congressional_elections = models.TextField(blank=True) #Raw JSON

    electoral_votes = models.IntegerField(default=-1)
    rv_dems = models.FloatField(default=-1)
    rv_reps = models.FloatField(default=-1)
    rv_other = models.FloatField(default=-1)

    senator_1 = models.CharField(max_length=100,default="not specified")
    senator_1_party = models.CharField(max_length=1,choices=PARTY_CHOICES,default="not specified")

    senator_2 = models.CharField(max_length=100,default="not specified")
    senator_2_party = models.CharField(max_length=1,choices=PARTY_CHOICES,default="not specified")

    mailin_reason = models.CharField(max_length=40,choices=MAIL_IN_CHOICES,default="not specified")
    mailin_notarization = models.CharField(max_length=40,choices=MAIL_IN_CHOICES,default="not specified")
    mainin_automated = models.BooleanField(default=False)
    mailin_id = models.BooleanField(default=False)
    person_id = models.BooleanField(default=False)

    mainin_deadline = models.DateTimeField(blank=True,null=True)
    must_be_recieved_by_above = models.BooleanField(default=False)

    turn_in_method = models.CharField(max_length=60,default="not specified")

    pres_election_history = models.TextField(blank=True) #Raw json.  Each year to have votes for each party

    description = models.TextField(default="not specified")

##class District(models.Model):
##    name = models.CharField(max_length=500)
##    
##    party = models.CharField(max_length=1,choices=PARTY_CHOICES)
##    number = models.IntegerField() #Can switch to AL for electoral_votes=3 states when rendering
##    state = models.ForeignKey(State)
##
##class PreviousSenateRace(models.Model):
##    state = models.ForeignKey(State)
##    year = models.IntegerField()
##
##    candidate_winner_name = models.CharField(max_length=100)
##    candidate_winner_party = models.CharField(max_length=1,choices=PARTY_CHOICES)
##    candidate_winner_votes = models.FloatField() #Percentage Please
##
##    candidate_loser_name = models.CharField(max_length=100)
##    candidate_loser_party = models.CharField(max_length=1,choices=PARTY_CHOICES)
##    candidate_loser_votes = models.FloatField() #Percentage Please
##
##
##class PreviousHouseRace(models.Model):
##    district = models.ForeignKey(District)
##    year = models.IntegerField()
##
##    candidate_winner_name = models.CharField(max_length=100)
##    candidate_winner_party = models.CharField(max_length=1,choices=PARTY_CHOICES)
##    candidate_winner_votes = models.FloatField() #Percentage Please
##
##    candidate_loser_name = models.CharField(max_length=100)
##    candidate_loser_party = models.CharField(max_length=1,choices=PARTY_CHOICES)
##    candidate_loser_votes = models.FloatField() #Percentage Please
##
##    


#Blogpost Tag (or for anything else)
class Tag(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State, null=True, on_delete=models.SET_NULL)
    #If an article is tagged with a state, it should be visible in that state's
    #States and their tags should be created in bulk
    
#Relatively simple if there are no authors
class Blogpost(models.Model):
    title = models.CharField(max_length=500)
    description = models.TextField() #When it appears on the homepage/state profile
    content = models.TextField() #Actual markdown content
    tags = models.ManyToManyField(Tag)
