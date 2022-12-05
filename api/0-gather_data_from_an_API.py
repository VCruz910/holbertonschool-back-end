#!/user/bin/python3
"""
 Python script that, using this REST API,
 for a given employee ID,
 returns information about
 his/her TODO list progress.
 """

if __name__ == "__main__":
    import sys
    import requests

    User_ID = sys.argv[1]
    URL_Emp = "https://jsonplaceholder.typicode.com/users/{}"\
            .format(User_ID)
    URL_Todo = "https//jsonplaceholder.typicode.com/todos?userId={}"\
            .format(User_ID)
    Req_Emp = requests.get(URL_Emp)
    EN = Req_Emp.json().get('name')
    Req_Todo = requests.get(URL_Todo)
    TOTAL_T = len(Req_Todo.json)
    TASKS = 0
    NUMT = 0
    Lists = []

    while TASKS < TOTAL_T:
        if Req_Todo.json()[TASKS].get('completed') is True:
            list.append(Req_Todo.json()[TASKS].get('title'))
            NUMT += 1
        TASKS += 1

    print("Employee {} is done with tasks({}/{}): ".format(EN, NUMT, TOTAL_T))
    for T in Lists:
        print("\t {}".format(T))
