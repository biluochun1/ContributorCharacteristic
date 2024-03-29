# 统计仓库个人开发量
git log --author="username" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -
# 统计每个人的增删代码量
git log --format='%aN' | sort -u | while read name; do
  echo -en "$name\t"
  git log --author="$name" --pretty=tformat: --numstat | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "added lines: %s, removed lines: %s, total lines: %s\n", add, subs, loc }' -
done
# 查看仓库提交者排名前 5
git log --pretty='%aN' | sort | uniq -c | sort -k1 -n -r | head -n 5
# 贡献者数量统计
git log --pretty='%aN' | sort -u | wc -l
# 提交数量统计
git log --oneline | wc -l
# 统计代码总行数：
# shellcheck disable=SC2038
find . -name "*.m" -or -name "*.h" -or -name "*.xib" -or -name "*.c" | xargs grep -v "^$" | wc -l

# git2json command
/Users/weizijian/anaconda3/bin/git2json --git-dir ./FFmpeg/.git > ffmpeg-git-log.json
