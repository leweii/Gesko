---
title: "Code Interpreter"
create_time: 2023-07-09 21:00
tags:
  - tech
  - practice
---

昨晚，花了一些时间，跟老婆过了一遍平时困扰她的工作内容，简单的了解业务知识之后，很快就通过GPT 找到了解决方案，而且是可复制，自动化的方案。

之后久久不能平复自己的心情，生成式AI，解锁 Code Interpreter之后，对各行各业，比如会计，文员，软件开发，都会有change the way of how we work 的趋势。

### Code Interpreter
Code Interpreter 是GPT 七月份上线的一个新特性，大致的思路是

> ![Image]({{ site.url }}/images/post_images/2023-07-09-code-interpreter/1.png)

输入需求 -> GPT 拆解任务 -> 生成解决细分任务的方案代码(python) -> 分配一个或者多个可执行代码的空间 -> 运行代码 -> 输出结果

单看整个过程并没有什么特别的技术突破，但是能够看得出来， OpenAI意图上，是希望向通用人工智能迈进的一步。而从工程实践角度看，这个特性解锁了非常多种可能性。

其中，GPT 拆解任务是一个关键所在，在拆解任务时，GPT需要决定往后的细分任务中，要选取什么更加具体的模型来解决问题。如果我的问题是来自图形处理，那么任务就需要有图形处理模型。如果我的问题是文本，那么就是LLM。

通过这种工程的方式，而不是科学的方式，GPT串联了各种AI模型来解决更加复杂的任务。

举个例子：
软件工程中，我们定义，实现一个pipeline，以自动化我们的工作，让我们从繁琐重复的事情释放出时间，像是给工作加了一个杠杆，做一个杠杆解决了我们五百次的重复。

checkout -> build -> data migration -> deploy

那么今天这个OpenAI 的Code Interpreter 就是在杠杆上加了一个杠杆，他定义了一个pipeline 之上的pipeline。一个pipeline 只在一种场景下适用，如java + mongodb + k8s，但是pipeline 之上的pipeline 一次开发却解决了多个场景的pipeline。

拿软件工程里的CD 举例，不同项目之间，build 方式可以是完全不一样的，比如java，python，go有着完全不一样的build 定义，data migration步骤，不同数据库类型有完全不同的migration 脚本，deploy 同理。
那么一个AI环境下的pipeline 将会是这样的：

+--+----------+--------+----------------+--------+
|  | checkout | build  | data migration | deploy |
+--+----------+--------+----------------+--------+
|  | github   | go     | Mongodb        |        |
+--+----------+--------+----------------+--------+
|  | gitlab   | python | MySQL          |        |
+--+----------+--------+----------------+--------+
|  | svn      | Java   | PostgreSQL     |        |
+--+----------+--------+----------------+--------+

那么我们基于AI 的pipeline 一次解决了3 * 3 * 3 = 27 种应用场景。

虽然AI 的scope 远大于这种应用，但是这是Code Interpreter 是一种很容易落地，能够迅速帮助到企业的工程实践。

> 投入产出肯定不能简单的times times相乘往上，因为虽然开发-> 实现的功能在指数增长，但是涉及到的调试测试工作量也是指数往上走。

### 行业

#### 会计
传统行业必然受到很大的冲击，特别像我老婆所在的会计行业。像会计这种发展了几百年的行业，从算盘 -> 计算器 -> 电子表格 -> 。
每次工具的更新都会很大的影响对应的工作方式。信息化自动化刚落地会计没多久，就迎来了AI 从业人员需要迅速适应，实现降维打击才是正解。
以后只有两种会计，用AI的会计和不用AI的会计。就像用算盘的会计和用计算器的会计一样。

#### 软件
软件开发门槛会迅速下降，任何人都能简单的通过与AI互动进行信息化和自动化的编程。语言学习成本将不再是障碍。开发普通功能，根本不再需要学习编程语法，C、Java、Python的基本实现只需要问GPT。
- 我0基础Python 只花了半小时，帮老婆写了一个爬虫，爬了他们公司的所有车型。
- 我0基础VB 只花了半小时，帮老婆写了个宏，实现了自动化发邮件。
- 我0基础excel运算公式，一句话实现统计，中间要过滤各种数据，学习各种公式的过程都变成了需求描述。

再打一个比方，以前会用Excel 就能开一个文印电，处理一些文档工作。
现在经过简单的学习就能掌握一些数据处理的需求，并且迅速导出结果，而且使用巧妙的情况下，还能避开合规问题，因为我只实现算法，我不需要真正的数据，只需要少量的脱敏数据就能实现结果验证。
程序员过几年就是街边开文印店一样的门槛

工程实践上，以往我们会对业务进行抽象，那么在AI的场景下，我们要对业务进行抽象再抽象，以前我们开发计算器，做的是开发“加，减，乘，除”功能，现在做的是开发“计算”功能，至于计算什么，怎么计算，可以直接由客户提出，中间的业务逻辑代码实现，全部交给AI。

#### 搜索

google 搜索是对现有知识进行检索，

提问 -> google -> 检索类似方案 -> 学习方案解决思路 -> 举一反三

但是AI是定制化答案。一切的技巧都体现在提问，以前我们要很有解题思路，如今我们更加需要的是提问思路。以前是学生思维，现在是考官思维。

提问 -> AI -> 解答 -> 问题存在不确定性 -> 修复问题 -> 提问 -> 如此反复

相比google，用GPT提问方式节约了，检索问题时间，理解学习现有方案时间。

GPT 的方式解决问题，技巧在于出题人要要避免多解，我们提问给AI的需求描述也要把定量，变量描述清晰，这样AI的解答能够趋向于真理。

#### 最后
AI从很fundamental 的方面change the way of how we solve problem。本人非常想从可落地，和身边的难题着手，利用AI来出解决方案。🙆‍♂️读到这里的小伙伴们，咱们多多交流！
