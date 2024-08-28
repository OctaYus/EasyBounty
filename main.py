import subprocess
import sys
import dns.resolver

# ANSI color codes for terminal output
BLUE = "\033[0;34m"
RED = "\033[91m"
GREEN = "\033[32m"
END = "\033[0m"

# Logo
print(f"""{BLUE}
  ______                         ____                            _           
 |  ____|                       |  _ \                          | |          
 | |__      __ _   ___   _   _  | |_) |   ___    _   _   _ __   | |_   _   _ 
 |  __|    / _` | / __| | | | | |  _ <   / _ \  | | | | | '_ \  | __| | | | |
 | |____  | (_| | \__ \ | |_| | | |_) | | (_) | | |_| | | | | | | |_  | |_| |
 |______|  \__,_| |___/  \__, | |____/   \___/   \__,_| |_| |_|  \__|  \__, |
                          __/ |                                         __/ |
                         |___/                                         |___/
                                                             coder : https://octayus.com/OctaYus
                                                             MyTwitter : https://x.com/OctaYus0x01
{END} 
""")


# Function to check SPF record
def check_spf(domain) :
    try :
        answers = dns.resolver.resolve(domain, 'TXT')
        for record in answers :
            if record.to_text().startswith('"v=spf1') :
                return True
        return False
    except dns.resolver.NoAnswer :
        return False
    except dns.resolver.NXDOMAIN :
        return False
    except Exception as e :
        print(f"Error checking SPF for {domain}: {e}")
        return False


# Function to check DMARC record
def check_dmarc(domain) :
    try :
        answers = dns.resolver.resolve(f'_dmarc.{domain}', 'TXT')
        for record in answers :
            if record.to_text().startswith('"v=DMARC1') :
                return True
        return False
    except dns.resolver.NoAnswer :
        return False
    except dns.resolver.NXDOMAIN :
        return False
    except Exception as e :
        print(f"Error checking DMARC for {domain}: {e}")
        return False


# Function to validate domains and check SPF and DMARC records
def validate_domains(domains, output_file) :
    with open(output_file, 'w') as f_out :
        for domain in domains :
            spf_valid = check_spf(domain)
            dmarc_valid = check_dmarc(domain)

            # Format the output based on SPF and DMARC validity
            spf_output = f"{GREEN}(*) The SPF for {domain} is Valid{END}" if spf_valid else f"{RED}(*) {domain} is vulnerable, SPF Record is Invalid{END}"
            dmarc_output = f"{GREEN}(*) The DMARC for {domain} is Valid{END}" if dmarc_valid else f"{RED}(*) {domain} is vulnerable, The DMARC Policy not Found {END}"

            # Print and write the output
            print(spf_output)
            print(dmarc_output)
            f_out.write(spf_output + '\n')
            f_out.write(dmarc_output + '\n')



def main() :
    if len(sys.argv) != 3 :
        print(f"{RED}[+] Usage: {sys.argv[0]} <list_of_domains> <output_file.txt>{END}")
        print(f"{RED}[+] Example: {sys.argv[0]} domains.txt output.txt{END}")
        sys.exit(1)

    domains_file = sys.argv[1]
    output_file = sys.argv[2]

    # Read the list of domains from the file
    try :
        with open(domains_file, 'r') as f :
            domains = [line.strip() for line in f if line.strip()]
    except FileNotFoundError :
        print(f"{RED}Error: The file {domains_file} was not found.{END}")
        sys.exit(1)

    # Run validation and write output to file
    validate_domains(domains, output_file)


if __name__ == "__main__" :
    main()
