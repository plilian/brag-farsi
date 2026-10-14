#!/usr/bin/env python3
"""ساخت گویندگی فارسی با یکی از دو صدای Mana یا Amir مردانه."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

MANA_SPACE = "abreza/mana-tts"
PIPER_VOICE = "fa_IR-amir-medium"


class PersianArgumentParser(argparse.ArgumentParser):
    """Render the CLI help headings in Persian."""

    def format_help(self) -> str:
        return super().format_help().replace("usage:", "روش اجرا:", 1)

    def format_usage(self) -> str:
        formatter = self._get_formatter()
        return formatter._format_usage(
            self.usage,
            self._actions,
            self._mutually_exclusive_groups,
            prefix="روش اجرا: ",
        )


def configure_console_encoding() -> None:
    """نمایش درست پیام‌های فارسی در کنسول ویندوز و خروجی هدایت‌شده."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is None:
            continue
        try:
            reconfigure(encoding="utf-8", errors="replace")
        except (OSError, ValueError):
            pass


def piper_cache_dir() -> Path:
    configured = os.environ.get("PERSIAN_TTS_CACHE_DIR")
    if configured:
        return Path(configured).expanduser()

    local_app_data = os.environ.get("LOCALAPPDATA")
    if local_app_data:
        return Path(local_app_data) / "brag" / "piper-voices"

    return Path.home() / ".cache" / "brag" / "piper-voices"


def generate_mana(text: str, output_path: Path, add_pauses: bool) -> None:
    try:
        from gradio_client import Client
    except ImportError as error:
        raise RuntimeError("برای صدای Mana اجرا کن: python -m pip install gradio_client") from error

    client = Client(MANA_SPACE, verbose=False)
    result = client.predict(
        text=text,
        add_pauses=add_pauses,
        api_name="/generate_speech",
    )
    if isinstance(result, dict):
        source_value = result.get("path") or result.get("name") or result.get("url")
    else:
        source_value = result
    if isinstance(source_value, (list, tuple)):
        source_value = source_value[0] if source_value else None
    if not source_value:
        raise RuntimeError("سرویس Mana فایل صوتی برنگرداند.")

    source_path = Path(str(source_value))
    if not source_path.is_file():
        raise RuntimeError(f"مسیر فایل صوتی برگشتی از Mana پیدا نشد: {source_value}")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source_path, output_path)


def generate_amir(text: str, output_path: Path) -> None:
    try:
        import piper  # noqa: F401 - بررسی نصب Piper پیش از اجرای فرمان آن
    except ImportError as error:
        raise RuntimeError("برای صدای مردانهٔ Amir اجرا کن: python -m pip install piper-tts") from error

    model_dir = piper_cache_dir()
    model_path = model_dir / f"{PIPER_VOICE}.onnx"
    model_config_path = model_dir / f"{PIPER_VOICE}.onnx.json"
    if not model_path.is_file() or not model_config_path.is_file():
        model_dir.mkdir(parents=True, exist_ok=True)
        print("بارگیری یک‌بارهٔ مدل صدای مردانهٔ Amir (حدود ۶۴ مگابایت)…")
        try:
            subprocess.run(
                [
                    sys.executable,
                    "-m",
                    "piper.download_voices",
                    PIPER_VOICE,
                    "--download-dir",
                    str(model_dir),
                ],
                check=True,
            )
        except subprocess.CalledProcessError as error:
            raise RuntimeError("بارگیری مدل Piper انجام نشد؛ اتصال اینترنت را بررسی کن.") from error

    output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(
            [
                sys.executable,
                "-m",
                "piper",
                "--model",
                str(model_path),
                "--output-file",
                str(output_path),
                "--sentence-silence",
                "0.25",
                "--",
                text.replace("\n", " "),
            ],
            check=True,
        )
    except subprocess.CalledProcessError as error:
        raise RuntimeError("ساخت صدای مردانهٔ Amir با Piper انجام نشد.") from error


def main() -> int:
    configure_console_encoding()
    parser = PersianArgumentParser(
        description="ساخت گویندگی فارسی با صدای Mana یا صدای مردانهٔ Amir",
        add_help=False,
    )
    parser._positionals.title = "ورودی‌ها"
    parser._optionals.title = "گزینه‌ها"
    parser.add_argument("-h", "--help", action="help", help="نمایش این راهنما و خروج")
    parser.add_argument("text", nargs="?", type=Path, help="فایل UTF-8 متن گویندگی")
    parser.add_argument("--output", type=Path, help="مسیر WAV خروجی")
    parser.add_argument(
        "--voice",
        choices=("mana", "amir"),
        default="mana",
        help="صدای فارسی: mana (صدای تأییدشده) یا amir (صدای مردانهٔ محلی)",
    )
    parser.add_argument(
        "--no-segment-pauses",
        action="store_true",
        help="حذف مکث‌های کوتاه Mana میان بخش‌های روایت؛ فقط برای --voice mana",
    )
    parser.add_argument(
        "--list-voices",
        action="store_true",
        help="نمایش دو صدای فارسی موجود",
    )
    args = parser.parse_args()

    if args.list_voices:
        print("mana | صدای آنلاینِ نمونه‌شنوی‌شده؛ بدون کلید API یا پرداخت")
        print("amir | صدای مردانهٔ Piper؛ اجرا روی دستگاه، با بارگیری یک‌بارهٔ مدل")
        return 0

    if not args.text or not args.output:
        parser.error("برای ساخت صدا، فایل متن و --output لازم است.")
    if args.output.suffix.lower() != ".wav":
        parser.error("هر دو صدای فارسی فایل WAV می‌سازند؛ پسوند --output را .wav بگذار.")
    if args.voice == "amir" and args.no_segment_pauses:
        parser.error("--no-segment-pauses فقط برای --voice mana قابل استفاده است.")

    try:
        text = args.text.read_text(encoding="utf-8").strip()
        if not text:
            raise ValueError("متن روایت خالی است.")

        if args.voice == "mana":
            generate_mana(text, args.output, add_pauses=not args.no_segment_pauses)
        else:
            generate_amir(text, args.output)

        print(f"گویندگی فارسی ذخیره شد: {args.output}")
    except (OSError, ValueError, RuntimeError) as error:
        print(f"ساخت گویندگی انجام نشد: {error}", file=sys.stderr)
        if args.voice == "mana":
            print("برای Mana اینترنت لازم است؛ کلید API یا حساب پرداخت لازم نیست.", file=sys.stderr)
        else:
            print(
                "صدای Amir روی دستگاه اجرا می‌شود؛ برای بارگیری یک‌بارهٔ مدل اینترنت لازم است، اما کلید یا پرداخت لازم نیست.",
                file=sys.stderr,
            )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
