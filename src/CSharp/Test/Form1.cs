using Emgu.CV;
using Emgu.CV.Util;
using Emgu;
using Emgu.CV.Structure;
using System;
using System.Text.RegularExpressions;
using Emgu.CV.CvEnum;
using System.Reflection.Metadata;
using System.Drawing;

namespace Test
{
    public partial class Form1 : Form
    {
	    public string SignatureCoordinatesPath = "";
        private readonly string _signaturePath = "";
        private readonly Image<Bgr, byte> _inputImage;
        private const double MinRectanglePerimeter = 0.4;
        private const double PartOfPerimeterEpsilon = 0.07;

        public Form1()
        {
	        string inputImageName;
	        InitializeComponent();

            var types = new char[2] { 'F', 'G' };
            foreach (var type in types)
            {
                for (var i = 1; i <= 9; i++)
                {
                    for (var j = 1; j <= 9; j++)
                    {
                        inputImageName = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/" +
                                         $"u0{i}_{type}_0{j}.png";
                        _inputImage = new Image<Bgr, byte>(inputImageName);
                        //inputImageName = Regex.Match(inputImageName, @"\\([^\\]+)\.(png|jpg)").ToString()[..^4];
                        inputImageName = $"u0{i}_{type}_0{j}";
                        _signaturePath = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/" +
                                         $"{inputImageName}.png";
                        var outputImage = _inputImage.SmoothGaussian(5).Convert<Gray, byte>().ThresholdBinaryInv(
	                        new Gray(230), new Gray(255));
                        SearchAndCropByRectangle(outputImage);
                    }
                }
                for (var i = 1; i <= 9; i++)
                {
                    for (var j = 10; j <= 30; j++)
                    {
                        inputImageName = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/" +
                                         $"u0{i}_{type}_{j}.png";
                        _inputImage = new Image<Bgr, byte>(inputImageName);
                        //inputImageName = Regex.Match(inputImageName, @"\\([^\\]+)\.(png|jpg)").ToString()[..^4];
                        inputImageName = $"u0{i}_{type}_{j}";
                        _signaturePath = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/" +
                                         $"{inputImageName}.png";
                        var outputImage = _inputImage.SmoothGaussian(5).Convert<Gray, byte>().ThresholdBinaryInv(
	                        new Gray(230), new Gray(255));
                        SearchAndCropByRectangle(outputImage);
                    }
                }
                for (var i = 10; i <= 45; i++)
                {
                    for (var j = 1; j <= 9; j++)
                    {
                        inputImageName = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/" +
                                         $"u{i}_{type}_0{j}.png";
                        _inputImage = new Image<Bgr, byte>(inputImageName);
                        //inputImageName = Regex.Match(inputImageName, @"\\([^\\]+)\.(png|jpg)").ToString()[..^4];
                        inputImageName = $"u{i}_{type}_0{j}";
                        _signaturePath = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/" +
                                         $"{inputImageName}.png";
                        var outputImage = _inputImage.SmoothGaussian(5).Convert<Gray, byte>().ThresholdBinaryInv(
	                        new Gray(230), new Gray(255));
                        SearchAndCropByRectangle(outputImage);
                    }
                }
                for (var i = 10; i <= 45; i++)
                {
                    for (var j = 10; j <= 30; j++)
                    {
                        inputImageName = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/" +
                                         $"u{i}_{type}_{j}.png";
                        _inputImage = new Image<Bgr, byte>(inputImageName);
                        //inputImageName = Regex.Match(inputImageName, @"\\([^\\]+)\.(png|jpg)").ToString()[..^4];
                        inputImageName = $"u{i}_{type}_{j}";
                        _signaturePath = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/" +
                                         $"{inputImageName}.png";
                        var outputImage = _inputImage.SmoothGaussian(5).Convert<Gray, byte>().ThresholdBinaryInv(
	                        new Gray(230), new Gray(255));
                        SearchAndCropByRectangle(outputImage);
                    }
                }
            }

            foreach (var type in types)
            {
                for (var i = 1; i <= 9; i++)
                {
                    for (var j = 1; j <= 9; j++)
                    {
                        inputImageName = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/" +
                                         $"u0{i}_{type}_0{j}.png";
                        _inputImage = new Image<Bgr, byte>(inputImageName);
                        //inputImageName = Regex.Match(inputImageName, @"\\([^\\]+)\.(png|jpg)").ToString()[..^4];
                        inputImageName = $"u0{i}_{type}_0{j}";
                        _signaturePath = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/AllCoordinates/" +
                                         $"{inputImageName}.txt";
                        /*var outputImage = inputImage.SmoothGaussian(5).Convert<Gray, byte>().
	                        ThresholdBinaryInv(new Gray(230), new Gray(255));*/
                        FindCoordinates(_signaturePath, _inputImage);
                    }
                }
                for (var i = 1; i <= 9; i++)
                {
                    for (var j = 10; j <= 30; j++)
                    {
                        inputImageName = "C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/" +
                                         $"u0{i}_{type}_{j}.png";
                        _inputImage = new Image<Bgr, byte>(inputImageName);
                        //inputImageName = Regex.Match(inputImageName, @"\\([^\\]+)\.(png|jpg)").ToString()[..^4];
                        inputImageName = $"u0{i}_{type}_{j}";
                        _signaturePath = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/AllCoordinates/" +
                                         $"{inputImageName}.txt";
                        /*var outputImage = inputImage.SmoothGaussian(5).Convert<Gray, byte>()
	                        .ThresholdBinaryInv(new Gray(230), new Gray(255));*/
                        FindCoordinates(_signaturePath, _inputImage);
                    }
                }
                for (var i = 10; i <= 45; i++)
                {
                    for (var j = 1; j <= 9; j++)
                    {
                        inputImageName = "C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/" +
                                         $"u{i}_{type}_0{j}.png";
                        _inputImage = new Image<Bgr, byte>(inputImageName);
                        //inputImageName = Regex.Match(inputImageName, @"\\([^\\]+)\.(png|jpg)").ToString()[..^4];
                        inputImageName = $"u{i}_{type}_0{j}";
                        _signaturePath = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/AllCoordinates/" +
                                         $"{inputImageName}.txt";
                        /*var outputImage = inputImage.SmoothGaussian(5).Convert<Gray, byte>()
	                        .ThresholdBinaryInv(new Gray(230), new Gray(255));*/
                        FindCoordinates(_signaturePath, _inputImage);
                    }
                }
                for (var i = 10; i <= 45; i++)
                {
                    for (var j = 10; j <= 30; j++)
                    {
                        inputImageName = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/" +
                                         $"u{i}_{type}_{j}.png";
                        _inputImage = new Image<Bgr, byte>(inputImageName);
                        //inputImageName = Regex.Match(inputImageName, @"\\([^\\]+)\.(png|jpg)").ToString()[..^4];
                        inputImageName = $"u{i}_{type}_{j}";
                        _signaturePath = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/AllCoordinates/" +
                                         $"{inputImageName}.txt";
                        /*var outputImage = inputImage.SmoothGaussian(5).Convert<Gray, byte>()
	                        .ThresholdBinaryInv(new Gray(230), new Gray(255));*/
                        FindCoordinates(_signaturePath, _inputImage);
                    }
                }
            }
        }

