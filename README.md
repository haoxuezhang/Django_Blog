---
layout:     post
title:      "用Django开发个人博客"
subtitle:   " \"博客开发\""
date:       2017-2-12 14:19:09
author:     "好学长"
header-img: "img/post-bg-2015.jpg"
catalog: true
tags:
    - Python
    - Django
---

> “开始 ”


# 开始

　　这是运用Django开发的一个简单的Blog web，最近一直在学习Django，根据官方教程学习了基本的东西后就开始在网上找相关的项目教程，在简书上看到这个[Blog教程](http://www.jianshu.com/p/3bf9fb2a7e31)，写的还不错，基本稍微高级点的用法都有解释，并且给出了源码，自己clone下来后通过`python manage.py runserver`命令运行项目，发现可以正常运行，这下就有信心来学习这个项目了，毕竟最后是可以实现的。
#开发过程
　　我是在Linux系统中通过`virtualenv venv`搭建的虚拟环境中进行开发的，这样不会破坏系统的环境，最后删除也比较干净。
　　项目开始是建立项目、应用和修改`setting`文件，这三个是最基本的工作，已经很熟悉了。然后就是编写`models`文件，由于是Blog项目，所以最基本的需要Article和Category这两个类，当然后来为了实现更多功能还需要添加其他的模板类，例如标签和评论等。
　　项目中充分用到了通用视图，这样可以简化开发，避免重复造轮子，虽然之前也知道一些，但是通过这个项目学习到了更多，这也是我在这个项目中最大的收获。
　　这个项目前前后后我写了3遍，对其中代码的用法现在已经很熟悉了，下一步会尝试难一点的项目。
　　这是我的项目地址

#总结
　　从开始的什么都不知道再到现在可以开发简单的项目，断断续续的学习，由于平时也有老师的科研任务，所以在Django的学习上效率不高，我是提前返校的，最开始在改老师的C#代码，昨天开始才又学习了一些Django的东西，时间不长，但是还是有很多收获的。
　　明天就开学了，以后学习Django的时间又少了，但是我会尽量挤出时间来学习，学好技术总是好的。

