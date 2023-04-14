debug = False
popupDebug = False


def NewProcess(process_name):
    print(">========[ CLOSE PROCESS ]========<")
    print("")
    print("")
    print(">=========[ NEW PROCESS ]=========<")
    print("==>> " + process_name)
    print(">=================================<")


def ClearLine():
    print(">---------------------------------<")


def PrintError(error_output, data = ""):
    output_string = str(error_output) + " " + str(data)

    print("")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(">> Opps Loggy Had An Accident!")
    print(">> " + output_string)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("")


def PrintErrorPause(error_output, data = ""):
    output_string = str(error_output) + " " + str(data)

    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(">> Opps Loggy Had An Accident!")
    print(">> " + output_string)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("")
    input("==> Press Enter To Continue....")

def PrintImport(import_output, data = ""):
    output_string = str(import_output) + " " + str(data)

    print(":=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:")
    print(":=: Importing: " + output_string)
    print(":=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:=:")

def PrintStatement(statement_output, data = ""):
    output_string = str(statement_output) + " " + str(data)

    print(">~~~~~~~~~~{ STATEMENT }~~~~~~~~~~<")
    print(">> " + output_string)
    print(">~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~<")

def PrintSuccess(success_output, data = ""):
    output_string = str(success_output) + " " + str(data)

    print("===================================")
    print(">> (SUCCESS) " + output_string)
    print("===================================")


def PrintAlert(alert_output, data = ""):
    output_string = str(alert_output) + " " + str(data)

    print("***********************************")
    print(">> (ALERT) " + output_string)
    print("***********************************")

def Print(print_output, data = ""):
    output_string = str(print_output) + " " + str(data)
    print("==> " + print_output)

def PrintDebug(print_output, data = ""):
    if debug == True:         
        output_string = str(print_output) + " " + str(data)
        print("==> " + print_output)


