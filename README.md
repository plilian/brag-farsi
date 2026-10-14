# Brag فارسی

نسخهٔ فارسیِ گردش‌کار متن‌باز [Brag](https://github.com/latent-spaces/brag) برای ساخت ویدیوی معرفی محصول. آدرس وب‌سایت یا مسیر پروژه را بده؛ مهارت سایت زنده را بررسی می‌کند، مسیر واقعی محصول را پیدا می‌کند، شواهد را ثبت می‌کند و با روایت فارسی، تایپوگرافی راست‌به‌چپ، موسیقی و افکت هماهنگ، ویدیوی MP4 می‌سازد.

این پروژه یک Agent Skill است و از ساختار مشترک مهارت‌ها استفاده می‌کند. نصب یکسان برای Claude Code، Codex، Gemini CLI و Qwen Code:

~~~sh
npx skills add plilian/brag-farsi --skill brag -a claude-code -a codex -a gemini-cli -a qwen-code
~~~

برای نصب سراسری، `-g` را اضافه کن. برای دیدن جزئیات نصب و پرسش‌های تأیید، گزینهٔ `-y` را اضافه نکن.

## نصب افزونهٔ بومی

برای Codex:

~~~text
codex plugin marketplace add plilian/brag-farsi
codex plugin add brag@brag-farsi
~~~

برای Claude Code:

~~~text
/plugin marketplace add plilian/brag-farsi
/plugin install brag@brag-farsi
~~~

Gemini CLI و Qwen Code از دستور مشترک `npx skills` بالا پشتیبانی می‌کنند. اگر خواستی نصب را از خود Gemini CLI انجام بدهی، از `gemini skills install https://github.com/plilian/brag-farsi` استفاده کن. برای نصب مستقیم در Qwen Code، پوشهٔ مهارت را در `~/.qwen/skills/brag/` قرار بده.

## شروع

از پوشهٔ پروژه اجرا کن و آدرس واقعی محصول را بده:

~~~text
/brag https://example.com
~~~

یا مسیر پروژهٔ محلی را به مهارت معرفی کن:

~~~text
/brag برای پروژهٔ ./path/to/product یک ویدیوی معرفی فارسی بساز.
~~~

پیش‌فرض‌ها فارسی ایران، صدای Mana، موسیقی و افکت‌های کم‌شمار است. دو انتخاب گویندگی همین‌ها هستند:

| صدا | ویژگی | اجرا |
| --- | --- | --- |
| **Mana** | صدای پیش‌فرضِ تأییدشده؛ متن روایت برای ساخت صدا به Space عمومی فرستاده می‌شود. | آنلاین؛ بدون کلید یا پرداخت |
| **Amir** | صدای مردانهٔ فارسی | Piper روی دستگاه؛ مدل حدود ۶۴ مگابایت است و بار اول دریافت می‌شود |

برای تغییر صدا یا خاموش‌کردن هر لایه، در درخواست بگو:

~~~text
/brag --voice amir
/brag --no-voice
/brag --no-music
/brag --no-sfx
~~~

پیش از استفاده از Mana، توجه کن که متن روایت به سرویس بیرونی می‌رود و کارت مدل استفاده را به پژوهش و توسعه محدود کرده است. برای ویدیوی تجاری باید از نگه‌دارندگان مجوز بگیری. راهنمای کامل در [اطلاعیهٔ مجوزها](THIRD_PARTY_NOTICES.md) است.

## بررسی درست محصول

اگر آدرس سایت داده شود، مهارت آن را در مرورگر باز می‌کند و صفحهٔ معرفی را از خود برنامه جدا می‌کند. مسیر اصلی را تا نتیجه دنبال می‌کند، فقط ادعاهایی را در متن می‌آورد که در سایت، رابط در حال اجرا یا کد محصول شاهد دارند، و برای هر ادعا منبع را در طرح داخلی می‌نویسد. اگر بخش برنامه نیاز به ورود داشته باشد، فقط از نشست مجاز و دادهٔ آزمایشی استفاده می‌کند؛ خرید، پرداخت، انتشار یا تغییر واقعی داده را انجام نمی‌دهد. اگر سایت در دسترس نباشد، چیزی را حدس نمی‌زند.

## فونت فارسی

فونت پیش‌فرض **Vazirmatn** است و فایل متغیرش همراه مهارت بسته‌بندی شده؛ برای رندر به نصب سیستم یا دانلود فونت وابسته نیست. برای انتخاب خودت بگو:

~~~text
/brag --font Estedad --title-font Lalezar
~~~

| فونت | کاربرد پیشنهادی |
| --- | --- |
| Vazirmatn | متن بدنه و زیرنویس؛ خوانایی بالا در قاب کوچک |
| Estedad | متن بدنه یا تیتر حرفه‌ای |
| Shabnam | لحن نرم و دوستانه |
| Sahel | لحن گرم و ساده |
| Lalezar | فقط تیتر نمایشی و کوتاه |

مهارت فونت را در پروژهٔ ویدیو محلی بار می‌کند و مجوزش را همراه فایل نگه می‌دارد. برای فونت‌های انتخابیِ دیگر از منبع رسمی استفاده کن. قواعد کامل شکل‌دهی فارسی، نیم‌فاصله، اعداد و قطعه‌های لاتین در [راهنمای تایپوگرافی فارسی](skills/brag/references/persian-typography.md) آمده است.

## مسیر ساخت

۱. وب‌سایت، رابط زنده و در صورت وجود کد پروژه را بررسی می‌کند و شواهد قابلیت‌ها را ثبت می‌کند.
۲. زاویهٔ خلاقه، قلاب آغازین، روایت و storyboard فارسی را بر اساس همان شواهد می‌چیند.
۳. رابط واقعی محصول را بازسازی یا قاب‌بندی می‌کند؛ از تصویرهای سایت فقط به‌عنوان مرجع استفاده می‌کند.
۴. ترکیب، حرکت، صدا و رندر را با Hyperframes می‌سازد و خروجی را از نظر فارسی، زمان‌بندی و ادعاها بازبینی می‌کند.

خروجی نهایی مهارت MP4 است. طرح، صداها و فایل‌های میانی داخل پوشهٔ `work/` می‌مانند. اجرای کامل با هر چهار ابزار یکسان است؛ نسخهٔ کم‌حجم `brag-slim` فقط وقتی استفاده می‌شود که خودت صریحاً حالت سبک را بخواهی.

### انتخاب سبک و قاب

~~~text
/brag --format vertical --tone polished --duration 20
~~~

قاب‌ها: `landscape`، `vertical`، `square`. لحن‌ها: `default`، `polished`، `yc-parody`، `chaotic`، `deadpan`، `cinematic` و `app-store`. درخواست عادی را هم می‌توانی با زبان طبیعی بنویسی؛ خواستهٔ صریح تو مقدم است.

## نیازمندی‌ها

- یکی از Claude Code، Codex، Gemini CLI یا Qwen Code؛
- Node.js نسخهٔ ۲۲ یا بالاتر و Hyperframes CLI برای ساخت ویدیو؛
- FFmpeg در `PATH`؛
- Python نسخهٔ ۳٫۱۱ یا بالاتر برای اسکریپت‌های صدا و تحلیل موسیقی؛
- برای Mana بستهٔ `gradio_client`؛ برای Amir بستهٔ `piper-tts`.

برای ساخت دستی گویندگی، ابتدا متن UTF-8 را در فایل ذخیره کن:

~~~sh
python -m pip install gradio_client
python skills/brag/scripts/generate_persian_voiceover.py path/to/voiceover.txt --voice mana --output path/to/voiceover.wav
~~~

~~~sh
python -m pip install piper-tts
python skills/brag/scripts/generate_persian_voiceover.py path/to/voiceover.txt --voice amir --output path/to/voiceover.wav
~~~

## مجوز و نگه‌داری

کد و مستندات این مخزن تحت MIT و با حفظ اعتبار پروژهٔ اصلی Brag عرضه می‌شوند. موسیقی، افکت‌ها، فونت‌ها و مدل‌های گفتار مجوزهای جداگانه دارند؛ اعتبار و محدودیت هرکدام در [اطلاعیهٔ دارایی‌های ثالث](THIRD_PARTY_NOTICES.md) ثبت شده است. فایل ویدیوی ساخته‌شده جزو مخزن منبع نیست.

## منابع

- [مخزن اصلی Brag](https://github.com/latent-spaces/brag)
- [راهنمای Agent Skills در skills CLI](https://github.com/vercel-labs/skills)
- [مستندات مهارت‌های Gemini CLI](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/using-agent-skills.md)
- [مستندات مهارت‌های Qwen Code](https://github.com/QwenLM/qwen-code/blob/main/docs/users/features/skills.md)
- [مستندات بسته‌بندی افزونهٔ Codex](https://developers.openai.com/plugins/build/plugins)
- [Space صدای Mana](https://huggingface.co/spaces/abreza/mana-tts) و [کارت مدل](https://huggingface.co/MahtaFetrat/Persian-Tacotron2-on-ManaTTS)
- [Piper](https://github.com/OHF-Voice/piper1-gpl)، [مدل فارسی Amir](https://huggingface.co/rhasspy/piper-voices/tree/main/fa/fa_IR/amir/medium)
- [Vazirmatn](https://github.com/rastikerdar/vazirmatn)، [Estedad](https://github.com/aminabedi68/Estedad)، [Shabnam](https://github.com/rastikerdar/shabnam-font)، [Sahel](https://github.com/rastikerdar/sahel-font)، [Lalezar](https://github.com/BornaIz/Lalezar)
