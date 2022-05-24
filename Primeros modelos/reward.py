import numpy as np
import math


# Thresholds 
DIRECTION_THRESHOLD = 10.0
SPEED_THRESHOLD = 1
MAX_SPEED_THRESHOLD = 2

def reward_function(params):
    '''
    Example of rewarding the agent to follow center line
    '''
    # Read input parameters
    track_width = params['track_width']
    distance_from_center = params['distance_from_center']
    all_wheels_on_track = params['all_wheels_on_track']
    waypoints = params['waypoints']
    speed = params['speed']
    closest_waypoints = _getClosestWaypoints(params)
    heading = _getHeading(params)
    
    
    #Calculate direction 
    track_direction = getTrackDirection(waypoints, closest_waypoints)
    
    # Give higher reward if the car is inside the track
    if all_wheels_on_track:
        # Give higher reward if the car is closer to center line and vice versa
        reward = markersPenalty(distance_from_center, track_width)
        reward = speedPenalty(track_direction, speed, reward)
        
        # Penalize the reward if the difference is too large
        if getDirectionDiff(track_direction, heading) > DIRECTION_THRESHOLD:
            reward *= 0.5
    else:
        reward = 1e-6  # likely crashed/ close to off track
        
    
    return float(reward)

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

def markersPenalty(distance_from_center, track_width):
  for marker in np.arange(0,1,0.05):
    if distance_from_center <= marker * track_width:
      return 1-marker

def speedPenalty(track_direction, speed, reward):

  deltaAngle = 5
  goodAngles =  [0, 90, 180 ,270]

  if speed > MAX_SPEED_THRESHOLD: #si se va de la maxima velocidad, lo penalizamos
      reward *= 0.3
      return reward


  for angle in goodAngles:
    if angle - deltaAngle <= track_direction <= angle + deltaAngle: #no dejarlo ir rapido al doblar 
      if speed <= SPEED_THRESHOLD:
          if reward:
            reward += 0.8
          else:
            reward = 0.8
      else:
        reward *= 0.5
  
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