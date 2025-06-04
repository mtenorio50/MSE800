# Last In Last Out

browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
last = browsing_session.pop(0)
print(last)
print(browsing_session)
print("redirect", browsing_session[-2])
if not browsing_session:  # this check is to see if the list is empty
    print("No browsing session")
