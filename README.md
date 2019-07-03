基于关键词的小说分类
===
模块框架
---
>本作品共分为三个框架，分别为文本预处理，关键词提取和敏感词过滤。其中文本预处理包括内容抓取，数据清洗和分词三个部分，敏感词过滤分为用户自定义黑名单和百度AI，先根据用户自定义敏感词库进行匹配与标记，再调用百度文本审核接口进一步扩大审核范围。
![框架](https://github.com/xu798/-/blob/master/%E5%9B%BE%E7%89%87/%E6%95%B4%E4%BD%93%E6%80%9D%E8%B7%AF.png)

整体思路
---
>本作品是通过爬虫将网络读物下载并进行分词操作，得到的文本再经过关键词提取，并进一步通过敏感词过滤技术实现网络读物的分类。
数据抓取负责用爬虫爬取白熊阅读网站，获得了一定数量的小说。分词部分负责将小说进行预处理，筛掉无关符号并且根据语言模型进行分词。关键词的筛选是根据内在模式和外在模式熵差进行的提取。敏感词过滤与分类是首先根据用户自定义敏感词库进行匹配与标记，再根据百度文本审核接口进一步扩大审核范围。

文本处理
---
1）文本抓取及预处理
---
>本项目主要目的是对小说进行分类，因此采用pytho n对网络上面的小说进行抓取，本项目以白熊阅读网为目标网站。为避免网站进行反爬虫，本作品采用伪装用户代理及使用代理IP的方式抵抗反爬虫策略，其对象为白熊阅读网站上面的部分连载与完结小说，获得其章节目录及主要内容。由于网站上存在部分付费小说，因此不能完整爬取，该问题会在之后进行改进。
本作品主要使用pyth on自带的requ ests模块和BeautifulSoup4模块来进行小说的抓取，首先抓取西刺代理网站的代理IP，再从中随机选取一个IP作为IP地址对目标网站即白熊阅读中的小说进行抓取并将之保存到txt文件中以供使用。其中使用reque sts.post()方法对申请网页，得到网页的html代码，使用find()和find_all()函数根据代码提取其中的内容；然后对提取后的内容进行清洗，清除其中的标签之类的不属于文章本身内容的部分，保存在txt文件中。

2）分词
---
>分词部分调用pytho n写的类库snownlp，可以方便的处理中文文本内容。snownlp通过使用SRILM工具实现，SRILM是一个统计和分析语言模型的工具，其最基础和最核心的模块是n-gram模块。n－gram 模型认为第i 个词的出现只与前面的 i－1个词有关，整句的概率就是各个词出现概率的乘积。

3）提取关键词
---
>关键词提取是通过内在和外在模式之间的熵差提取关键字技术实现的。该方法利用内在模式和外在模式之间的香农熵差，评估和排列文本中单词的相关性。由于书面文字反映了作者的意图，相关词语表现出单词聚类的统计特性，即内在模式表征。外在模式则表示单词聚类消失的统计特性。因为高度重要的词语往往受到作者目的的调节，无关词语在文本中随机分布，所以相关度高的词语在内在模式和外在模式之间表现出较高差异。该技术将关键字提取代码封装为DLL，关键字提取软件通过调用DLL实现该功能。本项目在该软件代码的基础上进行调整与优化，实现对一个TXT文本内容的去符号与去常用字的关键字提取，保存关键字为TXT文本等功能。

文本审核
---
>敏感词过滤与分类模块是由两部分组成：用户自定义黑名单过滤和百度文本审核。用户自定义黑名单是通过根据输入的文本准确匹配黑名单中的敏感词汇，并进行相应的类别标记而得，满足了用户个性化审核要求；通过调用百度文本审核接口，使用其深度学习技术与海量敏感词汇数据库进行过滤和分类，可以进一步提高命中率。

创新与展望
---
>1)   提出对网络读物内容审核的模型
本组运用基于语言模型的文本分词的模块对网络读物进行语义划分，并且按章节进行关键词提取，最后运用百度文本审核框架以及用户自定义黑名单进一步对内容进行审核，并且将含有的敏感词汇进行分类和输出。
2)   黑名单与人工智能技术结合提高命中率
对于敏感词过滤与分类模块，本组添加了用户自定义的敏感词汇黑名单匹配分类模块，与百度文本人工智能文本审核技术结合，实现两次过滤机制，在满足个性化审核的同时提高了文本敏感词汇的命中率。
3)   关键词可视化满足用户体验
本组根据关键词输出的加权比例进行了可视化显示，满足用户视觉体验，可以直观感受是否出现敏感词汇。
