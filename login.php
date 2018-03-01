<?php
//<meta http-equiv="content-type" content="text/html"; charset="utf-8">
//用户登录并建立cookie

$Button = $_POST["Button"];
if($Button == "Submit")
{
  $s_level = $_POST["s_level"];
  $l_eva = $_POST["l_eva"];
  $num_pro = $_POST["num_of_pro"];
  $work_hours = $_POST["work_hours"];
  $time_spent = $_POST["time_spent"];
  $work_acc = $_POST["work_acc"];
  
  $slry= $_POST["slry"];
  $dpt = $_POST["dpt"];
  $promotion = $_POST["promotion"];
   
   /*switch ($dpt)
{
case 'sales':
  code to be executed if expression = label1;
  break;  
case label2:
  code to be executed if expression = label2;
  break;
default:
  code to be executed
  if expression is different 
  from both label1 and label2;
}*/


//'sales':1,'accounting':2,'hr':3,'technical':4,
//'support':5,'management':6,'IT':7,'product_mng':8,'marketing':9,'RandD':10},inplace=True) 
//'satisfaction_level','average_montly_hours','promotion_last_5years','salary','number_project'

  if($dpt=='Sales')
    {
      $dpt1=1;
    }
    else if($dpt=='accounting')
    {
      $dpt1=2;
    }
    else if($dpt=='hr')
    {
      $dpt1=3;
    }
    else if($dpt=='tec')
    {
      $dpt1=4;
    }
    else if($dpt=='support')
    {
      $dpt1=5;
    }
    else if($dpt=='mng')
    {
      $dpt1=6;
    }
    else if($dpt=='IT')
    {
      $dpt1=7;
    }
    else if($dpt=='pro_mng')
    {
      $dpt1=8;
    }
    else if($dpt=='markerting')
    {
      $dpt1=9;
    }
    else
    {
      $dpt1=10;
    }


  
if($slry=='low')
  {
    $a="1";
    
  }
  if($slry=='medium')
  {
    $a="2";

  }
  if($slry=='high')
  {
    $a="3";
  }


  if($promotion=='Yes')
  {
    $b="1";
    
  }
  else
    {$b="0";}


  if($work_acc=='Yes')
  {
    $c="1";
    
  }
  else
    {$c="0";}
 
    exec("python projectFinal2.py $s_level $l_eva $num_pro $work_hours $time_spent $c $b $dpt1 $a",$result,$status);
 

    //exec("python test.py 2 2 2 2 2 2 2 2 2",$result,$status);
    //exec("python test.py $s_level $l_eva $num_pro $work_hours $time_spent $work_acc $promotion $dpt1 $a",$result,$status);
    //exec("python projectFinal1.py 2 2 2 2 2 2 2 2 2",$result,$status);
    //exec("python test.py $s_level $work_hours $promotion $a $num_pro",$result,$status);

   // echo "get here";
    //$txt=“lllll”;
    //print_r($result);
    //print_r(count($result));

    //print_r($result[264]);
   //if($result[264]==1)
    //print_r("OK!");

    //$salary=array(1,0,0);
    //print_r(count($result));
    //echo $result[0];
    //echo "<script>alert($result);history.back();</script>"
}//if

?>
<html>
<head>
<link href="css/bootstrap.css" type="text/css" rel="stylesheet" media="all">
<link href="css/style.css" type="text/css" rel="stylesheet" media="all">
<link rel="stylesheet" href="css/lightbox.css">
<!-- Custom Theme files -->
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<meta name="keywords" content="Collective Responsive web template, Bootstrap Web Templates, Flat Web Templates, Android Compatible web template, 
  Smartphone Compatible web template, free webdesigns for Nokia, Samsung, LG, SonyEricsson, Motorola web design" />
<script type="application/x-javascript"> addEventListener("load", function() { setTimeout(hideURLbar, 0); }, false); function hideURLbar(){ window.scrollTo(0,1); } </script>
<!-- //Custom Theme files -->
<!-- js -->
<script src="js/jquery-1.11.1.min.js"></script> 
<!-- //js --> 
<!--animate-->
<link href="css/animate.css" rel="stylesheet" type="text/css" media="all">
<script src="js/wow.min.js"></script>
  <script>
     new WOW().init();
  </script>
