**windows代理软件需要开启允许LAN连接**   

### 1. 安装 polipo   
`sudo apt install polipo`   
### 2. 配置 polipo   
`vim /etc/polipo/config`   
在文件中写入如下内容:  
```
socksParentProxy = "localhost:1080"
socksProxyType = socks5
proxyPort = 8123
```
`socksParentProxy` 填的是你 windows 系统 ss 软件所设置的代理地址和端口号。  
`socksProxyType` 是 socks 类型，如果是 ss 就填上 socks5。  
`proxyPort` 是你想在 linux 子系统上使用的代理端口地址。  
### 3. 重启 polipo  
```
service polipo stop 
service polipo start 
```
### 4. 在终端设置代理端口  
`export http_proxy=http://localhost:8123`  
将第二步中设置的 proxyPort 值填入上面的命令就可以了。
使用 `curl www.google.com` 来测试是否设置成功。需要注意的是这个 export 命令在退出 bash 后会失效。   
### 5. 登入 wsl 后自动开启代理  
新建一个 shell 文件  
`vim /usr/local/sbin/polipo.sh`  
并填入设置代理端口的命令  
```
#!/bin/bash  
export http_proxy=http://localhost:8123
```
保存退出，编辑 ~/.bashrc 文件。      
`vim ~/.bashrc`  
在文件末添加语句    
`source /usr/local/sbin/polipo.sh`  
保存退出，注销 bash 并重新登录，使用`curl www.google.com` 查看代理是否已自动开启。  

###### 参考自 https://liuzhilin.io/archives/46