import os
import socket
import sys
from argparse import ArgumentParser
from contextlib import closing


def connect_to_host(host: str = "0.0.0.0", port: int = 9001, timeout_seconds: float = 5.0) -> None:
    """Establish a TCP connection to the specified host and port.

    Raises an exception if the connection fails.
    """
    with closing(socket.create_connection((host, port), timeout_seconds)) as sock:
        local_ip, local_port = sock.getsockname()
        print(f"Successfully connected to {host}:{port} from {local_ip}:{local_port}")


if __name__ == "__main__":
    parser = ArgumentParser(description="Simple TCP connectivity checker")
    parser.add_argument("--host", default=os.getenv("HOST", "0.0.0.0"))
    parser.add_argument("--port", type=int, default=int(os.getenv("PORT", "9001")))
    parser.add_argument("--timeout", type=float, default=float(os.getenv("TIMEOUT", "5.0")))
    args = parser.parse_args()

    try:
        connect_to_host(args.host, args.port, args.timeout)
    except Exception as exc:  # noqa: BLE001 - surface the error to stderr for visibility
        print(f"Connection to {args.host}:{args.port} failed: {exc}", file=sys.stderr)
        sys.exit(1)
