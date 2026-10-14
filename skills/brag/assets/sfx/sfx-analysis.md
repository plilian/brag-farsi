# راهنمای انتخاب افکت

## منبع و مجوز

خانواده‌های افکت `casino`، `impact`، `interface` و `ui` از مجموعهٔ Kenney هستند و CC0 دارند. ۳۲ فایل `keyboard/keypress-*.wav` از Keyboard Soundpack #1 ساختهٔ unicae_games در [OpenGameArt](https://opengameart.org/content/keyboard-soundpack-1-typing-and-single-keystrokes) آمده‌اند و آن‌ها هم CC0 هستند. مجوز MIT کد مخزن این فایل‌های صوتی را پوشش نمی‌دهد.

این خلاصه برای انتخاب افکت‌های موجود در پوشهٔ assets/sfx است. صدا را مطابق حرکت تصویر انتخاب کن؛ صداهای تیز، بلند و تکراری در ویدیوی کوتاه زود خسته‌کننده می‌شوند.

## شاخص‌ها

- **brightness**: گرمی یا روشنی صدا بر پایهٔ مرکز طیفی و انرژی فرکانس بالا.
- **highFrequencyRisk**: خطر تیزی یا خستگی گوش؛ ریسک بالا را در افکت تکراری به‌کار نبر.
- **brightBurden**: مقدار انرژی فرکانس بالای صدا با درنظرگرفتن بلندی و مدت.
- **highActiveDuration**: مدت فعال‌بودن انرژی روشن.
- **envelopeShape**: شکل صدا؛ گذرا، بافت‌دار یا پیوسته.
- **transient.sharpness**: میزان کلیکی و ضربه‌ای‌بودن لحظهٔ شروع.
- **duration**: صدای خیلی کوتاه برای رابط و تایپ مناسب است؛ صدای بلندتر برای آشکارسازی و گذار.

## انتخاب‌های کم‌خطر

- impact/impactSoft_medium_001.ogg — حدود ۰٫۱۸ ثانیه؛ گرم و مناسب آشکارسازی.
- impact/impactSoft_medium_004.ogg — حدود ۰٫۱۵ ثانیه؛ ضربهٔ نرم و کوتاه.
- interface/bong_001.ogg — حدود ۰٫۱۲ ثانیه؛ تأکید عمومی و نرم.
- interface/click_003.ogg، click_002.ogg یا click_005.ogg — کلیک رابط.
- ui/click2.ogg — کلیک کم‌خطر برای کنش کوتاه.

## تطبیق با لحظه

- کلیک یا انتخاب: interface/click_* یا ui/click*.
- toggle: interface/switch_* یا ui/switch*.
- کارت و swipe: casino/card-slide-*؛ فقط برای حرکت کارت.
- آشکارسازی: impact/impactSoft_medium_*.
- موفقیت یا پایان لوگو: impact/impactBell_heavy_*.
- لحظهٔ کمدی یا آشفته: interface/glitch_* یا casino/dice-throw-*، فقط اگر لحن تحملش را دارد.

در سکانس‌های پیاپی هر آیتم را صداگذاری نکن؛ صدای اول، آخر یا مهم‌ترین مورد کافی است. صدای روشن را کوتاه، آرام و تنها نگه دار. آغاز افکت را با شروع حرکت یا لحظهٔ فرود آن هماهنگ کن.
