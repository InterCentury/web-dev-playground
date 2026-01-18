import os

def create_structure(base_path):
    folders = [
        "01_python_basics/notebooks",
        "01_python_basics/scripts",

        "02_math_for_ml/linear_algebra",
        "02_math_for_ml/probability_statistics",
        "02_math_for_ml/calculus",

        "03_machine_learning/supervised/linear_regression",
        "03_machine_learning/supervised/logistic_regression",
        "03_machine_learning/supervised/decision_trees",
        "03_machine_learning/unsupervised/kmeans",
        "03_machine_learning/unsupervised/pca",
        "03_machine_learning/evaluation_metrics",

        "04_deep_learning/neural_network_basics",
        "04_deep_learning/cnn",
        "04_deep_learning/rnn",

        "datasets",
        "experiments",
        "notes"
    ]

    for folder in folders:
        path = os.path.join(base_path, folder)
        os.makedirs(path, exist_ok=True)

    # Create some starter files
    open(os.path.join(base_path, "README.md"), "a").close()
    open(os.path.join(base_path, "requirements.txt"), "a").close()
    open(os.path.join(base_path, "notes", "learning_log.md"), "a").close()

    print("\n✅ ML/DL learning journey structure created successfully!")
    print(f"📁 Location: {base_path}")


if __name__ == "__main__":
    print("📌 ML & DL Learning Journey Folder Generator\n")

    base_path = input("Enter the full path where you want to create the project:\n> ").strip()

    if not base_path:
        print("❌ Path cannot be empty.")
    else:
        create_structure(base_path)