        /*public void ClearAllBoxes()
        {
            textBox1.Clear();
            textBox2.Clear();
            listBox1.Items.Clear();
        }*/

        /*private void openToolStripMenuItem_Click(object sender, EventArgs e)
        {*/
            //ClearAllBoxes();
            //try
            //{
            //    DialogResult result = openFileDialog1.ShowDialog();

            //    if (result == DialogResult.OK)
            //    {
            //        inputImageName = openFileDialog1.FileName;
            //        inputImage = new Image<Bgr, byte>(inputImageName);
            //        inputImageName = Regex.Match(openFileDialog1.FileName,
            //            @"\\([^\\]+)\.(png|jpg)").ToString()[..^4];
            //        pictureBox1.Image = inputImage.ToBitmap();
            //        signatureCoordinatesPath = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/AllCoordinates/{inputImageName}.txt";
            //        //signaturePath = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/{inputImageName}.png";
            //    }
            //    else
            //    {
            //        MessageBox.Show("No file selected", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            //    }
            //}
            //catch (Exception exception)
            //{
            //    MessageBox.Show(exception.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            //}
        /*}*/
		
        /// <summary>
        /// Найти контуры.
        /// </summary>
        /// <param name="image">Изображение.</param>
        /// <returns>Контуры.</returns>
        private static VectorOfVectorOfPoint GetCountors(IInputOutputArray image)
        {
            var contours = new VectorOfVectorOfPoint();
            var hierarchy = new UMat();
            CvInvoke.FindContours(image, contours, hierarchy,
                Emgu.CV.CvEnum.RetrType.Tree, Emgu.CV.CvEnum.ChainApproxMethod.ChainApproxSimple);

            return contours;
        }
		
