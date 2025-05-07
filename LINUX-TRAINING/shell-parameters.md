



| Variable | Description |
|----------|-------------|
| `$#`     | Stores the number of command-line arguments passed to the shell script. |
| `$?`     | Stores the exit status of the last executed command. |
| `$0`     | Stores the name of the script or shell program. |
| `$1`, `$2`, ... | Stores the first, second, etc., command-line arguments individually. |
| `$*`     | Stores all command-line arguments as a single word (space-separated). Not recommended in most cases. |
| `"$@"`   | Stores all command-line arguments, each quoted separately (`"$1"`, `"$2"`, ...). Recommended for looping over arguments. |
| `$!`     | Stores the process ID of the most recently executed background process. |
| `$$`     | Stores the process ID of the current shell. |
| `#!`     | Shebang: specifies the interpreter that should execute the script. |
| `$-`     | Displays the current shell flags (e.g., `-x`, `-v`, etc.). |


| Command         | Description |
|----------------|-------------|
| `set -e`        | Stops the script immediately if any command (including `declare`) exits with a non-zero status. |
| `set -x`        | Enables debugging mode; prints each command (including `declare`) to the terminal as it is executed. |



what is difference b/w it
p=cat id

p=$(cat id)
