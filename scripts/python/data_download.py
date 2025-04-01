
import kagglehub
import os
import shutil

def download_college_data(output_dir="data/raw"):
    dataset_path = kagglehub.dataset_download("programmerrdai/comprehensive-u-s-college-scorecard-data")

    print(f"Dataset downloaded to: {dataset_path}")

    # Create output dir if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Copy files to data/raw/
    for file_name in os.listdir(dataset_path):
        full_file_path = os.path.join(dataset_path, file_name)
        destination_path = os.path.join(output_dir, file_name)
        
        if os.path.isfile(full_file_path):
            shutil.copy(full_file_path, destination_path)
            print(f"Copied file: {file_name}")
            
        elif os.path.isdir(full_file_path):
            shutil.copytree(full_file_path, destination_path, dirs_exist_ok=True)
            print(f"Copied directory: {file_name}")

    print(f"\nAll files copied to {output_dir}.")

if __name__ == "__main__":
    download_college_data()
