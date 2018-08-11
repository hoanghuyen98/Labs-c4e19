from pymongo import MongoClient

# Connect to our class’s Mongo Database with this URI:
uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

# connect to database 
client = MongoClient(uri)

# get database
db = client.get_default_database()

# create collection
posts = db['posts']


# create document
new_posts = {
    "title" : " Đôi lời gửi tới anh trợ giảng =)) ",
    "author" : "HTH",
    "content" : """
    Anh #Q :))) 
    - Nhìn anh cũng tàm tạm, sắc đẹp của anh chỉ tầm trung ( :v hê ), nhưng mà đẹp trai kiểu dâm dâm
    - Là một người nhiệt tình 
    - Dễ gần , vui tính nhưng dự là ai càng thân với anh thì tai của họ hơi mệt 
    - Là người dễ nói chuyện, dễ troll mà ko sợ mất lòng :3 
    - Nói thế nào nhể ! Anh có chút "thông minh" mặt anh toát lên điều ấy =)) ( Ý em là anh nhìn rất thông minh , nhanh nhẹn =)) hihi) 
    - Em thề là nhìn anh giống em béc dê nhà em ở điểm nhìn thì dữ nhưng mà hiền 
    - ........... vân vân .............
    - Nhìn chung hình tượng của anh đối với em là 1 người không bình thường
    Nghĩ ra em sẽ nói tiếp. chưa kết.* chấm phẩy *
    """
}



# Insert doc into collection
posts.insert_one(new_posts)

