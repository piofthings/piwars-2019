import sys
import os.path
sys.path.append(os.path.abspath(os.path.join(
    os.path.dirname(__file__), "..")) + "/models/")

from steering_status import SteeringStatus

steerConfig = SteeringStatus(json_file="../config/steering_status.json")

print(steerConfig.front_left_delta)
print(steerConfig.front_right_delta)
print(steerConfig.rear_left_delta)
print(steerConfig.rear_right_delta)

steerConfig.front_left_delta = 1
steerConfig.Save()
