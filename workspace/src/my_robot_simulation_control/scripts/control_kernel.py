#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64, Bool

class ControllerCommandPublisher:
    def __init__(self):
        self.flag = False
        self.value = 0.0
        # Определяем список топиков для управления шарнирами
        self.joint_topics = [
            "/control/joint1_position_controller/command",
            "/control/joint2_position_controller/command"
        ]
        
        # Подписка на флаг и значение
        self.flag_subscriber = rospy.Subscriber("/flag", Bool, self.flag_cb)
        self.value_subscriber = rospy.Subscriber("/value", Float64, self.value_cb)

        # Создаём словарь паблишеров для каждого топика
        self.publishers = {
            topic: rospy.Publisher(topic, Float64, queue_size=10)
            for topic in self.joint_topics
        }
 
        # Частота публикации (в герцах)
        self.rate = rospy.Rate(10)

        # Время для синусоидального управления
        self.start_time = rospy.get_time()

    def flag_cb(self, msg):
        # Получаем значение флага
        self.flag = msg.data

    def value_cb(self, msg):
        # Получаем значение
        self.value = msg.data

    def publish_commands(self):
        while not rospy.is_shutdown():
            vel = self.value / 200  # Вычисление скорости, делим на 200 для корректной работы
            # rospy.loginfo(f"Vel = {vel}")
            # Вычисляем текущее время с момента запуска
            current_time = rospy.get_time() - self.start_time
            
            # Формируем команды для каждого контроллера
            commands = {
                "/control/joint1_position_controller/command": -1 if not self.flag else vel - 1,
                "/control/joint2_position_controller/command": 1 if not self.flag else -vel - 1
            }

            # Публикуем команды в соответствующие топики
            for topic, command in commands.items():
                if topic in self.publishers:
                    self.publishers[topic].publish(Float64(data=command))

            # Ждём следующего цикла публикации
            self.rate.sleep()

if __name__ == "__main__":
    rospy.init_node("controller_command_publisher")
    controller = ControllerCommandPublisher()

    try:
        controller.publish_commands()
    except rospy.ROSInterruptException:
        rospy.loginfo("Controller Command Publisher node terminated.")
