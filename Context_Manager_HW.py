
import datetime



class MyOpen:
	def __init__(self, file_path, method):
		self.file_path = file_path
		self.method = method


	def __enter__(self):
		self.file = open(self.file_path, self.method)
		self.start_time = datetime.datetime.now()
		if self.method == "w":
			self.file.write(f"\nМенеджер по продажам начал свою работу в {str(self.start_time)}\n\n")

		return self.file


	def __exit__(self, exc_type, exc_val, exc_tb):
		if self.method == "w":
			finish_time = datetime.datetime.now()
			work_time = finish_time - self.start_time
			self.file.write(f"\nМенеджер по продажам закончил свою работу в {str(finish_time)}\nВремя работы - {str(work_time)}\n")

		if exc_type:
			self.file.write(f"\nВ работе программы случилась следующая ошибка:\n{exc_val}\nОшибка случилась в:\n{exc_tb.tb_frame}")

		self.file.close()




if __name__ == '__main__':
	with MyOpen("Calls_to_clients.txt", "w") as test_file:
		test_file.write("Здесь будет информация о том, сколько клиентов обзвонил менеджер по продажам\n")
		