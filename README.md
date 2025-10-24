# Stash 规则配置

这是一个用于 Stash 的规则配置文件集合，旨在提供灵活的代理、DNS、策略组和规则配置，以优化网络访问体验。

## 立场声明

本项目仅用于作者个人使用、学习和技术交流，不鼓励、不提倡、不协助任何违反当地法律法规的行为。使用者应自行承担所有风险和责任。也请您在使用时擦亮眼睛，明辨是非，切勿盲目相信任何未经验证的信息。更请您在使用过程中遵守当地法律法规，对于因访问或使用本项目产生的任何风险、法律责任或争议，用户需自行承担。  

## 文件结构

-   `Default.yaml`: Stash 的主配置文件，包含了代理提供者、端口、DNS 设置、策略组定义和规则。
-   `domain-adblock.txt`: 包含需要屏蔽的广告域名列表，用于实现广告过滤。
-   `domain-direct.txt`: 包含需要直连的域名列表，用于绕过代理直接访问。
-   `sort_rules.sh`: 一个用于排序和去重 `.txt` 规则文件的脚本。

## 使用指南

### 导入 `Default.yaml` 到 Stash

1.  打开 Stash 应用。
2.  导航到配置页面。
3.  选择导入本地文件或通过 URL 导入 `Default.yaml`。

### 排序和去重规则文件

可以使用 `sort_rules.sh` 脚本来对 `domain-adblock.txt` 和 `domain-direct.txt` 等 `.txt` 规则文件进行排序和去重。这有助于保持规则文件的整洁和高效。

**用法:**

```bash
./sort_rules.sh <文件1> [文件2] ...
```

**示例:**

```bash
./sort_rules.sh domain-direct.txt domain-adblock.txt
```

脚本会显示被删除的重复行（如果有）。

### 更新 `domain-adblock.txt` 和 `domain-direct.txt`

这些文件可以通过编辑本地文件或通过 Stash 的规则提供者功能进行更新。`Default.yaml` 中已经配置了从 GitHub 仓库自动更新这些规则的链接。

### 自定义配置

您可以根据自己的需求修改 `Default.yaml` 文件中的代理提供者、策略组和规则。

## 注意事项

-   `Default.yaml` 中的 `subscribe-url` 字段在 MacOS 上管理订阅时需要填写订阅链接才能显示流量信息，iOS 版本可留空。
-   请确保您的代理订阅链接有效，并且 `proxy-providers` 中的 `url` 配置正确。

## 侵权声明

如有内容侵犯您的权益，请联系 [sifanlian@gmail.com]，我们将及时处理。

## 贡献

如果您有任何改进建议或新的规则，欢迎提交 Pull Request。
