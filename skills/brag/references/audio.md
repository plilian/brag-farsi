# راهنمای صدا

صدا بخشی از تدوین است: گفتار باید فهمیده شود، موسیقی حس را بسازد و افکت فقط حرکت‌های مهم را برجسته کند. موسیقی و گویندگی پیش‌فرض روشن‌اند؛ اگر کاربر `--no-music`، `--no-sfx` یا `--no-voice` گفت، همان لایه را در طرح، brief، ترکیب و MP4 حذف کن. سکوت را فقط وقتی انتخاب کن که کاربر خواسته یا داستان با سکوت قوی‌تر می‌شود.

## مسیر دارایی‌ها

تمام مسیرها نسبت به `<skill-dir>` هستند؛ این همان پوشه‌ای است که `SKILL.md` در آن قرار دارد. مسیر نصب را حدس نزن.

- افکت‌ها: `<skill-dir>/assets/sfx/{casino,impact,interface,ui}/`
- تک‌صدای کلیدها: `<skill-dir>/assets/sfx/keyboard/`
- موسیقی: `<skill-dir>/assets/music/`
- presetهای cue موسیقی: `<skill-dir>/assets/music/cues/<track-stem>.music-cues.{md,json}`
- تحلیل افکت: `<skill-dir>/assets/sfx/sfx-analysis.{md,json}`

Hyperframes فایل را از پوشهٔ ترکیب می‌خواند. فایل‌های لازم را پیش از رندر از دارایی مهارت به `<output-dir>/composition/assets/` کپی کن؛ فقط انتخاب‌های همان ویدیو را کپی کن، نه کل کتابخانه را. سپس در HTML ترکیب مسیر نسبی از پوشهٔ `composition/` بده:

~~~
mkdir -p <output-dir>/composition/assets/sfx/interface <output-dir>/composition/assets/sfx/impact <output-dir>/composition/assets/sfx/casino <output-dir>/composition/assets/sfx/ui <output-dir>/composition/assets/music
cp <skill-dir>/assets/sfx/interface/bong_001.ogg <output-dir>/composition/assets/sfx/interface/
cp <skill-dir>/assets/sfx/impact/impactBell_heavy_000.ogg <output-dir>/composition/assets/sfx/impact/
cp <skill-dir>/assets/music/happy-beats-business-moves-vol-1-by-ende-dot-app.mp3 <output-dir>/composition/assets/music/
~~~

در ترکیب مسیرها به این شکل‌اند: `assets/sfx/interface/bong_001.ogg`، `assets/sfx/impact/impactBell_heavy_000.ogg` و `assets/music/<track>.mp3`. مسیر مطلق رایانه مثل `/Users/...` یا مسیر پوشهٔ مهارت را در HTML نگذار؛ در renderer کار نمی‌کند. اگر فایل موسیقی وجود ندارد، آن را رد کن و پس از رندر به کاربر بگو.

## منبع و مجوز دارایی‌ها

- خانواده‌های افکت `casino`، `impact`، `interface` و `ui` از مجموعهٔ Kenney هستند و CC0 دارند.
- ۳۲ فایل `keyboard/keypress-001.wav` تا `keypress-032.wav` از Keyboard Soundpack #1 ساختهٔ unicae_games در OpenGameArt هستند و CC0 دارند.
- پنج ترک موجود از Sascha Ende در ENDE.APP هستند و CC BY 4.0 دارند. استفاده و بازتوزیع تجاری مجاز است، اما باید اعتباردهی شود. نام ترک، سازنده، منبع، مجوز و هر تغییر را در توضیحات انتشار ویدیو بیاور.

متن‌های آماده و پیوند منابع در `assets/music/README.md` و `THIRD_PARTY_NOTICES.md` مخزن هستند. مجوز MIT کد، مجوز فایل‌های صوتی را جایگزین نمی‌کند.

## کتابخانهٔ افکت

پیش از انتخاب، `sfx-analysis.md` را بخوان؛ آن فایل افکت‌های امن‌تر و ریسک فرکانس بالا را ثبت می‌کند. برای تدوین polished یا افکت تکراری، کم‌ریسک را ترجیح بده؛ افکت تیز فقط برای لحظهٔ منفرد و کوتاه مناسب است.

