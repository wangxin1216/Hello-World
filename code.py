
# coding: utf-8

# In[ ]:

import PIL
from PIL import Image,ImageDraw,ImageFont

class MakeReportTest(object):
    
    def DrawReport(self,image):
        '''输入：白色空白图片
           输出：化验单框架
           只能用PIL显示'''
    
        draw = ImageDraw.Draw(image)

        font = ImageFont.truetype("SIMLI.TTF", 30,index=0,)
        fonts = ImageFont.truetype("simsun.ttc", 20,index=1 )
        draw.text((170, 20), '内蒙古大学', 'black', font,)
        draw.text((210,60),'医务室','black',fonts)
        #
        draw.line((30,100,470,100), 'black')
        #
        font1 = ImageFont.truetype("simsun.ttc", 15)
        draw.text((30,120),'姓名:','black',font1)
        draw.text((140,120),'性别:','black',font1)
        draw.text((260,120),'年龄:','black',font1)
        draw.text((360,120),'ID号:','black',font1)
        # 
        font2 = ImageFont.truetype("simsun.ttc", 15)
        draw.text((30,150),'申请科室:','black',font2)
        draw.text((140,150),'申请医师:','black',font2)
        draw.text((260,150),'检查项目:','black',font2)
        draw.text((360,150),'住院号:','black',font2)
        #
        font3 = ImageFont.truetype("simsun.ttc", 15)
        draw.text((30,180),'临床诊断:','black',font3)
        draw.text((180,180),'检查仪器:','black',font3)
        draw.text((360,180),'检查号:','black',font3)
        draw.line((30,200,470,200), 'black')
        #
        font4 = ImageFont.truetype("simsun.ttc", 15)
        draw.text((30,380),'超声所见:','black',font4)
        draw.text((30,520),'超声提示:','black',font4)
        #
        font5 = ImageFont.truetype("simsun.ttc", 15)
        draw.text((30,620),'报告医师:','black',font5)
        draw.text((340,620),'报告日期:','black',font5)
        draw.line((30,640,470,640), 'black')
        #copy_img.show()
        return image

    def InsertPicture(self,image):
        '''插入检测图'''
        #imgs = Image.open('miao1.jpg')
		imgs = Image.open('test2.jpg')
        box = (150,220,380,370)
        re_imgs = imgs.resize((box[2]-box[0],box[3]-box[1]))
        image.paste(re_imgs,box) 
        return image

    def FillBlank(self,image):
        ''' 填充刚才生成的框架'''
        draw = ImageDraw.Draw(image)
    
        font1 = ImageFont.truetype("SIMLI.TTF", 15)
        draw.text((80,120),'JiaNan','black',font1)
        draw.text((180,120),'boy','black',font1)
        draw.text((300,120),'18','black',font1)
        draw.text((400,120),'123456','black',font1)
        # 
        draw.text((100,150),'a','black',font1)
        draw.text((210,150),'b','black',font1)
        draw.text((330,150),'c','black',font1)
        draw.text((420,150),'d','black',font1)
        #
        draw.text((100,180),'e','black',font1)
        draw.text((250,180),'f','black',font1)
        draw.text((430,180),'g','black',font1)
        #
        draw.text((100,400),'为什么偷看我','black',font1)
        draw.text((100,540),'我没毛病！','black',font1)
        #
        draw.text((100,620),'ShiJie','black',font1)
        draw.text((410,620),'2018.10.15','black',font1)
        #copy_img.show()
        return image   
    
if __name__ == '__main__':
    # 创建一副RGB的高为700宽为500的纯白图像
    bg_image = Image.new(mode='RGB',size=(500,700),color='White')
    # 保留原图
    copy_img = bg_image.copy()
    
    mp = MakeReportTest()
    img = mp.DrawReport(copy_img)
    inter = mp.InsertPicture(img)
    res = mp.FillBlank(inter)
    res.show()

