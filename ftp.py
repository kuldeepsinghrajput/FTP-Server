# Import the required modules
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Create an authorizer that allows anonymous access
authorizer = DummyAuthorizer()
authorizer.add_anonymous("C:\\Z_DND_STORE", perm="elradfmw")

# Create a handler that uses the authorizer
handler = FTPHandler
handler.authorizer = authorizer

# Create a server that listens on port 21
server = FTPServer(("0.0.0.0", 3725), handler)

# Start the server
server.serve_forever()
