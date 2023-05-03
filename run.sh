if !command -v python &> /dev/null
then
    echo "Python could not be found. Please install Python and try again."
    exit 1
fi
python disasm.py $1
read -p "Press enter to continue"