#simple setup for running main via the terminal under specific specs laid out in prompt:
#python3 LastName_UCP.py <input file>

# python3 Macro
PYTHON = python3

# store run function
.PHONY = run

#default:
#    Wullen_UCP.py = $(main.py)
#    python3 Wullen_UCP.py C://Users//pwull//PyCharmProjects//ExactUCP

run:
    ${PYTHON} main.py C://Users//pwull//PyCharmProjects//ExactUCP