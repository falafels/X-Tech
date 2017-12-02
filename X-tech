def priortize(entry):
    A = ["Finger","Thumb","Hand","Wrist","Scaphoid","Forearm","Elbow","Radial Head"]
    B = ["Humerus","Shoulder","Clavicle","A/C jts","Scapula"]
    C = ["Toes","Foot","Calcaneus","Ankle","Tib-Fib"]
    D = ["Knee","Intercondylar Fossa","Patella"]
    E = ["Pelvis","Hip","Acetabulum","Hip","Ilium","T-Spine","L-Spine","Sacrum","Coccyx","SI jts"]
    F = ["C-spine","Soft Tissue Neck"]
    G = ["Chest","Ribs","Sternum"]

    queue = []
    w = 0
    if entry[2] == "urgent":
        for i in range(len(queue)):
            if queue[i][2] != "urgent":
                queue.insert(i,entry)
                w+=1
                break
    elif entry[2] == "emergency":
        for i in range(len(queue)):
            if queue[i][2] != "emergency" and queue[i][2] != "urgent":
                queue.insert (i,entry)
                w+=1
                break
    else:
        if entry[3]-queue[-1][3] > 5:
            queue.insert(-1,entry)
        else:
            for i in range(w,len(queue)):
                if entry[1] in A and queue[i][1] in A:
                    queue.insert(i+1,entry)
                elif entry[1] in B and queue[i][1] in B:
                    queue.insert(i+1,entry)
                elif entry[1] in C and queue[i][1] in C:
                    queue.insert(i+1,entry)
                elif entry[1] in D and queue[i][1] in D:
                    queue.insert(i+1,entry)
                elif entry[1] in E and queue[i][1] in E:
                    queue.insert(i+1,entry)
                elif entry[1] in F and queue[i][1] in F:
                    queue.insert(i+1,entry)
                elif entry[1] in G and queue[i][1] in G:
                    queue.insert(i+1,entry)
    return queue
