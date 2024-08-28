# EasyBounty

**EasyBounty** is a lightweight Python tool designed to help bug bounty hunters and security researchers quickly validate the existence of SPF and DMARC records across multiple domains. The tool automates the process of checking these records, which are crucial for preventing email spoofing and ensuring domain security.


## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Features

- **SPF Record Validation**: Checks if the specified domain has a valid SPF (Sender Policy Framework) record.
- **DMARC Record Validation**: Checks if the specified domain has a valid DMARC (Domain-based Message Authentication, Reporting, and Conformance) policy.
- **ANSI Color-coded Output**: Terminal output is color-coded for easier readability.
- **Batch Processing**: Validate multiple domains from a list with a single command.
- **Customizable Output**: Save results to a specified output file for later analysis.

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/OctaYus/EasyBounty.git
   cd EasyBounty
   ```

2. **Install the Required Dependencies:**

   Ensure you have Python 3 installed, then install dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Basic Command

```bash
python easybounty.py <list_of_domains.txt> <output_file.txt>
```

### Example

```bash
python easybounty.py domains.txt results.txt
```

### Command Explanation

- `<list_of_domains.txt>`: The path to a text file containing a list of domains (one per line) to be validated.
- `<output_file.txt>`: The path to a text file where the results will be saved.

### Output

The tool provides terminal output indicating the validity of SPF and DMARC records with color-coded messages:

- **Green**: Indicates that the SPF or DMARC record is valid.
- **Red**: Indicates a missing or invalid SPF or DMARC record, signaling potential vulnerabilities.

## Contributing

We welcome contributions from the community. Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any inquiries or issues, feel free to reach out:

- **Bugcrowd Profile**: [OctaYus.com](https://bugcrowd.com/OctaYus)
- **Twitter**: [@OctaYus0x01](https://x.com/OctaYus0x01)

---

By providing an easy way to validate SPF and DMARC records, **EasyBounty** helps improve the security posture of your domains. Happy hunting! 🎯

---
