import time

class cm_timer_1:
    def __enter__(self):
        self.start_time = time.time()  #начальное время
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed_time = time.time() - self.start_time  # разницу времени
        print(f"time: {elapsed_time:.2f}")


from contextlib import contextmanager

@contextmanager #контекстный менеджер
def cm_timer_2():
    start_time = time.time()  # начало измер
    try:
        yield
    finally:
        elapsed_time = time.time() - start_time
        print(f"time: {elapsed_time:.2f}")
import time

if __name__ == "__main__":
    print("Using cm_timer_1:")
    with cm_timer_1():
        time.sleep(2.5)

    print("\nUsing cm_timer_2:")
    with cm_timer_2():
        time.sleep(3.0)

#генератор позволяет приостанавливать выполнение функции и
# возвращать значение, сохраняя состояние выполнения,
