import pandas as pd
import os

def read_and_sort_csv(filename):
    """Read CSV file and sort by Name column."""
    df = pd.read_csv(filename)
    return df.sort_values('Name')

def generate_markdown_table(df, include_link_column=True):
    """Generate markdown table from DataFrame."""
    # Create header
    if include_link_column:
        columns = ['Name', 'Brief Description', 'Key Features', 'Licensing Model', 'Pricing', 'Link']
    else:
        columns = ['Name', 'Brief Description', 'Key Features', 'Licensing Model', 'Pricing']
    
    # Create header row
    header = '| ' + ' | '.join(columns) + ' |'
    separator = '| ' + ' | '.join(['---' for _ in columns]) + ' |'
    
    # Create data rows
    rows = []
    for _, row in df.iterrows():
        # Create clickable link in Name column
        name = f"[{row['Name']}]({row['Link']})"
        if include_link_column:
            row_data = [name, row['Brief Description'], row['Key Features'], 
                       row['Licensing Model'], row['Pricing'], row['Link']]
        else:
            row_data = [name, row['Brief Description'], row['Key Features'], 
                       row['Licensing Model'], row['Pricing']]
        rows.append('| ' + ' | '.join(str(x) for x in row_data) + ' |')
    
    return '\n'.join([header, separator] + rows)

def update_readme():
    """Update README.md with sorted tables."""
    # Read and sort both CSV files
    literature_df = read_and_sort_csv('literature_tools.csv')
    coding_df = read_and_sort_csv('coding_tools.csv')
    
    # Save sorted data back to CSV files
    literature_df.to_csv('literature_tools.csv', index=False)
    coding_df.to_csv('coding_tools.csv', index=False)
    
    # Generate markdown tables
    literature_table = generate_markdown_table(literature_df, include_link_column=False)
    coding_table = generate_markdown_table(coding_df, include_link_column=False)
    
    # Read existing README.md
    with open('README.md', 'r') as f:
        content = f.read()
    
    # Split content at table sections
    parts = content.split('##')
    
    # Reconstruct README.md with updated tables
    new_content = parts[0]  # Keep the title and description
    new_content += '\n## Literature Search and Review Tools\n\n'
    new_content += literature_table
    new_content += '\n\n## Coding and Software Development Tools\n\n'
    new_content += coding_table
    
    # Write updated content back to README.md
    with open('README.md', 'w') as f:
        f.write(new_content)

if __name__ == '__main__':
    update_readme()
    print("Tables have been updated and sorted alphabetically.") 