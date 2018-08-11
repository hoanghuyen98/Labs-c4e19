from gmail import GMail
from gmail import Message
from random import choice

html_content = """<p style="padding-left: 150px;">C&ocirc;̣ng hòa xã h&ocirc;̣i chủ nghĩa Vi&ecirc;̣t Nam</p>
<p style="padding-left: 180px;">Đ&ocirc;̣c l&acirc;̣p - Tự do - Hạnh phúc</p>
<p style="padding-left: 180px;"><strong>Đơn Xin Nghỉ Học</strong></p>
<p style="padding-left: 30px;">Kính gửi : Boss đã dìu dắt chúng em trong thời gian qua.</p>
<p style="padding-left: 30px;">Em t&ecirc;n là Hoàng Thanh Huy&ecirc;̀n, lý do em vi&ecirc;́t đơn này ,{{sickness}}</p>"""

reason = [' Mẹ em bảo gà nhà em mới chết nên phải ở nhà ăn canh gà', ' Boss ơi! Ngày mai em sốt',' Phải nghỉ học ở nhà chăm con Talking Tom']
rand = choice(reason)
html_to_send = html_content.replace("{{sickness}}", rand)
gmail = GMail('hoangthanhhuyenhbh2016@gmail.com', 'Huyen123')
msg = Message(  'test gmail',
                to = '20130075@student.hust.edu.vn', 
                html = html_to_send)
gmail.send(msg)