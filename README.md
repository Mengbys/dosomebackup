# backup.py

用于备份文件的简单脚本。可以让它每天定时执行一次。

## 使用

在执行脚本之前，需要在`config.yaml`中配置相关信息，如：要备份的文件夹、放备份文件的文件夹。下面是一个简单的例子：

```yaml
target:
  - '/home/lxh/workspace/ut/backup-test/important-files'
  - '/home/lxh/workspace/ut/backup-test/notes'
  - '/home/lxh/workspace/ut/backup-test/passwords'
backup_dir: '/home/lxh/workspace/ut/backup-test/bf'
```

执行脚本之前，确保`config.yaml`与`backup.py`在同一个文件夹下。

### 手动执行

```bash
$ python backup.py  # 如果python不行就换成python3
```

### 系统定时执行

使用Linux系统的`crontab`程序可以实现。

假设`backup.py`文件的路径是：`~/dosomebackup/back.py`。下面的步骤将实现：每天凌晨3:00执行一次备份操作，并将相关信息记录在同文件夹下的`log.txt`中。

执行`crontab -e`，在打开的文件的最后一行加入以下语句：

```
0 3 * * * /usr/bin/env python3 ~/dosomebackup/backup.py >> ~/dosomebackup/log.txt
```

如果你觉得`log.txt`一直在变大有点让人不爽，那么你可以在`crontab`中加多一个定时执行的任务：

```
0 3 * * * /usr/bin/env python3 ~/dosomebackup/backup.py >> ~/dosomebackup/log.txt
0 0 */30 * * echo '' > ~/dosomebackup/log.txt
```

第二个任务的意思是：每30天清空日志文件`log.txt`的信息。

`crontab`程序的使用方法可以参考如下两个网站：

- <https://betterprogramming.pub/scheduling-python-scripts-on-linux-fa0d28a8f915>
- <https://www.geeksforgeeks.org/scheduling-python-scripts-on-linux/>

## 注意

不要把其他文件放到备份文件夹中，避免被删除。

## TODO

- [ ] YAML配置文件中加一个最大备份数量的参数
- [ ] 实现定时执行脚本
