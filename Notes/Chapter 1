""" Introduction to Data Science

    1. Finding Key Connectors
    Given a dict of ids and names, and a list of tuples
    containing pairs of connections, find the number of
    connections each id has with the others
"""

# Given dict:
users = [
{"id": 0, "name": "Hero" },
{"id": 1, "name": "Dunn" },
{"id": 2, "name": "Sue" },
{"id": 3, "name": "Chi" },
{"id": 4, "name": "Thor" }
{"id": 5, "name": "Clive" },
{"id": 6, "name": "Hicks" },
{"id": 7, "name": "Devin" },
{"id": 8, "name": "Kate" },
{"id": 9, "name": "Klein" }
]

# Given list of pairs of IDs:
friendship_pairs = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
                    (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# Turn the list into a dict to iterate through more efficiently
friendships = {user["id"]: [] for user in users}    # initialize with empty list

for i, j in friendship_pairs:       # loop over friendship pairs to fill it
friendships[i].append(j)            # Add j as a friend of user i
friendships[j].append(i)            # Add i as a friend of user j

# What's the average number of connections?
def number_of_friends(user):        # First, find total connections
    """How many friends does _user_ have?"""
    user_id = user["id"]
    friend_ids = friendships[user_id]
    return len(friends_ids)

total_connections = sum(number_of_friends(user) for user in users)      #24

num_users = len(users)      # Length of users list
avg_connections = total_connections / num_users     # 24 / 10 == 2.4

# Who are the most 'connected' people?
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

num_friends_by_id.sort(                                 # Sort the list
    key = lambda id_and_friends: id_and_friends[1],     # by num_friends
    reverse = True)                                     # largest to smallest
        # Output:
        # [(1, 3), (2, 3), (3, 3), (5, 3), (8, 3),
        # (0, 2), (4, 2), (6, 2), (7, 2), (9, 1)]
        # This is the network metric 'degree centrality'

# Create a friend suggester
def foaf_ids_bad(user):
    """foaf is short for 'friend of a friend'"""
    return [foaf_id for friend_id in friendships[user["id"]]
                    for foaf_id in friendships[friend_id]]
    # This returns the following when called on users[0]:
    # [0, 2, 3, 0, 1, 3]

# Create a count of mutual friends, excluding those already known
from collections import Counter

def friends_of_friends(user):
    user_id = user["id"]
    return Counter(
        foaf_id
        for friend_id in friendships[user_id]       # For each of my friends,
        for foaf_id in friendships[friend_id]       # find their friends
        if foaf_id != user_id                       # who aren't me
        and foaf_id not in friendships[user_id]     # and aren't my friends
    )

print(friends_of_friends(users[3]))     # Counter({0: 2, 5: 1})
                                        # i.e. user #3 has two mutual friends
                                        # with user #0 and one with user #5

# Explore the salary data of data scientists
salaries_and_tenures = [ (83000, 8.7), (88000, 8.1),    # (salary, tenure)
                         (48000, 0.7), (76000, 6),
                         (69000, 6.5), (76000, 7.5),
                         (60000, 2.5), (83000, 10),
                         (48000, 1.9), (63000, 4.2)]

# Look at average salary for each tenure
from collections import defaultdict

salary_by_tenure = defaultdict(list)    # Keys are years, values are lists
                                        # of the salaries for each tenure
for salary, tenure in salaries_and tenures:
    salary_by_tenure[tenure].append(salary)

average_salary_by_tenure = {                   # Keys are years, values are
    tenure: sum(salaries) / len(salaries)      # average salary for that tenure
    for tenure, salaries in salary_by_tenure.items()
}

# Bucket the tenures to return more helpful information on salaries
def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"

salaries_by_tenure_bucket = defaultdict(list)   # Keys are tenure buckets
                                                # Values are lists of salaries
for salary, tenure in salaries_and_tenures:
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# Compute the average salary for each group
average_salary_by_bucket = {
        tenure_bucket: sum(salaries) / len(salaries)
        for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}
    # Output:
    # {"between two and five": 61500.0,
    #  "less than five": 48000.0,
    #  "more than five": 79166.67}
