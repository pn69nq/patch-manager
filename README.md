# 部署 web 服务器
1、安装

    1.1、安装Flask
    
        pip install Flask
    
    1.2、安装gunicorn ()
    
        pip install gunicorn
    
    1.3、安装virtualenv
    
        pip install virtualenv
2、部署flask

```
    //创建python虚拟环境
    virtualenv venv
    source venv/bin/activate
    //关闭 venv
    gunicorn -w4 -b0.0.0.0:5000 patch-manager:app
    #w worker数量，b 访问的地址
    #结束gunicron 使用pkill gunicorn
    
```

3、设置nginx


参考http://www.jianshu.com/p/be9dd421fb8d
