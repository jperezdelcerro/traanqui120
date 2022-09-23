def reward_function(params):
    center_variance = params["distance_from_center"] / params["track_width"]

    
    left_lane = [14,15,16,17,18,19,20,21,22,23,24,25,26,27,
                39,40,41,42,43,57,58,59,60,61,62,63,64,65,66,67,85,86,87,88,89,90,91,  
                102,103,104,105,106,107,108,109,110,111,112,  
                133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,  
                159,160,161,162,163,164, 193,194,195,196,197,198,199,200,201,   
                225,226,227,228,243,244,245,246,247,248,249,250 ]

    center_lane = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,28,29,30,31,36,37,38,  
                   44,45,46, 55,56,57,67, 68,69, 82,83,84,  92,93,   
                   99,100,101, 112,113,114,  
                   130,131,132, 144,145,146,147,148,149, 
                   150,151,152,153,154,  157,158,  165,166,167,168, 
                   176,177,178,179,180,181,182,183,184,185,186, 
                   191,192,193, 202,203, 210,211,212,213,214,215,216,218,219,220,221,222,223,224,225,226,227,228,229,230, 
                   240,241,242,  250,251,252,253,254]


    right_lane = [32,33,34,35,36, 
                  47,48,49,50,51,52,53,54, 
                  69,70,71,72,73,74,75,76,77,78,79,80,81,  
                  93,94,95,96,97,98,99,100,  
                  114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129, 
                  154,155,156,   168,169,170,171,172,173,174,175,  
                  187,188,189,190,  204,205,206,207,208,209,210,211,212, 
                  231,232,233,234,235,236,237,238,239
                                     ]

    fast = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,   
            27,28,29,30,31,32,33,34,35,36, 
            43,44,45,46,47,48,
            114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,  
            153,154,155,156,157,158,  
            164,165,166,167,168,169,170,171,172,173,174,175,176,177,178,179,180,181,182,183,184,  
            202,203,204,205,206,207,208,209,210,211,212,213,214,214,215,216,217,218,219,220,221,222,223,223,225,226, 
            242,243,244,245,246,247,248,249,250,251,252,253,254        ] 


    slow = [48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,  
            70,71,72,73,74,75,76,77,78,79, 89,90,91,92,93,94,95,96,  
            103,104,105,106,107,108,109,110,111,112,  191,192,193,194,195,196,197,198,199,200,201,202, 
            227,228,229,230,231,232,233,234,235,236,237,238,239,240,241
                    ] 

    middle = [65,66,67,68,69,     
              97,98,99,100,101,102, 113,114 ]
    
    middle1 = [15,16,17,18,19,20,21,22,24,25,26, 
               38,39,40,41,42,43,
               80, 81,82,83,84,85,86,87,88,
               147,148,149,150,151,152,153, 
               159,160,161,162,163,164, 185,186,187,188, 189,190,191]

    reward = 21
    MAX_SPEED = 4
    MIN_SPEED = 2

    speed = params["speed"]
    sigma = speed/(MAX_SPEED-MIN_SPEED)
    closet_waypoints_1 = params["closest_waypoints"][1]

    if closet_waypoints_1 in fast:
        if speed >= 3.0:
            reward += 10
            #if speed==4:
            #    reward += 3
        else:
            reward -= 10
    
    elif closet_waypoints_1 in slow:
        if speed <= 2.:
            reward += 10
            #if speed==2.0:
            #    reward += 1
        else:
            reward -= 10


    elif closet_waypoints_1 in middle:
        if speed == 2.2:
            reward += 10
        else:
            reward -= 10

    elif closet_waypoints_1 in middle1:
        if speed == 2.5:
            reward += 10
        else:
            reward -= 10

    isLeftOfCenter = params["is_left_of_center"]
    if closet_waypoints_1 in left_lane and isLeftOfCenter and center_variance > 0.35:
        reward += 10
    elif closet_waypoints_1 in right_lane and not isLeftOfCenter and center_variance >0.35:
        reward += 10
    elif closet_waypoints_1 in center_lane and center_variance < 0.35:
        reward += 10
    else:
        reward -= 10


    return float(reward)