#!/usr/bin/env python3

import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..")) + "/models/")

from steering_status import SteeringStatus


def test_Save():
    steerConfig = SteeringStatus()
    steerConfig.front_left_delta = 2
    steerConfig.front_right_delta = 2
    steerConfig.rear_left_delta = 2
    steerConfig.rear_right_delta = 2

    steerConfig.save("./data/steering_status.json")

    steerConfig = SteeringStatus(json_file="./data/steering_status.json")

    try:
        assert steerConfig.front_left_delta == 2
        print("Success front_left_delta")

    except AssertionError as e:
        print("Failed front_right_delta")

    try:
        assert steerConfig.front_right_delta == 2
        print("Success front_right_delta")
    except AssertionError as e:
        print("Failed front_right_delta")

    try:
        assert steerConfig.rear_left_delta == 2
        print("Success reart_left_delta")
    except AssertionError as e:
        print("Failed reart_left_delta")

    try:
        assert steerConfig.rear_right_delta == 2
        print("Success rear_right_delta")
    except AssertionError as e:
        print("Failed rear_right_delta")


def test_Load():
    steerConfig = SteeringStatus(json_file="./data/steering_status.json")

    try:
        assert steerConfig.front_left_delta == 2
        print("Success front_left_delta")

    except AssertionError as e:
        print("Failed front_right_delta")

    try:
        assert steerConfig.front_right_delta == 2
        print("Success front_right_delta")
    except AssertionError as e:
        print("Failed front_right_delta")

    try:
        assert steerConfig.rear_left_delta == 2
        print("Success reart_left_delta")
    except AssertionError as e:
        print("Failed reart_left_delta")

    try:
        assert steerConfig.rear_right_delta == 2
        print("Success rear_right_delta")
    except AssertionError as e:
        print("Failed rear_right_delta")


test_Save()

test_Load()
