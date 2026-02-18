import sys


def main():
    print("=== Player Score Analytics ===")
    args: list[str] = sys.argv

    if len(args) < 2:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        scores: list[int] = []
        try:
            for i in range(1, len(args)):
                scores.append(int(args[i]))
            print(f"Scores processed: {scores}")
            print(f"Total player: {len(scores)}")
            print(f"Total score: {sum(scores)}")
            print(f"Average score: {sum(scores) / len(scores)}")
            print(f"Hight score: {max(scores)}")
            print(f"Low score: {min(scores)}")
            print(f"Score range: {max(scores) - min(scores)}")
        except ValueError as e:
            print(f"Error: {e}")

    

if __name__ == "__main__":
    main()
