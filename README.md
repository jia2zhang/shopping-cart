# shopping-cart

## Setup

Navigate to the repo on the command line

# Create the anaconda virtual environment
```sh
conda create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env
```

# Install packages in the virtual environment
```sh
pip install pytest
pip install pandas
```

# If .DS_Store file appears, execute the following code in terminal to remove file
find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch
echo .DS_Store >> .gitignore
git add .gitignore
git commit -m '.DS_Store banished!'
git push

# Run the program
```sh
python shopping_cart.py
```