# -*- coding: utf-8 -*-

import os
import datetime
import json


class Transcoder(object):
    def __init__(self, file_name, hive_name):
        self.file_name = file_name
        self.hive_name = hive_name

    def decode(self):
        file_path = "./data/{0}".format(self.file_name)
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                source_json = json.load(f)

            for hive_item in source_json[self.hive_name]:
                name = hive_item["name"].encode('latin1').decode('unicode-escape').encode('latin1').decode('utf8')
                print(name)

                # timestamp = datetime.datetime.fromtimestamp(hive_item["timestamp"])
                # print("{0} ({1})".format(name, timestamp))
        else:
            raise Exception("File {0} does not exists".format(file_path))


def decode(file_name, hive):
    print("Decode file: {0}...".format(file_name))
    transcoder = Transcoder(file_name, hive)
    transcoder.decode()
    print("")
    print("---------------------------------------")
    print("")


def main():
    print("Start decode files...")
    print("")
    decode("your_friends.json", "friends_v2")
    decode("people_who_followed_you.json", "followers_v3")
    decode("who_you've_followed.json", "following_v3")
    decode("received_friend_requests.json", "received_requests_v2")
    decode("rejected_friend_requests.json", "rejected_requests_v2")
    decode("removed_friends.json", "deleted_friends_v2")
    decode("sent_friend_requests.json", "sent_requests_v2")
    print("Finished")


if __name__ == "__main__":
    main()
