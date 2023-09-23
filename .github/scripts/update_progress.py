import datetime

def calculate_progress():
    today = datetime.date.today()
    start_of_year = datetime.date(today.year, 1, 1)
    end_of_year = datetime.date(today.year, 12, 31)
    
    days_passed = (today - start_of_year).days + 1
    total_days = (end_of_year - start_of_year).days + 1
    
    progress = days_passed / total_days
    return progress

def update_readme(progress):
    progress_bar_length = 120
    position = int(progress * progress_bar_length)

    track = "-" * progress_bar_length
    track_list = list(track)
    track_list[position] = '🚴‍♂️'
    track = "".join(track_list)
    
    with open("README.md", "r") as f:
        content = f.readlines()

    for idx, line in enumerate(content):
        if "今年の進捗度" in line:
            content[idx + 1] = f"スタート |{track}| ゴール {int(progress * 100)}%\n"
            break

    with open("README.md", "w") as f:
        f.writelines(content)

if __name__ == "__main__":
    progress = calculate_progress()
    update_readme(progress)

