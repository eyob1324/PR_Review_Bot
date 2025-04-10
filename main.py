from github import Github 
import os


def get_pr_diff_from_api():
    try:
        github_token = os.environ.get("GITHUB_TOKEN")
        repo_name = os.environ.get("GITHUB_REPO")
        pull_number = int(os.environ.get("GITHUB_EVENT_PULL_REQUEST_NUMBER"))

        if not github_token or not repo_name or not pull_number:
            print("Error: Required environment variable not found")
            return None
        
        g = Github(github_token)
        repo = g.get_repo(repo_name)
        pull = repo.get_pull(pull_number)
        diff - pull.get_patch()
        return diff

    except Exception as e:
        print(f"An error occurred:{e}")
        return None






if __name__ == "__main__":
    diff_content = get_pr_diff_from_api()
    if diff_content:
        print("pull Request Diff (from API):")
        print(diff_content)

