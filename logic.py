from PyQt6.QtWidgets import QWidget
from gui import Ui_Form
from vote_manager import VoteManager

class Logic(QWidget):

    """
    This class handles the main voting window
    also deals with the GUI and vote submission
    """

    def __init__(self) -> None:
        """
        This sets up the GUI and connects the submit button.
        """
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.manager = VoteManager("votes.txt")
        self.ui.pushButtonSubmit.clicked.connect(self.submit_vote)

    def submit_vote(self) -> None:
        """
        Handles the vote when the button is clicked
        """

        voter_id: str = self.ui.lineEditId.text().strip()

        if self.ui.radioJane.isChecked():
            candidate: str = "Topuria"

        elif self.ui.radioJohn.isChecked():
            candidate = "Gaethje"

        else:
            self.ui.labelMessage.setText("Select candidate")
            self.ui.labelMessage.setStyleSheet("color: red;")
            return


        try:
            message: str = self.manager.submit_vote(voter_id, candidate)
            self.ui.labelMessage.setText(message)
            self.ui.labelMessage.setStyleSheet("color: green;")
            self.ui.lineEditId.clear()
            self.ui.radioJane.setChecked(False)
            self.ui.radioJohn.setChecked(False)


        except ValueError as error:
            self.ui.labelMessage.setText(str(error))
            self.ui.labelMessage.setStyleSheet("color: red;")
