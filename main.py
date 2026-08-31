from tqdm import tqdm
import time


def main():
    print("Hello from c02-l02-ein-projekt-anlegen!")
    for _ in tqdm(range(20)):
        time.sleep(0.05)
    print("Fertig!")


if __name__ == "__main__":
    main()
