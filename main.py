from run_pipeline import run_all
from src.jobs.run_ingestion_job import run_job


def menu():
    print("\n========================")
    print("HOMESCOPE CONTROL CENTER")
    print("========================")
    print("1. Run FULL pipeline")
    print("2. Run ingestion only")
    print("3. Exit")
    print("========================")


def main():
    while True:
        menu()
        choice = input("Select option: ")

        if choice == "1":
            run_all()

        elif choice == "2":
            run_job()

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()