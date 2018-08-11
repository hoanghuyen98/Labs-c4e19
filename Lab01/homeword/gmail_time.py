from gmail import GMail, Message
from random import choice
from datetime import datetime, time

html_content = """
<p style="text-align: center;">C&ocirc;̣ng hòa xã h&ocirc;̣i chủ nghĩa Vi&ecirc;̣t Nam</p>
<p style="text-align: center;">Đ&ocirc;̣c l&acirc;̣p - Tự do - Hạnh Phúc&nbsp;</p>
<h2 style="text-align: center;"><strong>Đơn Xin Nghỉ Học&nbsp;</strong></h2>
<p style="text-align: left;"><strong>Kính gửi</strong> : Boss - người đã dìu dắt chúg em trong thời gian qua !!&nbsp;</p>
<p style="text-align: left;"><strong>Em t&ecirc;n là</strong> : Hoàng Thanh Huy&ecirc;̀n</p>
<p style="text-align: left;"><strong>Em vi&ecirc;́t đơn này với ly do</strong> :</p>
<p style="text-align: left;">&nbsp; &nbsp; &nbsp; &nbsp;<span style="color: #ff0000;"><em>{{season}} n&ecirc;n em ko đi học được&nbsp;<img src="https://html-online.com/editor/tinymce4_6_5/plugins/emoticons/img/smiley-tongue-out.gif" alt="tongue-out" /><img src="https://html-online.com/editor/tinymce4_6_5/plugins/emoticons/img/smiley-tongue-out.gif" alt="tongue-out" /></em></span></p>
"""

reason = ["Thầy ơi, ngày mai em sốt", "Răng em đau", "Em thất tình", "Thầy ơi,em có triệu chứng tẩu hỏa nhập ma, toàn thân đau nhức, nội công giảm sút", " Gà nhà em chết , nên phải ở nhà ăn canh gà "]
rand = choice(reason)

htmt_to_update = html_content.replace("{{season}}", rand)

gmail = GMail("huyen.techkids@gmail.com", "Huyen123")
msg = Message(" Mail subject ", 
                to = "20130075@student.hust.edu.vn",   
                html = htmt_to_update)



while True:
    now = datetime.now().time().hour
    if now == 7 :
        gmail.send(msg)
        break