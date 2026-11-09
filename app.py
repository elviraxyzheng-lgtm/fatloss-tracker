# 减脂助手｜护膝姨妈友好版 身高1.65m
import streamlit as st
import pandas as pd
from datetime import date
import plotly.express as px

st.set_page_config(page_title="减脂助手", layout="wide")

# 基础参数
HEIGHT = 1.65
TARGET_BMI = 24
TARGET_WEIGHT = round(TARGET_BMI * HEIGHT ** 2, 2)

# 本地缓存体重记录
if "weight_data" not in st.session_state:
    st.session_state.weight_data = pd.DataFrame(columns=["记录日期", "体重kg", "BMI"])

# 一周食谱
menu_data = {
    "周一": {
        "早餐": "水煮蛋2个 + 纯牛奶250ml + 干燕麦40g + 小番茄",
        "上午加餐": "苹果1个（饿才吃）",
        "午餐": "杂粮饭80g熟重 + 去皮鸡腿120g + 西兰花+菠菜",
        "下午加餐": "无糖酸奶100g / 巴旦木6~8颗",
        "晚餐": "虾仁120g + 菌菇+娃娃菜一大盘",
        "外卖备选": "去皮鸡腿饭，米饭减半，不要红烧酱汁"
    },
    "周二": {
        "早餐": "玉米1根 + 鸡蛋1个 + 无糖豆浆300ml + 黄瓜",
        "上午加餐": "橙子1个（饿才吃）",
        "午餐": "杂粮饭80g熟重 + 瘦牛肉120g + 油麦菜",
        "下午加餐": "水煮蛋1个",
        "晚餐": "嫩豆腐200g + 金针菇+生菜",
        "外卖备选": "卤牛肉+清炒青菜，不要卤汁拌饭"
    },
    "周三": {
        "早餐": "全麦面包2片 + 鸡蛋1个 + 无糖酸奶150g",
        "上午加餐": "猕猴桃1个（饿才吃）",
        "午餐": "杂粮饭80g熟重 + 巴沙鱼120g + 西葫芦",
        "下午加餐": "无糖酸奶100g",
        "晚餐": "去皮鸡腿肉120g + 海带+青菜",
        "外卖备选": "清蒸鱼套餐，避开浓汤"
    },
    "周四": {
        "早餐": "水煮蛋2个 + 纯牛奶250ml + 干燕麦40g + 小番茄",
        "上午加餐": "苹果1个（饿才吃）",
        "午餐": "杂粮饭80g熟重 + 虾仁120g + 荷兰豆",
        "下午加餐": "巴旦木6~8颗",
        "晚餐": "豆腐200g + 菌菇拼盘",
        "外卖备选": "白灼虾+时蔬"
    },
    "周五": {
        "早餐": "玉米1根 + 鸡蛋1个 + 无糖豆浆300ml + 黄瓜",
        "上午加餐": "橙子1个（饿才吃）",
        "午餐": "杂粮饭80g熟重 + 瘦牛肉120g + 菠菜",
        "下午加餐": "水煮蛋1个",
        "晚餐": "巴沙鱼120g + 生菜+蘑菇",
        "外卖备选": "轻食，酱汁单独放，只用少量油醋汁"
    },
    "周六": {
        "早餐": "全麦面包2片 + 鸡蛋1个 + 无糖酸奶150g",
        "上午加餐": "猕猴桃1个（饿才吃）",
        "午餐": "【放松餐】7分饱，正常吃喜欢的，不暴食",
        "下午加餐": "无糖酸奶100g（饿才吃）",
        "晚餐": "虾仁120g + 大量绿叶菜，不吃主食",
        "外卖备选": "优先清淡，不喝奶茶不吃甜品"
    },
    "周日": {
        "早餐": "水煮蛋2个 + 纯牛奶250ml + 干燕麦40g + 小番茄",
        "上午加餐": "苹果1个（饿才吃）",
        "午餐": "杂粮饭80g熟重 + 去皮鸡腿120g + 时蔬",
        "下午加餐": "巴旦木6~8颗",
        "晚餐": "嫩豆腐200g + 娃娃菜",
        "外卖备选": "豆腐汤+清炒时蔬"
    }
}

# 一周运动（护膝版，无跑跳）
sport_data = {
    "周一": "椭圆机50min + 力量（臀桥、蚌式、跪姿俯卧撑、弹力带划船、死虫、平板支撑）",
    "周二": "平地快走50min（步子小，不爬坡，膝盖不舒服就休息）",
    "周三": "休息日，可慢走20分钟，不强制运动",
    "周四": "游泳 / 卧式动感单车50min",
    "周五": "快走50min + 力量训练",
    "周六": "椭圆机50min",
    "周日": "低强度有氧45min + 午餐放松餐"
}

# 两个标签页
tab_menu, tab_record = st.tabs(["📅 每周食谱&运动", "📊 体重 & BMI记录"])

with tab_menu:
    st.header("减脂食谱｜护膝+姨妈友好版")
    day_select = st.selectbox("选择星期", list(menu_data.keys()))
    menu = menu_data[day_select]
    sport = sport_data[day_select]

    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"{day_select} 饮食安排")
        for title, content in menu.items():
            st.markdown(f"**{title}：** {content}")
    with col2:
        st.subheader(f"{day_select} 运动安排")
        st.info(sport)
        st.warning("⚠️ 左膝刺痛立刻停；经期前3天只做臀桥+蚌式，有氧改为慢走25~30分钟")

    st.divider()
    st.markdown("""
    ✅ 通用规则：
    - 饮水：2000–2400ml，尽量23点前入睡
    - 不要完全不吃脂肪（蛋黄、少量坚果），保护姨妈
    - 外卖备注：少油、酱汁单独分装
    """)

with tab_record:
    st.header("体重 & BMI追踪面板")
    st.write(f"身高：{HEIGHT}m｜目标BMI：{TARGET_BMI}｜目标体重：{TARGET_WEIGHT}kg")

    c1, c2 = st.columns(2)
    with c1:
        record_date = st.date_input("记录日期", value=date.today())
    with c2:
        w = st.number_input("本次体重(kg)", min_value=40.0, max_value=120.0, step=0.1)

    if st.button("✅ 保存这条记录"):
        bmi_val = round(w / (HEIGHT ** 2), 2)
        new_row = pd.DataFrame([[record_date, w, bmi_val]], columns=["记录日期", "体重kg", "BMI"])
        st.session_state.weight_data = pd.concat([st.session_state.weight_data, new_row], ignore_index=True)
        st.success(f"保存成功，本次BMI：{bmi_val}")

    df = st.session_state.weight_data
    if len(df) > 0:
        df["记录日期"] = pd.to_datetime(df["记录日期"])
        df = df.sort_values("记录日期")

        fig_weight = px.line(df, x="记录日期", y="体重kg", markers=True, title="体重趋势")
        fig_weight.add_hline(y=TARGET_WEIGHT, line_dash="dash", annotation_text="目标体重")
        st.plotly_chart(fig_weight, use_container_width=True)

        fig_bmi = px.line(df, x="记录日期", y="BMI", markers=True, title="BMI趋势")
        fig_bmi.add_hline(y=TARGET_BMI, line_dash="dash", annotation_text="目标BMI线")
        st.plotly_chart(fig_bmi, use_container_width=True)

        st.dataframe(df, use_container_width=True)

        if st.button("🗑️ 清空所有记录"):
            st.session_state.weight_data = pd.DataFrame(columns=["记录日期", "体重kg", "BMI"])
            st.warning("记录已清空")
    else:
        st.info("还没有记录，填写上方体重点保存！")
