# <center><font face="微软雅黑"><font color='orange'>Android端自动化测试框架</font><center>
![](https://img.shields.io/badge/made%20by-Pyethon3.9-blue)
![](https://img.shields.io/badge/TestTool-Appium-orange)
![](https://img.shields.io/badge/platform-Android-yellowgreen)  
![GitHub Repo stars](https://img.shields.io/github/stars/Geek-monk/UIautoTest_for_Android?style=social)
![GitHub forks](https://img.shields.io/github/forks/Geek-monk/UIautoTest_for_Android?style=social)
![Bitbucket open issues](https://img.shields.io/bitbucket/issues/Geek-monk/UIautoTest_for_Android)  
![Git](https://img.shields.io/badge/-Git-333333?style=flat&logo=git)
![pycharm](https://img.shields.io/badge/-Pycharm-333333?style=flat&logo=pycharm&logoColor=31f400)
<br>

![logo](https://github.com/Geek-monk/Geek-monk/blob/main/icons/40ae58cc.gif?raw=true)
* 此项目使用Appium+Python+Unitest+HTMLTestRunner,搭建测试框架，对Android平台进行UI自动化测试

### 1. <font color='OliveDrab'>目录结构</font>
- <font color='Magenta'>UI_AutomatedTesting</font>
    - <font color='Brown'>config</font>
      - <font color='green'>desired_caps.yaml</font> ------ driver 相关配置文件
    - <font color='Brown'>moudules</font>
      - <font color='green'>Login.py</font> ------ 包含登录、更换账号相关函数
      - <font color='green'>main_UIcontrol.py</font> ------ 控件封装
      - <font color='green'>Report_To_DINGTalk.py</font> ------发送钉钉模块
      - <font color='green'>SetUp.py</font> ------读取 driver 配置文件
      - <font color='green'>swipescreen.py</font> ------ 滑动函数封装
    - <font color='Brown'>report</font>
      - <font color='green'>每次执行后，脚本的通过情况</font>
    - <font color='Brown'>testcase</font>
      - <font color='green'>测试用例</font>
    - <font color='Brown'>readme.md</font>
    - <font color='Brown'>start_testcase.py</font> ------ 开始执行测试
<br>
### 2. <font color='OliveDrab'>环境搭建</font>
- 请自行 google 搜索 appium 的环境搭建。
- 连接Android真机或者模拟器
<br>

### 3. <font color='OliveDrab'>测试用例设计原则</font>

- Page Object是一种程序设计模式，将面向过程转变为面向对象(页面对象)，将测试对象（按钮、输入框、标题等）及单个的测试步骤封装在每个Page对象中，以page为单位进行管理。

### 优点

- 以页面为单位，集中管理元素对象和方法。当页面元素或流程变动时只需要修改相关页面方法即可，不需要修改相应脚本
- 编写脚本简单，顺着业务逻辑写脚本。page object模式以业务逻辑上的每一步操作作为区分点，页面方法代表了此页面的一个业务操作并严格控制此操作的后续流程
- 后期维护方便
<br>