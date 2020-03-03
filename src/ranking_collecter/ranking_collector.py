from string import Template
import requests
import user_info

def collect_ranks(event, context):
    usernames = user_info.USERNAMES
    weekly_rankings = []
    contest = user_info.CONTEST
    weeklyContest = user_info.WEEKLYCONTEST

    temp = Template('https://raw.githubusercontent.com/AWice/leetcode/master/leaderboard/scraped/${contestNo}weekly-contest-${weeklyContestNo}.txt')
    url = temp.substitute(contestNo=contest, weeklyContestNo=weeklyContest)

    github_request = requests.get(url = url)
    data = github_request.text.split("\n")

    for index, user in enumerate(data):
        if user in usernames:
            weekly_rankings.append(user)
            usernames.remove(user)
            if len(usernames) == 0:
                break;
    return {
        "rankings" : weekly_rankings,
        "not_participated" : usernames
    }