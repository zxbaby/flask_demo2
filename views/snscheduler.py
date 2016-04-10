from flask import Blueprint, render_template, request, jsonify, g, url_for, redirect, session, make_response
from apscheduler.schedulers.background import BackgroundScheduler
from classes.utils import *
from forms.forms import *
from datetime import datetime, timedelta

snsche = BackgroundScheduler()
snsche.start()
snscheduler = Blueprint('snscheluler', __name__,)

@snscheduler.route('/snsche')
def index():
    jobs = snsche.get_jobs()
    return render_template('snscheduler/index.html', jobs=jobs)

@snscheduler.route('/snsche/getjob/<id>')
def getjob(id):
    job = snsche.get_job(id)
    return 'this is %s'%job

@snscheduler.route('/snsche/add',methods=['GET', 'POST'])
def addjob():
    form = SnschedulerForm()
    if request.method == 'GET':
        return render_template('snscheduler/job_add.html', form=form)
    else:
        dic = {}
        func = job
        dic['func'] = func.func_name
        dic['ip'] = request.form.get('ip')
        dic['name'] = request.form.get('name')
        dic['id'] = dic.get('name')
        dic['trigger'] = request.form.get('trigger')
        dic['cmd'] = request.form.get('cmd')
        dic['comment'] = request.form.get('comment')
        dic['args'] = {'cmd':dic['cmd'], 'ip':dic['ip']}
        if dic['trigger'] == u'interval':
            dic['seconds'] = request.form.get('sec') or 0
            dic['minutes'] = request.form.get('min') or 0
            dic['hour'] = request.form.get('hour') or 0
            dic['day'] = request.form.get('day') or 0
            dic['weekend'] = request.form.get('weekend') or 0
            dic['start_date'] = request.form.get('start_date') or datetime.now()
            dic['end_date'] = request.form.get('end_date') or '9999-12-30'
            snsche.add_job(func=func, trigger=dic['trigger'], args=[dic['args']], id=dic['id'],
                           seconds=int(dic['seconds']), minutes=int(dic['minutes']),hours=int(dic['hour']),
                           days=int(dic['day']), start_date=dic['start_date'], end_date=dic['end_date']
                           )
        elif dic['trigger'] == u'cron':
            dic['seconds'] = request.form.get('sec') or '*'
            dic['minutes'] = request.form.get('min') or '*'
            dic['hour'] = request.form.get('hour') or '*'
            dic['day'] = request.form.get('day') or '*'
            dic['weekend'] = request.form.get('weekend') or '*'
            dic['month'] = request.form.get('month') or '*'
            dic['year'] = request.form.get('year') or '*'
            dic['start_date'] = request.form.get('start_date') or datetime.now()
            dic['end_date'] = request.form.get('end_date')  or '9999-12-30'
            snsche.add_job(func=func, trigger=dic['trigger'], args=[dic['args']], id=dic['id'],
                           second=dic['seconds'], minute=dic['minutes'],hour=dic['hour'],
                           day=dic['day'], day_of_week=dic['weekend'], month=dic['month'],
                           year=dic['year'], start_date=dic['start_date'], end_date=dic['end_date']
                           )
        elif dic['trigger'] == u'date':
            dic['run_date'] = request.form.get('run_date') or datetime.now() + timedelta(seconds=50)
            snsche.add_job(func=func, trigger=dic['trigger'], args=[dic['args']], id=dic['id'], run_date=dic['run_date'])
        # dic['jobs'] = snsche.get_jobs()
        print dic
        return redirect('/snsche')




@snscheduler.route('/snsche/pause', methods=['GET', 'POST'])
def pausejob():
    idstr = request.get_data('idstr')
    ids=idstr.split(',')
    map(snsche.pause_job, ids)
    return 'pause job %s!' % ids

@snscheduler.route('/snsche/resume', methods=['GET', 'POST'])
def resumejob():
    idstr = request.get_data('idstr')
    ids=idstr.split(',')
    map(snsche.resume_job, ids)
    return 'resume job %s!' % ids

@snscheduler.route('/snsche/delete', methods=['GET', 'POST'])
def deletejob():
    idstr = request.get_data('idstr')
    ids=idstr.split(',')
    map(snsche.remove_job, ids)
    return 'delete job %s!' % ids


def job_add(dic):
    func = dic.get('func')
    trigger = dic.get('trigger')
    id = dic.get('id')
    args = dic.get('args') or None
    seconds = dic.get('seconds')
    minutes = dic.get('minutes') or 0
    snsche.add_job(func=func, trigger=trigger, args=args, id=id, minutes=minutes, seconds=seconds)