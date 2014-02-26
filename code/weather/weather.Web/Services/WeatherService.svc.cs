using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.Serialization;
using System.ServiceModel;
using System.Text;
using System.Net;
using System.IO;
using System.Web.Script.Serialization;
using System.Xml.Linq;
using System.Web;
using weather.Web.Models;

namespace weather.Web.Services
{
    // 注意: 使用“重构”菜单上的“重命名”命令，可以同时更改代码、svc 和配置文件中的类名“WeatherService”。
    public class WeatherService : IWeatherService
    {
        public void DoWork()
        {
        }
        public Weather GetWeatherInfo(string cityName)
        {
            Weather weather = new Weather();
            weatherinfo weatherInfo = new weatherinfo();
            weather.weatherinfo = weatherInfo;
            weatherInfo.city = "";
            /*string path = AppDomain.CurrentDomain.BaseDirectory + "CityCodeDB.xml";
            XDocument doc = XDocument.Load(path);
            string cityCode = "101230201"; //默认厦门城市代码
            IEnumerable<XAttribute> attributeList = doc.Descendants("City").Attributes().Where(p => p.Value == cityName);
            if (attributeList.Count() != 0)
                cityCode = attributeList.FirstOrDefault().Parent.Value;*/
            string requestUriString = "http://m.weather.com.cn/data/101120101.html";
            HttpWebRequest request = (HttpWebRequest)WebRequest.Create(requestUriString);
            try
            {
                HttpWebResponse response = (HttpWebResponse)request.GetResponse(); //获得响应流
                Stream stream = response.GetResponseStream();
                StreamReader read = new StreamReader(stream, System.Text.Encoding.UTF8);
                JavaScriptSerializer serializer = new JavaScriptSerializer();
                string str = read.ReadToEnd();
                weather = ((Weather)serializer.Deserialize(str, typeof(Weather)));
                stream.Close();
            }
            catch (Exception)
            {

            }

            return weather;
        }
        public String GetAirInfo()
        {
            String source;
            String url = "http://www.pm25.in/jinan";
            Uri uri = new Uri(url);
            WebClient wc = new WebClient();
            wc.Encoding = System.Text.Encoding.UTF8;
            source=wc.DownloadString(uri);
            return source;
        }
    }
}