### `keyboard/` — صدای کلید

۳۲ فایل کلید مجزا، هرکدام با شدت و رنگ اندکی متفاوت. برای انیمیشن تایپ می‌توان در هر کاراکتر یکی را به‌شکل تصادفی انتخاب کرد تا تایپ تکراری و ماشینی نشود. این صداها CC0 هستند.

### `interface/` — صداهای رابط

| فایل | حس | کاربرد |
|---|---|---|
| `click_001–005.ogg` | تیز و دقیق | لمس دکمه یا CTA |
| `glitch_002.ogg`، `glitch_004.ogg` | اعوجاج دیجیتال | لحظهٔ فناوری یا تأکید آشفته |
| `error_005–006.ogg` | هشدار منفی | شکست بامزه یا انتخاب نادرست |
| `switch_001–002.ogg`، `switch_004–007.ogg` | کلید تغییر | روشن‌شدن ویژگی یا تغییر حالت |
| `drop_001–003.ogg` | فرود نرم | نشستن یا قرارگرفتن عنصر |
| `bong_001.ogg` | زنگ بم | اعلام مهم؛ با خویشتن‌داری |
| `select_008.ogg` | انتخاب | ناوبری یا تمرکز روی مورد |

### `impact/` — ضربه

برای آشکارسازی بزرگ و گذار مناسب‌ترند. انتخاب را با جنس حرکت تطبیق بده.

| فایل | کاربرد |
|---|---|
| `impactSoft_medium_000–004.ogg` | نمایان‌شدن یا گذار اصلی؛ خانوادهٔ کم‌خطر |
| `impactSoft_heavy_000–004.ogg` | ضربهٔ کارتونی یا تأکید سنگین |
| `impactBell_heavy_000/003/004.ogg` | آشکارسازی سینمایی یا ورود لوگو |
| `impactPunch_heavy_000–004.ogg` | لحظهٔ پرخاشگر یا آشفته |
| `impactPunch_medium_000–004.ogg` | تأکید میانی |
| `impactWood_light/medium/heavy_000–004.ogg` | ضربهٔ چوبی گرم و طبیعی |
| `impactPlank_medium_000–004.ogg` | حرکت فیزیکی یا شوخی کارتونی |
| `impactPlate_light/medium/heavy_000–004.ogg` | ضربهٔ فلزی از سبک تا سنگین |
| `impactTin_medium_000–004.ogg` | برخورد فلزیِ سبک و قدیمی |
| `impactGeneric_light_000–004.ogg` | تأکید عمومی و کوتاه |
| `impactMetal_light/medium/heavy_*.ogg` | صدای فلز با شدت‌های مختلف |
| `impactGlass_light/medium/heavy_*.ogg` | درخشش شیشه‌ای تا برخورد سنگین |
| `impactMining_001.ogg` | ضربهٔ صنعتی و سنگین |

### `casino/` — کارت، ژتون و تاس

| فایل | کاربرد |
|---|---|
| `card-slide-1–8.ogg` | swipe یا ورود کارت |
| `card-place-1–4.ogg` | فرود کارت یا آیتم |
| `card-fan-1–2.ogg` | بازشدن پیاپی کارت‌ها |
| `card-shove-1–4.ogg` | حرکت محکم کارت |
| `card-shuffle.ogg` | گذار همراه حرکت کارت |
| `chip-lay-1–3.ogg` | گذاشتن یا تأیید آمار |
| `chips-stack-1–6.ogg` | شمارنده یا چیدن پیاپی |
| `chips-collide-1–4.ogg` | موفقیت یا جشن کوتاه |
| `chips-handle-1–4.ogg` و `chips-handle-6.ogg` | حرکت معمول ژتون |
| `dice-shake-1–3.ogg` | انتظار پیش از نتیجه |
| `dice-grab-1–2.ogg` | برداشتن سریع تاس |
| `dice-throw-1–3.ogg`، `die-throw-1–4.ogg` | کنش شانسی یا آشفته |
| `cards-pack-open-1–2.ogg` | آشکارسازی یا معرفی محصول |

