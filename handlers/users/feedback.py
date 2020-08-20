from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command, Text, CommandStart
from aiogram.types import ReplyKeyboardRemove

from data import constants
from keyboards.default import buttons

from loader import dp, db
from aiogram import types

from states import States


@dp.message_handler(CommandStart() | Text(equals=[constants.restart_uz,constants.restart_ru]))
async def start(message: types.Message):
    await message.answer(f"Salom {message.from_user.full_name}!\n"
                         f"Tilni tanlang!\n\n"
                         f"Привет {message.from_user.full_name}!\n"
                         f"Выберите язык!", reply_markup=buttons.lang)

    await States.Language.set()


@dp.message_handler(Text(equals=[constants.Uz, constants.Ru]), state=States.Language)
async def get_language(message: types.Message, state: FSMContext):
    language = message.text

    await state.update_data(language=language)

    if language == constants.Uz:
        await message.answer(
            f"Xizmat sifatini oshirish maqsadida telefon raqamingizni ulashing",
            reply_markup=buttons.share_number_uz)
    else:
        await message.answer(
            f"В целях повышения качества обслуживания поделитесь контактами",
            reply_markup=buttons.share_number_ru)

    await States.next()


@dp.message_handler(state=States.Number, content_types=types.ContentType.CONTACT)
async def get_number(message: types.Message, state: FSMContext):
    number = message.contact
    data = await state.get_data()
    await state.update_data(number=number)

    if data.get("language") == constants.Uz:
        await message.answer(
            f"Viloyatingizni tanlang:", reply_markup=buttons.regions_uz)
    else:
        await message.answer(
            f"Выберите свой регион:", reply_markup=buttons.regions_ru)
    await States.next()


@dp.message_handler(state=States.Region)
async def get_region(message: types.Message, state: FSMContext):
    region = message.text
    data = await state.get_data()
    await state.update_data(region=region)

    if data.get("language") == constants.Uz:
        await message.answer(
            f"Ishchilar pora so\'rashganmi?", reply_markup=buttons.money_uz)
    else:
        await message.answer(
            f"Рабочие просили взятки?", reply_markup=buttons.money_ru)
    await States.next()


@dp.message_handler(Text(equals=["Ha", "Yo\'q", "Да", "Нет"]), state=States.Money)
async def get_money(message: types.Message, state: FSMContext):
    money = message.text
    data = await state.get_data()
    await state.update_data(money=money)
    if data.get("language") == constants.Uz:
        await message.answer(
            f"Qo\'shimcha ma\'lumotingiz bormi?", reply_markup=ReplyKeyboardRemove())
    else:
        await message.answer(
            f"У вас есть дополнительная информация?", reply_markup=ReplyKeyboardRemove())
    await States.next()


@dp.message_handler(state=States.Feedback)
async def get_feedback(message: types.Message, state: FSMContext):
    feedback = message.text
    data = await state.get_data()
    await state.update_data(feedback=feedback)

    await db.add_user(message.from_user.full_name, data.get('number').phone_number, data.get('region'), True, feedback)

    if data.get("language") == constants.Uz:
        await message.answer(
            f"Raxmat so\'rovnomada ishtirok etganingiz uchun!\n", reply_markup=buttons.restart_uz)
    else:
        await message.answer(
            f"Спасибо за участие в опросе!\n", reply_markup=buttons.restart_ru)
    await state.finish()
