
class MusicPlayer(object):

    instance = None
    init_flag = False

    def __new__(self, *args, **kwargs):
        #print("创建实例对象内存……")
        if MusicPlayer.instance is None: 
            MusicPlayer.instance = super().__new__(self)
        
        return MusicPlayer.instance

    def __init__(self, name):
        if MusicPlayer.init_flag:
            return
        self.name = name
        print("歌曲：【%s】即将播放" % name)
        MusicPlayer.init_flag = True

    def play_song(self):
        print("歌曲：【%s】正在播放中……" % self.name)

def main():
    
    p1 = MusicPlayer("吻别")
    p2 = MusicPlayer("相思风雨中")

    print(p1)
    print(p2)

    p1.play_song()
    p2.play_song()

if __name__ == "__main__":
    main()