import collections

FILENAME = 'dummy-access.log'
fp = open(FILENAME)
file_lines = fp.readlines()
fp.close()


ip1_count = 0
ip2_count = 0

for line in file_lines:
	search = line.find('79.136.245.135')
	if search > -1:
		ip1_count += 1
	else:
		search = line.find('127.0.0.1')
		if search > -1:
			ip2_count += 1

print(f"Count of requests to server from IP 79.136.245.135: {ip1_count}")
print(f"Count of requests to server from IP 127.0.0.1: {ip2_count}")


counter = collections.Counter()
for line in file_lines:
	words = line.split()
	counter[words[0]] += 1

print(f"Max number of requests is {counter.most_common(1)[0][1]} for IP {counter.most_common(1)[0][0]}")
print(f"Min number of requests is {counter.most_common()[-1][1]} for IP {counter.most_common()[-1][0]}")


list_of_requests_count = []
for i in counter.most_common():
	list_of_requests_count.append(i[1])
print(f"List of counted requests: {list_of_requests_count}")

requests_sum = sum(list_of_requests_count)
print(f"Sum of requests: {requests_sum}")

requests_count = len(list_of_requests_count)
print(f"Count of requests: {requests_count}")

mean = requests_sum / requests_count
print(f"Mean of requests: {round(mean, 0)}")