"""Imports models"""
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Social


class User(AbstractUser):
    username = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    def __str__(self):
        return "{}".format(self.email)


@receiver(post_save, sender=User)
def create_neccessities(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        UserStatistics.objects.create(user=instance)
        Friends.objects.create(user=instance)


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, related_name='profile')
    slug = models.SlugField(null=True)
    balance = models.IntegerField(default=0)
    dob = models.DateField(null=True)
    address = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=50, null=True)
    city = models.CharField(max_length=50, null=True)
    zip = models.CharField(max_length=5, null=True)
    photo = models.ImageField(upload_to='uploads', blank=True)

    # def __str__(self):
    #    return str(self.user.)

    def get_absolute_url(self):
        return "/users/{}".format(self.slug)


class UserStatistics(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, related_name='profile_stats')

    net_gain = models.DecimalField(
        default=0, max_digits=20, decimal_places=2)


@receiver(post_save, sender=UserStatistics)
def create_lifetimecards(sender, instance, created, **kwargs):
    if created:
        NBA19LifetimeCard.objects.create(user_stats=instance)
        Madden19LifetimeCard.objects.create(user_stats=instance)
        FIFA19LifetimeCard.objects.create(user_stats=instance)
        NHL19LifetimeCard.objects.create(user_stats=instance)


class NBA19LifetimeCard(models.Model):
    user_stats = models.OneToOneField(UserStatistics,
                                      on_delete=models.CASCADE, related_name='NBA_profile')
    net_gain = models.IntegerField(default=0)

    avg_score = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    avg_fieldgoalper = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_3pointper = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_fastbreakpoints = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_pointsinpaint = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_secondchance = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_benchpoints = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_assists = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_offensiveboards = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_defensiveboards = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_steals = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    avg_blocks = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    avg_turnovers = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_fouls = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    avg_biggestlead = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_posession = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_timeoutsremain = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)


class Madden19LifetimeCard(models.Model):
    user_stats = models.OneToOneField(UserStatistics,
                                      on_delete=models.CASCADE, related_name='Madden_profile')
    net_gain = models.IntegerField(default=0)

    avg_score = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    avg_totaloffense = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_rushingyards = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_passingyards = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_firstdowns = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_pryards = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_kryards = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_totalyards = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_turnovers = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_3rdconversions = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_4thconversions = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)


class FIFA19LifetimeCard(models.Model):
    user_stats = models.OneToOneField(UserStatistics,
                                      on_delete=models.CASCADE, related_name='FIFA_profile')
    net_gain = models.IntegerField(default=0)

    avg_score = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    avg_shots = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    avg_possession = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_tackles = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_fouls = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    avg_corners = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_shotaccuracy = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_passaccuracy = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)


class NHL19LifetimeCard(models.Model):
    user_stats = models.OneToOneField(UserStatistics,
                                      on_delete=models.CASCADE, related_name='NHL_profile')
    net_gain = models.IntegerField(default=0)

    avg_score = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    avg_totalshots = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_hits = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    avg_timeonattack = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_passing = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_faceoffswon = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_penaltyminute = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_powerplays = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_powerplayminutes = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    avg_shorthandedgoals = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)


class Friends(models.Model):
    friends = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='Official_Friends')
    requests = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name='Friend_Requests')
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE, related_name='user_friends')

    @classmethod
    def make_friend(cls, user, new_friend):
        friend, created = cls.objects.get_or_create(
            user=user
        )
        friend.users.add(new_friend)

    @classmethod
    def remove_friend(cls, user, new_friend):
        friend, created = cls.objects.get_or_create(
            user=user
        )
        friend.users.remove(new_friend)

    def __str__(self):
        return str(self.user)

# Game Cards

# GameChallange


class GameRequest(models.Model):
    to_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='to_user_challenge')
    from_user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='from_user_challenge')
    game = models.CharField(max_length=250)
    wager = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    # Game Choices
    # STAT_TYPES = (
    #    ('MAT', 'Match Statistics'),
    #    ('AGG', 'Team Aggregate Statistics'),
    # )
    # HOME_OR_AWAY = (
    #    ('HOME', 'As Home Team'),
    #    ('AWAY', 'As Away Team')
    # )
    #match = models.ForeignKey(Match)
    #stat_type = models.CharField(max_length=3, choices=STAT_TYPES, db_index=True)
    #home_or_away = models.CharField(max_length=4, choices=HOME_OR_AWAY, null=True, db_index=True)
    # https://gist.github.com/iamwithnail/283d3d6f9464126a0abdd05d0d5309e2
    def __str__(self):
        return "From {}, to {}".format(self.from_user.name, self.to_user.name)


