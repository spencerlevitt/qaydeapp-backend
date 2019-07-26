"""Imports User class"""
from rest_framework import serializers
from api.models import User, UserProfile, UserStatistics, Friends, GameRequest, FinishedGame
from api.models import NBA19LifetimeCard, Madden19LifetimeCard, FIFA19LifetimeCard, NHL19LifetimeCard
from api.models import NBA19GameCard, Madden19GameCard, FIFA19GameCard, NHL19GameCard
from django.contrib.auth.validators import UnicodeUsernameValidator


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = (
            'balance',
            'dob',
            'address',
            'country',
            'city',
            'zip',
            'photo'
        )
        read_only_fields = ['balance']


class NBA19LifetimeCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NBA19LifetimeCard
        fields = (
            'net_gain',
            'avg_score',
            'avg_fieldgoalper',
            'avg_3pointper',
            'avg_fastbreakpoints',
            'avg_pointsinpaint',
            'avg_secondchance',
            'avg_benchpoints',
            'avg_assists',
            'avg_offensiveboards',
            'avg_defensiveboards',
            'avg_steals',
            'avg_blocks',
            'avg_turnovers',
            'avg_fouls',
            'avg_biggestlead',
            'avg_posession',
            'avg_timeoutsremain'
        )


class Madden19LifetimeCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Madden19LifetimeCard
        fields = (
            'net_gain',
            'avg_score',
            'avg_totaloffense',
            'avg_rushingyards',
            'avg_passingyards',
            'avg_firstdowns',
            'avg_pryards',
            'avg_kryards',
            'avg_totalyards',
            'avg_turnovers',
            'avg_3rdconversions',
            'avg_4thconversions'
        )


class FIFA19LifetimeCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FIFA19LifetimeCard
        fields = (
            'net_gain',
            'avg_score',
            'avg_shots',
            'avg_possession',
            'avg_tackles',
            'avg_fouls',
            'avg_corners',
            'avg_shotaccuracy',
            'avg_passaccuracy'
        )


class NHL19LifetimeCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NHL19LifetimeCard
        fields = (
            'net_gain',
            'avg_score',
            'avg_totalshots',
            'avg_hits',
            'avg_timeonattack',
            'avg_passing',
            'avg_faceoffswon',
            'avg_penaltyminute',
            'avg_powerplays',
            'avg_powerplayminutes',
            'avg_shorthandedgoals'
        )


