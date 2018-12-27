from time import sleep
import threading
import datetime

exitFlag = 0


class myThread(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter

    def run(self):
        print
        "Запуск " + self.name
        # Получить lock для синхронизации потоков
        threadLock.acquire()
        sleep(1)
        print_date(self.name, self.counter)
        # Фиксатор для следующего потока
        threadLock.release()
        print
        "Выход " + self.name


def print_date(threadName, counter):
    datefields = []
    today = datetime.date.today()
    datefields.append(today)
    print
    "%s[%d]: %s" % (threadName, counter, datefields[0])


threadLock = threading.Lock()
threads = []

# Создание нового потока
thread1 = myThread("Нить", 1)
thread2 = myThread("Нить", 2)

# Запуск нового потока
thread1.start()
thread2.start()

# Добавлять потоки в список нитей
threads.append(thread1)
threads.append(thread2)

# Ждать для всех потоков, чтобы завершить
for t in threads:
    t.join()
print
"Выход из программы!!!"