from google.oauth2 import service_account
from google.cloud import secretmanager_v1


# You need to replace PROJECT_NUMBER and SECRET_NAME with yours
SECRET_PATH = 'project/PROJECT_NUMBER/secrets/SECRET_NAME/versions/latest'
FILENAME = 'PATH_TO_SERVICE_ACCOUNT_KEY_FILE'


def get_secret(secret_path: str) -> str:
    credentials = service_account.Credentials.from_service_account_file(filename=FILENAME)
    client = secretmanager_v1.SecretManagerServiceClient(credentials=credentials)
    response = client.access_secret_version(request={'name': secret_path})
    secret = response.payload.data.decode('utf-8')
    return secret


def main():

    # The below secret is Python string containing your secret you created in Google Cloud Secret Manager
    secret = get_secret(SECRET_PATH)


if __name__ == '__main__':
    main()
