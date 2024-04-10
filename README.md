# Server-Client-MSP-using-socket-programing

## Installation

1. Create a new environment Python versions
```
conda -n socket_env python 3.9.13
```
2. Activate environment variable
```
conda activate socket_env
```

3. Install python dependence
```
pip install -r requirements.txt
```

## Run version_2.1 
1. Run server.py Once run it will run continuously
```
python version_2.1/server.py
```

2. Then Run client.py It one go run
```
python version_2.1/client.py
```


## Run version_2.2
1. Run server.py Once run it will run continuously
```
python version_2.2/server.py --h 0.0.0.0 -p 9999
```

2. Then Run client.py It one go run
```
python version_2.1/client.py --h ip_address
```
