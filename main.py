import dotenv
dotenv.load_dotenv()
from prompt import queryInformation


if __name__ == "__main__":
    result = queryInformation(person_name="Yubaraj Shrestha")
    print(result)
