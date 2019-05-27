<!DOCTYPE html><html><head>  <title>抖音短视频</title><meta charset="utf-8"><meta http-equiv="Cache-Control" content="no-transform"><meta http-equiv="Cache-Control" content="no-siteapp">  <meta name="baidu-site-verification" content="szjdG38sKy"><meta name="keywords" content="抖音、抖音音乐、抖音短视频、抖音官网、amemv"><meta name="description" content="抖音短视频，一个旨在帮助大众用户表达自我，记录美好生活的短视频分享平台。应用人工智能技术为用户创造丰富多样的玩法，让用户在生活中轻松快速产出优质短视频。">  <link rel="shortcut icon" href="//s3.bytecdn.cn/aweme/resource/web/static/image/logo/favicon_v2_7145ff0.ico" type="image/x-icon"><meta http-equiv="X-UA-Compatible" content="IE=Edge;chrome=1"><link rel="dns-prefetch" href="//s3.bytecdn.cn/"><link rel="dns-prefetch" href="//s3a.bytecdn.cn/"><link rel="dns-prefetch" href="//s3b.bytecdn.cn/"><link rel="dns-prefetch" href="//s0.pstatp.com/"><link rel="dns-prefetch" href="//s1.pstatp.com/"><link rel="dns-prefetch" href="//s2.pstatp.com/">  <meta property="og:image" content="https://p9.pstatp.com/large/204140002e8f0f7185d49.jpg">  <link rel="stylesheet" href="//s3.bytecdn.cn/aweme/resource/web/static/style/base_4a834a9.css">  <link rel="stylesheet" href="//s3a.bytecdn.cn/aweme/resource/web/pkg/page/reflow_video_08b0f3a.css" />  <!--[if IE]><script src="//s3a.bytecdn.cn/aweme/resource/web/static/script/lib/fix-ie8_e8a0650.js"></script><![endif]--><script src="//s3.bytecdn.cn/aweme/resource/web/static/script/lib/core_1f49c51.js"></script>  <script src="//s3.bytecdn.cn/aweme/resource/web/static/script/lib/raven_8c2f9e8.js"></script>   <script>window.PAGEVIEW_NAME = '/share/video';</script>  <script>// BA全局变量
var baAccount = window.AME_BA_ID || 'fe557d1f75199e';
var baevent = function(){};

(function(){
    var sampleRate = 100; // 采样比例，即上报量占总流量的百分比

    !function (t, e, a, n, s, c){t.ToutiaoAnalyticsObject = s, t[s] = t[s] || function (){
    (t[s].q = t[s].q || []).push(arguments)}, t[s].t = 1 * new Date, t[s].s = c;var i = e.createElement(a);
    i.async = 1, i.src = n, e.getElementsByTagName("head")[0].appendChild(i)
    }(window, document, "script", "//s3.bytecdn.cn/ta/resource/v0/analytics.js", "ba");

    ba('create', baAccount, {'sampleRate': sampleRate});
    ba('send', 'pageview');

    baevent = function(category, action, label, value){
        console.log("ba:"+category+","+action+","+label);
        if(category != 'event') {
            ba('send', 'event', category, action, label, typeof value !== 'undefined' ? value: 1);
        }
    };
})();</script> <script>var gaAccount = window.AME_GA_ID || 'UA-75850242-4';

var _gaq = _gaq || [];
var gaqpush=function(){};
var gaevent=function(){};
var gapageview=function(){};
var trackPV = gapageview;

var sampleRate = 20;

function initGA(){

    if(sampleRate && gaAccount){
        window.onerror = function(message, file, line) {
            var msg = message,
                f = file,
                l = line;
            if(typeof message === 'object') {
                msg = message.message;
                f = message.fileName;
                l = message.lineNumber;
            }
            var sFormattedMessage = '[' + f + ' (' + l + ')]' + msg;
            window.gaevent ? gaevent('Exceptions', sFormattedMessage, location.pathname + '::::' + navigator.userAgent) : '';
        };

        var test_channel = "",
            test_version = "",
            utm_source = "";

        // var ua = navigator.userAgent;

        (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
            (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
            m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
        })(window,document,'script','//www.google-analytics.com/analytics.js','ga');

        // Replace with your property ID.
        ga('create', gaAccount, {'sampleRate': sampleRate});


        //Init GA Function
        gapageview = function(pageName) {
            ga('send', 'pageview', pageName);
            console.log('ga:pageview', pageName);
        };

        gaqpush = function(ga_event, ga_label){
            gaevent('event',ga_event,ga_label);
        };

        gaevent = function(category, action, label, value){
            if(test_channel.indexOf(action) >-1) label = label+test_version;
            console.log("ga:"+category+","+action+","+label);
            if(category != 'event') {
                ga('send', 'event', category, action, label, typeof value !== "undefined" ? value: 1);
            }
            if(typeof window.baevent == "function") {
                baevent(category, action, label, value);
            }
        };

        gapageview(window.PAGEVIEW_NAME);

        $("html").on('click', '[ga_event]', function(e){
            var $this =  $(this);
            var ga_category = $this.attr('ga_category') || 'event';
            var ga_event = $this.attr('ga_event');
            var ga_label = $this.attr('ga_label');
            gaevent(ga_category,ga_event,ga_label);
            if($this.is('a')){
                var href = $this.attr('href')||'', target = this.target;
                if(!( href[0]==='#' || target === "_blank" || e.isDefaultPrevented())) {
                    setTimeout(function(){
                        location.href = href
                    },400);
                    return false
                }
            }
        });
    }
}

