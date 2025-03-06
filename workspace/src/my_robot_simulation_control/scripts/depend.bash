#!/bin/bash

set -e  # Остановить выполнение при ошибке

# Установка python3-rosdep
sudo apt install -y python3-rosdep

# Инициализация и обновление rosdep
sudo rosdep init || echo "rosdep уже инициализирован"
sudo rosdep update

# Установка зависимостей
rosdep install --from-paths src --ignore-src -r -y

# Обновление пакетов и установка необходимых ROS-компонентов
sudo apt update
sudo apt install -y ros-noetic-ros-control ros-noetic-ros-controllers ros-noetic-effort-controllers ros-noetic-position-controllers ros-noetic-joint-state-controller

# Очистка и сборка catkin workspace
catkin clean -y
catkin build

# Источник setup.bash
source devel/setup.bash

echo "Скрипт выполнен успешно!"
