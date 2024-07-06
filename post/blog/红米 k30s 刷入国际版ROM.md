# 红米 k30s 5G 刷入国际版ROM或最新开发版

## 国际版ROM

* 国际版ROM：https://c.mi.com/global/miuidownload/index , 选择`Mi 10T/Pro/Lite`都行
* 最新开发版ROM：https://github.com/mooseIre/update_miui_ota

## 解锁BL

* http://www.miui.com/unlock

## 刷入三方 REC

* https://www.lanzoui.com/b01tt66li 密码: dshvv
* 双击**移动叔叔论坛一键写rec.exe**，按照提示将**红米k30s至尊版基于wzsx150魔改（twr）.img.zip**解压并重命名.
* 手机按电源键+音量下键进入bootloader
* 手机连接电脑之后就可以通过****移动叔叔论坛一键写rec.exe****刷入三方rec
* 手机重启进入三方 rec
* 将国际版ROM放置手机合适路径
* 根据界面提示刷入国际版ROM
* **刷完后，记得选择 高级>恢复官方rec. **
* **然后再重启按电源键+音量上键进入官方rec执行双清，否则会卡米.**
* 再次重启手机进入系统，即可成功安装国际版ROM.

## ADB 安装

* ADB On Windows: https://dl.google.com/android/repository/platform-tools-latest-windows.zip
* ADB On macOS: https://dl.google.com/android/repository/platform-tools-latest-darwin.zip
* ADB On Linux: https://dl.google.com/android/repository/platform-tools-latest-linux.zip

## Google Play 设备注册

获取android_id

```she
adb root
adb shell 'sqlite3 /data/data/com.google.android.gsf/databases/gservices.db "select * from main where name = \"android_id\";"'
```

向谷歌提交 android_id：https://www.google.com/android/uncertified

## 总结

国际版确实比国内版广告少，预装软件也少。但是缺点就是本地化差，界面丑。
