# UT NSC 325 Project 5 Group 2
## Set Up
```bash
git clone https://github.com/neil-sriv/nsc-325.git
cd nsc-325
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```
## Usage
### Device Discovery
> Make sure to edit the `test.py` file with the IP Address range you want:
```python
target_ip = "<Target IP>.1/24"
```
Current usage gets list of MAC Addresses connected to your router
```bash
python test.py
```

## Contribution
Try to always use branches to commit and merge to Main!