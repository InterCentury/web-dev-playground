import os

def touch(file_path):
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "a"):
        pass

def create_ml_dl_structure(base_path):
    paths = [
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

        # datasets & notebooks
        "datasets/README.md",
        "notebooks/experiments.ipynb",

        # experiments & notes
        "experiments/sandbox.py",
        "notes/learning_log.md",
        "notes/roadmap.md",

        # root files
        "requirements.txt",
        "README.md",
    ]

    for relative_path in paths:
        full_path = os.path.join(base_path, relative_path)
        touch(full_path)

    print("\n✅ ML/DL detailed structure created successfully")
    print(f"📁 Location: {base_path}")

if __name__ == "__main__":
    print("📦 ML/DL Learning Journey Structure Generator\n")
    base_path = input("Enter the full project path:\n> ").strip()

    if not base_path:
        print("❌ Invalid path")
    else:
        create_ml_dl_structure(base_path)
