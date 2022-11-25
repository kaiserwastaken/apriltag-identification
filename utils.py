from datetime import datetime



def log(message, level="[INFO]"):
    now = datetime.now()
    formatted_time = now.strftime("%H:%M:%S, %d/%m/%Y")
    print(f"{level}: {message}  |{formatted_time}")

