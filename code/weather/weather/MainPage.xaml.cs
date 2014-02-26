using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Animation;
using System.Windows.Shapes;
using weather.ServiceReference1;
using System.Text.RegularExpressions;

namespace weather
{
    public partial class MainPage : UserControl
    {
        public class pmdata
        {
            public String str1 { get; set; }
            public String str2 { get; set; }
            public String str3 { get; set; }
            public String str4 { get; set; }
            public String str5 { get; set; }
            public String str6 { get; set; }
            public String str7 { get; set; }
            public String str8 { get; set; }
            public String str9 { get; set; }
            public pmdata(List<String> pm)
            {
                str1 = pm[0]; str2 = pm[1]; str3 = pm[2]; str4 = pm[3]; str5 = pm[4]; str6 = pm[5]; str7 = pm[6];
                str8 = pm[7]; str9 = pm[8];
            }
        }
        public MainPage()
        {
            InitializeComponent();
            
        }
        #region 天气
        private void weat_Click(object sender, RoutedEventArgs e)
        {
            ServiceReference1.WeatherServiceClient WSClient = new WeatherServiceClient();
            WSClient.GetWeatherInfoAsync("济南");
            WSClient.GetWeatherInfoCompleted += new EventHandler<GetWeatherInfoCompletedEventArgs>(WSClient_GetWeatherInfoCompleted);
        }

        void WSClient_GetWeatherInfoCompleted(object sender, GetWeatherInfoCompletedEventArgs e)
        {
            Weather weather = e.Result as Weather;
            MessageBox.Show(weather.weatherinfo.weather1);
        }
#endregion
        private void button1_Click(object sender, RoutedEventArgs e)
        {
            ServiceReference1.WeatherServiceClient WSClient = new WeatherServiceClient();
            WSClient.GetAirInfoAsync();
            WSClient.GetAirInfoCompleted += new EventHandler<GetAirInfoCompletedEventArgs>(WSClient_GetAirInfoCompleted);
        }
        
        void WSClient_GetAirInfoCompleted(object sender, GetAirInfoCompletedEventArgs e)
        {
            String source = e.Result;
            source = source.ToUpper();
            String pattern1 = @"<TH>.{3,14}</TH>";
            String pattern2 = @"<TD>.{1,5}</TD>";
            MatchCollection matches1 = Regex.Matches(source, pattern1);
            MatchCollection matches2 = Regex.Matches(source, pattern2);
            char[] ch1 = { '<', '/', 'T', 'H', '>' };
            char[] ch2 = { '<', '/', 'T', 'D', '>' };
            String temp;
            List<String> va1 = new List<string>();
            List<String> va2 = new List<string>();
            List<pmdata> pmdatagrid = new List<pmdata>();
            for (int i = 0; i < matches1.Count; i++)
            {
                temp = matches1[i].Value.Trim(ch1);
                temp=temp.Replace("<BR>", "");
                va1.Add(temp);
            }
            pmdatagrid.Add(new pmdata(va1));
            for (int i = 0; i < matches2.Count; i++)
            {
                va2.Add(matches2[i].Value.Trim(ch2));
                if(i==8||i%9==8)
                {
                    pmdatagrid.Add(new pmdata(va2));
                    va2.Clear();
                }
            }
            dataGrid1.ItemsSource = pmdatagrid;
        }
    }
}
