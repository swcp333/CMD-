# CMD下的彩色动画（Python）

可以直接把视频转换成CMD里的字符画，其实就是调用系统的api，实现指定位置输出字符。

---

![效果图](image1.jpg)

通过添加不同字符，颜色稍微多了点……

![效果图](image2.jpg)

最后可以完成一个小动画，[测试效果](http://www.bilibili.com/video/av8544788/)：

get image  --------------  利用ffmpeg获取视频截图

image to data  ----------  求余弦距离，匹配最符合的控制台颜色，保存到文件

data to diffdata  -------  逐帧比较画面差异，只保存差异，用于输出
