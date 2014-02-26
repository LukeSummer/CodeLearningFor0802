using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Runtime.Serialization;

namespace weather.Web.Models
{
    [DataContract]
    public class weatherinfo
    {
        [DataMember]
        public string city { get; set; }

        [DataMember]
        public string date_y { get; set; }

        [DataMember]
        public string tomorrow { get; set; }

        [DataMember]
        public string aftertomorrow { get; set; }

        [DataMember]
        public string week { get; set; }

        [DataMember]
        public string temp1 { get; set; }

        [DataMember]
        public string temp2 { get; set; }

        [DataMember]
        public string temp3 { get; set; }

        [DataMember]
        public string temp4 { get; set; }

        [DataMember]
        public string temp5 { get; set; }

        [DataMember]
        public string temp6 { get; set; }

        [DataMember]
        public string weather1 { get; set; }

        [DataMember]
        public string weather2 { get; set; }

        [DataMember]
        public string weather3 { get; set; }

        [DataMember]
        public string weather4 { get; set; }

        [DataMember]
        public string weather5 { get; set; }

        [DataMember]
        public string weather6 { get; set; }

        [DataMember]
        public string img_title1 { get; set; }

        [DataMember]
        public string img_title2 { get; set; }

        [DataMember]
        public string img_title3 { get; set; }

        [DataMember]
        public string img_title4 { get; set; }

        [DataMember]
        public string img_title5 { get; set; }

        [DataMember]
        public string img_title6 { get; set; }

        [DataMember]
        public string img_title7 { get; set; }

        [DataMember]
        public string img_title8 { get; set; }

        [DataMember]
        public string img_title9 { get; set; }

        [DataMember]
        public string img_title10 { get; set; }

        [DataMember]
        public string img_title11 { get; set; }

        [DataMember]
        public string img_title12 { get; set; }
    }
}