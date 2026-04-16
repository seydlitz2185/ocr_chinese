# mpl_chinese.py
#
# 在 Docker/Linux 环境中统一配置 matplotlib 的中文字体和负号正常显示
# 推荐在任何需要画中文图的脚本最前面先 `import mpl_chinese`

import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

# 1. 推荐字体名称（按优先级从高到低）

PREFERRED_FONTS = [
    "Noto Sans CJK JP",       # Debian/Ubuntu 上 fonts-noto-cjk 的常见名称
    "Noto Serif CJK JP",
    "WenQuanYi Zen Hei",      # 文泉驿正黑，作为备份
    "SimHei",                 # Windows 常见黑体
    'Hei', 'Arial', 'Helvetica', 'Times New Roman'
]

def _choose_font():
    """从系统已安装字体中选择一个可用的中文字体名称"""
    # 获取系统所有字体名称
    available_fonts = set(
        f.name for f in font_manager.fontManager.ttflist
    )

    for fname in PREFERRED_FONTS:
        if fname in available_fonts:
            return fname

    # 如果一个都匹配不到，最后退回到默认 sans-serif
    return "sans-serif"

def setup_chinese():
    """配置 matplotlib 使用中文字体，并修复负号显示问题"""
    font_name = _choose_font()

    # 设定全局字体
    matplotlib.rcParams["font.sans-serif"] = [font_name]
    matplotlib.rcParams["font.family"] = "sans-serif"

    # 修复负号显示问题
    matplotlib.rcParams["axes.unicode_minus"] = False

    # （可选）设置字体大小、LaTeX 数学字体等
    # matplotlib.rcParams["font.size"] = 12

    print(f"[mpl_chinese] 使用字体: {font_name}")

