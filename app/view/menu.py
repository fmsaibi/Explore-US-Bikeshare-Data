from app.constants import DisplayMessages, ErrorMessages, CommonConstants
import pandas as pd

class Menu:
    """
    (module) Menu
    """
    def get_menu(self, question:str, items:list) -> str:
        """
        Take user input from the terminal or command prompt, based on the display period list

        Args:
            User Input: Numeric value or String associated with the period table

        Returns:
            String: The Name of the Period selected
        
        Raise:
            Invalid Mesaage: If the input is invalid or not in the list provided
        """
        selected = str()
        print(question)
        menu_table = pd.Series(data=items, index=range(1, len(items)+1))

        for index, value in menu_table.items():
            if value is not CommonConstants.NULL:
                print(f'{index}. {value.title()}')

        while not selected:
            user_input = input(DisplayMessages.INPUT_HERE)
            try:
                if (user_input.lower() in menu_table.values) or \
                    (int(user_input) in menu_table.index):
                    if user_input.isnumeric():
                        selected = menu_table[int(user_input)]
                    else:
                        selected = user_input.lower()
                else:
                    print(ErrorMessages.INVALID_INPUT)
            except ValueError:
                print(ErrorMessages.INVALID_INPUT)

        print(CommonConstants.LINE)

        return selected
