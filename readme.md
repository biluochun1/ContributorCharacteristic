# 2020 本科毕设 开源贡献者的特征分析
## Todo List
- github爬虫 （完成）
- 数据存储 
- 分析算法
- 开题报告
- 论文

### github 爬虫
目前封装在github包里面，完成 github api V3 版本 功能的封装

### git 仓库分析
- 使用shell git命令对仓库进行分析，一些分析命令记录在了git_command_record.md中
- 使用 gitstats 进行分析，可以生成可视化的界面

## 本项目目录结构
      ContributorCharacteristic
       |----algorithm(特征分析算法)
       |----github(github restful v3 接口封装)
           |----event     
           |----gists
           |----event
           |----gitdata
           |----issues
           |----orgs
           |----pullreqs
           |----repos
           |----users
           |----github.py (对外暴露接口)
           