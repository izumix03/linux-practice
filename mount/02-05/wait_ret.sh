#! /bin/bash
false &
wait $! # falseの終了待ち
echo "false 終了!: $?"