import requests
import datetime
from os import system

def date_pars(some_list):
    for k in range(len(some_list)):
        some_list[k] = str(some_list[k]).replace('Z', "")
        some_list[k] = (some_list[k]).replace('T', " ")
        if some_list[k] != 'None':
            some_list[k] = datetime.datetime.strptime(some_list[k], '%Y-%m-%d %H:%M:%S')
        else:
            continue
    return some_list


def closed_req(close_req):
    closed_week, closed_day = [], []
    for l in range(len(close_req)):
        if close_req[l] != 'None':
            closed_week.append((close_req[l]).isoweekday())
            closed_day.append((close_req[l]).isocalendar()[1])
        else:
            closed_week.append(close_req[l])
            closed_day.append(close_req[l])
    return closed_week, closed_day

if __name__ == "__main__":
    try:
        name = input('GitHub name:')
        passwd = input('GitHub password:')
        i = 1
        re = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls?page=1&per_page=7&state=all',auth=(name, passwd))
        req = re.json()
        while re.content != '[]':
            reqs2 = requests.get('https://api.github.com/repos/alenaPy/devops_lab/pulls?page=' + str(i) + '&per_page=7&state=all',auth=(name, passwd))
            if reqs2.content == '[]':
                break
            else:
                req2 = reqs2.json()
                req.extend(req2)
            i += 1
    except AttributeError:
        exit('Wrong username or password!')
    system('clear')
    user = input('Enter GitHub user to get statistic about him: ')
    closed_week, login, comments, times, closed_time, title_com, hours_create, week_day, week_od_day_opened, number_days_created, merged, merged_at, closed_day, ids = [], [], [], [], [], [], [], [], [], [], [], [], [], []
    num_of_pull_req = req[0]['number']
    for i in range(int(num_of_pull_req)):
        login.append(req[i]['user']['login'])
        times.append((req[i]['head']['repo']['created_at']))
        closed_time.append((req[i])['closed_at'])
        merged.append(req[i]['merged_at'])
        title_com.append([req[i]['title']])
        date_parsed = date_pars(times)
        closed_time = date_pars(closed_time)
        merged_parswd = date_pars(merged)
        for k in range(len(date_parsed)):
            hours_create.append(date_parsed[k].hour)
            week_od_day_opened.append(date_parsed[k].isoweekday())
            week_day.append(date_parsed[k].isocalendar()[1])
            number_days_created.append(((datetime.datetime.now()) - date_parsed[k]).days)
            merged.append(merged_parswd[k])

    closed_week, closed_day = closed_req(closed_time)
    if user in login:
        for k in range(len(login)):
            if login[k] == user:
                ids.append(k)
    else:
        print('No such user')
        exit(0)

    while (True):
        choice = input('Choose action:')
        for l in ids:
            if choice == 'merged':
                print("Were your pull request merged? " + str(merged[l]))
            elif choice == 'create_date':
                print( "How much days left since creating of your pull request? " + str(number_days_created[l]) + " days")
            elif choice == 'day_week_open':
                print("Your pull request were created on " + str(week_od_day_opened[l]) + " day of the week")
            elif choice == 'week_of_create':
                print("Your pull request were opened in the " + str(week_day[l]) + " week")
            elif choice == 'closed_week':
                print("Your pull request were closed in the " + str(closed_day[l]) + " week")
            elif choice == 'closed_day':
                print("Your pull request were closed on " + str((closed_week[l])) + " day of the week")
            elif choice == 'create_hour':
                print("Your pull request were created at " + str(hours_create[l]) + " o'clock")
            elif choice == 'comments':
                print("Your comments: " + str(title_com[l][0]))
            elif choice == 'exit':
                exit('Goodbye!')
            elif choice == '/help':
                print("merged - Whether your pull request closed or not.\ncreate_date - How many days left after your made pull request\nday_week_open - Get the day of the week when you made pull request\nweek_of_create - Get number of the week when you made pull request\nclosed_week - Get number of the week when you made pull request.None means that your request haven't closed yet\nclosed_day - Get day of the week when your pull request were closed.None means that your request haven't closed yet\ncreate_hour - Get hour when you made pull request\ncomments - Get your comments to pull request\n/help - Get help\nexit - Leave the program")
                break
            else:
                print("Incorrect choice.Please use /help")
                break
