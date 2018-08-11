from youtube_dl import YoutubeDL

# # 1: Download a single youtube video
# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=YkubSLmyBnc'])

# 2: Download multiple youtube video
# dl = YoutubeDL()
# # put lis of song urls in download function to download them, one by one
# dl.download(['https://www.youtube.com/watch?v=KpycAhJv3Q4', 'https://www.youtube.com/watch?v=BnsKLD1PjoU'])

# # 3:  Download audio 
# options = {
#     'format': 'bestaudio/audio'
# }
# dl = YoutubeDL(options)
# dl.download(['https://www.youtube.com/watch?v=bg7RjxsghNY'])

# # 4: Search and then download the first video 
# options = {
#     'default_search': 'ytsearch',
#     'max_downloads': 1
# }
# dl = YoutubeDL(options)
# dl.download(['Đóa Hoa Hồng'])

# 5: Search and then download the first audio   
options = {
    'default_search': 'ytsearch',
    'max_downloads': 1,
    'format': 'bestaudio/audio'
}
dl = YoutubeDL(options)
dl.download(['Yêu đương'])