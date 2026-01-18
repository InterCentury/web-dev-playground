import os

PLACEHOLDER_NAME = "placeholder.txt"

def ensure_folder_with_txt(folder_path):
    os.makedirs(folder_path, exist_ok=True)
    txt_path = os.path.join(folder_path, PLACEHOLDER_NAME)
    open(txt_path, "a").close()

def create_file(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "a").close()

def create_ml_dl_structure(base_path):
    folders = [
        # basics
        "basics",
        "basics/python",
        "basics/numpy",
        "basics/pandas",
        "basics/matplotlib",

        # math
        "math",
        "math/linear_algebra",
        "math/probability",
        "math/calculus",

        # machine learning
        "machine_learning",
        "machine_learning/supervised",
        "machine_learning/supervised/linear_regression",
        "machine_learning/supervised/logistic_regression",
        "machine_learning/supervised/decision_trees",
        "machine_learning/unsupervised",
        "machine_learning/unsupervised/kmeans",
        "machine_learning/unsupervised/pca",
        "machine_learning/evaluation",

        # deep learning
        "deep_learning",
        "deep_learning/fundamentals",
        "deep_learning/cnn",
        "deep_learning/rnn",

        # misc
        "datasets",
        "notebooks",
        "experiments",
        "notes",
    ]

    files = [
        # basics
        "basics/python/__init__.py",
        "basics/numpy/__init__.py",
        "basics/pandas/__init__.py",
        "basics/matplotlib/__init__.py",

        # math
        "math/linear_algebra/notes.md",
        "math/probability/notes.md",
        "math/calculus/notes.md",

        # machine learning
        "machine_learning/supervised/linear_regression/model.py",
        "machine_learning/supervised/logistic_regression/model.py",
        "machine_learning/supervised/decision_trees/model.py",
        "machine_learning/unsupervised/kmeans/model.py",
        "machine_learning/unsupervised/pca/model.py",
        "machine_learning/evaluation/metrics.py",

        # deep learning
        "deep_learning/fundamentals/nn_from_scratch.py",
        "deep_learning/cnn/cnn_model.py",
        "deep_learning/rnn/rnn_model.py",

        # misc
        "datasets/README.md",
        "notebooks/experiments.ipynb",
        "experiments/sandbox.py",
        "notes/learning_log.md",
        "notes/roadmap.md",

        # root
        "requirements.txt",
        "README.md",
    ]

    # Create folders + placeholder.txt
    for folder in folders:
        ensure_folder_with_txt(os.path.join(base_path, folder))

    # Create files
    for file in files:
        create_file(os.path.join(base_path, file))

    print("\n✅ Structure created successfully")
    print("📄 Every folder contains an empty placeholder.txt")
    print(f"📁 Location: {base_path}")

if __name__ == "__main__":
    print("📦 ML/DL Learning Journey Structure Generator\n")
    base_path = input("Enter full project path:\n> ").strip()

    if not base_path:
        print("❌ Path cannot be empty")
    else:
        create_ml_dl_structure(base_path)
