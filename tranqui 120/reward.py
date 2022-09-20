def reward_function(params):
    center_variance = params["distance_from_center"] / params["track_width"]


    left_lane =[12,13,14,15,16,17,18,19,20,26,27,28,29,30,31, 53,54,55,56,57,58, 59, 60, 83,84,85,86,87,88,89, 109,110,111,112,113,114,115,116,117
                                     ]

    center_lane = [1,2,3,4,5,6,7,8,9,10,11,21,22,23,24,25,32,33,34,47, 48, 49,50,51,52, 61, 62,63,64,65,66,67, 68,69,70,71,72,73,74,75,76,77,78,79, 80,81,82, 90,91,92,93,104,105,106,107,108, 118,119,120,121,122,123,123,125,126,127,128,129,
                                          130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,145,147,148,149,150,151,152,153,154,155,156,157,158,159]

    right_lane = [35,36,37,38,39,40,41,42,43,44,45,46,94,95,96,97,98,99,100,101,102,103,
                                     ]

    fast = [1,2,3,4,5,6,7,8,9,10,11,12,13,27,28,29,30,31,32,33,34,35,36,37,38,39,
                                85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,145,146,147,148,149,150,151,152,153,154,155,156,157,158,159
                                                                ]  # Fill in the waypoints


    slow = [24,25,26,40,41,42,43,44,82,83,84
                    ] 

    middle = [14,15,16,17,18,19,20,21,22,23,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,
                              78,79,80,81,110                                                        ]

    middle1 = [111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144]


    reward = 21
    closest_waypoints = params["closest_waypoints"][1]
    speed = params["speed"]

    if closest_waypoints in fast:
        if speed >= 3.6:
            reward += 10
            if speed==4:
                reward += 5
        else:
            reward -= 10
    
    elif closest_waypoints in slow:
        if speed <= 2.3:
            reward += 10
        else:
            reward -= 10


    elif closest_waypoints in middle:
        if speed == 3.0:
            reward += 10
        else:
            reward -= 10

    elif closest_waypoints in middle1:
        if speed == 3.0:
            reward += 10
        else:
            reward -= 10

    if closest_waypoints in left_lane and params["is_left_of_center"]:
        reward += 10
    elif closest_waypoints in right_lane and not params["is_left_of_center"]:
        reward += 10
    elif closest_waypoints in center_lane and center_variance < 0.4:
        reward += 10
    else:
        reward -= 10


    return float(reward)
