#!/usr/bin/env python3
"""
Setup script for Energy Consumption Analysis Project
"""

import os
import subprocess
import sys


def run_command(command, description):
    """Run a command and handle errors"""
    print(f"🔄 {description}...")
    try:
        result = subprocess.run(
            command, shell=True, check=True, capture_output=True, text=True
        )
        print(f"✅ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} failed: {e.stderr}")
        return False


def main():
    print("🚀 Setting up Energy Consumption Analysis Project")
    print("=" * 60)

    # Check if virtual environment exists
    if not os.path.exists(".venv"):
        print("📦 Creating virtual environment...")
        if not run_command("python -m venv .venv", "Virtual environment creation"):
            return False
    else:
        print("✅ Virtual environment already exists")

    # Activate virtual environment and install requirements
    if sys.platform.startswith("win"):
        activate_cmd = ".venv\\Scripts\\activate"
        pip_cmd = ".venv\\Scripts\\pip"
    else:
        activate_cmd = "source .venv/bin/activate"
        pip_cmd = ".venv/bin/pip"

    # Install requirements
    install_cmd = f"{pip_cmd} install -r requirements.txt"
    if not run_command(install_cmd, "Installing requirements"):
        return False

    # Check if data exists
    if not os.path.exists("data/Energy_consumption.csv"):
        print("⚠️  Warning: Original dataset not found in data/ directory")
        print("   Please ensure Energy_consumption.csv is in the data/ folder")

    # Check if processed data exists
    if not os.path.exists("data/processed/energy_data_processed.csv"):
        print("⚠️  Warning: Processed data not found")
        print("   Please run the feature engineering notebook first")

    print("\n🎉 Setup completed successfully!")
    print("\n📋 Next steps:")
    print("1. Activate virtual environment:")
    if sys.platform.startswith("win"):
        print("   .venv\\Scripts\\activate")
    else:
        print("   source .venv/bin/activate")
    print("2. Launch Jupyter:")
    print("   jupyter notebook")
    print("3. Run notebooks in order:")
    print("   - 01_data_exploration.ipynb")
    print("   - 02_feature_engineering.ipynb")
    print("   - 03_model_development.ipynb")
    print("   - 04_model_evaluation.ipynb")
    print("   - 05_business_insights.ipynb")


if __name__ == "__main__":
    main()
