from operator import itemgetter

import requests

# Зробити виклик через API та зберегти відповідь.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Обробити інформацію щодо кожної публікації.
submmision_ids = r.json()
submission_dicts = []

for submission_id in submmision_ids[:30]:
	# Зробити окремий виклик через API для кжного допису.
	url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
	r = requests.get(url)
	print(f"id: {submission_id}\tstatus: {r.status_code}")
	response_dict = r.json()

	# Зробити словник для кожного допису.
	if 'descendants' in response_dict:
		submission_dict = {
			'title': response_dict['title'],
			'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
			'comments': response_dict['descendants'],
	}
	submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
							reverse=True)

for submission_dict in submission_dicts:
	print(f"\nTitle: {submission_dict['title']}")
	print(f"Discussion link: {submission_dict['hn_link']}")
	print(f"Comments: {submission_dict['comments']}")