# made by Aryqman
import csv

class Candidate:
    def __init__(self, name):
        self.name = name
        self.votes = 0

    def increment_votes(self):
        self.votes += 1


class VotingMachine:
    def __init__(self, candidates):
        self.candidates = candidates
        self.data_file = 'voting_data.csv'

        # Load existing voting data from the CSV file
        self.load_data()

    def load_data(self):
        try:
            with open(self.data_file, 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    candidate_name, vote_count = row
                    for candidate in self.candidates:
                        if candidate.name == candidate_name:
                            candidate.votes = int(vote_count)
        except FileNotFoundError:
            # If the data file doesn't exist, it will be created when saving the results
            pass  # Add this line to avoid the indentation error

    def save_data(self):
        with open(self.data_file, 'w', newline='') as file:
            writer = csv.writer(file)
            for candidate in self.candidates:
                writer.writerow([candidate.name, candidate.votes])

    def vote(self, candidate_index):
        if candidate_index < 0 or candidate_index >= len(self.candidates):
            print("Invalid candidate index!")
            return

        candidate = self.candidates[candidate_index]
        candidate.increment_votes()
        print(f"Thank you for votin!")

    def display_results(self):
        print("Election Results:")
        for candidate in self.candidates:
            print(f"{candidate.name}: {candidate.votes} votes")

    def run_voting_machine(self):
        try:
            while True:
                print("\n==== Voting for Head Boy ====")
                print("Candidates:")
                for i, candidate in enumerate(self.candidates):
                    print(f"{i + 1}. {candidate.name}")
                

                choice = input("Enter the candidate number: ")
                if choice == '0':
                    break

                try:
                    candidate_index = int(choice) - 1
                    self.vote(candidate_index)
                except ValueError:
                    print("Invalid choice! Please enter a valid candidate number.")

        except KeyboardInterrupt:
            print("Voting process interrupted.")

        finally:
            self.save_data()
            self.display_results()


# Sample usage
candidates = [
    Candidate("Candidate A"),
    Candidate("Candidate B"),
    Candidate("Candidate C"),
    Candidate("Candidate D"),
]

voting_machine = VotingMachine(candidates)
voting_machine.run_voting_machine()