initGA();</script> </head><body>   <header class="header"><div class="container"><div class="logo-warpper"><a class="logo" href="/"></a></div><div class="name-warpper"><a class="app-name" href="/">抖音</a> <a class="app-slogen" href="/">| 记录美好生活</a></div>  </div></header>  <div class="main-content-block">  <div id="pageletReflowVideo"> <div class="detail clrfix ">  <div class="video-box fl">  <div class="video-player" data-node="player" style="background-image:url(https://p9.pstatp.com/large/204140002e8f0f7185d49.jpg)"><div class="play-btn"></div></div>  </div>  <div class="info-box fl"><div class="download"><p class="title text-center">【扫码下载抖音，观看更多有趣视频】</p><div class="qrcode"><img src="//s3a.bytecdn.cn/aweme/resource/web/static/image/qrcode_ccd70da.png" alt="抖音"></div></div><div class="video-info">  <div class="user-info clrfix"><div class="avatar fl"><img src="https://p9-dy.bytecdn.cn/aweme/100x100/1b54a0005b44c41f3dd17.jpeg" alt="张家界途亚旅游咨询"></div><div class="info"><p class="name nowrap">@张家界途亚旅游咨询</p></div></div>    <div class="challenge-info"><p class="name"><span class="inner">抖音张家界</span></p></div>    <p class="desc">大山里的天梯。#抖音张家界</p>  </div></div>  <div class="not-found hide"><p class="tips text-center">视频找不到了，看看其他精彩作品吧！</p><div class="download"><p class="title text-center">【扫码下载抖音，观看更多有趣视频】</p><div class="qrcode"><img src="//s3a.bytecdn.cn/aweme/resource/web/static/image/qrcode_ccd70da.png" alt="抖音"></div></div></div></div> </div><script src="//s3.bytecdn.cn/aweme/resource/web/pkg/page/reflow_video_3672eb2.js"></script>
<script type="text/javascript">
(function() {
    $(function() {
        if (~location.hostname.indexOf('iesdouyin')) {
            $('.gognan-box').remove();
        }
        console.log('xxx');
        $('#copyYear').text((new Date).getFullYear());
    })
})();
</script>
<script>$(function(){
            require('web:component/reflow_video/index').create({
                hasData: 1,
                videoWidth: 720,
                videoHeight: 1280,
                playAddr: "https://aweme.snssdk.com/aweme/v1/playwm/?video_id=v0200f830000bj4mvhgnrm1veueti230&line=0",
                cover: "https://p9.pstatp.com/large/204140002e8f0f7185d49.jpg"

            });
        });
</script>  </div>  <footer class="footer"><div class="container"><div class="infomation"><p><span id="copyYear">2018</span>&nbsp;&copy;&nbsp;抖音&nbsp;&nbsp;|&nbsp;京ICP备16016397号-3&nbsp;|&nbsp;北京微播视界科技有限公司 |&nbsp; 地址&nbsp;:&nbsp;北京市海淀区知春路51号4层408&nbsp;</p><p><a target="_blank" href="http://www.12377.cn/">中国互联网举报中心</a>&nbsp;|&nbsp;网络文化许可证-京网文-（2016）2282-264号&nbsp;|&nbsp;违法和不良信息举报：010-83434212</p><div class="gognan-box"><a target="_blank" href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010802023605"><img src="//s3.bytecdn.cn/aweme/resource/web/static/image/gongan_d0289dc.png"> <span>京公网安备 11010802023605号</span></a></div></div></div></footer>     </body></html>