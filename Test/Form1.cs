using Emgu.CV;
using Emgu.CV.Util;
using Emgu;
using Emgu.CV.Structure;
using System;
using System.Text.RegularExpressions;
using Emgu.CV.CvEnum;

namespace Test
{
    public partial class Form1 : Form
    {
        private string signatureCoordinatesPath = "";
        private string signaturePath = "";
        private Image<Bgr, byte> inputImage = null;
        const double minRectanglePerimeter = 0.4;
        const double partOfPerimeterEpsilon = 0.07;
		private static string inputImageName = "";

        public Form1()
        {
            InitializeComponent();

            char[] types = new char[2] { 'F', 'G' };
            foreach (char type in types)
            {
                for (int i = 1; i <= 9; i++)
                {
                    for (int j = 1; j <= 9; j++)
                    {
                        inputImageName = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/u0{i}_{type}_0{j}.png";
                        inputImage = new Image<Bgr, byte>(inputImageName);
                        //inputImageName = Regex.Match(inputImageName, @"\\([^\\]+)\.(png|jpg)").ToString()[..^4];
                        inputImageName = $"u0{i}_{type}_0{j}";
                        signaturePath = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/{inputImageName}.png";
                        Image<Gray, byte> outputImage = inputImage.SmoothGaussian(5).Convert<Gray, byte>().ThresholdBinaryInv(new Gray(230), new Gray(255));
                        SearchAndCropByRectangle(outputImage);
                    }
                }
                for (int i = 1; i <= 9; i++)
                {
                    for (int j = 10; j <= 30; j++)
                    {
                        inputImageName = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/u0{i}_{type}_{j}.png";
                        inputImage = new Image<Bgr, byte>(inputImageName);
                        //inputImageName = Regex.Match(inputImageName, @"\\([^\\]+)\.(png|jpg)").ToString()[..^4];
                        inputImageName = $"u0{i}_{type}_{j}";
                        signaturePath = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/{inputImageName}.png";
                        Image<Gray, byte> outputImage = inputImage.SmoothGaussian(5).Convert<Gray, byte>().ThresholdBinaryInv(new Gray(230), new Gray(255));
                        SearchAndCropByRectangle(outputImage);
                    }
                }
                for (int i = 10; i <= 45; i++)
                {
                    for (int j = 1; j <= 9; j++)
                    {
                        inputImageName = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/u{i}_{type}_0{j}.png";
                        inputImage = new Image<Bgr, byte>(inputImageName);
                        //inputImageName = Regex.Match(inputImageName, @"\\([^\\]+)\.(png|jpg)").ToString()[..^4];
                        inputImageName = $"u{i}_{type}_0{j}";
                        signaturePath = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/{inputImageName}.png";
                        Image<Gray, byte> outputImage = inputImage.SmoothGaussian(5).Convert<Gray, byte>().ThresholdBinaryInv(new Gray(230), new Gray(255));
                        SearchAndCropByRectangle(outputImage);
                    }
                }
                for (int i = 10; i <= 45; i++)
                {
                    for (int j = 10; j <= 30; j++)
                    {
                        inputImageName = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/u{i}_{type}_{j}.png";
                        inputImage = new Image<Bgr, byte>(inputImageName);
                        //inputImageName = Regex.Match(inputImageName, @"\\([^\\]+)\.(png|jpg)").ToString()[..^4];
                        inputImageName = $"u{i}_{type}_{j}";
                        signaturePath = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/{inputImageName}.png";
                        Image<Gray, byte> outputImage = inputImage.SmoothGaussian(5).Convert<Gray, byte>().ThresholdBinaryInv(new Gray(230), new Gray(255));
                        SearchAndCropByRectangle(outputImage);
                    }
                }
            }
        }

        public void ClearAllBoxes()
        {
            textBox1.Clear();
            textBox2.Clear();
            listBox1.Items.Clear();
        }

