import pybullet as p
from time import sleep 

p.connect(p.GUI)
p.setGravity(0,0,-10)

angle=p.addUserDebugParameter('Streeing',-0.5,0.5,0)
throttle=p.addUserDebugParameter('Throttle',0,20,0)
car=p.loadURDF("simplecar.urdf")
plane=p.loadURDF("simpleplane.urdf")

wheel_indices = [1, 3, 4, 5]
hinge_indices = [0, 2]

while True:
    user_angle = p.readUserDebugParameter(angle)
    user_throttle = p.readUserDebugParameter(throttle)
    for joint_index in wheel_indices:
        p.setJointMotorControl2(car, joint_index,
                                p.VELOCITY_CONTROL,
                                targetVelocity=user_throttle)
    for joint_index in hinge_indices:
        p.setJointMotorControl2(car, joint_index,
                                p.POSITION_CONTROL, 
                                targetPosition=user_angle)
    p.stepSimulation()

    
p.disconnect()

