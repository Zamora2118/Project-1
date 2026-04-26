import os

class VoteManager:
    """
    The class handles checking votes and saving them to the file
    """

    def __init__(self, filename: str) -> None:
        """
        This stores the file name for the votes.
        """
        self._filename: str = filename

    def has_voted(self, voter_id: str) -> bool:
        """
        This checks if an ID already voted before.
        """
        if not os.path.exists(self._filename):
            return False

        try:
            with open(self._filename, "r") as file:
                for line in file:
                    parts: list[str] = line.strip().split(",")

                    if len(parts) == 2 and parts[0] == voter_id:
                        return True
        except Exception:
            return False

        return False

    def save_vote(self, voter_id: str, candidate: str) -> None:
        """
        Saves one vote to the file
        """
        try:
            with open(self._filename, "a") as file:
                file.write(voter_id + "," + candidate + "\n")
        except Exception:
            raise ValueError("Problem saving vote")

    def submit_vote(self, voter_id: str, candidate: str) -> str:
        """
        Checks the vote info and saves it if everything is good
        """
        if voter_id == "":
            raise ValueError("Enter ID")

        if not voter_id.isdigit():
            raise ValueError("ID must be numeric")

        if len(voter_id) != 4:
            raise ValueError("ID must be 4 digits")

        if self.has_voted(voter_id):
            raise ValueError("Already Voted")

        self.save_vote(voter_id, candidate)
        return "Vote Submitted"