<!--//end-animate-->
<!-- image-hover -->
<script type="text/javascript" src="js/mootools-yui-compressed.js"></script>
<!-- //image-hover -->
<link href='http://fonts.useso.com/css?family=Open+Sans:400,300,300italic,400italic,600,600italic,700,700italic,800,800italic' rel='stylesheet' type='text/css'>
</head>


<body>
<div style="text-align:center">STAFF PREDICTION</div>
<div class="header">
    <div class="container">
      <div class="header-info navbar-left wow fadeInLeft animated" data-wow-delay=".5s" style="visibility: visible; -webkit-animation-delay: .5s;">
        <p><span class="glyphicon glyphicon-earphone" aria-hidden="true"></span>Contact :1-xxxxxxxxx</p>
      </div>        
      <div   class="header-info navbar-right wow fadeInRight animated" data-wow-delay=".5s" style="visibility: visible; -webkit-animation-delay: .5s;">
          <p>Staff Prediction System</p>
        </div> 
    </div>  
  </div>

<div align="center">
<h1>Staff Prediction System</h1>
</div>




<div id="contact" class="contact-form pt-section">
    <div class="container">
      
      <div class="col-md-7 contact-right wow fadeInLeft animated" data-wow-delay=".5s" style="visibility: visible; -webkit-animation-delay: .5s;">        
        <form id="myform" method="post" action="index.php"  align="left">
        <table>
        <tr>
        <p align="left" height="10px"  width="35px" type="text"> The prediction is :</p>
        </tr>

       <tr>
        <p align="left" height="10px"  width="35px" type="text"> 


        <?php
  
 if($result[14]=="1")
 {
   
    

  echo "Left";
   
 }
 else
  echo "Stay";

  
  ?> 

 

        </tr>
        <tr>
        <p align="left" height="10px"  width="35px" type="text"> 
   <?php
    echo $result[13];

     ?> 
     </tr>

      
  
        <br>
        
        </table>

        
          <div>
          <input type="submit"id="Button1" value="Back" name="Button">
          
          </div>
        </form>
        
      </div>
      <div class="col-md-5 contact-left wow fadeInRight animated" data-wow-delay=".5s" style="visibility: visible; -webkit-animation-delay: .5s;">
        <p><span class="glyphicon glyphicon-warning"aria-hidden="true"></span>Only For HR!</p>
        <ul>
          <li><span class="glyphicon glyphicon-envelope" aria-hidden="true"></span>mail@example.com</li>
          <li><span class="glyphicon glyphicon-earphone" aria-hidden="true"></span>+8</li>
        </ul>
      </div>            
      <div class="clearfix"> </div>
    </div>    
</div>      
  
<div>
  




</div>








</body>
</html>
<br>
<script src="js/responsiveslides.min.js"></script>
     <script>
      // You can also use "$(window).load(function() {"
        $(function () {
        // Slideshow 3
          $("#slider3").responsiveSlides({
          auto: true,
          pager:true,
          nav:true,
          speed: 500,
          namespace: "callbacks",
          before: function () {
          $('.events').append("<li>before event fired.</li>");
          },
          after: function () {
            $('.events').append("<li>after event fired.</li>");
          }
        }); 
      });
    </script>
    <!--//End-slider-script -->
    <!-- start-smoth-scrolling-->
    <script type="text/javascript" src="js/move-top.js"></script>
    <script type="text/javascript" src="js/easing.js"></script> 
    <script type="text/javascript">
        jQuery(document).ready(function($) {
          $(".scroll").click(function(event){   
            event.preventDefault();
            $('html,body').animate({scrollTop:$(this.hash).offset().top},1000);
          });
        });
    </script>
    <!--//end-smoth-scrolling-->
    <!--smooth-scrolling-of-move-up-->
    <script type="text/javascript">
      $(document).ready(function() {
        /*
        var defaults = {
          containerID: 'toTop', // fading element id
          containerHoverID: 'toTopHover', // fading element hover id
          scrollSpeed: 1200,
          easingType: 'linear' 
        };
        */
        
        $().UItoTop({ easingType: 'easeOutQuart' });
        
      });
    </script>
    
    <a href="#" id="toTop" style="display: block;"> <span id="toTopHover" style="opacity: 1;"> </span></a>
    <!--//smooth-scrolling-of-move-up-->
  <!-- Bootstrap core JavaScript
    ================================================== -->
    <!-- Placed at the end of the document so the pages load faster -->
    <script src="js/bootstrap.js"> </script>