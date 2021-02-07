from tkinter import *
import tkinter as tk


class App:
    """Creates an instance of the calculator application

    Attributes:
        master -- root
        title -- sets the title of the window
    """

    def __init__(self, master, title):
        self.master = master
        self.master.title(title)

        calc = Calculator(self.master, 1, 1)


class Calculator:
    """Create a calculator application.

    Attributes:
        window -- The window in which the application resides
        container -- The frame within the window that holds the calculator
        x_placement -- Placement relative to the x-axis
        y_placement -- Placement relative to the y-axis

    Methods:
        error_lbl(text, font_size, x_grid)
            Creates a label to display any error encountered.

        equation_lbl(text, font_size, x_grid)
            Creates an output screen that displays the equation entire
            equation.

        input_lbl(text, font_size, x_grid)
            Creates a label displaying the value(s) of the user's input
            prior to the event of entering a operator.

        button(text, x_grid, y_grid, bg_col='grey10', fg_col='white')
            Creates a regular button with a commands that displays the input
            of the button that has been clicked.

        button_clear(text, x_grid, y_grid, bg_col='grey25', fg_col='white')
            Creates a button that clears all inputs all inputs stored in the
            variables and anything being displayed on the labels.

        button_delete(text, x_grid, y_grid, bg_col='grey25', fg_col='white')
            A button with a command that deletes the most recent input.

        button_equals(text, x_grid, y_grid)
            A button with a command that evaluates the expression.

        normal_btn_click(value)
            Displays input of the input, number or operator, excluding the
            customized buttons.

        clear_btn_click()
            Clears all inputs from the screen including errors.

        equals_btn_click()
            Evaluates the equation and displays the value on the input label.

        delete_btn_click()
            Deletes most recent input.
    """

    # Class variables
    equation = ''  # Stores all input for the current session
    input_value = ''  # Temporary storage for all inputs

    def __init__(self, window: str, x_placement: int, y_placement: int):
        self.window = window

        # Framework
        self.container = tk.Frame(self.window)
        self.container.grid(row=x_placement, column=y_placement)

        # Widget configurations
        self.label_y_span = 4
        self.button_width = 10
        self.button_height = 3

        # Labels
        self.error_label = self.error_lbl('', '30', 0)
        self.equation_label = self.equation_lbl(self.equation, 20, 1)
        self.input_label = self.input_lbl('', 50, 2)
        print(type(self.error_label))

        # Buttons
        self.button_clear('C', 3, 0)
        self.button_delete('Del', 3, 1)
        self.button('%', 3, 2, 'grey25', 'white')
        self.button('/', 3, 3, 'orange', 'black')

        self.button('7', 4, 0)
        self.button('8', 4, 1)
        self.button('9', 4, 2)
        self.button('x', 4, 3, 'orange', 'black')

        self.button('4', 5, 0)
        self.button('5', 5, 1)
        self.button('6', 5, 2)
        self.button('-', 5, 3, 'orange', 'black')

        self.button('1', 6, 0)
        self.button('2', 6, 1)
        self.button('3', 6, 2)
        self.button('+', 6, 3, 'orange', 'black')

        self.button('-/+', 7, 0)
        self.button('0', 7, 1)
        self.button('.', 7, 2)
        self.button_equals('=', 7, 3)

    def error_lbl(self, text: str, font_size: str, x_grid: int):
        """Creates a label to display any error encountered.

        Args:
            text -- text to be displayed
            font_size -- adjusts the font size of the text
            x -- grid placement on the x-axis

        Returns:
            A label widget for displaying errors located above
            the equation label
        """

        self.lbl = tk.Label(
            self.container, text=text, font=font_size)
        self.lbl.grid(
            row=x_grid, columnspan=self.label_y_span, sticky=tk.W)

        return self.lbl

    def equation_lbl(self, text: str, font_size: str, x_grid: int):
        """Creates an output screen that displays the equation entire equation.

        Args:
            text -- text to be displayed
            font_size -- adjusts the font size of the text
            x -- grid placement on the x-axis

        Returns:
            A label widget for displaying the equation
        """

        self.lbl = tk.Label(
            self.container, text=text, font=font_size)
        self.lbl.grid(
            row=x_grid, columnspan=self.label_y_span, sticky=tk.E)

        return self.lbl

    def input_lbl(self, text: str, font_size: str, x_grid: int):
        """Creates a label displaying the value(s) of the user's input prior to
        the event of entering a operator.

        Args:
            text -- text to be displayed
            font_size -- adjusts the font size of the text
            x -- grid placement on the x-axis

        Returns:
            A label widget for displaying the inputs.
        """

        self.lbl = tk.Label(
            self.container, text=text, font=font_size)
        self.lbl.grid(
            row=x_grid, columnspan=self.label_y_span, sticky=tk.E)

        return self.lbl

    def button(self, text: str, x_grid: int, y_grid: int, bg_col='grey10', fg_col='white'):
        """Creates a regular button with a commands that displays the input
        of the button that has been clicked.


        Args:
            text -- text to be displayed
            x -- grid placement on the x-axis
            y -- grid placement on the y-axis
            bg_col -- Background colour of the widget
            fg_col -- Foreground colour of the text

        Returns:
            A standard button widget.
        """
        self.btn = tk.Button(
            self.container, text=text, width=self.button_width,
            height=self.button_height, borderwidth=2,
            command=lambda: self.normal_btn_click(text),
            bg=bg_col, fg=fg_col)
        self.btn.grid(row=x_grid, column=y_grid)

    def button_clear(self, text: str, x_grid: int, y_grid: int):
        """Creates a button that clears all inputs all inputs stored in the
        variables and anything being displayed on the labels.

        Args:
            text -- text to be displayed
            x -- grid placement on the x-axis
            y -- grid placement on the y-axis

        Returns:
            A customized button widget with the command clear_btn_click.
        """

        self.btn = tk.Button(
            self.container, text=text, width=self.button_width,
            height=self.button_height, borderwidth=2, bg='grey25', fg='white',
            command=self.clear_btn_click)
        self.btn.grid(row=x_grid, column=y_grid)

    def button_delete(self, text: str, x_grid: int, y_grid: int):
        """A button with a command that deletes the most recent input.

        Args:
            text -- text to be displayed
            x -- grid placement on the x-axis
            y -- grid placement on the y-axis

        Returns:
            A customized button widget with the command delete_btn_click.
        """

        self.btn = tk.Button(
            self.container, text=text, width=self.button_width,
            height=self.button_height, borderwidth=2, bg='grey25', fg='white',
            command=self.delete_btn_click)
        self.btn.grid(row=x_grid, column=y_grid)

    def button_equals(self, text: int, x_grid: int, y_grid: int):
        """A button with a command that evaluates the expression.

        Args:
            text -- text to be displayed
            x -- grid placement on the x-axis
            y -- grid placement on the y-axis

        Returns:
            A customized button widget with the command equals_btn_click.
        """

        self.btn = tk.Button(
            self.container, text=text, width=self.button_width,
            height=self.button_height, bg='orange', fg='black',
            borderwidth=2, command=self.equals_btn_click)
        self.btn.grid(row=x_grid, column=y_grid)

    # Functionality
    def normal_btn_click(self, value: str) -> str:
        """Displays input of the input, number or operator, excluding the
        customized buttons.

        Args:
            value -- passes the value of the button that was entered.

        Returns:
            The value that the button holds that has been entered.
        """

        # Clear error msg if there is any present
        self.error_label.config(text='')

        if value.isdigit():
            # Add the inputs to input_value and update the input_label
            self.input_value += value
            self.input_label.config(text=self.input_value)

        elif value == 'x':
            self.equation += self.input_value + '*'
            self.equation_label.config(text=self.equation)
            self.input_value = ''
            self.input_label.config(text=self.input_value)

        elif value == '-/+':
            # Determines whether to change the value of the number to a
            # positive or a negative
            find_minus = self.input_value.find('-')
            if find_minus == -1:
                # If there is no minus, add a minus before the input
                self.input_value = '-' + self.input_value
                self.input_label.config(text=self.input_value)
            else:
                # Remove the negation from the input
                self.input_value = self.input_value[1:]
                self.input_label.config(text=self.input_value)

        else:
            # If the input is an operator add the inputs and the operator
            # to the equation label and clear the input_value
            self.equation += self.input_value + value
            self.equation_label.config(text=self.equation)
            self.input_value = ''
            self.input_label.config(text=self.input_value)

    def clear_btn_click(self) -> None:
        """Clears all inputs from the screen including errors."""

        # Reset error Label
        self.error_label.config(text='')
        # Resets equation and the label
        self.equation = ''
        self.equation_label.configure(text='')
        # Resets the input_value and the input label
        self.input_value = ''
        self.input_label.configure(text='')

    def equals_btn_click(self) -> str:
        """Evaluates the equation and displays the value on the input label.

        Returns:
            The value of the evaluated expression.

        Raises:
            SyntaxError: If the evaulated expression doesn't result to a value
        """

        try:
            ans = eval(self.equation + self.input_value)
        except SyntaxError:
            error_msg = 'Invalid input'
            self.error_label.config(text=error_msg)
        else:
            # Add the last input value and an equals sign at the end,
            # then displays the result on the input label
            self.equation += self.input_value + '='
            self.equation_label.config(text=self.equation)
            self.input_label.config(text=ans)

    def delete_btn_click(self) -> None:
        """Deletes most recent input."""

        if self.input_value == '':
            # If the input label is empty, delete from the equation variable
            self.equation = self.equation[:-1]
            self.equation_label.config(text=self.equation)
        else:
            # Delete the most recent input
            self.input_value = self.input_value[:-1]
            self.input_label.config(text=self.input_value)


if __name__ == '__main__':
    root = tk.Tk()
    mainframe = App(root, 'Calculator')
    root.mainloop()