        private void openToolStripMenuItem_Click(object sender, EventArgs e)
        {
            ClearAllBoxes();
            try
            {
                DialogResult result = openFileDialog1.ShowDialog();

                if (result == DialogResult.OK)
                {
                    inputImageName = openFileDialog1.FileName;
                    inputImage = new Image<Bgr, byte>(inputImageName);
                    inputImageName = Regex.Match(openFileDialog1.FileName,
                        @"\\([^\\]+)\.(png|jpg)").ToString()[..^4];
                    pictureBox1.Image = inputImage.ToBitmap();
                    signatureCoordinatesPath = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/AllCoordinates/{inputImageName}.txt";
                    //signaturePath = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/{inputImageName}.png";
                }
                else
                {
                    MessageBox.Show("No file selected", "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            catch (Exception exception)
            {
                MessageBox.Show(exception.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        public static VectorOfVectorOfPoint MuralsGetCountors(Image<Gray, byte> image)
        {
            VectorOfVectorOfPoint contours = new VectorOfVectorOfPoint();
            var hierarchy = new UMat();
            CvInvoke.FindContours(image, contours, hierarchy,
                Emgu.CV.CvEnum.RetrType.Tree, Emgu.CV.CvEnum.ChainApproxMethod.ChainApproxSimple);

            return contours;
        }

        private void findContoursToolStripMenuItem_Click(object sender, EventArgs e)
        {
            ClearAllBoxes();
            try
            {
                Image<Gray, byte> outputImage =
                    inputImage.SmoothGaussian(5).Convert<Gray, byte>().ThresholdBinaryInv(new Gray(230), new Gray(255));

                VectorOfVectorOfPoint contours = MuralsGetCountors(outputImage);

                Array points = contours.ToArrayOfArray();

                var totalPoints = 0;
                var outputString = new StreamWriter(signatureCoordinatesPath);

                foreach (Point[] pointCoordinate in points)
                {
	                totalPoints++;
					if (totalPoints > 4)
	                {
		                foreach (Point point in pointCoordinate)
		                {
			                listBox1.Items.Add(point);
			                outputString.WriteLine(point.X.ToString() + ", " + point.Y.ToString());
			                //totalPoints++;
						}
                        //continue;
					}
					//totalPoints++;
				}

                outputString.Close();
                textBox1.Text = (totalPoints - 4).ToString();

                if (checkBox1.Checked)
                {
                    Image<Gray, byte> blackBackground = new Image<Gray, byte>(inputImage.Width, inputImage.Height, new Gray(0));

                    CvInvoke.DrawContours(inputImage, contours, -1, new MCvScalar(0, 0, 255));

                    pictureBox2.Image = blackBackground.ToBitmap();

                }
                else
                {
                    CvInvoke.DrawContours(inputImage, contours, -1, new MCvScalar(74, 144, 226));

                    pictureBox2.Image = inputImage.ToBitmap();
                }
            }
            catch (Exception exception)
            {
                MessageBox.Show(exception.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        public void SearchAndCropByRectangle(Image<Gray, byte> outputImage)
        {
            VectorOfVectorOfPoint shapesContours = new VectorOfVectorOfPoint();
            var hierarchy = new UMat();
            CvInvoke.FindContours(outputImage, shapesContours, hierarchy,
                Emgu.CV.CvEnum.RetrType.External, Emgu.CV.CvEnum.ChainApproxMethod.ChainApproxSimple);
            //var outputString = new StreamWriter($"C:/Users/Кирилл/source/repos/TrialSignaturesWF/123.txt");

			for (int i = 0; i < shapesContours.Size; i++)
            {
                double perimeter = CvInvoke.ArcLength(shapesContours[i], true);

                if (perimeter < minRectanglePerimeter) 
	                continue;

                var approximation = new VectorOfPoint();

                CvInvoke.ApproxPolyDP(shapesContours[i], approximation, partOfPerimeterEpsilon * perimeter, true);

				//CvInvoke.DrawContours(inputImage, shapesContours, i,
				//    new MCvScalar(0, 0, 255), 2);

				//pictureBox3.Image = inputImage.ToBitmap();

				//Moments moments = CvInvoke.Moments(shapesContours[i]);

				//int x = (int)(moments.M10 / moments.M00);

				//int y = (int)(moments.M01 / moments.M00);
				

				if (approximation.Size >= 4 && approximation.Size <= 8 && CvInvoke.IsContourConvex(approximation))
                {

                    //            var stringHelper = "";
                    List<int> xPoInts = new List<int>();
                    List<int> yPoInts = new List<int>();
                    foreach (Point point in approximation.ToArray())
                    {
                        yPoInts.Add(point.Y);
                        xPoInts.Add(point.X);
                    }
                    //               outputString.WriteLine(stringHelper);

                    Rectangle rectangleTest = new Rectangle(xPoInts.Min() + 2, 
															yPoInts.Min() + 5, 
															xPoInts.Max() - xPoInts.Min() - 2,
															yPoInts.Max() - yPoInts.Min() - 2);
					Rectangle rectangle = CvInvoke.BoundingRectangle(approximation);
					//Rectangle rectangle = new Rectangle(xPoInts.Min() + 10, 
														//yPoInts.Min() + 10, 
														//xPoInts.Max() - xPoInts.Min() + 1, 
														//yPoInts.Max() - yPoInts.Min() + 1);
	                
					UMat croppedUmat = new UMat(inputImage.ToUMat(), rectangleTest);
                    croppedUmat.ToBitmap().Save(signaturePath);
                }
            }
            //outputString.Close();
		}

    }
}