# Prod - QR Documents Validation
![prod-logo](https://github.com/gautam132002/prod/assets/68372911/4792a19d-44ec-4b54-98b8-766413cc4e4d)



## Introduction

Prod is a software designed to provide a validation mark on documents to prevent alteration and forgery issues. Many laboratories and corporations face problems with reports (PDFs) being tampered using PDF editing tools, which can lead to serious consequences. To address this issue, Prod proposes a solution by adding a QR code to the original PDF report. If any values in the PDF are altered, the QR code can be scanned to verify the document's authenticity using the original PDF.

## Features

- Adds a QR code to a PDF document for validation purposes.
- Stores the PDF with the QR code in the cloud (Firebase) for secure access and verification.

## Usage

1. Clone the repository from GitHub:
   ```
   git clone https://github.com/gautam132002/prod
   ```

2. Activate the virtual environment:
   ```
   source bin/activate
   ```


3. Create an account on Firebase and obtain the required API key. Store this key in a file named `your_auth_json_file` and place it in the `rec` directory.

4. Update the code in `main.py` to use your Firebase API key:
   ```python
   cred = credentials.Certificate("rec/your_auth_json_file")
   initialize_app(cred, {'storageBucket': 'base-c5b39.appspot.com'})
   ```

5. Run the `main.py` file:
   ```
   python main.py
   ```

   Alternatively, you can use the precompiled executable file `main.exe` provided with the software, which runs on Prod's Firebase. Simply create a shortcut for `main.exe` and execute it.


6. Follow the on-screen prompts to use the tool effectively. Alternatively, you can follow the instructions below:

   - Place the file(s) you want to validate in the `pdf` folder.

   - Select the mode:
     - Enter `0` for manual mode.
     - Enter `1` for automatic mode.

   - The generated PDF, with the QR code added for validation, will be stored in the `result/pdf` folder.

   - You can find the QR code images in the `qr` folder.

## Contribution

Contributions to Prod are welcome! If you want to contribute to this project, please follow these guidelines:

1. Fork the repository and create your branch from the `main` branch.
2. Make sure to document your code and explain any new features or changes thoroughly.
3. Test your contributions to ensure they work as expected.
4. Submit a pull request with your changes, and our team will review it.

## Rules of Contributions

- Be respectful and considerate of others' contributions and ideas.
- Follow coding standards and keep the code clean and organized.
- Discuss major changes or new features in an issue before working on them.

## License

Prod is licensed under the MIT License. You can find the full license text in the `LICENSE` file.

## Contact

For any questions or support related to Prod, you can reach out to our team at gautamnegi0202@protonmail.com.

---

Thank you for using Prod! We hope this tool helps you secure your valuable documents and prevents unauthorized alterations. If you have any feedback or suggestions, feel free to let us know. Happy document validation!
