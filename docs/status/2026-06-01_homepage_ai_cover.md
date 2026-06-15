# 首页 AI 封面主视觉精修记录

日期：2026-06-01

## 调整原因

首页初版使用椭圆轨道、焦点和扫面积扇形 SVG，视觉语言与命题1样板页过于接近。首页是整个线上讲义的封面，不应只讲述单一命题，而应表达牛顿力学体系、宇宙引力、物体运动与现代数学重述的整体故事。

## 生成与选择

- 使用内置 `image_gen` 生成首页专属 AI 位图。
- 生成与精修指令已固化：`docs/visual_prompts/homepage_hero_ai_v1.md`。
- 第一版建立太阳系尺度引力秩序与抛射运动叙事。
- 第二版精修移除地景和塔形装饰，降低轨道线密度，加强连续曲线、切线、微分分段与流线语言。
- 选择第二版作为首页正式候选。

## 接入方式

- 主资产：`assets/images/heroes/principia_main/homepage_hero_ai_v1.png`
- Web 副本：`web/public/assets/heroes/principia_main/homepage_hero_ai_v1.png`
- 资产配置：`assets/theme/hero_visuals.json` 中的 `principia-homepage`
- 页面组件：`web/src/components/home/PrincipiaHero.astro`
- 页面样式：`web/src/styles/global.css`

首页 Hero 使用 AI 位图单层渲染。CSS 只叠加低强度渐变以保证标题可读性，不再叠加命题1式 SVG 科学图。

## 验证

- `python scripts/sync_web_public_assets.py`：通过。
- `npm.cmd run build`：通过，生成 3 个静态页面。
- 桌面截图：`exports/screenshots/homepage_ai_cover/homepage-ai-desktop.png`
- 窄屏截图：`exports/screenshots/homepage_ai_cover/homepage-ai-mobile.png`
- 移动端 CDP 指标：`innerWidth=412`、`document.scrollWidth=412`，无横向溢出。
