#!/usr/bin/env python3

import sys
import time
import os.path
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..")) + "/models/")

from bt_request import BtRequest


def test_bt_request_load():
    btRequest = BtRequest(json_def='{ "cmd": "steering", "action": "move", "data": {"speedLeft": 0.1, "directionLeft": 1, "speedRight":0.1, "directionRight": 1 }}')

    try:
        assert btRequest.cmd == "steering"
        print("Success cmd")

    except AssertionError as e:
        print("Failed front_right_delta")

    try:
        assert btRequest.action == "move"
        print("Success action")
    except AssertionError as e:
        print("Failed front_right_delta")

    try:
        assert btRequest.data.speedLeft == 0.1
        print("Success data.speedLeft")
    except AssertionError as e:
        print("Failed reart_left_delta")

    try:
        assert btRequest.data.directionLeft == 1
        print("Success data.directionLeft")
    except AssertionError as e:
        print("Failed rear_right_delta")

    try:
        assert btRequest.data.speedRight == 0.1
        print("Success data.speedLeft")
    except AssertionError as e:
        print("Failed reart_left_delta")

    try:
        assert btRequest.data.directionRight == 1
        print("Success data.directionLeft")
    except AssertionError as e:
        print("Failed rear_right_delta")


def test_bt_request_load_speed():
    timeStart = time.perf_counter()
    btRequest = BtRequest(json_def='{ "cmd": "steering", "action": "move", "data": {"speedLeft": 0.1, "directionLeft": 1, "speedRight":0.1, "directionRight": 1 }}')
    timeEnd = time.perf_counter()
    timeTaken = timeEnd - timeStart
    print("TimeTaken (seconds):" + str(timeTaken))


test_bt_request_load()
test_bt_request_load_speed()
