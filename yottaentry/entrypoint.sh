#!/bin/bash
/opt/yottadb/current/ydb << "EOF"
D ^%GI
/home/yotta/cars.go
Y
EOF
chmod +x /tmp/run.sh
/tmp/run.sh
