import kagglehub

# Login menggunakan API Token
kagglehub.login()

# Download Titanic competition
path = kagglehub.competition_download('titanic')

print("Dataset downloaded to:", path)