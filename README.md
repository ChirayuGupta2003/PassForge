## Passforge: Your Secure Password Generator

**Tired of weak and repetitive passwords?** Passforge is here to help! This command-line tool generates strong, random passwords that are unique and easy to remember.

**Features:**

* **Customizable length:** Choose the password length that best suits your needs (up to 50 characters).
* **Character types:** Include uppercase, lowercase, numbers, and symbols for maximum security.
* **Simple and intuitive:** Use clear and concise command-line options to configure your password generation.
* **Secure and reliable:** Passforge generates passwords using a cryptographically secure random number generator.

**Usage:**

```
passforge [OPTIONS]
```

**Options:**

* **--length INTEGER:** Length of password (max=50). Defaults to 16.
* **--u BOOLEAN:** Include uppercase letters (True or False). Defaults to True.
* **--l BOOLEAN:** Include lowercase letters (True or False). Defaults to True.
* **--n BOOLEAN:** Include numbers (True or False). Defaults to True.
* **--s BOOLEAN:** Include symbols (True or False). Defaults to True.
* **--help:** Show this help message and exit.

**Examples:**

Generate a 20-character password with all character types:

```
passforge --length 20
```

Generate a 12-character password with lowercase letters and numbers:

```
passforge --length 12 --u False --s False
```

**Get started today and create strong, secure passwords for all your online accounts!**
