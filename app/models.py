from . import db
from flask import jsonify

class Team(db.Model):
    __tablename__='teams'

    id=db.Column(db.Integer,primary_key=True)
    team=db.Column(db.String(255))
    team_id=db.Column(db.String(255))

    @classmethod
    def search_teams(cls,name):
        results=[]
        result_list=[]
        teams=Team.query.all()
        for teame in teams:
            # if str(name) in str(teame.team):
            result_list.append(str(teame.team_id))
        for tea in result_list:
            if name in tea:
                print(len(result_list))
                results.append(tea)
        return results


    def save_team(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def get_teams(cls):
        teams=Team.query.all()
        teams_list=[]
        for teamq in teams:
            each=teamq.team_id
            teams_list.append(each)
        return teams_list

    @classmethod
    def get_team(cls,name):
        team_object=Team.query.filter_by(team=name).first()
        if team_object==None:
            print ('<><><>< none found<><><><><<')


        return team_object


    def __repr__(self):
        return f'Team {self.team}'

class Match(db.Model):
    __tablename__='matches'

    id=db.Column(db.Integer,primary_key=True)
    week=db.Column(db.Integer)
    date=db.Column(db.String(255))
    home_team= db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    away_team= db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    status= db.Column(db.String(255))
    score= db.Column(db.String(255))
    country=db.Column(db.Integer)
    date_time=db.Column(db.DateTime,nullable=True)
    home = db.relationship("Team",foreign_keys=[home_team])
    away = db.relationship("Team",foreign_keys=[away_team])

    # def update_fixture(self,data):
        
    def save_fixture(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_week(cls,number):
        all_fixtures=Match.query.filter_by(week=number).all()
        matches=Match.process_matches(all_fixtures)
        return matches
    @classmethod
    def get_fixtures(cls,name):
        team_name=Team.query.filter_by(team_id=name).first()
        print (team_name.id)
        home_fixtures=Match.query.filter_by(home_team=team_name.id).all()
        away_fixtures=Match.query.filter_by(away_team=team_name.id).all()
        all_fixtures=home_fixtures+away_fixtures

        sorted_objs=sorted(all_fixtures, key=lambda fixture: fixture.id)
        matches=Match.process_matches(sorted_objs)

        return matches
    @classmethod
    def process_matches(cls,match_list):
        match_dict=[]
        for match in match_list:
            home=Team.query.filter_by(id=match.home_team).first()
            away=Team.query.filter_by(id=match.away_team).first()

            object_dict= {'date_time':match.date_time,'home':home.team,'home_id':home.team_id,'away':away.team,'away_id':away.team_id,'date':match.date,'status':match.status,'score':match.score[0]+'-'+match.score[1]}
            match_dict.append(object_dict)
        return match_dict


class League(db.Model):
    __tablename__="leagues"

    id=db.Column(db.Integer,primary_key=True)
    position=db.Column(db.Integer)
    team=db.Column(db.String(255))
    team_id=db.Column(db.String(255))
    played=db.Column(db.Integer)
    gd=db.Column(db.Integer)
    points=db.Column(db.Integer)
    country=db.Column(db.Integer)

    def save_team(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_league(cls,namec):
        count_id=Country.query.filter_by(name=namec).first()
        league_data=League.query.filter_by(country=count_id.id).all()
        print(len(league_data))
        # for stan in league_data:
        #     result_dict = jsonify(stan)
        #     league_list.append(result_dict)
        # print(league_list)
        sorted_objs=sorted(league_data, key=lambda fixture: fixture.points, reverse=True)
        league_results=League.process_leagues(sorted_objs)
        return league_results

    @classmethod
    def process_leagues(cls,orms):
        league_list=[]
        qwe=1
        for stan in orms:
            object_dict= {'pos':qwe,'team':stan.team,'team_id':stan.team_id,'played':stan.played,'gd':stan.gd,'points':stan.points}
            league_list.append(object_dict)
            qwe +=1
        return league_list

class Country(db.Model):
    __tablename__='countries'

    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255))

    def save_country(self):
        db.session.add(self)
        db.session.commit()
        
