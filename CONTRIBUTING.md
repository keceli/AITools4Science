# Contributing to AITools4Science

Thank you for your interest in contributing to AITools4Science! This guide explains how you can contribute by adding or updating AI tools in our collection.

## Contribution Process

### 1. Fork and Clone the Repository
```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/YOUR_USERNAME/AITools4Science.git
cd AITools4Science
```

### 2. Edit the CSV Files
The repository contains two CSV files that store the tool information:
- `literature_tools.csv`: For literature search and review tools
- `coding_tools.csv`: For coding and software development tools

Each CSV file has the following columns:
- `Name`: Tool name
- `Brief Description`: Short description of the tool
- `Key Features`: Main features, separated by semicolons
- `Licensing Model`: Type of license (e.g., Proprietary, Open-source)
- `Pricing`: Pricing information
- `Link`: Official website URL

Example entry:
```csv
Name,Brief Description,Key Features,Licensing Model,Pricing,Link
Example Tool,AI-powered example tool,"Feature 1; Feature 2; Feature 3",Proprietary (freemium),"Free tier; Pro $10/month",https://example.com
```

### 3. Update the Tables
After editing the CSV files, run the update script to regenerate the README.md:
```bash
# Make sure you have Python and pandas installed
pip install pandas

# Run the update script
python update_tables.py
```

This script will:
1. Sort the tools alphabetically by name
2. Update the CSV files with the sorted order
3. Regenerate the README.md with properly formatted tables

### 4. Create a Pull Request
1. Commit your changes:
```bash
git add literature_tools.csv coding_tools.csv README.md
git commit -m "Add/Update: [Tool Name] - [Brief description of changes]"
```

2. Push to your fork:
```bash
git push origin main
```

3. Create a Pull Request on GitHub:
   - Go to your fork on GitHub
   - Click "Pull Request"
   - Select the main branch of the original repository as the base
   - Add a description of your changes
   - Submit the PR

## Guidelines for Adding Tools

1. **Accuracy**: Ensure all information is accurate and up-to-date
2. **Completeness**: Fill in all required fields
3. **Formatting**:
   - Use semicolons to separate multiple features
   - Keep descriptions concise but informative
   - Include pricing details when available
4. **Links**: Always include the official website URL
5. **Categories**: Add tools to the appropriate CSV file based on their primary function

## Need Help?

If you have any questions or need assistance:
1. Open an issue in the repository
2. Check existing issues and pull requests
3. Contact the maintainers

Thank you for contributing to making AITools4Science a valuable resource for the scientific community! 