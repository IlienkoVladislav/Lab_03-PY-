from datetime import date


class Person:
    """
    Class to represent a contact book entry.
    """

    def __init__(self, surname, first_name, birth_date, nickname=None):
        """
        Initialize a class instance.

        Args:
            surname (str): Contact's last name.
            first_name (str): Contact's first name.
            birth_date (str): Birth date in YYYY-MM-DD format.
            nickname (str, optional): Contact's nickname.
        """
        self.surname = surname
        self.first_name = first_name
        self.nickname = nickname
        self.birth_date = self._parse_birth_date(birth_date)

    def _parse_birth_date(self, birth_date_str):
        """
        Convert birth date string to datetime.date object.

        Args:
            birth_date_str (str): Birth date in YYYY-MM-DD format.

        Returns:
            datetime.date: Birth date object.
        """
        year, month, day = map(int, birth_date_str.split("-"))
        return date(year, month, day)

    def get_age(self):
        """
        Calculates the person's age in full years.

        Returns:
            str: Age in "N" format.
        """
        today = date.today()
        years = today.year - self.birth_date.year
        if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
            years -= 1
        return str(years)

    def get_fullname(self):
        """
        Returns the contact's full name.

        Returns:
            str: Full name (last name + first name).
        """
        full_name = f"{self.surname} {self.first_name}"
        if self.nickname:
            full_name += f" ({self.nickname})"
        return full_name


person1 = Person("Komarov", "Dmitro", "1986-02-01", "TheWorld")
person2 = Person("Dniprov", "Andriy", "2002-11-03", "JoskiyDruce")

print(f"Full name: {person1.get_fullname()}")  
print(f"Age: {person1.get_age()} years")  

print(f"\nFull name: {person2.get_fullname()}") 
print(f"Age: {person2.get_age()} years") 

def modifier(filename):
    """
    Modifies a file containing contact data by adding full name and age columns.

    Args:
        filename (str): Path to the file to modify.
    """
    full_path = "C:\Users\iceco\OneDrive\Рабочий стол\Lab_03/contacts.txt" 

    with open(full_path, 'r') as file:
        data = file.read()

