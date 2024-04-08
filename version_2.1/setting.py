from dotenv import load_dotenv
import os

# Load environment variables from a .env file, if present.
load_dotenv()

# Retrieve configuration settings from environment variables.
# HOST: The host address for the server to bind to or the client to connect to.
HOST = os.getenv('HOST')

# PORT: The port number for the server to listen on or the client to connect to.
# It's important to note that PORT should be an integer, but os.getenv returns a string.
# Therefore, when using PORT, it should be converted to an integer where necessary.
PORT = int(os.getenv('PORT'))

# MESSAGE_SIZE: The maximum size of a message that can be sent or received.
# Similar to PORT, MESSAGE_SIZE should be used as an integer in the code.
MESSAGE_SIZE = int(os.getenv('MESSAGE_SIZE'))
