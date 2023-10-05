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
        private Image<Gray, byte> inputImage = null;

        private string inputImageName = "";

        public Form1()
        {
            InitializeComponent();
        }

        public void ClearAllBoxes()
        {
            textBox1.Clear();
            textBox2.Clear();
            textBox3.Clear();
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
                    inputImage = new Image<Gray, byte>(inputImageName);
                    inputImageName = Regex.Match(openFileDialog1.FileName, 
                        @"\\([^\\]+)\.(png|jpg)").ToString()[..^4];
                    pictureBox1.Image = inputImage.ToBitmap();
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

        public static VectorOfVectorOfPoint GetCountors(Image<Gray, byte> image)
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
                Image<Gray, byte> outputImage = inputImage.Convert<Gray,
                    byte>().ThresholdBinary(new Gray(100), new Gray(255));

                var contours = GetCountors(outputImage);
                Array points = contours.ToArrayOfArray();

                var totalPoints = 0;
                var outputString = new StreamWriter(
                        $"C:/Users/Кирилл/source/repos/TrialSignaturesWF/AllCoordinates/{inputImageName}.txt");
                
                foreach (Point[] pointCoordinate in points)
                {
                    foreach (Point point in pointCoordinate)
                    {
                        if (totalPoints >= 4)
                        {
                            listBox1.Items.Add(point);
                            outputString.WriteLine(point.ToString());
                        }
                        totalPoints++;
                    }
                }
                
                outputString.Close();
                textBox1.Text = (totalPoints - 4).ToString();

                if (checkBox1.Checked)
                {
                    Image<Gray, byte> blackBackground = new Image<Gray, byte>(inputImage.Width, inputImage.Height, new Gray(0));


                    CvInvoke.DrawContours(blackBackground, contours, -1, new MCvScalar(255, 0, 0));

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

        private void listBox1_SelectedIndexChanged(object sender, EventArgs e)
        {
            textBox3.Text = listBox1.SelectedItem.ToString();
        }
    }
}