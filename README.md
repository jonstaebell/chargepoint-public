# 🔌 ChargePoint Public

Checks status of chargepoint chargers associated with an account

## 🚀 Features

- Polls all chargers on a Chargepoint account and determines whether any are plugged in
- Outputs a boolean result: `True` if any car is plugged in, `False` otherwise
- Can be used in home automation workflows (e.g., with Home Assistant, systemd services, or crontab), e.g.:
    - use from CLI to check whether car is plugged in
    - set up crontab to check whether car is plugged in before bedtime
      (optional discord webhook to alert if car is not plugged in)

requires three environment variables:
- USERNAME - chargepoint.com username
- PASSWORD - chargepoint.com password
- WEBHOOK_URL - optional webhook to be invoked if no chargers in use
  (can be overridden by supplying any argument to the program)

example of a bash script to run the program:
    #!/bin/bash
    export USERNAME='abc@abc.com'
    export PASSWORD='password123'
    export WEBHOOK_URL=''
    python3 /home/pi/piprojects/chargepoint-public/chargepoint.py $1

## 🛠 Requirements

- Python 3.x
- python_chargepoint (see https://pypi.org/project/python-chargepoint/)

## 📦 Usage

python3 chargepoint.py [n]

    The optional n argument suppresses discord webhook (for use in terminal, e.g.)

    Prints a message that includes True or False to stdout

## ⚙️ Integration Example

Use in crontab or another monitoring script (e.g., detectarr) to check car charging status.

## 🔒 Security

The chargepoint.com username and password are required to be in environment
variables for security.

## 🙏 Credits

Uses API from https://pypi.org/project/python-chargepoint/

Created by Jon Staebell jonstaebell@gmail.com May 31, 2025

## License

Copyright (C) 2025 Jon Staebell

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see http://www.gnu.org/licenses/.