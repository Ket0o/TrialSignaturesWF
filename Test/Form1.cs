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

        private static string inputImageName = "";

        public Form1()
        {
            InitializeComponent();
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
                    signaturePath = $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/Podpisi/{inputImageName}.png";
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

                SearchAndCropByRectangle(outputImage);

                VectorOfVectorOfPoint contours = MuralsGetCountors(outputImage);

                Array points = contours.ToArrayOfArray();

                var totalPoints = 0;
                var outputString = new StreamWriter(signatureCoordinatesPath);

                foreach (Point[] pointCoordinate in points)
                {
                    foreach (Point point in pointCoordinate)
                    {
                        listBox1.Items.Add(point);
                        outputString.WriteLine(point.X.ToString() + ", " + point.Y.ToString());
                        totalPoints++;
                    }
                }

                outputString.Close();
                textBox1.Text = totalPoints.ToString();

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

            for (int i = 0; i < shapesContours.Size; i++)
            {
                double perimeter = CvInvoke.ArcLength(shapesContours[i], true);

                var approximation = new VectorOfPoint();

                CvInvoke.ApproxPolyDP(shapesContours[i], approximation, 0.04 * perimeter, true);

                //CvInvoke.DrawContours(inputImage, shapesContours, i,
                //    new MCvScalar(0, 0, 255), 2);

                //pictureBox3.Image = inputImage.ToBitmap();

                //Moments moments = CvInvoke.Moments(shapesContours[i]);

                //int x = (int)(moments.M10 / moments.M00);

                //int y = (int)(moments.M01 / moments.M00);

                if (approximation.Size == 4)
                {
                    var pointsOfSquare = approximation.ToArray();
                    int x = pointsOfSquare[0].X;
                    int y = pointsOfSquare[0].Y;
                    var width = 0;
                    var height = 0;
                    foreach (Point point in approximation.ToArray())
                    {
                        if (point.X != x)
                        {
                            width = Math.Abs(point.X - x) + 1;
                        }
                        if (point.Y != y)
                        {
                            height = Math.Abs(point.Y - y) + 1;
                        }
                    }

                    Rectangle rectangle = new Rectangle(x, y, width, height);
                    UMat croppedUmat = new UMat(inputImage.ToUMat(), rectangle);
                    croppedUmat.ToBitmap().Save(signaturePath);
                }
            }
        }

    }
}