        /// <summary>
        /// Найти координаты.
        /// </summary>
        /// <param name="signatureCoordinatesPath">Путь для записи.</param>
        /// <param name="inputImage">Входное изображение.</param>
        private void FindCoordinates(string signatureCoordinatesPath, Image<Bgr, byte> inputImage)
        {
	        var outputImage =
		        inputImage.SmoothGaussian(5).Convert<Gray, byte>().ThresholdBinaryInv(
			        new Gray(230), new Gray(255));

	        var contours = GetCountors(outputImage);

	        var poInts = new List<Point>();

			for (var i = 0; i < contours.Size; i++)
	        {
				var approximation = new VectorOfPoint();

				CvInvoke.ApproxPolyDP(contours[i], approximation, PartOfPerimeterEpsilon * CvInvoke.ArcLength(
					contours[i], true), true);

				if (approximation.Size < 4 || approximation.Size > 8 ||
				    !CvInvoke.IsContourConvex(approximation)) continue;
				poInts.AddRange(approximation.ToArray());
	        }
			
	        Array points = contours.ToArrayOfArray();
	        
	        const int totalPoints = 0;
	        var outputString = new StreamWriter(signatureCoordinatesPath);

			foreach (Point[] pointsCoordinate in points)
			{
				var pointCoordinate = poInts.Aggregate(pointsCoordinate, (current, point) => current
					.Where(e => e != point).ToArray());

				foreach (var point in pointCoordinate)
				{
					outputString.WriteLine(point.X.ToString() + ", " + point.Y.ToString());
				}
			}
			
			outputString.Close();
	        textBox1.Text = (totalPoints - 4).ToString();
		}

    //    private void findContoursToolStripMenuItem_Click(object sender, EventArgs e)
    //    {
    //        ClearAllBoxes();
    //        try
    //        {
    //            Image<Gray, byte> outputImage =
    //                inputImage.SmoothGaussian(5).Convert<Gray, byte>().ThresholdBinaryInv(new Gray(230), new Gray(255));

    //            VectorOfVectorOfPoint contours = GetCountors(outputImage);

    //            Array points = contours.ToArrayOfArray();

    //            var totalPoints = 0;
    //            var outputString = new StreamWriter(signatureCoordinatesPath);

    //            foreach (Point[] pointCoordinate in points)
    //            {
	   //             totalPoints++;
				//	if (totalPoints > 4)
	   //             {
		  //              foreach (Point point in pointCoordinate)
		  //              {
			 //               listBox1.Items.Add(point);
			 //               outputString.WriteLine(point.X.ToString() + ", " + point.Y.ToString());
			 //               //totalPoints++;
				//		}
    //                    //continue;
				//	}
				//	//totalPoints++;
				//}

    //            outputString.Close();
    //            textBox1.Text = (totalPoints - 4).ToString();

    //            if (checkBox1.Checked)
    //            {
    //                Image<Gray, byte> blackBackground = new Image<Gray, byte>(inputImage.Width, inputImage.Height, new Gray(0));

    //                CvInvoke.DrawContours(inputImage, contours, -1, new MCvScalar(0, 0, 255));

    //                pictureBox2.Image = blackBackground.ToBitmap();

    //            }
    //            else
    //            {
    //                CvInvoke.DrawContours(inputImage, contours, -1, new MCvScalar(74, 144, 226));