class NBA19GameCard(models.Model):
    team1 = models.CharField(max_length=255)
    team1_score = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_fieldgoalper = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_3pointper = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_fastbreakpoints = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_pointsinpaint = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_secondchance = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_benchpoints = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_assists = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_offensiveboards = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_defensiveboards = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_steals = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_blocks = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_turnovers = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_fouls = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_biggestlead = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_posession = models.DecimalField
    team1_timeoutsremain = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)

    team2 = models.CharField(max_length=255)
    team2_score = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_fieldgoalper = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_3pointper = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_fastbreakpoints = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_pointsinpaint = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_secondchance = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_benchpoints = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_assists = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_offensiveboards = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_defensiveboards = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_steals = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_blocks = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_turnovers = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_fouls = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_biggestlead = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_posession = models.DecimalField
    team2_timeoutsremain = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def winning_team(self):
        if self.team1_score > self.team2_score:
            return self.team1
        return "team1"


class Madden19GameCard(models.Model):
    team1 = models.CharField(max_length=255)
    team1_score = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_totaloffense = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_rushingyards = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_passingyards = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_firstdowns = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_pryards = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_kryards = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_totalyards = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_turnovers = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_3rdconversions = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_4thconversions = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)

    team2 = models.CharField(max_length=255)
    team2_score = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_totaloffense = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_rushingyards = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_passingyards = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_firstdowns = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_pryards = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_kryards = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_totalyards = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_turnovers = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_3rdconversions = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_4thconversions = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def winning_team(self):
        if self.team1_score > self.team2_score:
            return self.team1
        return "team1"


class FIFA19GameCard(models.Model):
    team1 = models.CharField(max_length=255)
    team1_score = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_penaltygoals = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_shots = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_possession = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_tackles = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_fouls = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_corners = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_shotaccuracy = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_passaccuracy = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)

    team2 = models.CharField(max_length=255)
    team2_score = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_penaltygoals = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_shots = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_possession = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_tackles = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_fouls = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_corners = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_shotaccuracy = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_passaccuracy = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def winning_team(self):
        if self.team1_score > self.team2_score:
            return self.team1
        return "team1"


class NHL19GameCard(models.Model):
    team1 = models.CharField(max_length=255)
    team1_score = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_penaltygoals = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_totalshots = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_hits = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    team1_timeonattack = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_passing = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_faceoffswon = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_penaltyminute = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_powerplays = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_powerplayminutes = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team1_shorthandedgoals = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)

    team2 = models.CharField(max_length=255)
    team2_score = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_penaltygoals = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_totalshots = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_hits = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    team2_timeonattack = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_passing = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_faceoffswon = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_penaltyminute = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_powerplays = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_powerplayminutes = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)
    team2_shorthandedgoals = models.DecimalField(
        max_digits=5, decimal_places=2, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def winning_team(self):
        if self.team1_score > self.team2_score:
            return self.team1
        return "team1"


# FinishedGames

class FinishedGame(models.Model):
    winner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='winner')
    winning_team = models.CharField(max_length=255)
    winning_score = models.IntegerField(default=0)

    loser = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='loser')
    losing_team = models.CharField(max_length=255)
    losing_score = models.IntegerField(default=0)

    game_played = models.CharField(max_length=255, default='EMPTY')
    NBA19MatchData = models.ForeignKey(
        NBA19GameCard, on_delete=models.PROTECT, related_name='nba_match_data', null=True)
    Madden19MatchData = models.ForeignKey(
        Madden19GameCard, on_delete=models.PROTECT, related_name='madden_match_data', null=True)
    NHL19MatchData = models.ForeignKey(
        NHL19GameCard, on_delete=models.PROTECT, related_name='nhl_match_data', null=True)
    FIFA19MatchData = models.ForeignKey(
        FIFA19GameCard, on_delete=models.PROTECT, related_name='fifa_match_data', null=True)

    wager_amount = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Gamecard = models.ForeignKey(whatever game)

    # Property allows you to talk to it as a regular property

    def winning_user(self):
        return self.winner

    def losing_user(self):
        return self.loser

    @property
    def wagered_total(self):
        return self.wager_amount
