import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button

class RocketSimulation:
    def __init__(self, rocket):
        self.rocket = rocket
        self.x_coords = []
        self.y_coords = []
        self.max_height = 0
        self.max_speed = 0
        self.time_elapsed = 0
        self.running = True  # Управление паузой
        self.speed_factor = 1  # Управление скоростью
        self.finished = False  # Флаг завершения симуляции

        # Создаем график
        self.fig, self.ax = plt.subplots(figsize=(10, 6))
        self.line, = self.ax.plot([], [], label="Траектория полета ракеты", color="blue")
        self.ax.set_title("Траектория полета ракеты (в реальном времени)")
        self.ax.set_xlabel("Горизонтальная длина (м)")
        self.ax.set_ylabel("Высота (м)")
        self.ax.grid()
        self.ax.legend()

        # Счетчик информации
        self.info_box = self.fig.text(
            0.02, 0.95, "", fontsize=10, bbox=dict(facecolor="white", alpha=0.8)
        )

        # Добавляем кнопки
        self.create_buttons()

    def create_buttons(self):
        """Создает кнопки управления"""
        ax_pause = plt.axes([0.7, 0.01, 0.1, 0.05])  # Позиция кнопки паузы
        ax_speed_up = plt.axes([0.81, 0.01, 0.1, 0.05])  # Позиция кнопки ускорения
        ax_slow_down = plt.axes([0.59, 0.01, 0.1, 0.05])  # Позиция кнопки замедления


        self.btn_pause = Button(ax_pause, "Пауза")
        self.btn_speed_up = Button(ax_speed_up, "Ускорить")
        self.btn_slow_down = Button(ax_slow_down, "Замедлить")

        # Привязываем функции к кнопкам
        self.btn_pause.on_clicked(self.toggle_pause)
        self.btn_speed_up.on_clicked(self.speed_up)
        self.btn_slow_down.on_clicked(self.slow_down)


    def toggle_pause(self, event):
        """Включение/выключение паузы"""
        self.running = not self.running
        self.btn_pause.label.set_text("Возобновить" if not self.running else "Пауза")

    def speed_up(self, event):
        """Ускоряет симуляцию"""
        self.speed_factor = min(4, self.speed_factor * 2)  # Максимум x4 скорости

    def slow_down(self, event):
        """Замедляет симуляцию"""
        self.speed_factor = max(0.25, self.speed_factor / 2)  # Минимум x0.25 скорости


    def update_rocket_flight(self):
        """Обновляет параметры ракеты на каждом шаге симуляции"""
        g = 9.81  # Ускорение свободного падения
        air_density = 1.240 * np.exp(-0.00014 * self.rocket["height"])  # Плотность воздуха

        # Вычисляем силу тяги или сопротивления
        if self.rocket["full_weight"] <= self.rocket["weight"] - self.rocket["fuel_weight"]:  # Если топливо закончилось
            force = -air_density * self.rocket["speed"] ** 2 / 2 * self.rocket["resistance_coefficient"]
        else:  # Если двигатель работает
            force = self.rocket["engine_thrust"] - air_density * self.rocket["speed"] ** 2 / 2 * self.rocket["resistance_coefficient"]

        # Обновляем скорости по X и Y
        self.rocket["speedX"] += force / self.rocket["full_weight"] * np.cos(self.rocket["inclination_angle"]) * self.rocket["det_time"]
        self.rocket["speedY"] += (force / self.rocket["full_weight"] * np.sin(self.rocket["inclination_angle"]) - g) * self.rocket["det_time"]

        # Если есть топливо, уменьшаем массу
        if self.rocket["full_weight"] > self.rocket["weight"] - self.rocket["fuel_weight"]:
            self.rocket["full_weight"] -= self.rocket["fuel_weight"] / self.rocket["engine_operating_time"] * self.rocket["det_time"]

        # Пересчитываем угол наклона ракеты
        self.rocket["inclination_angle"] = np.arctan2(self.rocket["speedY"], self.rocket["speedX"])

        # Общая скорость ракеты
        self.rocket["speed"] = np.sqrt(self.rocket["speedX"] ** 2 + self.rocket["speedY"] ** 2)

        # Обновляем координаты
        self.rocket["height"] += self.rocket["speedY"] * self.rocket["det_time"]
        self.rocket["length"] += self.rocket["speedX"] * self.rocket["det_time"]

    def simulate(self):
        """Симулирует полет ракеты с реальной отрисовкой графика"""
        while self.rocket["height"] >= 0 and not self.finished:  # Пока ракета не упала или не завершена
            if not self.running:  # Если пауза
                plt.pause(0.1)
                continue

            # Сохраняем текущие координаты
            self.x_coords.append(self.rocket["length"])
            self.y_coords.append(self.rocket["height"])

            # Обновляем состояние ракеты
            self.update_rocket_flight()

            # Обновляем максимальные значения
            self.max_height = max(self.max_height, self.rocket["height"])
            self.max_speed = max(self.max_speed, self.rocket["speed"])
            self.time_elapsed += self.rocket["det_time"] * self.speed_factor

            # Обновляем график
            self.line.set_data(self.x_coords, self.y_coords)
            self.ax.set_xlim(0, max(self.x_coords) + 100)
            self.ax.set_ylim(0, max(self.y_coords) + 100)

            # Обновляем информацию на счетчике
            self.info_box.set_text(
                f"Время: {self.time_elapsed:.2f} сек\n"
                f"Макс высота: {self.max_height:.2f} м\n"
                f"Макс скорость: {self.max_speed:.2f} м/с"
            )

            plt.pause(0.01 / self.speed_factor)  # Учитываем скорость симуляции

        plt.ioff()  # Отключаем интерактивный режим
        plt.show()