    //                pictureBox2.Image = inputImage.ToBitmap();
    //            }
    //        }
    //        catch (Exception exception)
    //        {
    //            MessageBox.Show(exception.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
    //        }
    //    }

		/// <summary>
		/// Метод обрезки изображения по прямоугольнику. 
		/// </summary>
		/// <param name="inputImageInBit">Входное изображение в битах.</param>
		/// <param name="croppingRectangle">Прямоугольник по которому обрезать.</param>
		/// <returns>Обрезанное изображение.</returns>
        public static Bitmap cropAtRect(Bitmap inputImageInBit, Rectangle croppingRectangle)
        {
	        using var nb = new Bitmap(croppingRectangle.Width, croppingRectangle.Height);
	        using Graphics g = Graphics.FromImage(nb);
	        g.DrawImage(inputImageInBit, -croppingRectangle.X, -croppingRectangle.Y);
	        return nb;
        }

		/// <summary>
		/// Находит прямоугольник и обрезает по нему.
		/// </summary>
		/// <param name="outputImage">Итоговое изображение.</param>
        private void SearchAndCropByRectangle(Image<Gray, byte> outputImage)
        {
            var shapesContours = new VectorOfVectorOfPoint();
            var hierarchy = new UMat();
            CvInvoke.FindContours(outputImage, shapesContours, hierarchy,
                Emgu.CV.CvEnum.RetrType.External, Emgu.CV.CvEnum.ChainApproxMethod.ChainApproxSimple);
            //var outputString = new StreamWriter($"C:/Users/Кирилл/source/repos/TrialSignaturesWF/123.txt");

			for (var i = 0; i < shapesContours.Size; i++)
            {
                var perimeter = CvInvoke.ArcLength(shapesContours[i], true);

                if (perimeter < MinRectanglePerimeter) 
	                continue;

                var approximation = new VectorOfPoint();

                CvInvoke.ApproxPolyDP(shapesContours[i], 
	                approximation, PartOfPerimeterEpsilon * perimeter, true);

                //CvInvoke.DrawContours(inputImage, shapesContours, i,
                //    new MCvScalar(0, 0, 255), 2);

                //pictureBox3.Image = inputImage.ToBitmap();

                //Moments moments = CvInvoke.Moments(shapesContours[i]);

                //int x = (int)(moments.M10 / moments.M00);

                //int y = (int)(moments.M01 / moments.M00);


                //           try
                //           {
                //            Rectangle rectangleTest = new Rectangle(new Point(10, 10),
                //             new Size(inputImage.Size.Width - 10, inputImage.Size.Height - 10));


                //            UMat croppedUmat = new UMat(inputImage.ToUMat(), rectangleTest);
                //            croppedUmat.ToBitmap().Save(signaturePath);
                //           }
                //           catch (Exception ex)
                //           {
                //continue;
                //           }


                if (approximation.Size < 4 || approximation.Size > 8 ||
                    !CvInvoke.IsContourConvex(approximation)) continue;
                //            var stringHelper = "";
                var xPoInts = new List<int>();
                var yPoInts = new List<int>();
                foreach (var point in approximation.ToArray())
                {
	                yPoInts.Add(point.Y);
	                xPoInts.Add(point.X);
                }
                //               outputString.WriteLine(stringHelper);

                var rectangleTest = new Rectangle(xPoInts.Min(),
	                yPoInts.Max(),
	                xPoInts.Max() - xPoInts.Min(),
	                yPoInts.Max() - yPoInts.Min());


                var rectangle = CvInvoke.BoundingRectangle(approximation);
                //Rectangle rectangle = new Rectangle(xPoInts.Min() + 10, 
                //yPoInts.Min() + 10, 
                //xPoInts.Max() - xPoInts.Min() + 1, 
                //yPoInts.Max() - yPoInts.Min() + 1);
                //rectangle.X = 10;
                //rectangle.Y = yPoInts.Max();

                
                var croppedUmat = new UMat(_inputImage.ToUMat(), rectangle);
                croppedUmat.ToBitmap().Save(_signaturePath);

                //var croppedBitMap = cropAtRect(inputImage.ToBitmap(), rectangleTest);
                //croppedBitMap.Save(signaturePath);
            }
            //outputString.Close();
        }

    }
}