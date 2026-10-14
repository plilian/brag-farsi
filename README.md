<div align="center">
  <img src="assets/brag-farsi-banner.svg" alt="نمای گرافیکی از تبدیل مسیر محصول به ویدیوی فارسی" width="100%" />
  <h1>Brag فارسی</h1>
  <p dir="rtl"><strong>از مسیر واقعی محصول تا ویدیوی معرفی فارسی</strong></p>
  <p>
    <a href="LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-8b7cf6?style=flat-square" /></a>
    <img alt="زبان فارسی" src="https://img.shields.io/badge/language-Persian-168f75?style=flat-square" />
    <img alt="Claude Code" src="https://img.shields.io/badge/Claude_Code-supported-6b58c7?style=flat-square" />
    <img alt="Codex" src="https://img.shields.io/badge/Codex-supported-20242e?style=flat-square" />
    <img alt="Gemini CLI" src="https://img.shields.io/badge/Gemini_CLI-supported-3478f6?style=flat-square" />
    <img alt="Qwen Code" src="https://img.shields.io/badge/Qwen_Code-supported-7b58c8?style=flat-square" />
  </p>
</div>

یک نسخهٔ فارسی از گردش‌کار متن‌باز [Brag](https://github.com/latent-spaces/brag): آدرس سایت یا مسیر پروژه را به مهارت بده تا محصول را بررسی کند، سناریو و storyboard بسازد و ویدیوی کوتاه فارسی را با چیدمان راست‌به‌چپ، گویندگی و موسیقی رندر کند. خروجی نهایی یک فایل MP4 است.

## شروع سریع

با [skills CLI](https://github.com/vercel-labs/skills) مهارت کامل را برای ابزارهای دلخواه نصب کن:

```sh
npx skills add plilian/brag-farsi --skill brag -a claude-code -a codex -a gemini-cli -a qwen-code
```

از پوشهٔ پروژه در عامل کدنویسی اجرا کن:

```text
/brag https://example.com
```

یا مسیر پروژهٔ محلی را بده:

```text
/brag برای پروژهٔ ./path/to/product یک ویدیوی معرفی فارسی بساز.
```

## گردش‌کار

۱. سایت را باز می‌کند و مسیر اصلی محصول را تا نتیجه دنبال می‌کند؛ صفحهٔ معرفی را با خود محصول اشتباه نمی‌گیرد.
۲. قابلیت‌ها و ادعاهای قابل‌استناد را ثبت می‌کند و بر همان اساس قلاب، روایت و طرح صحنه‌ها را می‌چیند.
۳. صحنه‌ها را با رابط محصول، تایپوگرافی راست‌به‌چپ، گفتار و صدای هماهنگ می‌سازد.
۴. پیش‌نمایش را از نظر فارسی، خوانایی، صدا و دقت محصول بازبینی می‌کند و MP4 را تحویل می‌دهد.

خرید، پرداخت یا تغییر واقعی داده انجام نمی‌شود. برای بخش‌هایی که ورود می‌خواهند، فقط از نشست مجاز یا محیط نمایشی استفاده کن.

## گفتار فارسی

| گزینه | شیوهٔ ساخت | نکته |
| --- | --- | --- |
| **Mana** | آنلاین، بدون کلید API | متن روایت برای ساخت صدا به Space عمومی فرستاده می‌شود. کارت مدل استفاده را به پژوهش و توسعه محدود می‌کند؛ برای استفادهٔ تجاری مجوز لازم است. |
| **Amir** | Piper روی دستگاه | صدای مردانهٔ فارسی؛ مدل در اجرای اول دریافت می‌شود و متن برای ساخت صدا به سرویس بیرونی فرستاده نمی‌شود. |

Mana صدای پیش‌فرض است. برای انتخاب Amir یا خاموش‌کردن صدا، موسیقی یا افکت‌ها:

```text
/brag --voice amir
/brag --no-voice
/brag --no-music
/brag --no-sfx
```

هر دو گزینه بدون API key و پرداخت کار می‌کنند. جزئیات و محدودیت مجوزها در [اطلاعیهٔ دارایی‌های ثالث](THIRD_PARTY_NOTICES.md) آمده است.

## فارسی و تایپوگرافی

- متن، روایت و زیرنویس به فارسی ایران نوشته می‌شود؛ نام رسمی برند، URL و عبارت فنی لازم دست‌نخورده می‌ماند.
- چیدمان راست‌به‌چپ و نشانه‌گذاری فارسی رعایت می‌شود؛ اعراب لازم برای تلفظ پیش از ساخت گفتار اضافه می‌شود.
- **Vazirmatn** فونت پیش‌فرض است و فایل فونت و مجوزش همراه مهارت می‌آیند. می‌توانی **Estedad**، **Shabnam**، **Sahel** یا **Lalezar** را برای تیتر انتخاب کنی.
- روش استفاده از فونت و قواعد فاصله‌گذاری و ترکیب متن فارسی و لاتین در [راهنمای تایپوگرافی](skills/brag/references/persian-typography.md) توضیح داده شده است.

## پیش‌نیازهای رندر

- Claude Code، Codex، Gemini CLI یا Qwen Code؛
- Node.js نسخهٔ ۲۲ یا بالاتر و Hyperframes CLI برای ساخت ویدیو؛
- FFmpeg؛
- Python نسخهٔ ۳٫۱۱ یا بالاتر برای اسکریپت‌های صوتی؛
- بستهٔ `gradio_client` برای Mana یا `piper-tts` برای Amir.

خروجی هر اجرا در پوشهٔ `brag-output/` ساخته می‌شود؛ فایل نهایی `brag.mp4` است. اگر این پوشه از قبل وجود داشته باشد، مهارت پوشهٔ تازه‌ای با زمان اجرا می‌سازد.

## مجوزها و اعتبار

کد و مستندات این مخزن تحت مجوز MIT هستند و این پروژه بر پایهٔ [Brag اصلی](https://github.com/latent-spaces/brag) ساخته شده است. موسیقی‌های ضمیمه‌شده CC BY 4.0 هستند و افکت‌ها CC0؛ گفتار، فونت و وابستگی‌ها مجوزهای جداگانه دارند. پیش از بازنشر یا استفاده، [اطلاعیهٔ کامل مجوزها و اعتباردهی](THIRD_PARTY_NOTICES.md) را بخوان.

---

<p align="center" dir="rtl">اگر برای فارسی‌سازی یا سازگاری با عامل دیگری بهبودی داری، issue یا pull request باز کن.</p>