def choose_rocket():
    """Меню для выбора ракеты"""
    print("Выберите ракету:")
    print("1. Falcon 9 (легкая, быстрая)")
    print("2. Сатурн V (тяжелая, мощная)")
    print("3. Терминатор-5 (средняя, мощная)")
    print("4. Дельта-7 (тяжелая, сверхмощная)")
    print("5. Custom (настройка вручную)")
    choice = input("Введите номер ракеты: ")
    if choice == "1":
        return {
            "weight": 100,  # Сухой вес ракеты (без топлива), кг
            "full_weight": 150,  # Полный вес ракеты (с топливом), кг
            "fuel_weight": 50,  # Вес топлива, кг
            "engine_operating_time": 1,  # Время работы двигателя, сек
            "engine_thrust": 80000,  # Сила тяги двигателя, Н
            "resistance_coefficient": 0.8 * 3.14 * pow(0.155, 2) / 4,  # Коэффициент сопротивления
            "inclination_angle": np.radians(float(input("Угол наклона (в градусах): "))),
            # Угол, заданный пользователем
            "det_time": 0.1,  # Временной шаг симуляции, сек
            "height": 0,  # Начальная высота
            "length": 0,  # Горизонтальная длина
            "speed": 0,
            "speedX": 0,
            "speedY": 0,
        }
    elif choice == "2":
        return {
            "weight": 500,  # Сухой вес ракеты, кг
            "full_weight": 2000,  # Полный вес ракеты, кг
            "fuel_weight": 1500,  # Вес топлива, кг
            "engine_operating_time": 180,  # Время работы двигателя, сек
            "engine_thrust": 3500000,  # Сила тяги двигателя, Н
            "resistance_coefficient": 0.5* 3.14 * pow(0.155, 2) / 4,
            "inclination_angle": np.radians(float(input("Угол наклона (в градусах): "))),
            "det_time": 0.1,
            "height": 0,
            "length": 0,
            "speed": 0,
            "speedX": 0,
            "speedY": 0,
        }
    elif choice == "3":
        return {
            "weight": 300,  # Сухой вес ракеты, кг
            "full_weight": 300,  # Полный вес ракеты, кг
            "fuel_weight": 150,  # Вес топлива, кг
            "engine_operating_time": 2,  # Время работы двигателя, сек
            "engine_thrust": 1600 * 150 / 2,  # Сила тяги двигателя, Н
            "resistance_coefficient": 0.8 * 3.14 * pow(0.2, 2) / 4,
            "inclination_angle": np.radians(float(input("Угол наклона (в градусах): "))),
            "det_time": 0.1,
            "height": 0,
            "length": 0,
            "speed": 0,
            "speedX": 0,
            "speedY": 0,
        }
    elif choice == "4":
        return {
            "weight": 600,  # Сухой вес ракеты, кг
            "full_weight": 600,  # Полный вес ракеты, кг
            "fuel_weight": 300,  # Вес топлива, кг
            "engine_operating_time": 3,  # Время работы двигателя, сек
            "engine_thrust": 1600 * 300 / 3,  # Сила тяги двигателя, Н
            "resistance_coefficient": 0.8 * 3.14 * pow(0.3, 2) / 4,
            "inclination_angle": np.radians(float(input("Угол наклона (в градусах): "))),
            "det_time": 0.1,
            "height": 0,
            "length": 0,
            "speed": 0,
            "speedX": 0,
            "speedY": 0,
        }
    elif choice == "5":
        print("Настройка вручную:")
        return {
            "weight": float(input("Сухой вес ракеты (без топлива), кг: ")),
            "full_weight": float(input("Полный вес ракеты (с топливом), кг: ")),
            "fuel_weight": float(input("Вес топлива, кг: ")),
            "engine_operating_time": float(input("Время работы двигателя, сек: ")),
            "engine_thrust": float(input("Сила тяги двигателя, Н: ")),
            "resistance_coefficient": float(input("Коэффициент сопротивления: ")),
            "inclination_angle": np.radians(float(input("Угол наклона (в градусах): "))),
            "det_time": 0.1,
            "height": 0,
            "length": 0,
            "speed": 0,
            "speedX": 0,
            "speedY": 0,
        }
    else:
        print("Некорректный ввод.")
        return choose_rocket()


# Запуск симуляции
rocket = choose_rocket()
simulation = RocketSimulation(rocket)
simulation.simulate()

