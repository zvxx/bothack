<?php
ob_start();
$API_KEY = "5738204033:AAH9mcP6Sw2JOORSmc1bo6UsTvonAbBc1N4";
define('API_KEY',$API_KEY);
function bot($method,$datas=[]){
    $ABoWaTaN = http_build_query($datas);
        $url = "https://api.telegram.org/bot".API_KEY."/".$method."?$ABoWaTaN";
        $ABoWaTaN_Sy = file_get_contents($url);
        return json_decode($ABoWaTaN_Sy);
}
$update = json_decode(file_get_contents('php://input'));
$message = $update->message;
$text = $message->text;
$number = explode(':', $text)[0];
$exp = explode(':', $text)[1];
$fille= 'proxy.txt'; // پروکسی;
$chat_id = $message->chat->id;
$name = $message->from->first_name;
$from_id = $message->from->id;
$ch = "u_e_k"; // بدون @ ;
$join = file_get_contents("https://api.telegram.org/bot".API_KEY."/getChatMember?chat_id=@$ch&user_id=".$from_id);
if($message && (strpos($join,'"status":"left"') or strpos($join,'"Bad Request: USER_ID_INVALID"') or strpos($join,'"status":"kicked"'))!== false){
bot('SendMessage',[
'chat_id'=>$chat_id,
'text'=>"
📡┇ هـذه قـناة البـوت :-
@$ch

🖲┇ اࢪسـل عـندما تـشـترك فـي الـقناة { /start }",
]);return false;}
if ($text == '/start') {
bot('sendMessage',[
'chat_id'=>$chat_id,
'text'=>"⋘──────━𓆩𝐋 𝐄 𝐕 𝐈𓆪‏━──────⋙\n❖ - **𝚆𝚎𝚕𝚌𝚘𝚖𝚎 𝚝𝚘 𝚊 𝚋𝚘𝚝 𝚝𝚑𝚊𝚝 𝚏𝚘𝚕𝚕𝚘𝚠𝚜 𝙸𝚗𝚜𝚝𝚊𝚐𝚛𝚊𝚖 𝚟𝚒𝚊 𝚝𝚑𝚎 𝙸𝙳 𝚂𝚎𝚗𝚍 𝚝𝚑𝚎 𝙸𝙳 𝚕𝚒𝚔𝚎 𝚝𝚑𝚒𝚜 .\n𝚃𝚊𝚐𝚎𝚝 𝙸𝙳:𝚈𝚘𝚞𝚛𝙸𝙳\n\n❖ - اهـلا بـك فـي بـوت ࢪشـق انـسـتا عـن طـࢪيق الايـدي اࢪسـل الايدي هـكذا .\nايـديـك:ايـدي الـضـحيه** \n⋘──────━𓆩𝐋 𝐄 𝐕 𝐈𓆪‏━──────⋙
",
'disable_web_page_preview'=>'true',
'parse_mode'=>'Markdown',
]);}
if($text != "/start" ){
  
 function RandomNumber($length){
    $str="";
    for($i=0;$i<$length;$i++){
    $str.=mt_rand(0,9);
    }
    return $str;
    }
    
    
    function rando($length) {
        $characters = '1234567890abcdefghijklmnopqrstuvwxyz';
        $charactersLength = strlen($characters);
        $randomString = '';
        for ($i = 0; $i < $length; $i++) {
            $randomString .= $characters[rand(0, $charactersLength - 1)];
        }
        return $randomString;
    }



  $x16=rando(16);
$x40=rando(40);

$ts=time();
$f = array("sameer","suresh","chettiar","jatin","chauhan","agarwal","rahul","tanmay","tiwari","kunal","rasania","sunil","kumar","gaurav","arihant","jain","falguni","yashashree","arpi","arshish","gupta","tanmay","samtgr","kiyera","atul","abhay","chandra","shoibaakriti","aanchal","talreja","aatholiy","abhijeet","akkalwar","abhijeet","bajpai","abhijeetsh","abhirup","roy","abhishek","sumit","kapil","suman","rani","ramu","souvik","yogesh","umesh","sahadat","ankit","prasant","pravakar","sunil","sibaram");
$fname = $f[mt_rand(0,50)];
$l = array("sameer","suresh","chettiar","jatin","chauhan","agarwal","rahul","tanmay","tiwari","kunal","rasania","sunil","kumar","gaurav","arihant","jain","falguni","yashashree","arpi","arshish","gupta","tanmay","samtgr","kiyera","atul","abhay","chandra","shoibaakriti","aanchal","talreja","aatholiy","abhijeet","akkalwar","abhijeet","bajpai","abhijeetsh","abhirup","roy","abhishek","sumit","kapil","rani","ramu","souvik","yogesh","umesh","sahadat","ankit","prasant","pravakar","sunil","sibaram");
$lname = $l[mt_rand(0,50)];
$no = rand(1,999);
$name=''.$fname.''.$lname.''.$no.'';


$url1='https://instaup.marsapi.com/get_likes/user/coins';



$data0='market=Bazaar&user_id='.$number.'&iad='.$x40.'&user_name='.$name;

$a1 = RandomNumber(2);
$a2 = RandomNumber(2);
$a3 = RandomNumber(2);
$a4 = RandomNumber(2);
$ipz = $a1.'.'.$a2.'.'.$a3.'.'.$a4;


$access=md5('45:8D:2E:5C:3A:B4:02:2D:B5:DD:3B:E0:98:4F:14:90:CB:5F:B5:45'.$number);


$headers1=['Xiaomi:29:M2007J20CI',
'access: '.$access,
'lng: en',
'cnt:in',
'versionName:17.0.1',
'version:90',
'pkg:f2c6d7a5b030a1542f7eb589d5013340',
'enMarket:EnglishWebPayment',
'market:PlayStore',
'uid:'.$number,
'api_key: ABCXYZ123TEST',
'crc:4653145854/23927768',
"Nagent:0/02:00:00:00:00:00/48/de2b83032671b409/0/de7d6788fcf061b1341cf0661af36fe35ec72647",
'dsl:36f9a8e7',
'aid:de7d6788fcf061b1341cf0661af36fe35ec72647',
'special-user:1',
'Host:instaup.marsapi.com',
'Connection:Keep-Alive',
'Accept-Encoding:gzip',
'cookie:  token=57759904674%3A9dZVITowT1CnJT%3A20%3AAYcAgyCFPo_h0n5ALf_SRnyhB1cTevgHQ7u0BPyoXA',];
$fiile = fopen($fille, 'r');
$proy = explode("\n", fgets($fiile))[0];
$proxy = explode(':', $proy);


	$ch = curl_init();
	curl_setopt($ch, CURLOPT_URL,$url1);
	curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
    curl_setopt($ch, CURLOPT_POST, 1);
  curl_setopt($ch, CURLOPT_PROXY, $proxy[0]);
  curl_setopt($ch, CURLOPT_PROXYPORT, $proxy[1]);
    curl_setopt($ch, CURLOPT_POSTFIELDS,$data0);
	   curl_setopt($ch, CURLOPT_HTTPHEADER,$headers1);
	curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
  curl_setopt($ch, CURLOPT_ENCODING, 'gzip');
	$output1= curl_exec ($ch);
	
	curl_close ($ch);
  
   $json1=json_decode($output1,true);
  $c1=$json1['coins'];
  $c2=$json1['message'];
  $d1 = $c1 / 4;
  $d2 = explode(".",$d1)['0'];
      $url0="https://instaup.marsapi.com/get_likes/order/follow";
  $idx=$number+3423;
  $d=$idx.'ig';

$i='3rFz>|)VHl-w+5I0';

if($d2 > 100000){
$d2 = '100000';
} else {
$d2 = $d2;
}

  $k='#p0yJmVK/@($nX?#';
$enc_data = base64_encode(openssl_encrypt($d,"AES-128-CBC",$k,OPENSSL_RAW_DATA,$i));
$tkv=md5($enc_data.':M3JGej58KVZIbC13KzVJMA==');





$dx=urlencode($dx);


$ll='https%3A%5C%2F%5C%2Finstagram.fccu3-1.fna.fbcdn.net%5C%2Fv%5C%2Ft51.2885-15%5C%2Fe35%5C%2Fs150x150%5C%2F264420143_435496831548995_8076441957316773167_n.jpg%3F_nc_ht%3Dinstagram.fccu3-1.fna.fbcdn.net%26_nc_cat%3D111%26_nc_ohc%3DvWrY6qsKOOAAX9ZgJLH%26edm%3DAPU89FABAAAA%26ccb%3D7-4%26oh%3D00_AT_GHVnpr10j1bCs8Dx5unohvTyp_1DgOtu8It7P_Nmpfw%26oe%3D61B616B1%26_nc_sid%3D86f79a';

 $data0='gift=0&order_count='.$d2.'&user_id='.$number.'&tokenV2='.$tkv.'&start_value=1700&media_url=%7B%22media_url%22%3A%22'.$ll.'%22%2C%22user_name%22%3A%22'.$fname.'%22%7D&order_id='.$exp;

 $ch = curl_init();
 curl_setopt($ch, CURLOPT_URL,$url0);
 curl_setopt($ch, CURLOPT_POST, 1);
 curl_setopt($ch, CURLOPT_POSTFIELDS,$data0);
 curl_setopt($ch, CURLOPT_PROXY, $proxy[0]);
 curl_setopt($ch, CURLOPT_PROXYPORT, $proxy[1]);
 curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
 curl_setopt($ch, CURLOPT_HTTPHEADER,$headers1);
 curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);
 curl_setopt($ch, CURLOPT_ENCODING, 'gzip');
  $cc= curl_exec ($ch);
 curl_close ($ch);
    $jsonn=json_decode($cc,true);
   $c=$jsonn['status'];
    if($c == 'Error'  && $c2 == 'Your account suspended due to unfollowing. If you think there is a mistake, call us at instaup.developers@gmail.com.'){
    $current = file_get_contents($fille);
    file_put_contents($fille, $current);
    $lines = file($fille);
    unset($lines[0]);
    file_put_contents($fille, implode('', $lines));
    bot('SendMessage',[
'chat_id'=>$chat_id,
'text'=>"تـم حـضـࢪ الـموقـع يـتم الان اسـتـبدال بـࢪوكـسي جـديـد",
'reply_to_message_id'=>$update->message->message_id,
]);
}elseif($c == 'Error'){
bot('SendMessage',[
'chat_id'=>$chat_id,
'text'=>"$output1==>$cc",
'reply_to_message_id'=>$update->message->message_id,
]);
}elseif($c == 'Successful'){
bot('SendMessage',[
'chat_id'=>$chat_id,
'text'=>"DONE ✅\n\nCOINS : $output1\nMESSAGE : مـتابـع $d2 تـم طـلـب الـࢪشـق\n\nBY : @u_r_r",
'reply_to_message_id'=>$update->message->message_id,
]);
}else {
$current = file_get_contents($fille);
file_put_contents($fille, $current);
$lines = file($fille);
unset($lines[0]);
file_put_contents($fille, implode('', $lines));
bot('SendMessage',[
'chat_id'=>$chat_id,
'text'=>"البـࢪوكـسـي ضـعيف يتـم تـغيره الان",
'reply_to_message_id'=>$update->message->message_id,
]);
}
}