### `ui/` — کلیک و کلید تغییر

| فایل | کاربرد |
|---|---|
| `click1–5.ogg` | کلیک‌های متنوع؛ گاهی نرم‌تر از `interface/click` |
| `mouseclick1.ogg` | کلیک نشانگر شبیه‌سازی‌شده |
| `rollover1–2.ogg`، `rollover4–5.ogg` | بازخورد بسیار نرم hover |
| بیشتر فایل‌های `switch1–38.ogg` | تغییر وضعیت؛ با حس مناسب انتخاب کن |

## تراکم افکت بر اساس لحن

| لحن | تراکم | رویکرد |
|---|---|---|
| `default` | متوسط | ۳ تا ۵ افکت روی لحظه‌های اصلی؛ کلیک یا drop برای ورود، زنگ برای موفقیت، ضربهٔ نرم برای آشکارسازی |
| `polished` | کم اما حاضر | ۲ یا ۳ افکت بسیار نرم؛ هیچ‌چیز تهاجمی نباشد |
| `yc-parody` | کم | ۲ یا ۳ تأکید خویشتن‌دار: آشکارسازی خشک، یک تعامل رابط و در صورت تناسب پایان |
| `chaotic` | متراکم | افکت روی ضرب‌های انتخابی؛ punch، glitch، تاس یا فلز را با کنترل ترکیب کن |
| `deadpan` | بسیار کم | موسیقی آرام و یک یا دو افکت خشک؛ سکوت کامل فقط وقتی در طرح شوخی است |
| `cinematic` | ۲ یا ۳ افکت درشت | زنگ برای قهرمان، ضربهٔ نرم برای آشکارسازی و تأکید پایان |
| `app-store` | لایهٔ سبک و یکنواخت | drop یا کلیک برای کارت ویژگی؛ صدای موفقیت در پایان، معمولاً با بلندی ۰٫۶۵ تا ۰٫۷۵ |

## رویداد به افکت

این‌ها مثال‌اند، نه دستور ثابت؛ صدا باید تدوین را تقویت کند، نه توجه را از تصویر بگیرد.

| لحظه | خانوادهٔ مناسب | یادداشت |
|---|---|---|
| بازشدن کارت یا موردهای پیاپی | `casino/card-slide-*`، `card-place-*`، `card-fan-*` یا `interface/drop_*` | جنس حرکت را تطبیق بده؛ در توالی متراکم فقط اول، آخر یا ضرب مهم را صداگذاری کن |
| آشکارسازی یا پایان | `impactBell_heavy_*`، `impactSoft_medium_*`، `interface/bong_001` | یک افکت کوتاه هنگام فرود کافی است |
| تایپ متن | کلیدهای `keyboard/keypress-*.wav` یا `interface/drop_*` | برای هر کاراکتر تصادفی انتخاب کن؛ اگر متن متراکم است، افکت را حذف یا کمتر کن |
| کنش کاربر | `interface/click_*`، `select_008`، `switch_*` یا `ui/mouseclick1` | فقط وقتی کلیک، لمس، کلید یا انتخاب در تصویر دیده می‌شود |
| موفقیت | `impactBell_heavy_*` یا `casino/chips-collide-*` | برای تأیید، match، نتیجه یا CTA پایانی |
| لحظهٔ آشفته یا بامزه | `glitch_*`، `error_*`، `impactPunch_*` یا `casino/dice-throw-*` | فقط اگر لحن چنین شدتی را تحمل می‌کند |

اگر مرددی، افکت‌های کمتر با زمان‌بندی بهتر انتخاب کن. یک پالت منسجم از چند صدای متناسب بهتر از مجموعه‌ای از صداهای بامزهٔ نامربوط است.

## زمان‌بندی افکت

وقتی زمان حرکت معلوم است:

