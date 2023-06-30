## Installation
1. Clone the repo:

`git clone git@github.com:vfosterm-ssh/privx-directory-tool.git`

2. copy the example configuration:
```
cd privx-directory-tool
cp example-config.py privxdt/config.py
```
3. Edit the configuration as needed:
```python
# PrivX instance variables.

HOSTNAME = "example.privx.com"
HOSTPORT = 443

CA_CERT = """
ADD PRIVX CA CERT HERE
"""

OAUTH_CLIENT_ID = "privx-external"
OAUTH_CLIENT_SECRET = "ADD OAUTH CLIENT SECRET HERE"

API_CLIENT_ID = "ADD API CLIENT ID HERE"
API_CLIENT_SECRET = "ADD API CLIENT SECRET HERE"
```
4. Install the tool using pip
`pip install .`

### Usage
After installation the privx-directory-tool can be used by running the privxdt command.
The privxdt command features 2 subcommands "list-directories" and "migrate".

#### Example commands
```sh
# run help for a subcommand
$ privxdt migrate -h

Usage: privxdt migrate [OPTIONS]

Options:
  -H, --host-id TEXT       ID of host to migrate  [required]
  -D, --directory-id TEXT  ID of directory to migrate to  [required]
  -h, --help               Show this message and exit.
```
```sh
# list directories
$ privxdt list-directories
                                                         Directories
                            ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━┓
                            ┃ ID                                   ┃ Name           ┃ Type       ┃
                            ┡━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━┩
                            │ 9027f812-d148-4d42-9c87-8ed8910e568d │ Local hosts    │ LOCALHOST  │
                            │ 67b9cc24-673d-58c6-693f-08d3db44c762 │ API clients    │ API-CLIENT │
                            │ 563ba283-263c-5a93-4a79-e149c92f2aa1 │ authentik ldap │ LDAP       │
                            │ 7e787419-f3aa-471c-bd25-15963cc61750 │ Local users    │ LOCAL      │
                            └──────────────────────────────────────┴────────────────┴────────────┘
```
```sh
# migrate a host from local host directory to the authentik ldap directory
$ privxdt migrate -H 63b8aaf5-c8eb-4945-7152-5d90151d2ab2 -D 563ba283-263c-5a93-4a79-e149c92f2aa1
success
```
