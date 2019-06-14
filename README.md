# shopping-cart

## Setup

Navigate to the repo on the command line
```sh
cd ~/shopping-cart
```

# Create the anaconda virtual environment
```sh
conda create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env
```

# Install packages in the virtual environment (One Time)
```sh
pip install pytest
pip install pandas
```

# If .DS_Store file appears, execute the following code in terminal to remove file
```sh
find . -name .DS_Store -print0 | xargs -0 git rm -f --ignore-unmatch
echo .DS_Store >> .gitignore
git add .gitignore
git commit -m '.DS_Store banished!'
git push
```

# Run the program
```sh
python shopping_cart.py
```

# To Test 'Handling Pricing per Pound' for Organic Bananas
Make sure the following product exists in the 'Products' list

```sh 
{"id":21, "name": "Organic Bananas", "department": "fruits", "aisle": "organic produce", "price": 0.79}
```
