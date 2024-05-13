from telebot import types

CNS = types.InlineKeyboardMarkup()
CNS.add(
    types.InlineKeyboardButton(text="Спинной мозг", callback_data='BM')
).add(
  types.InlineKeyboardButton(text="Головной мозг", callback_data='GM')
).add(
  types.InlineKeyboardButton(text="Возрастные особенности головного мозга ", callback_data='AGEVAR')
).add(
  types.InlineKeyboardButton(text="Оболочки головного мозга", callback_data='INFRB')
).add(
    types.InlineKeyboardButton(text="Назад", callback_data='markup')
)




P_GM = types.InlineKeyboardMarkup()
P_GM.add(
    types.InlineKeyboardButton(text="Конечный мозг", callback_data='LB')
).add(
    types.InlineKeyboardButton(text="Промежуточный мозг", callback_data='PM')
).add(
    types.InlineKeyboardButton(text="Средний мозг", callback_data='MB')
).add(
    types.InlineKeyboardButton(text="Задний мозг", callback_data='BB')
).add(
    types.InlineKeyboardButton(text="Продолговатый мозг", callback_data='SB')
).add(
    types.InlineKeyboardButton(text="Назад", callback_data='CNS')
)



P_BM = types.InlineKeyboardMarkup()
P_BM.add(
    types.InlineKeyboardButton(text="Общая информация", callback_data='AD')
).add(
    types.InlineKeyboardButton(text="Серое белое вещество спинного мозга", callback_data='GrBl')
).add(
    types.InlineKeyboardButton(text="Проводящие пути спинного мозга", callback_data='PrSt')
).add(
    types.InlineKeyboardButton(text="Оболочки спинного мозга", callback_data='ShBr')
).add(
    types.InlineKeyboardButton(text="Назад", callback_data='CNS')
)
P_SB= types.InlineKeyboardMarkup()
P_SB.add(types.InlineKeyboardButton(text="Продолговатый мозг", callback_data='SBr')
).add(
    types.InlineKeyboardButton(text="Четвёртый желудочек", callback_data='FZh')
).add(
    types.InlineKeyboardButton(text="Ромбовидная ямка", callback_data='Rmb')
).add(
    types.InlineKeyboardButton(text="5-12 пара", callback_data='FTW')
).add(
    types.InlineKeyboardButton(text="Назад", callback_data='P_GM')
)

P_PM = types.InlineKeyboardMarkup()
P_PM.add(types.InlineKeyboardButton(text="Промежуточный мозг", callback_data='PrB')
).add(
    types.InlineKeyboardButton(text="Третий желудочек", callback_data='TZh')
).add(
    types.InlineKeyboardButton(text="Назад", callback_data='P_GM')
)

P_LB =types.InlineKeyboardMarkup()
P_LB.add(types.InlineKeyboardButton(text="Кровеносные сосуды гм", callback_data='Bl')
).add(
    types.InlineKeyboardButton(text="Оболочки гм", callback_data='ShMB')
).add(
    types.InlineKeyboardButton(text="Синусы твердой гм", callback_data='Sin')
).add(
    types.InlineKeyboardButton(text="Сосуды и нервы твердой оболочки гм", callback_data='SNsh')
).add(
    types.InlineKeyboardButton(text="Назад", callback_data='P_GM')
)
