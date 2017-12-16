from flask_restplus import Namespace, Resource, fields
# from ..core import run_spiders
from json import dumps
from flask import jsonify
import json
from ..models import Team,Match,League,Country
from .. import db


api = Namespace('sports', description='team standings')


@api.route('/<name>',methods=['GET','POST'])
class Scraped_teams(Resource):
    def get(self,name):
        # teams=Team.get_teams()
        fixtures=Match.get_fixtures(name)
        # return teams
        return fixtures

@api.route('/week/<number>',methods=['GET','POST'])
class Scraped_fixtures(Resource):
    def get(self,number):
        matches=Match.get_week(number)
        results = {'week': matches}
        return jsonify(results)

@api.route('/league/<name>')
class Leagueq(Resource):
    def get(self,name):
        leagues=League.get_league(name)
        return jsonify(leagues)
@api.route('/search/<name>',methods=['Post','GET'])
class Search(Resource):
    def get(self,name):
        results=Team.search_teams(name)
        return jsonify(results)


# @api.route('/count')
# class Countryq(Resource):
#     def get(self):
#         lis=['epl','bundesliga','laliga']
#         for li in lis:
#             new_country=Country(name=li)
#             new_country.save_country()

        ## <><>><>>?>?>?>?>?><><><
        ## VERY IMPORTANT DONT DELETE
        ## <><>><>>?>?>?>?>?><><><
# @api.route('/leaguez')
# class Scraped_fixtures(Resource):
#     def get(self):
#         matches=[]
#         json_data=open('laliga.json').read()
#         data=json.loads(json_data)
#         week_list=[]
#
#         for week in data:
#             a=week['week']
#             week_number=int(a.split(' ')[1])
#             matches=week['matches']
#
#             for match in matches:
#                 status=match['status']
#                 if status=='FT':
#                     home=match['home'][0]
#                     away=match['away']
#                     home_score=match['home_score']
#                     away_score=match['away_score']
#                     home_ins=Team.get_team(home)
#                     away_ins=Team.get_team(away)
#                     if home_score==away_score:
#                         week_list.append([home_score,home_ins.id,away_score,away_ins.id,'draw'])
#                         ######SW#####D###D#D
#                         home_standing = League.query.filter_by( team_id = home_ins.team_id).first()
#                         away_standing = League.query.filter_by( team_id = away_ins.team_id).first()
#                         #
#                         home_standing.points += 1
#                         away_standing.points += 1
#                         db.session.commit()
#                         ######### reset
#                         # away_standing.gd=0
#                         # home_standing.gd=0
#                         # home_standing.points = 0
#                         # away_standing.points = 0
#                         # db.session.commit()
#
#
#                     elif home_score>away_score:
#                         week_list.append([home_score,home_ins.id,away_score,away_ins.id,'home win'])
#                         ########    # single_user = User.query.filter_by(id = 1).update({"username": "James Muriuki"})
#                         home_standing = League.query.filter_by( team_id = home_ins.team_id).first()
#                         away_standing = League.query.filter_by( team_id = away_ins.team_id).first()
#
#                         home_standing.gd +=(int(home_score)- int(away_score))
#                         home_standing.points += 3
#                         away_standing.gd -=(int(home_score)- int(away_score))
#                         db.session.commit()
#                         #########reset
#                         # away_standing.gd=0
#                         # home_standing.gd=0
#                         # home_standing.points = 0
#                         # away_standing.points = 0
#                         # db.session.commit()
#
#
#                     elif home_score<away_score:
#                         week_list.append([home_score,home_ins.id,away_score,away_ins.id,'away win'])
#                         # ######SDF######SD
#                         home_standing = League.query.filter_by( team_id = home_ins.team_id).first()
#                         away_standing = League.query.filter_by( team_id = away_ins.team_id).first()
#
#                         away_standing.gd +=(int(away_score)-int(home_score))
#                         away_standing.points += 3
#                         home_standing.gd -=(int(home_score)- int(away_score))
#                         db.session.commit()
#                         #########reset
#                         # away_standing.gd=0
#                         # home_standing.gd=0
#                         # home_standing.points = 0
#                         # away_standing.points = 0
#                         # db.session.commit()
#
#         return jsonify(week_list)

#

        ## <><>><>>?>?>?>?>?><><><
        ## VERY IMPORTANT DONT DELETE
        ## <><>><>>?>?>?>?>?><><><
# @api.route('/abc')
# class Scraped_fixtures(Resource):
#     def get(self):
#         matches=[]
#         json_data=open('laliga.json').read()
#         data=json.loads(json_data)
#         week_list=[]
#         for week in data:
#             a=week['week']
#             week_number=int(a.split(' ')[1])
#             matches=week['matches']
#             for match in matches:
#                 home=match['home'][0]
#                 status=match['status']
#                 home_ins=Team.get_team(home)
#                 away=match['away']
#                 away_ins=Team.get_team(away)
#                 date=match['date'][0]
#                 if status=='FT':
#                     home_score=match['home_score']
#                     away_score=match['away_score']
#                     score=home_score+away_score
#                     fixture=[home_ins.id,away_ins.id,date,week_number,score,status]
#                     week_list.append(fixture)
#                     match_object=Match(week=week_number,home_team=home_ins.id,away_team=away_ins.id,date=date,status=status,score=score,country=3)
#                     match_object.save_fixture()
#                 else:
#                     score='00'
#                     fixture=[home_ins.id,away_ins.id,date,week_number,score,status]
#                     week_list.append(fixture)
#                     match_object=Match(week=week_number,home_team=home_ins.id,away_team=away_ins.id,date=date,status=status,score=score,country=3)
#                     match_object.save_fixture()
#         print (len(week_list))
#         return jsonify(week_list)


        ## <><>><>>?>?>?>?>?><><><
        ## VERY IMPORTANT DONT DELETE
        ## <><>><>>?>?>?>?>?><><><
# @api.route('/zxc')
# class Scraped_saved_teams(Resource):
#     def get(self):
#         teams=[]
#         json_data=open('la.json').read()
#         data=json.loads(json_data)
#         print (len(data[0]['week'][0]))
#         week=data[0]['week']
#         for fixture in week:
#             home=fixture['home'][0]
#             home_id=home.lower().replace(" ","-")
#             home_team=Team(team=home,team_id=home_id)
#             home_team.save_team()
#
#             away=fixture['away']
#             away_id=away.lower().replace(" ","-")
#             away_team=Team(team=away,team_id=away_id)
#             away_team.save_team()
#
#             teams.append(home)
#             teams.append(away)
#         return teams




        ## <><>><>>?>?>?>?>?><><><
        ## VERY IMPORTANT DONT DELETE
        ## <><>><>>?>?>?>?>?><><><

# @api.route('/league')
# class Scraped_saved_teams(Resource):
#     def get(self):
#         teams=[]
#         json_data=open('la.json').read()
#         data=json.loads(json_data)
#         print (len(data[0]['week'][0]))
#         week=data[0]['week']
#         for fixture in week:
#             home=fixture['home'][0]
#             home_id=home.lower().replace(" ","-")
#             home_team=League(team=home,team_id=home_id,position=0,played=0,gd=0,points=0,country=3)
#             home_team.save_team()
#
#             away=fixture['away']
#             away_id=away.lower().replace(" ","-")
#             away_team=League(team=away,team_id=away_id,position=0,played=0,gd=0,points=0,country=3)
#             away_team.save_team()
#
#             teams.append(home)
#             teams.append(away)
#         return teams
