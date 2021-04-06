id_contest=input()
import importlib
contest = importlib.import_module(id_contest)
id_status=input()
print(contest.check(id_status))