# Contributing

- 先创建 Issue，说明任务、适用游戏和可观察证据。
- 参考对应 `models/Mxx_*/README.md` 的标签定义。
- 不提交未经许可可再分发的游戏画面、专有 UI 文件或第三方数据。
- 记录游戏版本、平台、模式、分辨率、帧率、语言、UI 缩放和采集会话。
- 按游戏/会话/视频片段划分数据，禁止相邻帧跨 train/test 泄漏。
- PR 应包含复现命令、测试结果、逐游戏指标和失败案例。
- 明确区分实测结果与目标指标；不得从随机帧划分推断跨游戏泛化。

- Keep one model directory scoped to one recognition task. Do not merge unrelated tasks to reduce model count.
- Shared encoders and utilities are welcome, but submit per-task ablations proving no single-task regression before proposing parameter sharing.
- Keep audio models independently labeled and evaluated; A02 gunshot and A03 reload audio are separate tasks.
