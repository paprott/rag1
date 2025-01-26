import openpyxl
import re


def main_loop():
    # Read the Excel file
    workbook = openpyxl.load_workbook('Piosenki-2.xlsx')
    worksheet = workbook.active

    # Iterate through rows, skipping headers
    for row in worksheet.iter_rows(values_only=False):
        if row[1] == 'autor' or row[2] == 'tytul' or row[3] == 'tekst':
            continue  # Skip header row

        author = str(row[1].value).strip()
        title = str(row[2].value).strip()
        text = str(row[3].value).strip()

        # Generate filename from title
        filename = "songs/" + title.strip() + '.txt'

        with open(filename, 'w', encoding='utf-8') as f:
            temp = title + "\n"
            temp = temp + author + "\n"
            
            res=re.findall(r"https:.*$", text)
            if len(res)>0:
                res = res[0]
            else:
                res="https://"
            
            temp = temp + res +"\n\n"
            temp = temp+ text + "\n"
            f.write(f"{temp}")
      
        
# Run the main loop
if __name__ == "__main__":
    main_loop()
    