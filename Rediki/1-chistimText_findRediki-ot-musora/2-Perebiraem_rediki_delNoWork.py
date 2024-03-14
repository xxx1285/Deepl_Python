def filter_urls(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as infile, \
         open(output_filename, 'w', encoding='utf-8') as outfile:
        for line in infile:
            # Remove lines containing "url?sa"
            if "url?sa" in line:
                continue

            # Keep lines containing "777.com"
            if "777.com" in line:
                outfile.write(line)

if __name__ == "__main__":
    input_filename = r'Linkbilding\1_Telegram_link_chistim\input\redici-2.txt'  # Replace with your actual input file path
    output_filename = r'Linkbilding\1_Telegram_link_chistim\output\redici-3-res.txt'  # Replace with your desired output file path

    filter_urls(input_filename, output_filename)
