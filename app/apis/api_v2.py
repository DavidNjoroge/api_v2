from flask_restplus import Namespace, Resource, fields
# from ..core import run_spiders
from json import dumps
from flask import jsonify
import json
from ..models import Team,Match,League,Country
from .. import db
import datetime as dt
from dateutil.parser import parse
from ..crawler import init_driver,lookup
from ..bs_crawler import livescore

api = Namespace('v2', description='some api calls')


@api.route('/today')
class Today_games(Resource):
    def get(self):
        date = dt.date.today()
        dat=f'{date:%A %d %Y}'
        all_matches=Match.query.all()
        # results=Today_games.search_week(dat)
        today_matches=[]
        for match in all_matches:
            b=parse(match.date)
            tod=dt.date(b.year,b.month,b.day)
            if tod==date:
                today_matches.append(match)
        print(len(today_matches))
        json_matches=Match.process_matches(today_matches)
        return json_matches
    @classmethod
    def search_week(cls,dat):
        results=[]
        result_list=[]
        # teams=Match.query.all()
        teams=Match.query.filter_by(week=12).all()

        for teame in teams:
            # if str(name) in str(teame.team):
            result_list.append(str(teame.date))
        print(len(result_list))
        for tea in result_list:
            
            if 'sunday' in tea:
                print(dat)  
                results.append(tea)
        return results


@api.route('/week/<number>',methods=['GET','POST'])
class Scraped_fixtures(Resource):
    def get(self,number):
        matches=Match.get_week(number)
        results = {'week': matches}
        return jsonify(results)

@api.route('/crawl',methods=['GET','POST'])
class Crawler(Resource):
    def get(self):
        # matches=Match.get_week(number)
        # results = {'week': matches}
        # return jsonify(results)
        # driver = init_driver()
        # status = lookup(driver)
        # time.sleep(5)
        # driver.quit()
        data = livescore()
        return jsonify(data)


