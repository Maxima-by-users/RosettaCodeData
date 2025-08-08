import os
import shutil

# Path to the Task directory
TASKS_DIR = os.path.join(os.path.dirname(__file__), '..', 'Task')

# Loop through each task folder
for task_name in os.listdir(TASKS_DIR):
    task_path = os.path.join(TASKS_DIR, task_name)
    if not os.path.isdir(task_path):
        continue
    for item in os.listdir(task_path):
        item_path = os.path.join(task_path, item)
        # Only preserve 00-TASK.txt, Common-Lisp, and Maxima
        if item in ('00-TASK.txt', 'Common-Lisp', 'Maxima'):
            continue
        try:
            if os.path.isfile(item_path) or os.path.islink(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        except Exception as e:
            print(f"Error deleting {item_path}: {e}")
