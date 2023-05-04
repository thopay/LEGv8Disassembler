if command -v python >/dev/null 2>&1; then
    PYTHON_CMD="python"
elif command -v python3 >/dev/null 2>&1; then
    PYTHON_CMD="python3"
elif command -v py >/dev/null 2>&1; then
    PYTHON_CMD="py"
else
    echo "Python is not installed or not in the PATH. Please install Python or add it to the PATH."
    exit 1
fi

$PYTHON_CMD disasm.py $1
read -p "Press enter to continue"