class UserStatisticsSerializer(serializers.HyperlinkedModelSerializer):
    NBA_profile = NBA19LifetimeCardSerializer(required=True)
    Madden_profile = Madden19LifetimeCardSerializer(required=True)
    FIFA_profile = FIFA19LifetimeCardSerializer(required=True)
    NHL_profile = NHL19LifetimeCardSerializer(required=True)

    class Meta:
        model = UserStatistics
        fields = (
            'user',
            'net_gain',
            'NBA_profile',
            'Madden_profile',
            'FIFA_profile',
            'NHL_profile'
        )
        extra_kwargs = {
            'user': {
                'validators': [UnicodeUsernameValidator()],
            }
        }

    def update(self, instance, validated_data):
        NBA_data = validated_data.pop('NBA_profile')
        NBA_profile = instance.NBA_profile

        Madden_data = validated_data.pop('Madden_profile')
        Madden_profile = instance.Madden_profile

        FIFA_data = validated_data.pop('FIFA_profile')
        FIFA_profile = instance.FIFA_profile

        NHL_data = validated_data.pop('NHL_profile')
        NHL_profile = instance.NHL_profile

        NBA_profile.net_gain = NBA_data.get('net_gain', NBA_profile.net_gain)
        NBA_profile.avg_score = NBA_data.get(
            'avg_score', NBA_profile.avg_score)
        NBA_profile.avg_fieldgoalper = NBA_data.get(
            'avg_fieldgoalper', NBA_profile.avg_fieldgoalper)
        NBA_profile.avg_3pointper = NBA_data.get(
            'avg_3pointper', NBA_profile.avg_3pointper)
        NBA_profile.avg_fastbreakpoints = NBA_data.get(
            'avg_fastbreakpoints', NBA_profile.avg_fastbreakpoints)
        NBA_profile.avg_pointsinpaint = NBA_data.get(
            'avg_pointsinpaint', NBA_profile.avg_pointsinpaint)
        NBA_profile.avg_secondchance = NBA_data.get(
            'avg_secondchance', NBA_profile.avg_secondchance)
        NBA_profile.avg_benchpoints = NBA_data.get(
            'avg_benchpoints', NBA_profile.avg_benchpoints)
        NBA_profile.avg_assists = NBA_data.get(
            'avg_assists', NBA_profile.avg_assists)
        NBA_profile.avg_offensiveboards = NBA_data.get(
            'avg_offensiveboards', NBA_profile.avg_offensiveboards)
        NBA_profile.avg_defensiveboards = NBA_data.get(
            'avg_defensiveboards', NBA_profile.avg_defensiveboards)
        NBA_profile.avg_steals = NBA_data.get(
            'avg_steals', NBA_profile.avg_steals)
        NBA_profile.avg_blocks = NBA_data.get(
            'avg_blocks', NBA_profile.avg_blocks)
        NBA_profile.avg_turnovers = NBA_data.get(
            'avg_turnovers', NBA_profile.avg_turnovers)
        NBA_profile.avg_fouls = NBA_data.get(
            'avg_fouls', NBA_profile.avg_fouls)
        NBA_profile.avg_biggestlead = NBA_data.get(
            'avg_biggestlead', NBA_profile.avg_biggestlead)
        NBA_profile.avg_posession = NBA_data.get(
            'avg_posession', NBA_profile.avg_posession)
        NBA_profile.avg_timeoutsremain = NBA_data.get(
            'avg_timeoutsremain', NBA_profile.avg_timeoutsremain)
        NBA_profile.save()

        Madden_profile.net_gain = Madden_data.get(
            'net_gain', Madden_profile.net_gain)
        Madden_profile.avg_score = Madden_data.get(
            'avg_score', Madden_profile.avg_score)
        Madden_profile.avg_totaloffense = Madden_data.get(
            'avg_totaloffense', Madden_profile.avg_totaloffense)
        Madden_profile.avg_rushingyards = Madden_data.get(
            'avg_rushingyards', Madden_profile.avg_rushingyards)
        Madden_profile.avg_passingyards = Madden_data.get(
            'avg_passingyards', Madden_profile.avg_passingyards)
        Madden_profile.avg_firstdowns = Madden_data.get(
            'avg_firstdowns', Madden_profile.avg_firstdowns)
        Madden_profile.avg_pryards = Madden_data.get(
            'avg_pryards', Madden_profile.avg_pryards)
        Madden_profile.avg_kryards = Madden_data.get(
            'avg_kryards', Madden_profile.avg_kryards)
        Madden_profile.avg_totalyards = Madden_data.get(
            'avg_totalyards', Madden_profile.avg_totalyards)
        Madden_profile.avg_3rdconversions = Madden_data.get(
            'avg_3rdconversions', Madden_profile.avg_3rdconversions)
        Madden_profile.avg_4thconversions = Madden_data.get(
            'avg_4thconversions', Madden_profile.avg_4thconversions)
        Madden_profile.save()

        FIFA_profile.net_gain = FIFA_data.get(
            'net_gain', FIFA_profile.net_gain)
        FIFA_profile.avg_score = FIFA_data.get(
            'avg_score', FIFA_profile.avg_score)
        FIFA_profile.avg_shots = FIFA_data.get(
            'avg_shots', FIFA_profile.avg_shots)
        FIFA_profile.avg_possession = FIFA_data.get(
            'avg_possession', FIFA_profile.avg_possession)
        FIFA_profile.avg_tackles = FIFA_data.get(
            'avg_tackles', FIFA_profile.avg_tackles)
        FIFA_profile.avg_fouls = FIFA_data.get(
            'avg_fouls', FIFA_profile.avg_fouls)
        FIFA_profile.avg_corners = FIFA_data.get(
            'avg_corners', FIFA_profile.avg_corners)
        FIFA_profile.avg_shotaccuracy = FIFA_data.get(
            'avg_shotaccuracy', FIFA_profile.avg_shotaccuracy)
        FIFA_profile.avg_passaccuracy = FIFA_data.get(
            'avg_passaccuracy', FIFA_profile.avg_passaccuracy)
        FIFA_profile.save()

        NHL_profile.net_gain = NHL_data.get('net_gain', NHL_profile.net_gain)
        NHL_profile.avg_score = NHL_data.get(
            'avg_score', NHL_profile.avg_score)
        NHL_profile.avg_totalshots = NHL_data.get(
            'avg_totalshots', NHL_profile.avg_totalshots)
        NHL_profile.avg_hits = NHL_data.get('avg_hits', NHL_profile.avg_hits)
        NHL_profile.avg_timeonattack = NHL_data.get(
            'avg_timeonattack', NHL_profile.avg_timeonattack)
        NHL_profile.avg_passing = NHL_data.get(
            'avg_passing', NHL_profile.avg_passing)
        NHL_profile.avg_faceoffswon = NHL_data.get(
            'avg_faceoffswon', NHL_profile.avg_faceoffswon)
        NHL_profile.avg_penaltyminute = NHL_data.get(
            'avg_penaltyminute', NHL_profile.avg_penaltyminute)
        NHL_profile.avg_powerplays = NHL_data.get(
            'avg_powerplays', NHL_profile.avg_powerplays)
        NHL_profile.avg_powerplayminutes = NHL_data.get(
            'avg_powerplayminutes', NHL_profile.avg_powerplayminutes)
        NHL_profile.avg_shorthandedgoals = NHL_data.get(
            'avg_shorthandedgoals', NHL_profile.avg_shorthandedgoals)
        NHL_profile.save()

        return instance


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)
    # profile_stats = UserStatisticsSerializer(required=True)

    class Meta:
        model = User
        fields = (
            'url',
            'email',
            'first_name',
            'last_name',
            'password',
            'profile',
        )
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        statistics_data = validated_data.pop('profile_stats')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(
            user=user, **profile_data, **statistics_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.slug = profile_data.get('slug', profile.slug)
        profile.balance = profile_data.get('balance', profile.balance)
        profile.dob = profile_data.get('dob', profile.dob)
        profile.address = profile_data.get('address', profile.address)
        profile.country = profile_data.get('country', profile.country)
        profile.city = profile_data.get('city', profile.city)
        profile.zip = profile_data.get('zip', profile.zip)
        profile.photo = profile_data.get('photo', profile.photo)
        profile.save()

        return instance


class FriendsSerializer(serializers.HyperlinkedModelSerializer):
    friends = UserSerializer(many=True)
    requests = UserSerializer(many=True)

    class Meta:
        model = Friends
        fields = (
            'user',
            'friends',
            'requests'
        )
        extra_kwargs = {
            'user': {
                'validators': [UnicodeUsernameValidator()],
            }
        }


class GameRequestSerializer(serializers.ModelSerializer):
    to_user = UserSerializer()
    from_user = UserSerializer()

    class Meta:
        model = GameRequest
        fields = (
            'id',
            'to_user',
            'from_user',
            'game',
            'wager',
            'timestamp'
        )


class NBA19GameCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = NBA19GameCard
        fields = (
            'team1',
            'team1_score',
            'team1_fieldgoalper',
            'team1_3pointper',
            'team1_fastbreakpoints',
            'team1_pointsinpaint',
            'team1_secondchance',
            'team1_benchpoints',
            'team1_assists',
            'team1_offensiveboards',
            'team1_defensiveboards',
            'team1_steals',
            'team1_blocks',
            'team1_turnovers',
            'team1_fouls',
            'team1_biggestlead',
            'team1_posession',
            'team1_timeoutsremain',

            'team2',
            'team2_score',
            'team2_fieldgoalper',
            'team2_3pointper',
            'team2_fastbreakpoints',
            'team2_pointsinpaint',
            'team2_secondchance',
            'team2_benchpoints',
            'team2_assists',
            'team2_offensiveboards',
            'team2_defensiveboards',
            'team2_steals',
            'team2_blocks',
            'team2_turnovers',
            'team2_fouls',
            'team2_biggestlead',
            'team2_posession',
            'team2_timeoutsremain',

            'created_at',
            'updated_at'
        )


class Madden19GameCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Madden19GameCard
        fields = (
            'team1',
            'team1_score',
            'team1_totaloffense',
            'team1_rushingyards',
            'team1_passingyards',
            'team1_firstdowns',
            'team1_pryards',
            'team1_kryards',
            'team1_totalyards',
            'team1_turnovers',
            'team1_3rdconversions',
            'team1_4thconversions',

            'team2',
            'team2_score',
            'team2_totaloffense',
            'team2_rushingyards',
            'team2_passingyards',
            'team2_firstdowns',
            'team2_pryards',
            'team2_kryards',
            'team2_totalyards',
            'team2_3rdconversions',
            'team2_4thconversions',

            'created_at',
            'updated_at'
        )


class FIFA19GameCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = FIFA19GameCard
        fields = (
            'team1',
            'team1_score',
            'team1_penaltygoals',
            'team1_shots',
            'team1_possession',
            'team1_tackles',
            'team1_fouls',
            'team1_corners',
            'team1_shotaccuracy',
            'team1_passaccuracy',

            'team2',
            'team2_score',
            'team2_penaltygoals',
            'team2_shots',
            'team2_possession',
            'team2_tackles',
            'team2_fouls',
            'team2_corners',
            'team2_shotaccuracy',
            'team2_passaccuracy',

            'created_at',
            'updated_at'
        )


class NHL19GameCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = NHL19GameCard
        fields = (
            'team1',
            'team1_score',
            'team1_penaltygoals',
            'team1_totalshots',
            'team1_hits',
            'team1_timeonattack',
            'team1_passing',
            'team1_faceoffswon',
            'team1_penaltyminute',
            'team1_powerplays',
            'team1_powerplayminutes',
            'team1_shorthandedgoals',

            'team2',
            'team2_score',
            'team2_penaltygoals',
            'team2_totalshots',
            'team2_hits',
            'team2_timeonattack',
            'team2_passing',
            'team2_faceoffswon',
            'team2_penaltyminute',
            'team2_powerplays',
            'team2_powerplayminutes',
            'team2_shorthandedgoals',

            'created_at',
            'updated_at'
        )


class FinishedGameSerializer(serializers.ModelSerializer):
    winner = UserSerializer()
    loser = UserSerializer()
    NBA19MatchData = NBA19GameCardSerializer(required=True)
    Madden19MatchData = Madden19GameCardSerializer(required=True)
    NHL19MatchData = NHL19GameCardSerializer(required=True)
    FIFA19MatchData = FIFA19GameCardSerializer(required=True)

    class Meta:
        fields = (
            'id',
            'winner',
            'winning_team',
            'winning_score',
            'loser',
            'losing_team',
            'losing_score',

            'game_played',
            'NBA19MatchData',
            'Madden19MatchData',
            'NHL19MatchData',
            'FIFA19MatchData',

            'wager_amount',
            'created_at',
            'updated_at'
        )
        model = FinishedGame
