# License申请操作指南 
## 申请License 
TECS_Director_License_Application_Operation_Guide 
摘要 : 
本节介绍申请TECS Director License的操作步骤，申请过程包括：访问申请网址、填写申请信息、提交申请、下载License。
步骤 : 
进入申请License页面
在浏览器的地址输入栏中输入License申请网址（http://csc.zte.com.cn/CSC/UILoader/Index_Internal.aspx），打开CSC客户支持中心页面。
 说明： 
浏览器推荐使用IE11及以上版本，Google
chrome 80版本及以上版本。 
单击打开软件许可证页签。
在左侧功能导航树中，单击核心网licence申请，弹出新建申请单页面，如[图1]所示。
图1  新建申请单页面
填写基本申请信息
在申请信息区域框中，填写License的基本申请信息。
 说明： 
带有的参数为必填项。
参数|说明
---|---
申请类型|有合同项目：务必准确填写合同号。无合同项目：如果有的项目合同号在系统中查不到，可以选无合同项目，合同号需手动填写。研发测试：用于实验局、演示局、外场测试、研究所内测试等场景。合同号填写“无”。
产品线（PDM）|产品线（PDM）选择云基础设施（CloudInfra）。
产品大类（PDM）|产品大类（PDM）选择云套件/云基础设施（CloudInfra）。
版本|单击版本后的查询按钮，如图2所示，在查询结果中勾选实际的版本。
申请原因|根据实际情况填写申请原因。
现网License Show结果|根据实际情况填写。
图2  查询License版本号
填写申请单
双击License申请excel模板，在打开的申请模板中填写具体信息并保存。 
 说明： 
License申请excel模板的获取方法：选择更多→系统管理→系统设置→License文件，打开License文件页面。单击下载许可模板按钮。 
打开模板时，如果提示“是否启用宏”，建议选中启用。 
excel内容限制可修改内容和范畴，按需修改。excel表的sheet页名字不能更改。License申请表（Application）sheet中不能修改的内容已加锁，无法进行修改。 
License申请表中的“本次授权”内容，需要找TECS规划/商务部经理根据正式合同中的功能范围来选择授权内容。 
“网元信息表”的“许可证序列号”需要查询TECS Director的MAC地址后填写，查询步骤：选择系统管理→系统设置→License文件，打开License文件页面。单击地址按钮，在弹出的窗口中查看MAC地址。 
 说明： 
CMS-DirV8.22.20.06版本之后，TECS Director支持多License申请模板，包括TECS Director基础版本、TECS Director标准版本、TECS Director旗舰版本、TECS Director自定义版本，系统用户按需/产品合同选择合适的License模板。
对TECS Director基础版本、TECS Director标准版本、TECS Director旗舰版本的License申请模板，用户仅可配置许可证序列号、产品有效时间和容量许可控制项，不可配置功能许可控制项；对TECS Director自定义版本的License申请模板，用户可配置许可证序列号、产品有效时间，以及全部许可控制项。
基础版本（Basic）：支持IaaS云管理和运维，支持基础IaaS服务比如ECS服务。 
标准版本（Standard）：基础版本基础上支持PaaS中间件服务，支持容器资源运维和应用管理，支持作业平台。 
旗舰版本（Ultimate）：标准版本基础上支持异构资源池管理、公有云管理，支持智能运维。 
自定义版本（Customize）：按运营商/用户需求，授权云管相关功能。 
在制作文件导入页签，单击上传按钮，选择申请模板，单击打开按钮，如[图3]所示。
图3  导入 License申请文件
填写其它信息
在相关组和人员页签，如[图4]所示，选择相关组和人员。
 说明： 
使用人和抄送人：用于邮件通知License申请的处理进度，根据需要增删。
图4  填写其它信息
单击提交按钮，完成License申请提交。
下载Licence
 说明： 
当收到CSC系统License文件制作完成的邮件通知后，可登录CSC系统下载License文件。 
在CSC客户支持中心页面的软件许可证页签，单击功能导航树中的我提交的。
在我提交的页面中，单击查询按钮，显示查询结果信息，如[图5]所示。
图5  查询结果
在查询结果区域框，单击申请单号，打开申请信息页面，如[图6]所示。
图6  申请信息页面
单击License文件名，将License.LCS文件下载到指定位置。
相关任务 : 
License申请失败的处理： 
如果收到CSC系统License文件制作失败的邮件，修改申请内容后重新提交申请，参见步骤[4]~步骤[8]。
## 导入License 
摘要 : 
在Licence申请成功并下载License文件后，将License文件导入到TECS Director系统中。
相关信息 : 
TECS Director的License证书以.lcs结尾，不区分TECS Director版本。
TECS Director版本和导入的License证书需要配套使用。
步骤 : 
登录云管统一平台后，单击导航菜单，选择系统管理→系统设置→License文件
，打开License文件页面，如[图1]所示。
图1  License文件页面
单击替换按钮，弹出提示框，如[图2]所示。
图2  替换提示框
单击确定按钮，选择License文件，单击打开按钮。
导入 License文件到系统后，页面显示License信息，如[图3]所示。
图3  显示License 信息