- افکت را به **شروع** حرکت وصل کن، نه پایان آن.
- ورود pop را حدود ۰ تا ۰٫۱ ثانیه پیش از اولین فریم عنصر بگذار.
- افکت گذار را سرِ زمان آغاز گذار قرار بده.
- صدای موفقیت را هنگامی پخش کن که آمار یا نتیجه کاملاً دیده می‌شود.
- برای موارد پیاپی، معمولاً اولین، آخرین یا قوی‌ترین ورود کافی است؛ همه را فقط اگر ریتمش عمدی و تمیز است صداگذاری کن.

نمونهٔ طرح داخلی:

~~~
نمای ۲ — آشکارسازی — ۳ ثانیه
  نام محصول در ثانیهٔ ۰٫۳ بزرگ می‌شود → impactSoft_medium_001 در ۰٫۲
  شعار در ثانیهٔ ۰٫۸ محو می‌شود → بدون افکت
  گذار در ثانیهٔ ۳ → drop_001 در ۲٫۹
~~~

## موسیقی

### ترک‌های موجود

همهٔ ترک‌ها از مجموعهٔ Happy Beats & Business Moves در ENDE.APP هستند. پاک، روشن و شرکتی‌اند؛ با چند لحن سازگارند. همه CC BY 4.0 هستند و اعتباردهی می‌خواهند؛ اطلاعات کامل در `assets/music/README.md` است.

| فایل | مدت | حس | مناسب برای |
|---|---:|---|---|
| `happy-beats-business-moves-vol-1-by-ende-dot-app.mp3` | ۲:۴۴ | روشن و پرانرژی | `default`، `app-store` |
| `happy-beats-business-moves-vol-9-by-ende-dot-app.mp3` | ۱:۵۴ | متوسط و کمی آرام‌تر | `default`، `yc-parody` |
| `happy-beats-business-moves-vol-10-by-ende-dot-app.mp3` | ۱:۰۰ | کوتاه و کوبنده | `default`، `chaotic` |
| `happy-beats-business-moves-vol-11-by-ende-dot-app.mp3` | ۱:۲۸ | گرم و کاری | `yc-parody`، `app-store` |
| `happy-beats-business-moves-vol-12-by-ende-dot-app.mp3` | ۱:۵۸ | یکنواخت و تمیز | `polished`، `cinematic` |

برای `deadpan` می‌توان vol-12 را با بلندی بسیار کم، حدود ۰٫۱۲ تا ۰٫۱۸، به‌کار برد. موسیقی را فقط وقتی خاموش کن که کاربر خواسته، فایل موجود نیست یا طرح آگاهانه سکوت را انتخاب کرده است.

### استفاده در ترکیب

پس از کپی فایل‌ها، مسیر نسبی از پوشهٔ `composition/` را بنویس. نمونه:

~~~html
<audio id="bg-music" data-start="0" data-duration="[duration]" data-track-index="10" data-volume="0.35" src="assets/music/happy-beats-business-moves-vol-1-by-ende-dot-app.mp3"></audio>
~~~

بلندی موسیقی معمولاً ۰٫۳۰ تا ۰٫۴۰ باشد و از ۰٫۵ بالاتر نرود. برای deadpan یا شوخی خویشتن‌دار ۰٫۱۲ تا ۰٫۲۲ مناسب است. افکت معمولاً ۰٫۵۵ تا ۰٫۸۵ است؛ در لحن polished یا deadpan نرم‌ترش کن. ابتدای و انتهای موسیقی را محو کن؛ هنگام گفتار آن را تا ۰٫۱۲ تا ۰٫۱۸ پایین بیاور و بعد به بلندی قبلی برگردان. افکت پایانی می‌تواند روی موسیقی بماند.

هر ترک صوتی هم‌پوشان `data-track-index` جداگانه و صعودی داشته باشد: مثلاً موسیقی ۱۰، صدای گویندگی ۱۱ و افکت بعدی ۱۲. شمارهٔ مشترک فقط وقتی مجاز است که کلیپ‌ها هم‌پوشانی نداشته باشند. Hyperframes قرارداد HTML و attributeها را تعیین می‌کند؛ از مستندات جاری خودش برای `data-start`، `data-duration`، `data-volume` و `data-track-index` پیروی کن.

