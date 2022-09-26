import numpy as np
import math


action_space = [
        {"steering_angle": -30, "speed": 1.4},
        {"steering_angle": -30, "speed": 1.4},
        {"steering_angle": 0,   "speed": 4.0},
        {"steering_angle": 0,   "speed": 4.0},
        {"steering_angle": 0,   "speed": 3.0},
        {"steering_angle": 0,   "speed": 3.0},
        {"steering_angle": 0,   "speed": 2.5},
        {"steering_angle": 0,   "speed": 2.5},
        {"steering_angle": 0,   "speed": 2.2},
        {"steering_angle": 0,   "speed": 2.2},
        {"steering_angle": 0,   "speed": 1.4},
        {"steering_angle": 0,   "speed": 1.4},
        {"steering_angle": 15,  "speed": 2.5},
        {"steering_angle": 15,  "speed": 2.5},
        {"steering_angle": 30,  "speed": 1.4},
        {"steering_angle": 30,  "speed": 1.4}]


def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    # Read input parameters
    waypoints = params['waypoints']
    speed = params['speed']
    closest_waypoints = _getClosestWaypoints(params)
    heading = _getHeading(params)

    
    #Calculate direction 
    track_direction = getTrackDirection(waypoints, closest_waypoints)
    direction_diff = getDirectionDiff(track_direction, heading) 
    
    
    reward = 21
    reward = curveSpeedPenalty(direction_diff, speed, reward)
    
    return float(reward) if reward else 1.0

def getTrackDirection(waypoints, closest_waypoints):
    # Calculate the direction of the center line based on the closest waypoints
    next_point = waypoints[closest_waypoints[1]]
    prev_point = waypoints[closest_waypoints[0]]
    
    # Calculate the direction in radius, arctan2(dy, dx), the result is (-pi, pi) in radians
    track_direction = math.atan2(next_point[1] - prev_point[1], next_point[0] - prev_point[0])
    # Convert to degree
    return math.degrees(track_direction)

def getDirectionDiff(track_direction, heading):
    # Calculate the difference between the track direction and the heading direction of the car
    direction_diff = abs(track_direction - heading)
    if direction_diff > 180:
        direction_diff = 360 - direction_diff
        
    return direction_diff

def curveSpeedPenalty(direction_diff, speed, reward):  #combinar con lo de dav id, chequear reinforment positivo
  #if the car isnt going staight, and the speed is 
    threshold = 15
    for space in action_space:
        if direction_diff == space["steering_angle"] and speed == space['speed']:
            reward += 20
            return reward
        elif direction_diff - threshold > space["steering_angle"] >  direction_diff + threshold: 
            threshold = 0.25
            if space['speed'] - threshold > speed > space['speed'] + threshold:
                reward += 10
            else:
                reward=-10
                return reward
    return reward



def _getClosestWaypoints(params):
    # closest_waypoints
    # Type:  [int, int]
    # Range: [(0:Max-1),(1:Max-1)]
    # The zero-based indices of the two neighboring waypoints closest to the agent's current position of (x, y).
    # The distance is measured by the Euclidean distance from the center of the agent. The first element refers to the
    # closest waypoint behind the agent and the second element refers the closest waypoint in front of the agent.
    return params['closest_waypoints']

def _getHeading(params):
    # heading
    # Type: float
    # Range: -180:+180
    # Heading direction, in degrees, of the agent with respect to the x-axis of the coordinate system.
    return params['heading']