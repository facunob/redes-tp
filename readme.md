# Run localhost
- uvicorn main:app --reload
- python client.py

# Run multiple host, same network
- uvicorn main:app --host 0.0.0.0 --reload
- python client.py <ipv4-sever-host>