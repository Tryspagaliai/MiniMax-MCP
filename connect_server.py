import socket
import sys
from contextlib import closing


def connect_to_host(host: str = "0.0.0.0", port: int = 9001, timeout_seconds: float = 5.0) -> None:
    """Establish a TCP connection to the specified host and port.

    Raises an exception if the connection fails.
    """
    with closing(socket.create_connection((host, port), timeout_seconds)) as sock:
        local_ip, local_port = sock.getsockname()
        print(f"Successfully connected to {host}:{port} from {local_ip}:{local_port}")


if __name__ == "__main__":
    HOST = "0.0.0.0"
    PORT = 9001
    try:
        connect_to_host(HOST, PORT)
    except Exception as exc:  # noqa: BLE001 - surface the error to stderr for visibility
        print(f"Connection to {HOST}:{PORT} failed: {exc}", file=sys.stderr)
        sys.exit(1)
