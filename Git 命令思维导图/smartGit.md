一般的版本，大家都知道，就是删除settings.xml文件。

Windows： %APPDATA%\syntevo\SmartGit\
OS X： ~/Library/Preferences/SmartGit/
Unix/Linux： ~/.smartgit/

从上面路径的版本号对应文件夹里，删除settings.xml文件


但是升级到19.1后，会发现，没有了setting.xml，经过对比，我发现多了的文件里的preferences.yml文件内容和原来的settings.xml内容相近：

然后故意破坏了这个文件名（也是相当于做个简单备份），再冲动时发现可以重新进入启动选项，可再选试用30天，或者选非商业。


对于选错的那种，适合删掉preferences.yml文件来重选非商业。
或过期的删除这个进行无限试用。
C:\Users\uidq2038\AppData\Roaming\syntevo\SmartGit\20.1
C:\Users\uidq2038\AppData\Roaming\syntevo\SmartGit\20.1\.backup




{DTC_nRfaMotorShortGND,     {0xA4,0xB7,0x12}, 1 , 1, 108, 148, 3, DTC_nCallBackGround1, DTC_u8RfaMotorShortGNDDtcStsImport}, 
会变为历史DTC，而后等待故障确认时间再变为当前DTC




{DTC_nLost_L_Sws,     {0xA8,0x56,0x00}, 1 , 2, 127, 129, 4, DTC_nCallBackGroundForAcc, DTC_u8Lost_L_SwsDtcStsImport},  
对于左右侧方向盘报文丢失 或者 按键故障，ACC ON，当前DTC不会变为历史DTC，而后等待故障确认时间再变为当前DTC