#!/bin/bash


    docker run  -ti --rm \
                -e "DISPLAY" \
                -e "QT_X11_NO_MITSHM=1" \
                -v "/tmp/.X11-unix:/tmp/.X11-unix:rw" \
                -e XAUTHORITY \
                -v /dev:/dev \
                -v /workspace:/workspace:rw \
               --net=host \
               --privileged \
               --name ros_course2023 ilya9kkk/ros_itmo:base
