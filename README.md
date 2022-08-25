# backup.py

用于做文件备份的简单脚本。可以让它每天定时执行一次。

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

## TODO

- [ ] YAML配置文件中加一个最大备份数量的参数
- [ ] 实现定时执行脚本
