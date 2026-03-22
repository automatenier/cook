import os
import glob

# Comprehensive list of path replacements
replacements = {
    # Main Root/Folders
    'AI_BRAIN': 'AI_BRAIN',
    'HMN_A INPUTS': 'HMN_A INPUTS',
    'AI_MEMORY': 'AI_MEMORY',
    'AI_MEMORY': 'AI_MEMORY',
    'PDCT_JO_Consult': 'PDCT_JO_Consult',
    'PDCT_Real_Estate': 'PDCT_Real_Estate',
    'AI_n8n': 'AI_n8n',
    'AI_Tools': 'AI_Tools',
    'VLT_Content/__VLT_OBSVAULT': 'VLT_Content/__VLT_OBSVAULT',
    '.tmp': '.tmp',
    'HMN_A Human': 'HMN_A Human',
    'HMN_A Human': 'HMN_A Human',
    
    # Cook/Content Folder structure (VLT_Content)
    'HMN_HUMAN': 'HMN_HUMAN',
    '01_HMN_INPUTS': '01_HMN_INPUTS',
    'AI_BRAIN': 'AI_BRAIN',
    'AI_ENGINE': 'AI_ENGINE',
    'AI_MEMORY': 'AI_MEMORY',
    'VLT_ASSETS': 'VLT_ASSETS',
    '02_HMN_HUMANFLOW': '02_HMN_HUMANFLOW',
    '03_HMN_REVIEW': '03_HMN_REVIEW',
    '05_VLT_FINAL': '05_VLT_FINAL',
    'HMN_HMN_A INPUTS': 'HMN_INBOX',
    'PDCT_JO_ED': 'PDCT_JO_ED',
    'PDCT_CLIENTS': 'PDCT_CLIENTS',
    'AI_AI_BRAIN': 'AI_BRAIN',
    'VLT_EXCALIDRAW': 'VLT_EXCALIDRAW',
    'PDCT_MASTERMIND': 'PDCT_MASTERMIND',
    'PDCT_MODULES': 'PDCT_MODULES',
    'VLT_NOTES': 'VLT_NOTES',
    
    # Generic prefixes
    'VLT_Content/': 'VLT_VLT_Content/',
    'VLT_Content/': 'VLT_VLT_Content/'
}

def update_file(filepath):
    if not os.path.isfile(filepath):
        return
    
    try:
        # Avoid binary files
        if filepath.endswith(('.png', '.jpg', '.jpeg', '.gif', '.pdf', '.exe', '.pyc')):
            return

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = content
        for old, new in replacements.items():
            new_content = new_content.replace(old, new)
            
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8', newline='') as f:
                f.write(new_content)
            print(f'Updated {filepath}')
    except Exception as e:
        # Silent fail for binary or encoding issues
        pass

# Expanded patterns to cover more files
patterns = [
    '*.md',
    '.agents/workflows/*.md',
    '.claude/commands/*.md',
    '.gemini/commands/*.md',
    'AI_Tools/*.py',
    'AI_BRAIN/**/*.md',
    'AI_MEMORY/**/*.md',
    'VLT_VLT_Content/**/*.md',
    'VLT_Content/__VLT_OBSVAULT/**/*.md',
    'HMN_A Human/**/*.md',
    'HMN_A INPUTS/**/*.md'
]

print("Starting migration...")
for pattern in patterns:
    for filepath in glob.glob(pattern, recursive=True):
        update_file(filepath)
print("Migration complete.")
