
# Working with Sets
from pyscript import display, document

grade_7 = {
    "Vita De Guzman",
    "Franchesca Dela Rosa",
    "MJ Madrelejos"
}

grade_8 = {
    "Julia Hadji Gapor",
    "Gurleen Kaur",
    "Chalanie Lumbang"
}

grade_9 = {
    "Santiago Valdez",
    "Kenneth Concepcion",
    "Raver Estacio"
}

grade_10 = {
    "Miguel Jimenez",
    "JJ Villante"
}

master_members = grade_7 | grade_8 | grade_9 | grade_10

def show_members():
    document.querySelector("#output").innerHTML = ""

    display("ALL CLUB MEMBERS", target="output")
    display(sorted(master_members), target="output")

    display(f"Total members: {len(master_members)}", target="output")

    display("GRADE 7", target="output")
    display(sorted(grade_7), target="output")

    display("GRADE 8", target="output")
    display(sorted(grade_8), target="output")

    display("GRADE 9", target="output")
    display(sorted(grade_9), target="output")

    display("GRADE 10", target="output")
    display(sorted(grade_10), target="output")

def add_member(event):
    first_name = document.querySelector("#first_name").value.strip()
    last_name = document.querySelector("#last_name").value.strip()

    full_name = f"{first_name} {last_name}"

    master_members.update({full_name})

    document.querySelector("#first_name").value = ""
    document.querySelector("#last_name").value = ""

    show_members()

show_members()
