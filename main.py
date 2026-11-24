# Entry writer: emits the fixed entry text to /output/entry.txt
import os


def main():
    entry = 'At 7:22 today, my 78-year-old dad sent his first voice note: six seconds of his kettle whistling, a startled "oh!", and him laughing, "Did I just mail you steam?"'
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(entry)


if __name__ == "__main__":
    main()
