class Program
{
	static void Main()
	{
		// Путь к файлу с координатами
		string filePath = "C:/Users/Кирилл/source/repos/TrialSignaturesWF/AllCoordinates/u01_F_01.txt";

		// Считывание координат из файла
		List<Tuple<double, double>> coordinates = ReadCoordinatesFromFile(filePath);

		//индекс точки, для которой необходимо вычислить радиус кривизны
		int pointIndex = 5;

		// Извлечение признаков из координат
		if (coordinates.Count > 0)
		{
			//общая длина
			double totalLength = CalculateTotalLength(coordinates);
			//средняя длина
			double averageLength = CalculateAverageLineLength(coordinates);
			//плотность
			double density = CalculateDensity(coordinates);
			// Рассчитываем углы между последовательными точками
			List<double> angles = CalculateAngles(coordinates);
			// Вычисление радиуса кривизны
			double curvatureRadius = CalculateCurvatureRadius(coordinates, pointIndex);
			// Вычилсение скорости изменения направления
			double directionChangeRate = CalculateDirectionChangeRate(coordinates);
			// Вычисление частоты изменения направления
			double directionChangeFrequency = CalculateDirectionChangeFrequency(coordinates);

			// Вывод результатов
			Console.WriteLine($"Общая длина: {totalLength}");
			Console.WriteLine($"Средняя длина: {averageLength}");
			Console.WriteLine($"Плотность: {density}");
			Console.WriteLine($"Радиус кривизны: {curvatureRadius}");
			Console.WriteLine($"Скорость изменения направления: {directionChangeRate}");
			Console.WriteLine($"Частота изменения направления: {directionChangeFrequency}");
			Console.WriteLine("Углы:");
			foreach (var angle in angles)
			{
				Console.WriteLine(angle);
			}
		}
	}

	// Функция для чтения координат из файла
	static List<Tuple<double, double>> ReadCoordinatesFromFile(string filePath)
	{
		var coordinates = new List<Tuple<double, double>>();

		try
		{
			string[] lines = File.ReadAllLines(filePath);
			foreach (string line in lines)
			{
				string[] values = line.Split(',');
				if (values.Length == 2 && double.TryParse(values[0], out double x) && double.TryParse(values[1], out double y))
				{
					coordinates.Add(new Tuple<double, double>(x, y));
				}
			}
		}
		catch (Exception ex)
		{
			Console.WriteLine("Ошибка чтения файла: " + ex.Message);
		}

		return coordinates;
	}

	// Функция для вычисления общей длины линий
	static double CalculateTotalLength(List<Tuple<double, double>> coordinates)
	{
		double totalLength = 0;
		for (int i = 1; i < coordinates.Count; i++)
		{
			double deltaX = coordinates[i].Item1 - coordinates[i - 1].Item1;
			double deltaY = coordinates[i].Item2 - coordinates[i - 1].Item2;
			totalLength += Math.Sqrt(deltaX * deltaX + deltaY * deltaY);
		}
		return totalLength;
	}

	// Функция для вычисления средней длины линий
	static double CalculateAverageLineLength(List<Tuple<double, double>> coordinates)
	{
		return CalculateTotalLength(coordinates) / (coordinates.Count - 1);
	}

	// Функция для вычисления плотности
	static double CalculateDensity(List<Tuple<double, double>> coordinates)
	{
		// Плотность может быть оценена как отношение общей длины к общей площади подписи
		// В данном примере используется простая оценка плотности
		double totalLength = CalculateTotalLength(coordinates);
		double maxX = coordinates.Max(c => c.Item1);
		double maxY = coordinates.Max(c => c.Item2);
		double minX = coordinates.Min(c => c.Item1);
		double minY = coordinates.Min(c => c.Item2);

		double width = maxX - minX;
		double height = maxY - minY;

		double totalArea = width * height;
		return totalLength / totalArea;
	}

	// Функция для вычисления углов между последовательными точками
	static List<double> CalculateAngles(List<Tuple<double, double>> coordinates)
	{
		List<double> angles = new List<double>();

		for (int i = 1; i < coordinates.Count - 1; i++)
		{
			double x1 = coordinates[i - 1].Item1 - coordinates[i].Item1;
			double y1 = coordinates[i - 1].Item2 - coordinates[i].Item2;
			double x2 = coordinates[i + 1].Item1 - coordinates[i].Item1;
			double y2 = coordinates[i + 1].Item2 - coordinates[i].Item2;

			double dot = x1 * x2 + y1 * y2;
			double det = x1 * y2 - y1 * x2;
			double angle = Math.Atan2(det, dot);
			angles.Add(angle);
		}

		return angles;
	}

	// Функция для вычисления радиуса кривизны
	static double CalculateCurvatureRadius(List<Tuple<double, double>> coordinates, int pointIndex)
	{
		// Рассмотрим три последовательные точки
		int previousPoint = Math.Max(pointIndex - 1, 0);
		int nextPoint = Math.Min(pointIndex + 1, coordinates.Count - 1);

		double x0 = coordinates[previousPoint].Item1;
		double y0 = coordinates[previousPoint].Item2;

		double x1 = coordinates[pointIndex].Item1;
		double y1 = coordinates[pointIndex].Item2;

		double x2 = coordinates[nextPoint].Item1;
		double y2 = coordinates[nextPoint].Item2;

		double curvatureRadius = Math.Abs((x1 - x0) * (y2 - y0) - (y1 - y0) * (x2 - x0)) /
		                         (Math.Sqrt(Math.Pow(x2 - x1, 2) + Math.Pow(y2 - y1, 2)) + 1e-6); // +1e-6 для избежания деления на ноль

		return curvatureRadius;
	}

	// Функция для вычисления скорости изменения направления
	static double CalculateDirectionChangeRate(List<Tuple<double, double>> coordinates)
	{
		double directionChangeRate = 0;

		for (int i = 2; i < coordinates.Count - 1; i++)
		{
			double x1 = coordinates[i - 2].Item1 - coordinates[i - 1].Item1;
			double y1 = coordinates[i - 2].Item2 - coordinates[i - 1].Item2;
			double x2 = coordinates[i - 1].Item1 - coordinates[i].Item1;
			double y2 = coordinates[i - 1].Item2 - coordinates[i].Item2;

			double dot = x1 * x2 + y1 * y2;
			double det = x1 * y2 - y1 * x2;
			double angle = Math.Atan2(det, dot);

			directionChangeRate += Math.Abs(angle);
		}

		return directionChangeRate / (coordinates.Count - 3);
	}

	// Функция для вычисления частоты изменения направления
	static double CalculateDirectionChangeFrequency(List<Tuple<double, double>> coordinates)
	{
		int directionChangeCount = 0;
		double threshold = 0.1; // Пример значения порога для изменения направления

		for (int i = 2; i < coordinates.Count - 1; i++)
		{
			double x1 = coordinates[i - 2].Item1 - coordinates[i - 1].Item1;
			double y1 = coordinates[i - 2].Item2 - coordinates[i - 1].Item2;
			double x2 = coordinates[i - 1].Item1 - coordinates[i].Item1;
			double y2 = coordinates[i - 1].Item2 - coordinates[i].Item2;

			double dot = x1 * x2 + y1 * y2;
			double det = x1 * y2 - y1 * x2;
			double angle = Math.Atan2(det, dot);

			if (Math.Abs(angle) > threshold) // Проверка на изменение направления, используя порог
			{
				directionChangeCount++;
			}
		}

		return (double)directionChangeCount / (coordinates.Count - 3);
	}
}