## منبع beat و cue

برای هر ترک می‌توان beat sync ساخت؛ از غنی‌ترین منبعی که محیط پشتیبانی می‌کند استفاده کن:

۱. **ترک ضمیمه با preset آماده:** سریع و بدون وابستگی است. Markdown متناظر را بخوان و مسیر JSON را در `composition-brief.md` ثبت کن:

~~~
<skill-dir>/assets/music/cues/<track-stem>.music-cues.md
<skill-dir>/assets/music/cues/<track-stem>.music-cues.json
~~~

۲. **هر ترک با تحلیل کامل:** برای آهنگ دلخواه یا به‌روزرسانی preset از `analyze_music_cues.py` استفاده کن. `uv` وابستگی‌های `librosa`، `numpy`، `scipy` و `soundfile` را از `<skill-dir>/scripts/pyproject.toml` فراهم می‌کند:

~~~
uv run --project <skill-dir>/scripts python <skill-dir>/scripts/analyze_music_cues.py <track>.mp3 --output-json <output-dir>/composition/assets/music/cues/<stem>.music-cues.json --output-md <output-dir>/composition/assets/music/cues/<stem>.music-cues.md
~~~

۳. **هر ترک با `hyperframes beats`:** راه ساده و بدون وابستگی Python؛ نیازمند Hyperframes ۰٫۶٫۹۹ یا جدیدتر است. پس از واردکردن موسیقی اجرا کن:

~~~
npx hyperframes beats <output-dir>/composition
~~~

این دستور grid ضرب هر ترک و `strength` نرمال‌شدهٔ هر beat را می‌نویسد؛ آرایهٔ `strongCues` جدا ندارد، پس beatهای `strength` بالاتر را انتخاب کن. محل فایل خروجی را از راهنمای جاری `hyperframes-cli` بخوان. اگر نسخهٔ Hyperframes قدیمی است، روش تحلیل `uv` را به‌کار ببر؛ اگر هیچ‌کدام در دسترس نیست، در طرح بنویس که بدون cue ادامه می‌دهی.

preset و `analyze_music_cues.py` این اطلاعات را دارند: `duration`، `tempo`، آرایهٔ `beats` با `time` و `intensity`، آرایهٔ `strongCues` با `time` و `intensity` و نوع cue (`strong_beat` یا `onset_peak`)، و مشخصات `scoring`. خروجی `hyperframes beats` فقط grid و `strength` دارد.

cueها زمان‌بندی را پیشنهاد می‌کنند، نه کنترل: آشکارسازی اصلی را در صورت مناسب‌بودن تا حدود ±۰٫۱۵ ثانیه به cue قوی، و ورود کوچک را تا ±۰٫۱۰ ثانیه به beat نزدیک کن. برای هر ویدیوی ۱۵ تا ۲۵ ثانیه‌ای معمولاً ۱ تا ۳ قفل cue قوی کافی است. اگر cue خوانایی متن، ریتم صحنه یا قصهٔ محصول را خراب می‌کند، نادیده‌اش بگیر. برای لحن deadpan یا خویشتن‌دار cueها کم، آرام یا محدود به نشان پایانی باشند.

دادهٔ cue و beat جای واکنش بصری به موسیقی را نمی‌گیرد: cue برای زمان‌بندی ضرب و swell است؛ دادهٔ واکنش صوتی برای تغییر ظریف ویژگی‌های دیداری موجود.

## افزودن افکت به ترکیب

موسیقی را روی track-index پایین‌تر بگذار و هر افکت هم‌پوشان را روی index بالاتر. نمونهٔ قرارداد (جزئیات دقیق را از Hyperframes فعلی بگیر):

~~~html
<audio id="sfx-1" data-start="0.2" data-duration="1" data-track-index="11" data-volume="0.80" src="assets/sfx/interface/drop_001.ogg"></audio>
~~~

افکت باید همراه حرکت برسد و بلندی‌اش با روایت و موسیقی سنجیده شود. صدا را به تمام حرکات اضافه نکن؛ فقط کنش‌های دیداری یا لحظه‌های مهم را تقویت کن.
